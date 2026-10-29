#!/usr/bin/env python3
"""Baixa e reduz as fotos da aba Relógios para o site público.

Uso: python3 baixar_fotos.py <planilha.xlsx> <pasta_fotos> [--minutos N] [--threads N]

- Cada link vira <pasta_fotos>/img/ab/<id>.webp (lado maior de 400 px, WebP).
- Quando o link é uma página (e não a imagem), usa a foto de capa da página
  (og:image / twitter:image / JSON-LD).
- <pasta_fotos>/manifest.json guarda o resultado de cada link, para nunca
  baixar duas vezes. Falhas passageiras (site ocupado, tempo esgotado) são
  tentadas de novo depois de 6 horas; as outras, depois de 14 dias.
- Para sozinho quando acaba o tempo (--minutos); a próxima execução continua.
"""
import argparse, io, json, os, re, sys, threading, time
import urllib.parse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import caminho_foto, links_da_planilha, logos_da_planilha  # noqa: E402

LADO = 400
QUALIDADE = 72
MENOR_ACEITO = 150          # fotos menores que isso costumam ser ícones ou logos
REPETIR_APOS = 14 * 86400   # erros permanentes (404, página sem foto...)
REPETIR_TRANSITORIO = 6 * 3600  # bloqueio temporário, servidor fora do ar, tempo esgotado
TRANSITORIOS = ("429", "500", "502", "503", "504", "Timeout", "ConnectionError", "SSLError", "ChunkedEncoding")
MAX_TENTATIVAS = 3
POR_SITE = 3                # downloads simultâneos no mesmo site
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

Image.MAX_IMAGE_PIXELS = 80_000_000
_local = threading.local()
_travas = defaultdict(lambda: threading.Semaphore(POR_SITE))
_travas_lock = threading.Lock()


def sessao():
    if not hasattr(_local, "s"):
        s = requests.Session()
        s.headers.update({"User-Agent": UA, "Accept-Language": "en,pt-BR;q=0.8"})
        _local.s = s
    return _local.s


def trava(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    with _travas_lock:
        return _travas[host]


def pegar(url, aceitar):
    origem = "{0.scheme}://{0.netloc}/".format(urllib.parse.urlparse(url))
    with trava(url):
        r = sessao().get(url, timeout=(10, 30), allow_redirects=True, stream=True,
                         headers={"Accept": aceitar, "Referer": origem})
        r.raise_for_status()
        corpo = r.raw.read(25_000_000, decode_content=True)
    return r.headers.get("Content-Type", "").lower(), corpo, r.url


RE_META = re.compile(
    r'<meta[^>]+(?:property|name)\s*=\s*["\'](?:og:image(?::secure_url)?|twitter:image(?::src)?)["\'][^>]*>', re.I)
RE_CONTENT = re.compile(r'content\s*=\s*["\']([^"\']+)["\']', re.I)
RE_JSONLD_IMG = re.compile(r'"image"\s*:\s*(?:\[\s*)?(?:\{[^}]*?"url"\s*:\s*)?"([^"]+)"', re.I)
RE_IMG_SRC = re.compile(r'<link[^>]+rel\s*=\s*["\']image_src["\'][^>]*href\s*=\s*["\']([^"\']+)', re.I)


def foto_da_pagina(html, base):
    texto = html[:2_000_000].decode("utf-8", "ignore")
    candidatos = []
    for tag in RE_META.findall(texto):
        m = RE_CONTENT.search(tag)
        if m:
            candidatos.append(m.group(1))
    candidatos += RE_IMG_SRC.findall(texto)
    candidatos += RE_JSONLD_IMG.findall(texto)
    for c in candidatos:
        c = c.replace("&amp;", "&").replace("\\/", "/").strip()
        if c and not c.startswith("data:"):
            return urllib.parse.urljoin(base, c)
    return ""


def abrir_imagem(dados):
    cab = dados[:600].lstrip().lower()
    if cab.startswith(b"<svg") or (cab.startswith(b"<?xml") and b"<svg" in dados[:4000].lower()):
        import cairosvg  # logos em SVG
        dados = cairosvg.svg2png(bytestring=dados, output_width=800)
    return Image.open(io.BytesIO(dados))


def reduzir(dados, destino, menor=MENOR_ACEITO):
    im = abrir_imagem(dados)
    im = ImageOps.exif_transpose(im)
    if max(im.size) < menor:
        raise ValueError(f"imagem pequena demais ({im.size[0]}x{im.size[1]})")
    tem_alfa = im.mode in ("RGBA", "LA", "PA") or (im.mode == "P" and "transparency" in im.info)
    im = im.convert("RGBA" if tem_alfa else "RGB")
    im.thumbnail((LADO, LADO), Image.LANCZOS)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    tmp = destino + ".tmp"
    im.save(tmp, "WEBP", quality=QUALIDADE, method=5)
    os.replace(tmp, destino)


def processar(url, pasta_img, menor=MENOR_ACEITO):
    rel = caminho_foto(url)
    destino = os.path.join(pasta_img, rel)
    tipo, corpo, final = pegar(url, "image/avif,image/webp,image/*,text/html;q=0.8,*/*;q=0.5")
    foto_url = final
    if "svg" not in tipo and ("html" in tipo or corpo[:200].lstrip().lower().startswith((b"<!doctype", b"<html"))):
        foto_url = foto_da_pagina(corpo, final)
        if not foto_url:
            raise ValueError("página sem foto de capa")
        _, corpo, foto_url = pegar(foto_url, "image/avif,image/webp,image/*,*/*;q=0.5")
    reduzir(corpo, destino, menor)
    return {"f": rel, "o": foto_url}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("planilha")
    ap.add_argument("pasta")
    ap.add_argument("--minutos", type=float, default=50)
    ap.add_argument("--threads", type=int, default=32)
    a = ap.parse_args()

    pasta_img = os.path.join(a.pasta, "img")
    arq_manifest = os.path.join(a.pasta, "manifest.json")
    manifest = {}
    if os.path.exists(arq_manifest):
        with open(arq_manifest, encoding="utf-8") as fh:
            manifest = json.load(fh)

    agora = time.time()
    logos = logos_da_planilha(a.planilha)
    eh_logo = set(logos)
    links = logos + [u for u in links_da_planilha(a.planilha) if u not in eh_logo]
    fila = []
    for u in links:
        m = manifest.get(u)
        if m and m.get("f") and os.path.exists(os.path.join(pasta_img, m["f"])):
            continue
        if m and m.get("e") and u in eh_logo and m.get("n", 1) == 1 and "pequena" in m["e"]:
            fila.append(u)
            continue
        if m and m.get("e"):
            transitorio = any(t in m["e"] for t in TRANSITORIOS)
            espera = REPETIR_TRANSITORIO if transitorio else REPETIR_APOS
            limite_tent = MAX_TENTATIVAS + (3 if transitorio else 0)
            if m.get("n", 1) >= limite_tent or agora - m.get("t", 0) < espera:
                continue
        fila.append(u)
    # intercala sites diferentes para não martelar um só
    por_host = defaultdict(list)
    for u in fila:
        por_host[urllib.parse.urlparse(u).netloc].append(u)
    fila = [u for grupo in zip_longest_all(por_host.values()) for u in grupo]

    print(f"links na planilha: {len(links)} | já resolvidos: {len(links) - len(fila)} | a baixar agora: {len(fila)}")
    limite = agora + a.minutos * 60
    ok = erro = 0
    lock = threading.Lock()

    def salvar():
        tmp = arq_manifest + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        os.replace(tmp, arq_manifest)

    def tarefa(u):
        if time.time() > limite:
            return u, None
        try:
            return u, processar(u, pasta_img, 40 if u in eh_logo else MENOR_ACEITO)
        except Exception as e:  # noqa: BLE001
            return u, {"e": f"{type(e).__name__}: {str(e)[:160]}"}

    with ThreadPoolExecutor(max_workers=a.threads) as ex:
        futuros = [ex.submit(tarefa, u) for u in fila]
        for i, fut in enumerate(as_completed(futuros), 1):
            u, res = fut.result()
            if res is None:
                continue
            with lock:
                if "e" in res:
                    ant = manifest.get(u, {})
                    res.update(t=int(time.time()), n=ant.get("n", 0) + 1)
                    erro += 1
                else:
                    ok += 1
                manifest[u] = res
                if i % 500 == 0:
                    salvar()
                    print(f"  {i}/{len(fila)}  ok={ok} erro={erro}", flush=True)
    salvar()
    resolvidos = sum(1 for u in links if manifest.get(u, {}).get("f"))
    pendentes = sum(1 for u in links if u not in manifest)
    print(f"nesta rodada: ok={ok} erro={erro} | total com foto: {resolvidos}/{len(links)} | ainda não tentados: {pendentes}")
    with open(os.path.join(a.pasta, "pendentes.txt"), "w") as fh:
        fh.write(str(pendentes))


def zip_longest_all(listas):
    listas = [list(l) for l in listas]
    i = 0
    while True:
        rodada = [l[i] for l in listas if i < len(l)]
        if not rodada:
            return
        yield rodada
        i += 1


if __name__ == "__main__":
    main()
