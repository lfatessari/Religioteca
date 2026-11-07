import sys, openpyxl
from openpyxl.worksheet.formula import ArrayFormula
ENT, SAI = sys.argv[1:3]
def snap(wb):
    return {ws.title: {c.coordinate: c.value for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb = openpyxl.load_workbook(ENT); antes = snap(wb); m = wb['Marcas']
lin = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == 'Addiesdive']
assert len(lin) == 1, lin; r = lin[0]
gc, gg = m.cell(r, 3).value, m.cell(r, 7).value
assert gc is None and gg == 'addiesdive.com', (gc, gg)
m.cell(r, 3).value = 'Shenzhen'
m.cell(r, 7).value = 'addiesdivewatches.com'
m.cell(r, 13).value = m.cell(r, 13).value + (' | Corrigido a pedido do usuário ("corrija", 07/11/2026): C vazio -> Shenzhen; '
    'G addiesdive.com -> addiesdivewatches.com (site do link do Instagram @addiesdivewatches).')
wb.save(SAI)
wb2 = openpyxl.load_workbook(SAI); depois = snap(wb2)
mud = {t: sorted(k for k in set(antes[t]) | set(depois[t]) if antes[t].get(k) != depois[t].get(k)) for t in antes}
print(mud)
ok = mud['Marcas'] == sorted([f'C{r}', f'G{r}', f'M{r}']) and all(not v for t, v in mud.items() if t != 'Marcas')
print('linha', r, '| C:', wb2['Marcas'].cell(r, 3).value, '| G:', wb2['Marcas'].cell(r, 7).value)
print('RESULTADO:', 'OK' if ok else 'FALHOU')
