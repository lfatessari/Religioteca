import openpyxl
A = openpyxl.load_workbook('Relogios_atualizada_492.xlsx'); B = openpyxl.load_workbook('Relogios_atualizada_493.xlsx')
a, b = A['Marcas'], B['Marcas']
def s(ws, r): return [(ws.cell(r, k).value, ws.cell(r, k).hyperlink.target if ws.cell(r, k).hyperlink else None) for k in range(1, 14)]
bad = [r for r in range(1, a.max_row + 1) if s(a, r) != s(b, r + (r >= 57) + (r >= 192))]
print('Marcas linhas antigas diferentes:', bad)
for r in (57, 193): print(r, [ (v[0] if not isinstance(v[0],str) else v[0][:40], v[1]) for v in s(b, r)])
ra, rb = A['Relógios'], B['Relógios']
diff = [r for r in range(1, ra.max_row + 1) if [ra.cell(r, k).value for k in range(1, 6)] != [rb.cell(r, k).value for k in range(1, 6)]]
print('Relógios linhas antigas diferentes:', diff[:10], '| max_row', ra.max_row, '->', rb.max_row)
novas = [(r, rb.cell(r, 1).value) for r in range(ra.max_row + 1, rb.max_row + 1)]
from collections import Counter; print(Counter(x[1] for x in novas))
ruins = [r for r, _ in novas if not rb.cell(r, 3).hyperlink or rb.cell(r, 3).hyperlink.target != rb.cell(r, 3).value]
print('hyperlinks ruins:', ruins)
for t in ('Planilha1', 'Tabela de faixa de preços'):
    print(t, {c.coordinate: c.value for c in A[t]._cells.values()} == {c.coordinate: c.value for c in B[t]._cells.values()})
print('RESULTADO:', 'OK' if not bad and not diff and not ruins else 'FALHOU')
