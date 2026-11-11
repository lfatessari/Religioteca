# -*- coding: utf-8 -*-
"""Completa células da aba Marcas de várias marcas (pedido direto do usuário em 11/11/2026: 'complete essas 3').
Como o corrigir_marca.py, mas aceita F (preço médio) quando a célula está VAZIA. Confere que nada mais mudou."""
import sys, json, copy, openpyxl
from openpyxl.worksheet.formula import ArrayFormula
ENT, SAI, CFG = sys.argv[1:4]
cfgs = json.load(open(CFG, encoding='utf-8'))
def snap(wb):
    return {ws.title: {c.coordinate: (('ARR', c.value.ref, c.value.text) if isinstance(c.value, ArrayFormula) else c.value)
                       for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb = openpyxl.load_workbook(ENT); before = snap(wb); m = wb['Marcas']
COLS = {'B': 2, 'C': 3, 'D': 4, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11}
perm = set()
for cfg in cfgs:
    lms = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == cfg['marca']]
    assert len(lms) == 1, lms; lm = lms[0]
    for col, val in cfg['correcoes'].items():
        cel = m.cell(lm, COLS[col])
        if col == 'F': assert cel.value in (None, ''), 'F já preenchido'
        if 'trecho' in cfg and col == 'I':
            a, b = cfg['trecho']; assert cel.value.count(a) == 1; val = cel.value.replace(a, b)
        print(f'{col}{lm}: {str(cel.value)[:70]!r} -> {str(val)[:70]!r}')
        cel.value = val; perm.add(f'{col}{lm}')
    c = m.cell(lm, 13); c.value = cfg['observacoes']; perm.add(f'M{lm}')
wb.save(SAI)
after = snap(openpyxl.load_workbook(SAI)); ok = True
for t in before:
    mud = sorted(k for k in set(before[t]) | set(after[t]) if before[t].get(k) != after[t].get(k))
    extra = [k for k in mud if k not in perm]
    print(t, 'mudanças:', mud)
    if extra: ok = False; print('  !! fora do permitido:', extra[:20])
print('RESULTADO:', 'OK' if ok else 'FALHOU — não entregar')
