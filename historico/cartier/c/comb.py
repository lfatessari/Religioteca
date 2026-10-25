import re,collections,openpyxl
def key(c):
    c=c.strip().upper()
    if c.startswith('CR') and len(c)>6 and c[2] in 'WH': c=c[2:]
    return re.sub(r'[^A-Z0-9]','',c).replace('O','0')
def isimg(u):
    u=u.lower().split('?')[0]; return u.endswith(('.jpg','.jpeg','.png','.webp')) or '/cdn/shop/' in u
files=[('v.txt',1),('s1.txt',2),('s2.txt',2),('cov2.txt',3),('cov3.txt',3),('cov4.txt',3),('cov5.txt',3),('cov6.txt',3),('cov7.txt',3),('lb.txt',4)]
D=collections.OrderedDict(); noc=[]
for f,p in files:
    for l in open(f,encoding='utf-8'):
        if not l.strip(): continue
        n,c,i,e=(l.rstrip('\n').split('|')+['',''])[:4]
        c=c.strip().upper()
        if c.startswith('CR') and len(c)>6 and c[2] in 'WH': c=c[2:]
        if not c: noc.append([n,'',i,e]); continue
        k=key(c); r=D.setdefault(k,{'c':c,'n':None,'np':9,'i':'','ip':9,'e':'','ep':9})
        if n and p<r['np']: r['n'],r['np']=n,p
        ip=(0 if isimg(i) else 5)+p
        if i and ip<r['ip']: r['i'],r['ip']=i,ip
        if e and p<r['ep']: r['e'],r['ep']=e,p
wb=openpyxl.load_workbook('../../Relogios_atualizada_233.xlsx',read_only=True); w=wb['Relógios']
ex={}
for i,row in enumerate(w.iter_rows(min_row=35661,max_row=36665,max_col=5,values_only=True),35661):
    b=row[1]; m=re.match(r'^(.*) - (\S+)$',b)
    if m: ex[key(m.group(2))]=(i,m.group(1),m.group(2),row[2] or '',row[4] or '')
    else: ex['N:'+b]=(i,b,'',row[2] or '',row[4] or '')
GEN={'Tank','Santos','Ballon Bleu de Cartier','Pasha de Cartier','Panthère de Cartier','Calibre de Cartier','Roadster','Drive de Cartier','Ronde de Cartier','Rotonde de Cartier','Clé de Cartier','Baignoire','Tortue','Cartier'}
new=[];imp=[]
for k,r in D.items():
    if k in ex:
        row,nm,cd,img,e=ex[k]; ch={}
        if nm in GEN and r['n'] and r['n']!=nm: ch['B']=f"{r['n']} - {cd}"
        if not isimg(img) and r['i'] and isimg(r['i']): ch['C']=r['i']; ch['E']=re.sub(r'\s*Visto só[^.]*\([^)]*\)\.','',e).strip() or None
        if ch: imp.append((row,ch))
    else:
        e=r['e']
        if not isimg(r['i']) and 'Visto só' not in e: e=(e+' ' if e else '')+'Visto só na página da fonte (link da página).'
        new.append([r['n'] or 'Cartier',r['c'],r['i'],e])
exn={v[1] for kk,v in ex.items() if kk.startswith('N:')}
for x in noc:
    if x[0] not in exn: new.append(x)
new.sort(key=lambda x:(x[0].lower(),x[1]))
with open('../../dados_cartier_c.txt','w',encoding='utf-8') as f:
    for x in new: f.write('|'.join(s.replace('|','/') for s in x)+'\n')
import json; json.dump(imp,open('imp.json','w'),ensure_ascii=False)
print('novos',len(new),'melhorias',len(imp),'renomes',sum('B' in c for _,c in imp),'fotos',sum('C' in c for _,c in imp))
