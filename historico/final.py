import json,re
m=json.load(open('merge.json')); items={k:list(v) for k,v in m['items'].items()}; order=m['order']; src=m['src']
d=json.load(open('pass2.json'))
def n(r): return re.sub(r'[^A-Z0-9]','',r.upper()).replace('O','0')
fonte_pass={}
for u in src.values(): fonte_pass.setdefault(u,1)
for pk,passn in (('P',2),('P3',3)):
    for u,lst in d[pk].items():
        fonte_pass.setdefault(u,passn)
        for a,b,c in lst:
            k=n(b) if b else n(a)
            if k in items:
                if items[k][2].startswith('IMGLESS') and c: items[k][2]=c
                continue
            items[k]=[a,b,c or 'IMGLESS'+u,'']; order.append(k); src[k]=u
for r,c in d['better'].items():
    k=n(r)
    if k in items and items[k][2].startswith('IMGLESS'): items[k][2]=c
out=[]
for k in order:
    a,b,c,e=items[k]
    if c.startswith('IMGLESS'):
        u=c[7:]; c=u
        if 'ebay' in u: why='Visto só em anúncio/lista do eBay (link da página, sem foto).'
        elif 'otto.de' in u: why='Visto só na lista da loja Otto (link da página, sem foto e sem referência).'
        elif '/products/' in u and u!='https://www.jowissa.com/products/magno-swiss-mens-watch-j4-276-l': why='Visto só no título da página do produto no site oficial, em resultado de busca (link da página, sem foto).'
        elif 'magno-swiss-mens-watch-j4-276-l' in u: why='Mostrador marrom-dourado com efeito madeira, caixa de 40 mm, data, pulseira de couro preta. Esgotado no site oficial (link da página, sem foto).'
        else: why='Visto só na lista de produtos do site oficial (link da página, sem foto).'
        e=(e+' ' if e else '')+why
    if a=='Seamon 300':
        a='Seamon 300 – edição limitada'
        e=(e+' ' if e else '')+'Conjunto de mergulho 300 m (pulseira de aço e de borracha HNBR), quartzo Ronda com indicador de fim de bateria, vidro de safira; o site oficial diz "limitado a 333 / 111 peças" sem dizer qual vale para cada versão.'
        if b=='J10.079.L': e+=' Mostrador preto raiado, 41 mm, €649,90.'
    out.append((a,b,c,e.strip()))
out.sort(key=lambda x:(x[0],x[1]))
with open('dados_Jowissa.txt','w') as f:
    for a,b,c,e in out: f.write(f'{a}|{b}|{c}|{e.replace("|","/")}\n')
print(len(out), sum(1 for x in out if 'cdn' in x[2] or 'ebayimg' in x[2] or 'check24' in x[2]),'com foto')
# fontes
from collections import Counter
cnt=Counter(src.values())
allf=[]
seen=set()
for l in open('parcial_Jowissa_fontes.txt'):
    p,u,_=l.strip().split('|'); allf.append((1,u))
for pk,passn in (('P',2),('P3',3)):
    for u in d[pk]: allf.append((passn,u))
extra2=['https://www.jowissa.com/collections/sale?page=12','https://www.jowissa.com/collections/schweizer-uhr-damen?page=35','https://www.jowissa.com/collections/schweizer-uhr-damen?page=41','https://www.jowissa.com/collections/mens-watches']+[
'https://www.galaxus.de/en/s8/product/jowissa-tiro-analogue-wristwatch-45-mm-wristwatches-6400751','https://www.galaxus.de/en/s8/product/jowissa-lewy-9-analogue-wristwatch-42-mm-wristwatches-10883084','https://www.galaxus.de/en/s8/product/jowissa-lewy-9-analogue-wristwatch-42-mm-wristwatches-9356401','https://www.galaxus.de/en/s8/product/jowissa-tiro-analogue-wristwatch-38-mm-wristwatches-6401175','https://www.galaxus.de/en/s8/product/jowissa-lewy-6-analogue-wristwatch-42-mm-wristwatches-10883100','https://www.galaxus.de/en/s8/product/jowissa-cosmo-swiss-made-36-mm-wristwatches-52341939','https://www.galaxus.de/en/s8/product/jowissa-lewy-3-analogue-wristwatch-42-mm-wristwatches-10883044','https://www.galaxus.de/en/s8/product/jowissa-alto-analogue-wristwatch-35-mm-wristwatches-9356507','https://www.galaxus.at/en/s8/product/jowissa-alto-analogue-wristwatch-35-mm-wristwatches-9356527','https://www.galaxus.de/en/s8/product/jowissa-tiro-analogue-wristwatch-45-mm-wristwatches-9356552']
for u in extra2: allf.append((2,u))
fontes=[]
for p,u in allf:
    if u in seen: continue
    seen.add(u); fontes.append({"url":u,"passada":p,"novos":cnt.get(u,0)})
# image-only src keys (ebay images, product pages from search) -> add to their page
print(len(fontes), Counter(f['passada'] for f in fontes), sum(f['novos'] for f in fontes))
json.dump(fontes,open('fontes.json','w'),indent=0)
