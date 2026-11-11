# -*- coding: utf-8 -*-
"""Base dos lotes sem história (a partir do lote 4). Uso num loteN.py:
    from lote_base import add, salvar
    add(nome, slug, pais, cidade, ano, fundador, caracteristica, site, instagram, "Modelo; U 350; movimento | Modelo 2; -; mov", obs)
    salvar("loteN.json")
Moedas: U = US$, E = €, G = £, S = S$, C = C$, R = ₹ (rúpia), P = ₱ (peso filipino), N = coroa norueguesa. "-" = sem preço."""
import json
CAMBIO = {"U": ("US$", 5.5), "E": ("€", 6.1), "G": ("£", 7.2), "S": ("S$", 4.2), "C": ("C$", 4.0), "R": ("₹", 0.065), "P": ("₱", 0.095), "N": ("NOK", 0.52)}
M = []
def faixa(p):
    for n, lim in enumerate((1000, 5000, 10000, 20000, 40000, 70000, 100000, 350000, 600000), start=1):
        if p <= lim: return n
    return 10
def add(nome, slug, pais, cidade, ano, fund, carac, site, ig, modelos, obs="", ativa=True):
    linhas, brl = [], []
    for m in [x.strip() for x in modelos.split(" | ") if x.strip()]:
        p = [y.strip() for y in m.split(";")] + ["", ""]
        n, pr, mov = p[0], p[1], p[2]
        partes = [mov] if mov and mov != "-" else []
        if pr and pr != "-":
            c, v = pr.split(); v = float(v); s, tx = CAMBIO[c]; brl.append(v * tx)
            partes.append(f"cerca de {s} {v:,.0f}".replace(",", "."))
        linhas.append(n + (" — " + "; ".join(partes) if partes else ""))
    f = round(sum(brl) / len(brl)) if brl else None
    ficha = "Fundação: " + (str(ano) if ano else "não informada no Atlas") + ". Fundador(es): " + (fund or "não informado no Atlas") + "."
    faltas = [t for t, v in (("H vazio: Instagram não informado no Atlas", ig), ("G vazio: site não informado no Atlas", site), ("C vazio: cidade não informada no Atlas", cidade), ("E/F vazios: o Atlas não traz preços confiáveis", f)) if not v]
    M.append({"A": nome, "B": pais, "C": cidade, "D": carac, "E": faixa(f) if f else None, "F": f, "G": site, "H": ("@" + ig if ig else None), "I": None,
              "J": "\n\n".join(linhas), "K": None, "L": None,
              "M": "Incluída a pedido do usuário em 11/11/2026 (marcas do Microbrand Atlas que faltavam). Dados da ficha do Atlas (microbrandatlas.com/brand/" + slug + "). " + ficha
                   + " História (I) em branco a pedido do usuário, que vai escrever depois. Preço médio = média dos preços de referência do Atlas convertidos (US$ 5,5; € 6,1; £ 7,2; S$ 4,2; C$ 4,0; ₹ 0,065; ₱ 0,095; NOK 0,52) — conferir no site oficial. Logo ainda a buscar. Só a aba Marcas; relógios não pesquisados."
                   + ("" if ativa else " O Atlas marca a marca como inativa ou encerrada.")
                   + "".join(" " + t + "." for t in faltas) + ((" " + obs) if obs else "")})
def salvar(arq):
    json.dump(M, open(arq, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(M), "marcas;", sum(1 for m in M if not m["H"]), "sem Instagram;", sum(1 for m in M if not m["F"]), "sem preço;", sum(1 for m in M if not m["G"]), "sem site")
