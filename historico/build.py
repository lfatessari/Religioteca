import json,re,unicodedata
def n(s,full=False):
    if not full: s=re.sub(r' – .*','',s)
    else: s=s.replace(' – ',' le ')
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower(); s=re.sub(r'[^a-z0-9 ]',' ',s); s=re.sub(r'\b(mm|the)\b',' ',s)
    return ' '.join(s.split())
db=json.load(open('cw_db.json'))
PDF='https://www.christopherward.com/on/demandware.static/-/Library-Sites-cw-library/default/'
hb=[l.rstrip('\n').split('|') for l in open('handbooks.txt')]
img={}
for l in open('hb_img.txt'):
    p=l.rstrip('\n').split('|')
    if len(p)<3: continue
    k=n(p[0],' – ' in p[0])
    if k not in img: img[k]=(p[1],p[2])
    elif not img[k][0] and p[1]: img[k]=(p[1],img[k][1] or p[2])
names=[n(v['nome']) for v in db.values()]
# equivalências manuais: manual -> prefixo de nome já presente
eq={'c60 trident biscay':'trident biscay automatic','c60 trident biscay bronze':'trident biscay bronze','c60 trident biscay gmt':'trident biscay gmt',
'c60 trident 30x30':'trident 30x30','c63 sealander rocks':'c63 sealander rocks','twelve ti':'twelve titanium','c65 dune aeolian automatic':'c65 dune aeolian',
'c1 bel canto negroni':'c1 bel canto classic negroni','ice cream twelves':'twelve 38 ice cream','twelve x':'twelve x ti','twelve x steel':'twelve x steel special edition',
'c63 sealander gmt extreme':'c63 sealander extreme gmt','c63 sealander automatic 2026':'c63 sealander automatic 39','c63 sealander gmt 2026':'c63 sealander gmt 42',
'goodison':'goodison 3 1','c12 loco':'c12 loco','c60 trident 316l orange':'c60 trident 316l orange','c60 trident lumiere':'c60 trident lumiere',
'c63 sh21 blue marine':'c63 sh21 blue marine','c1 loco 7326':'c1 loco 7326','c1 jump hour xv':'c1 jump hour xv','desk diver':'NAO',
'c60 pool diver':'c60 pool diver','c63 valour':'c63 valour','twelve 36 alta gold':'twelve 36 alta gold','c65 gmt worldtimer':'c65 gmt worldtimer'}
eqle={'c63 sealander rocks le edicao limitada':'c63 sealander rocks','c60 trident lumiere le edicao limitada':'c60 trident lumiere yellow'}
skip={'spring colour collection'}  # caderno de cores, não é um modelo
rows=[];vistos=set();hbn=0;hbimg=0
for nm,p in hb:
    k=n(nm); kf=n(nm,True)
    if kf in vistos or k in skip: continue
    vistos.add(kf)
    le=(' – ' in nm)
    tgt=eqle.get(kf) if le else eq.get(k,k)
    if tgt and any(x==tgt or x.startswith(tgt+' ') for x in names): continue
    u,e=img.get(kf,img.get(k,('','')) if not le else ('',''))
    if u: hbimg+=1
    ee=(e+'. ' if e else '')+'Modelo listado entre os manuais do proprietário do site oficial'+('' if u else ' (sem foto encontrada; link do manual em PDF)')
    rows.append((nm,'',u or PDF+p.split('#')[0],ee)); hbn+=1
for k,v in db.items():
    rows.append((v['nome'],v['cod'],v['img'],v['e']))
# nomes únicos para linhas sem código iguais
from collections import Counter
c=Counter((r[0],r[1]) for r in rows)
print('dup',[x for x,m in c.items() if m>1])
with open('dados_ChristopherWard.txt','w') as f:
    for r in rows:
        f.write('|'.join(x.replace('|','/').replace('\n',' ').strip() for x in r)+'\n')
print('total',len(rows),'manuais',hbn,'manuais com foto',hbimg)
