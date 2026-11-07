"""Corrige células da aba Marcas de UMA marca, sem tocar na aba Relógios.
Uso: python3 corrigir_marca.py ENTRADA.xlsx SAIDA.xlsx correcao.json
correcao.json: {"marca": "<coluna A>", "correcoes": {"I": "...", "J": "..."}, "observacoes": "texto para M"}
Só B, C, D, G, H, I, J e M podem mudar; a verificação compara tudo antes/depois."""
import sys, json, copy
import openpyxl
from openpyxl.worksheet.formula import ArrayFormula
ENT, SAI, CFG = sys.argv[1:4]
cfg = json.load(open(CFG, encoding='utf-8'))
def snap(wb):
    return {ws.title: {c.coordinate: (('ARR', c.value.ref, c.value.text) if isinstance(c.value, ArrayFormula) else c.value)
                       for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb = openpyxl.load_workbook(ENT); before = snap(wb); m = wb['Marcas']
lms = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == cfg['marca']]
assert len(lms) == 1, lms; lm = lms[0]
COLS = {'B': 2, 'C': 3, 'D': 4, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
perm = set()
for col, val in (cfg.get('correcoes') or {}).items():
    assert col in COLS, col
    print(f'{col}{lm}: {str(m.cell(lm, COLS[col]).value)[:90]!r}\n   -> {str(val)[:90]!r}')
    m.cell(lm, COLS[col]).value = val; perm.add(f'{col}{lm}')
if cfg.get('observacoes') is not None:
    c = m.cell(lm, 13); c.value = cfg['observacoes'] or None; c._style = copy.copy(m.cell(lm, 11)._style); perm.add(f'M{lm}')
wb.save(SAI)
after = snap(openpyxl.load_workbook(SAI)); ok = True
for t in before:
    mud = sorted(k for k in set(before[t]) | set(after[t]) if before[t].get(k) != after[t].get(k))
    extra = [k for k in mud if k not in perm]
    print(t, 'mudanças:', mud[:20])
    if extra: ok = False; print('  !! fora do permitido:', extra[:20])
print('RESULTADO:', 'OK' if ok else 'FALHOU — não entregar')
