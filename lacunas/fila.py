"""Monta o lote da Fase Marcas (regra corrigida pelo usuário em 14/11/2026).
Uso: python3 lacunas/fila.py planilha/Relogios_atualizada_NNN.xlsx [tamanho=40] [saida=/home/claude/trab]
Regra:
- Marca já tratada nesta fase (M contém "istória revisada", "istória preenchidas" ou
  "Lacunas e história preenchidas") -> PULA.
- Marca com "Lacunas revisadas" ou "preenchimento a pedido" em M (rodadas antigas: B–H, J, K
  já pesquisadas) -> falta = ["I"] só se a História estiver vazia; senão PULA.
- Demais -> falta = colunas vazias entre B, C, D, E, F, G, H, I, J, K; nenhuma vazia -> PULA.
- História já escrita NUNCA entra (não se confere nem reescreve).
Vazio = célula vazia ou "-", "—", "n/a".
Grava grupo1.json ... grupo8.json (5 marcas cada) e imprime o total restante na fila.
"""
import sys, json, os
import openpyxl

ENT = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 40
OUT = sys.argv[3] if len(sys.argv) > 3 else '/home/claude/trab'
L = 'ABCDEFGHIJKLM'
vazio = lambda v: v is None or str(v).strip() in ('', '-', '—', 'n/a')
FEITA = ('istória revisada', 'istória preenchidas')
ANTIGA = ('Lacunas revisadas', 'preenchimento a pedido')

def fila(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    out = []
    for i, r in enumerate(wb['Marcas'].iter_rows(min_row=2, max_col=13, values_only=True), start=2):
        if not r[0]:
            continue
        m = str(r[12] or '')
        if any(s in m for s in FEITA):
            continue
        if any(s in m for s in ANTIGA):
            falta = ['I'] if vazio(r[8]) else []
        else:
            falta = [L[j] for j in range(1, 11) if vazio(r[j])]
        if falta:
            out.append((i, r, falta))
    wb.close()
    return out

if __name__ == '__main__':
    q = fila(ENT)
    print('marcas na fila:', len(q))
    os.makedirs(OUT, exist_ok=True)
    lote = q[:N]
    for g in range(0, len(lote), 5):
        grp = [{'linha': i, 'marca': r[0], 'falta': f,
                'atual': {L[j]: (str(r[j])[:150] if r[j] is not None else '') for j in range(11) if L[j] != 'I'}}
               for i, r, f in lote[g:g+5]]
        json.dump(grp, open(f'{OUT}/grupo{g//5+1}.json', 'w'), ensure_ascii=False, indent=1)
    for i, r, f in lote:
        print(i, r[0], ''.join(f))
