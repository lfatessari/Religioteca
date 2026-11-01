import openpyxl, copy
from openpyxl.worksheet.formula import ArrayFormula
def snap(wb):
    return {ws.title:{c.coordinate:(('ARR',c.value.ref,c.value.text) if isinstance(c.value,ArrayFormula) else c.value) for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb=openpyxl.load_workbook('Relogios_atualizada_354.xlsx'); b=snap(wb); m=wb['Marcas']
r=[i for i in range(2,m.max_row+1) if m.cell(i,1).value=='Döttling']; assert len(r)==1; r=r[0]
c=m.cell(r,13); c.value="Não é marca de relógios: a Döttling faz cofres de luxo e watch winders (desde 1919); nenhum relógio de pulso, de bolso ou de mesa da marca foi encontrado, por isso não há linhas na aba Relógios. Sede em Sindelfingen (perto de Stuttgart), não Maulbronn. J vazio."
c._style=copy.copy(m.cell(r,11)._style)
wb.save('tmp_dottling.xlsx')
a=snap(openpyxl.load_workbook('tmp_dottling.xlsx'))
for t in b:
    mud=[k for k in set(b[t])|set(a[t]) if b[t].get(k)!=a[t].get(k)]; print(t,mud)
print('ARR',sum(1 for v in a['Marcas'].values() if isinstance(v,tuple) and v[0]=='ARR'))
