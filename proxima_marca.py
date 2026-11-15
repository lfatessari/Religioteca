#!/usr/bin/env python3
"""Lista as próximas marcas da aba Marcas, de cima para baixo, que AINDA NÃO têm
nenhum relógio na aba Relógios (pedido do usuário, 14/11/2026).

Uso: python3 proxima_marca.py planilha/Relogios_atualizada_NNN.xlsx [quantas=10]

Uma marca conta como "já feita" se o nome dela (coluna A da aba Marcas) aparece
na coluna A da aba Relógios, comparando sem acentos, maiúsculas, espaços e
pontuação, ou se está em APELIDOS abaixo (nome diferente nas duas abas).
"""
import sys, re, unicodedata, collections, openpyxl

# nome na aba Marcas -> nome usado na aba Relógios
APELIDOS = {
    "Victorinox Swiss Army": "Victorinox",
    "Zeno-Watch Basel": "Zeno Watch-Basel",
}


# marcas com só uns poucos relógios que entraram de passagem: pesquisar normalmente
# (pedido do usuário, 14/11/2026). Os relógios que já existem ficam; a bateria nova
# não deve duplicá-los.
PESQUISAR_MESMO_ASSIM = {"Tiffany & Co.", "Urban Jürgensen", "Wyler", "ZRC 1904"}


# marcas adiadas: sem fontes suficientes para a trava (pular até o usuário decidir ou a marca lançar).
# Adiadas em 15/11/2026 (v622); notas em historico/notas_<marca>.md. Para voltar a pesquisar, tirar daqui.
ADIADAS = {
    "Aft and Anchor Watch Co": "só o site oficial existe (4 relógios em pré-venda); sem fontes externas para a trava",
    "Agapever Watches": "pré-lançamento, sem site nem relógios publicados",
}


def chave(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def main():
    arq = sys.argv[1]
    quantas = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    wb = openpyxl.load_workbook(arq, read_only=True)
    feitas = collections.Counter(
        chave(r[0]) for r in wb["Relógios"].iter_rows(min_row=2, max_col=1, values_only=True) if r[0]
    )
    linhas = [
        (i, r[0]) for i, r in enumerate(wb["Marcas"].iter_rows(min_row=2, max_col=1, values_only=True), 2) if r[0]
    ]
    sem = [(i, m) for i, m in linhas
           if m not in ADIADAS and (m in PESQUISAR_MESMO_ASSIM or feitas[chave(APELIDOS.get(m, m))] == 0)]
    print(f"marcas sem relógios: {len(sem)} de {len(linhas)}")
    for m, motivo in ADIADAS.items():
        print(f"(adiada: {m} — {motivo})")
    for i, m in sem[:quantas]:
        print(i, m)


if __name__ == "__main__":
    main()
