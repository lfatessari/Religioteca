import sys, json, time, gc, openpyxl
ENT,SAI,CFG=sys.argv[1:4]; cfg=json.load(open(CFG)); t0=time.time()
def snap(p):
    wb=openpyxl.load_workbook(p,read_only=True)
    a=[list(r) for r in wb['Marcas'].iter_rows(max_col=13,values_only=True)]
    b=[list(r) for r in wb['Relógios'].iter_rows(max_col=5,values_only=True)]
    wb.close(); return a,b
m0,r0=snap(ENT)
wb=openpyxl.load_workbook(ENT); m=wb['Marcas']; w=wb['Relógios']
COL='ABCDEFGHIJKLM'; exp_m={}; exp_r={}
for marca,cols in cfg['marcas'].items():
    rows=[i+1 for i,r in enumerate(m0) if r[0]==marca]; assert len(rows)==1,rows; lr=rows[0]
    for c,v in cols.items():
        cell=m.cell(lr,COL.index(c)+1)
        if c=='M':
            old=(cell.value or '').strip(); v=(old+' | ' if old else '')+cfg['prefixo']+' em '+cfg['data_br']+': '+v
        cell.value=v; exp_m[(lr-1,COL.index(c))]=v
for it in cfg['relogios']:
    rows=[i+1 for i,r in enumerate(r0) if r[0]==it['marca'] and r[1]==it['modelo']]; assert len(rows)==1,rows
    ci=COL.index(it['col']); w.cell(rows[0],ci+1).value=it['valor']; exp_r[(rows[0]-1,ci)]=it['valor']
wb.save(SAI); del wb,m,w; gc.collect()
m1,r1=snap(SAI); ok=len(m0)==len(m1) and len(r0)==len(r1)
for (A,B,E_) in ((m0,m1,exp_m),(r0,r1,exp_r)):
    for i,(x,y) in enumerate(zip(A,B)):
        for j in range(len(x)):
            if (i,j) in E_:
                if y[j]!=E_[(i,j)]: ok=False; print('não aplicado',i+1,j)
            elif x[j]!=y[j]: ok=False; print('mudança inesperada',i+1,COL[j])
print('mudadas',len(exp_m),len(exp_r)); print('RESULTADO:','OK' if ok else 'FALHOU',round(time.time()-t0),'s')
