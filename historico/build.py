import re,collections
def norm(r): return re.sub(r'[^A-Z0-9]','',r.upper()).replace('O','0')
rows=[];seen=set()
# 1) linhas prontas
for l in open('parcial_Gant_relogios.txt'):
    if not l.strip(): continue
    n,c,u,e=l.rstrip('\n').split('|')
    if c: seen.add(norm(c))
    rows.append([n,c,u,e])
imgs={}
for l in open('imgs.txt'):
    r,u=l.strip().split('|',1); imgs.setdefault(norm(r),u)
specs={}
for l in open('specs.txt'):
    r,d=l.strip().split('|',1); specs.setdefault(norm(r),d)
wsl={}
for l in open('wsl.txt'):
    n,r,u=l.strip().split('|'); wsl.setdefault(norm(r),u)
master=[l.strip().split('|') for l in open('master_refs.txt') if l.strip()]
cut=[i for i,x in enumerate(master) if x[1]=='G305002'][0]
kulta={norm(x[1]) for x in master[:cut]}
wo={norm(x) for x in ['G195006','P730002','P730001','P106005','P106006','K280001','K280003']}|{norm(l.split('|')[0]) for l in open('wo_seen.txt')}
cat={}
for l in open('catalogo2014.txt'):
    n,r,d=l.rstrip('\n').split('|'); cat[norm(r)]=(n,r,d)
names={}
order=[]
for n,r in master:
    k=norm(r)
    if k not in names: names[k]=(n,r); order.append(k)
for k,(n,r,d) in cat.items():
    if k not in names: names[k]=(n,r); order.append(k)
fallback=collections.Counter()
for k in order:
    if k in seen: continue
    seen.add(k)
    n,r=names[k]
    e=specs.get(k,'')
    if k in cat and cat[k][2] and not e: e=cat[k][2]
    if k in imgs: u=imgs[k]
    elif k in kulta or k in wo:
        rl=r.lower(); u=f'https://www.watchesonline.com/media/catalog/product/{rl[0]}/{rl[1]}/{rl}.jpg'; fallback['wo']+=1
    elif k in wsl:
        u=wsl[k]; fallback['pagina']+=1
        e=(e+'. ' if e else '')+'Foto não encontrada; link da página do produto'
    elif k in cat:
        u='https://issuu.com/yukho/docs/gant_time_consumer_catalog_-_2014_f'; fallback['catalogo']+=1
        e=(e+'. ' if e else '')+'Visto no catálogo GANT Time outono/inverno 2014 (link do catálogo)'
    else:
        u=''; fallback['sem']+=1; print('SEM:',n,r)
    rows.append([n,r,u,e])
print(len(rows), fallback)
with open('dados_Gant.txt','w') as f:
    for n,c,u,e in rows: f.write('|'.join(x.replace('|','/') for x in (n,c,u,e))+'\n')
