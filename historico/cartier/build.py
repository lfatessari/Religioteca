import re,glob,collections
def norm(c): 
    c=c.strip().upper()
    if c.startswith('CR') and len(c)>6 and c[2] in 'WH': c=c[2:]
    return c
def key(c): return re.sub(r'[^A-Z0-9]','',c).replace('O','0')
COR={'Silver':'prateado','Black':'preto','Blue':'azul','Green':'verde','Pink':'rosa','Champagne':'champanhe','White':'branco','Grey':'cinza','Brown':'marrom','Red':'vermelho','Orange':'laranja','Mother of Pearl':'de madrepérola','Gold':'dourado','Yellow gold':'dourado','Steel':'aço','Palladium':'paládio','Rose gold':'ouro rosa','Silver (solid)':'prateado'}
COL={'tank':'Tank','santos':'Santos','ballonbleu':'Ballon Bleu de Cartier','pasha':'Pasha de Cartier','panthere':'Panthère de Cartier','calibre':'Calibre de Cartier','roadster':'Roadster','drive':'Drive de Cartier','ronde':'Ronde de Cartier','rotonde':'Rotonde de Cartier','cle':'Clé de Cartier'}
R=collections.OrderedDict()
def get(c):
    k=key(c)
    if k not in R: R[k]={'code':c,'name':None,'np':99,'img':'','ip':99,'e':'','ep':99}
    return R[k]
def put(c,name,np,img,ip,e,ep):
    r=get(c)
    if name and np<r['np']: r['name'],r['np']=name,np
    if img and ip<r['ip']: r['img'],r['ip']=img,ip
    if e and ep<r['ep']: r['e'],r['ep']=e,ep
noc=[]
def explicit(f,pri):
    for l in open(f,encoding='utf-8'):
        if not l.strip(): continue
        n,c,i,e=(l.rstrip('\n').split('|')+['',''])[:4]
        if c.strip(): put(norm(c),n,pri,i,pri+5 if 'collectorsquare.com/de/uhren/cartier/' in i and 'medias' not in i else pri,e,pri)
        else: noc.append([n,'',i,e])
explicit('p2.txt',1); explicit('p3.txt',1); explicit('extra.txt',2)
for f,p in (('wos_bb1.txt',3),('wos_all.txt',3)):
    for l in open(f,encoding='utf-8'):
        n,c,i=l.rstrip('\n').split('|')
        n=re.sub(r'^Cartier ','',n); n=re.sub(r',?\s*Ref\. \w+$','',n)
        put(norm(c),n,p,i,1,'',99)
for l in open('watchswiss_panthere.txt',encoding='utf-8'):
    n,c,i=l.rstrip('\n').split('|')
    ok=i and key(c) in key(i)
    if not ok: i='https://www.watchswiss.com/brands/cartier/panthere-de-cartier-collection/'; ok=True
    put(norm(c),n,4,i,2 if 'assetcdn' in i else 18,'',99)
for l in open('coveted.txt',encoding='utf-8'):
    n,c,i=l.rstrip('\n').split('|')
    put(norm(c),n,5,i,3,'',99)
for l in open('cartiercom_search.txt',encoding='utf-8'):
    n,c,i,e=l.rstrip('\n').split('|')
    put(norm(c),n,6,i,8,e,5)
for l in open('wc_names.txt',encoding='utf-8'):
    n,c=l.rstrip('\n').split('|'); col=n.split()[0].lower().replace('è','e').replace('-dumont','')
    pg={'baignoire':'https://watchcharts.com/watches/brand/cartier/baignoire','pasha':'https://watchcharts.com/watches/brand/cartier/pasha','drive':'https://watchcharts.com/watches/brand/cartier/drive','calibre':'https://watchcharts.com/watches/brand/cartier/calibre','roadster':'https://watchcharts.com/watches/brand/cartier/roadster','panthere':'https://watchcharts.com/watches/brand/cartier/panth%c3%a8re','santos':'https://watchcharts.com/watches/brand/cartier/santos'}.get(col,'')
    put(norm(c),n,7,pg,20,'Visto só na lista da WatchCharts (link da página).' if pg else '',20)
for f in glob.glob('loupe_*.txt'):
    col=COL[f[6:-4]]
    for l in open(f,encoding='utf-8'):
        d,c,i=l.rstrip('\n').split('|')
        img=f'https://pub-e6e8b7c57f1149b3a255036538c65266.r2.dev/watches/{i}.jpg' if i else ''
        e=f'Mostrador {COR.get(d,d.lower())}.' if d else ''
        pgs={'tank':'https://www.loupe.watch/watches/cartier/tank','santos':'https://www.loupe.watch/watches/cartier/santos','ballonbleu':'https://www.loupe.watch/prices/cartier/ballon-bleu','pasha':'https://www.loupe.watch/watches/cartier/pasha','panthere':'https://www.loupe.watch/prices/cartier/panth-re','calibre':'https://www.loupe.watch/prices/cartier/calibre','roadster':'https://www.loupe.watch/prices/cartier/roadster','drive':'https://www.loupe.watch/watches/cartier/drive','ronde':'https://www.loupe.watch/prices/cartier/ronde','rotonde':'https://www.loupe.watch/watches/cartier/rotonde','cle':'https://www.loupe.watch/watches/cartier/cle'}
        if not img: img=pgs[f[6:-4]]; e=(e+' ' if e else '')+'Visto só na lista do loupe.watch (link da página).'; put(norm(c),col,8,img,19,e,19)
        else: put(norm(c),col,8,img,4,e,6)
# remove duplicates sem código já cobertos
drop={'Privé Tank Normale – platina, mostrador bordô','Privé Tortue Chronographe Monopoussoir – platina','Privé Crash Squelette – edição limitada de 150 peças','Privé Tank Chinoise – edição limitada de 150 peças'}
noc=[x for x in noc if x[0] not in drop]
out=[]
for r in R.values():
    n=r['name'] or 'Cartier'
    e=r['e']
    im=r['img'].lower().split('?')[0]
    isimg=im.endswith(('.jpg','.jpeg','.png','.webp')) or 'r2.dev' in im or '/cdn/shop/' in im
    if isimg: e=re.sub(r'\s*Visto só[^.]*\([^)]*\)\.','',e).strip()
    if not isimg and 'Visto só' not in e: e=(e+' ' if e else '')+'Visto só na página da fonte (link da página).'
    out.append([n,r['code'],r['img'],e])
out+=noc
# ordenar por nome
out.sort(key=lambda x:(x[0].lower(),x[1]))
names=collections.Counter((x[0] if not x[1] else x[0]+x[1]) for x in out)
assert all(v==1 for v in names.values()), [k for k,v in names.items() if v>1]
with open('../dados_cartier.txt','w',encoding='utf-8') as f:
    for x in out: f.write('|'.join(s.replace('|','/') for s in x)+'\n')
print(len(out),'relógios;',sum(1 for x in out if x[2]),'com imagem/link;',sum(1 for x in out if not x[1]),'sem código')
