import openpyxl,copy,sys
from openpyxl.worksheet.formula import ArrayFormula
ENT,SAI=sys.argv[1:3]
def snap(wb):
    return {ws.title:{c.coordinate:(('ARR',c.value.ref,c.value.text) if isinstance(c.value,ArrayFormula) else c.value) for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb=openpyxl.load_workbook(ENT); b=snap(wb)
w=wb['Relógios']; m=wb['Marcas']
maxc=max(c.column for c in w._cells.values())
rows=[r for r in range(2,w.max_row+1) if w.cell(r,1).value=='ETA']
a,z=rows[0],rows[-1]; n=z-a+1; assert rows==list(range(a,z+1))
mr=w.max_row
before_rows=[[ (w.cell(r,c).value) for c in range(1,maxc+1)] for r in range(2,mr+1) if w.cell(r,1).value!='ETA']
for r in range(z+1,mr+1):
    for c in range(1,maxc+1):
        s=w.cell(r,c); d=w.cell(r-n,c)
        d.value=s.value; d._style=copy.copy(s._style)
        d.hyperlink=copy.copy(s.hyperlink) if s.hyperlink else None
        if d.hyperlink: d.hyperlink.ref=d.coordinate
for r in range(mr-n+1,mr+1):
    for c in range(1,maxc+1):
        cell=w.cell(r,c); cell.value=None; cell.hyperlink=None
w.delete_rows(mr-n+1,n)
lm=[r for r in range(2,m.max_row+1) if m.cell(r,1).value=='ETA'][0]
old=m.cell(lm,13).value or ''
m.cell(lm,13).value=('Não é marca de relógios (fabricante de movimentos): as 894 linhas de calibres foram removidas da aba Relógios a pedido do usuário em 04/11/2026. '+old).strip()
wb.save(SAI)
wb2=openpyxl.load_workbook(SAI); a2=snap(wb2); w2=wb2['Relógios']
after_rows=[[w2.cell(r,c).value for c in range(1,maxc+1)] for r in range(2,w2.max_row+1)]
print('max_row',mr,'->',w2.max_row,'| removidas',n,'| ETA restantes',sum(1 for r in after_rows if r[0]=='ETA'))
print('demais linhas iguais e na mesma ordem:',before_rows==after_rows)
bad=[r for r in range(2,w2.max_row+1) if w2.cell(r,3).value and w2.cell(r,3).hyperlink and w2.cell(r,3).hyperlink.target!=w2.cell(r,3).value]
print('hyperlinks divergentes (coluna C):',len(bad), bad[:5])
for t in b:
    if t=='Relógios': continue
    mud=[k for k in set(b[t])|set(a2[t]) if b[t].get(k)!=a2[t].get(k)]
    print(t,'mudanças:',mud)
print('ArrayFormula:',sum(1 for c in wb2['Marcas']._cells.values() if isinstance(c.value,ArrayFormula)))
