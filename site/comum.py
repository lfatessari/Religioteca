"""Funções compartilhadas pelo gerador do site e pelo baixador de fotos."""
import hashlib
import re
import unicodedata
import urllib.parse


def limpo(v):
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s in ("-", "—", "None", "N/A", "n/a") else s


def limpar_url(u):
    """Normaliza o link da coluna C/D da aba Relógios (tira srcset, redireciono do Google etc.)."""
    u = limpo(u)
    if not u:
        return ""
    u = u.split(", ")[0].split(" ")[0].strip()
    if "google." in u and "/url?" in u:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(u).query)
        if q.get("url"):
            u = q["url"][0]
    if u.startswith("//"):
        u = "https:" + u
    return u if u.startswith(("http://", "https://")) else ""


def id_foto(url):
    """Identificador estável da foto: mesmo link -> mesmo arquivo."""
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def caminho_foto(url):
    h = id_foto(url)
    return f"{h[:2]}/{h}.webp"


def chave(s):
    s = unicodedata.normalize("NFKD", str(s).lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s)


def links_da_planilha(planilha):
    """Todos os links de foto da aba Relógios, sem repetição, na ordem da planilha."""
    import openpyxl
    wb = openpyxl.load_workbook(planilha, read_only=True, data_only=True)
    vistos, saida = set(), []
    for r in wb["Relógios"].iter_rows(min_row=2, values_only=True, max_col=4):
        if not limpo(r[0]):
            continue
        u = limpar_url(r[2]) or limpar_url(r[3])
        if u and u not in vistos:
            vistos.add(u)
            saida.append(u)
    return saida
