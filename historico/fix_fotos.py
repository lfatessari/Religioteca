import openpyxl,sys
from openpyxl.worksheet.formula import ArrayFormula
from urllib.parse import quote
ENT,SAI,MAP=sys.argv[1:4]
def enc(u): return quote(u, safe=":/?&=%#+~;,@!$'()*[]-._")
mp=dict(l.rstrip('\n').split('|',1) for l in open(MAP) if '|' in l)
def snap(wb): return {ws.title:{c.coordinate:(('ARR',c.value.ref,c.value.text) if isinstance(c.value,ArrayFormula) else c.value) for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb=openpyxl.load_workbook(ENT); b=snap(wb); w=wb['Relógios']
done=[];alvo=set()
for r in range(2,w.max_row+1):
    if w.cell(r,1).value=='F.P. Journe' and w.cell(r,2).value in mp:
        u=enc(mp[w.cell(r,2).value]); w.cell(r,3).value=u; w.cell(r,3).hyperlink=u; done.append(w.cell(r,2).value); alvo.add(f'C{r}')
wb.save(SAI)
wb2=openpyxl.load_workbook(SAI); a=snap(wb2)
mud=[(t,k) for t in b for k in set(b[t])|set(a[t]) if b[t].get(k)!=a[t].get(k)]
print('trocadas',len(done),'de',len(mp)); print('mudanças fora das células-alvo:',[m for m in mud if not (m[0]=='Relógios' and m[1] in alvo)])
print('ArrayFormula',sum(1 for c in wb2['Marcas']._cells.values() if isinstance(c.value,ArrayFormula)))
w2=wb2['Relógios']; print('hyperlinks ok:',all(w2[k].hyperlink and w2[k].hyperlink.target==w2[k].value for k in alvo))
