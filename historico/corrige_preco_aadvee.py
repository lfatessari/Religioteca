import openpyxl, sys
E, S = 'Relogios_atualizada_558.xlsx', 'Relogios_atualizada_559.xlsx'
wb = openpyxl.load_workbook(E); m = wb['Marcas']
rows = [r for r in range(1, m.max_row + 1) if m.cell(r, 1).value == 'Aadvee']
assert len(rows) == 1, rows
r = rows[0]; print('linha', r, 'E', m.cell(r, 5).value, 'F', m.cell(r, 6).value)
assert m.cell(r, 5).value is None and m.cell(r, 6).value is None
m.cell(r, 5).value = 2
m.cell(r, 6).value = 2355
m.cell(r, 13).value = m.cell(r, 13).value + ' Preço em 11/11/2026 (v559): a própria marca respondeu num comentário do Instagram (review paga do @allabouthorology, instagram.com/allabouthorology/reel/C7tABHuS9Pa, resposta de ~fev/2025): "The AA-01 is priced at INR39,531". Convertido a ₹1 = R$ 0,05957 (Wise, 11/11/2026): R$ 2.355, faixa 2. O site não publica preço.'
wb.save(S); del wb
A = openpyxl.load_workbook(E); B = openpyxl.load_workbook(S); mud = []
for t in A.sheetnames:
    a = {c.coordinate: (c.value, c.hyperlink.target if c.hyperlink else None) for c in A[t]._cells.values()}
    b = {c.coordinate: (c.value, c.hyperlink.target if c.hyperlink else None) for c in B[t]._cells.values()}
    for k in set(a) | set(b):
        if a.get(k, (None, None)) != b.get(k, (None, None)): mud.append((t, k))
print(sorted(mud))
ok = set(mud) == {('Marcas', f'E{r}'), ('Marcas', f'F{r}'), ('Marcas', f'M{r}')}
print('RESULTADO:', 'OK' if ok else 'FALHOU'); sys.exit(0 if ok else 1)
