import re,json
B="https://www.jowissa.com/cdn/shop/files/"
def n(r): return re.sub(r'[^A-Z0-9]','',r.upper()).replace('O','0')
items={}; order=[]; src={}
def add(line,ref,img,desc,s):
    k=n(ref) if ref else n(line)
    if k in items:
        old=items[k]
        if old[2].startswith('IMGLESS') and not img.startswith('IMGLESS'):
            items[k]=(old[0],ref,img,desc or old[3])
        return
    items[k]=(line,ref,img,desc); order.append(k); src[k]=s
for l in open('parcial_Jowissa_relogios.txt'):
    a,b,c,d=l.rstrip('\n').split('|')
    if 'cdn/shop' not in c: c='IMGLESS'+c
    add(a,b,c,d,'p0')
amap=[('Facet Bee','facet'),('Crystal','facet'),('Facet Strass','facet'),('Facet','facet'),('Safira 12','facet'),('Magic','facet'),('Aura','facet'),('LeWy','lewy'),('Octa 6','chrono'),('Octa 3','lewy'),('Virtuo','man'),('Magno','elegant'),('Seamon','elegant'),('Tiro Ethno','elegant')]
S={'facet':'https://jowissa.com/pages/collection-group/facetted-womens-watches','lewy':'https://www.jowissa.com/en-dk/pages/collection-group/lewy','chrono':'https://jowissa.com/pages/collection-group/chronographs','man':'https://www.jowissa.com/fr-mc/pages/collection-group/man-watch-collections','elegant':'https://www.jowissa.com/pages/collection-group/elegant-timepieces-for-him'}
for l in open('add1.txt'):
    a,b,c=l.rstrip('\n').split('|')
    s='facet' if (a=='Tiro' and b.startswith('J6')) else ('elegant' if a=='Tiro' else next(v for k,v in amap if a.startswith(k)))
    if b=='J4.578.L': s='man'
    add(a,b,B+c,'',S[s])
for l in open('img2.txt'):
    a,b,c,d=l.rstrip('\n').split('|'); add(a,b,c,d,c if 'ebay' in c or 'museum' in c else 'https://www.jowissa.com/products/lux-swiss-mens-watch-j7-098-l')
for f in ('noimg1.txt','noimg2.txt'):
    for l in open(f):
        a,b,u=l.rstrip('\n').split('|')
        add(a,b,'IMGLESS'+u,'',u)
from collections import Counter
print(len(items), sum(1 for k in items if not items[k][2].startswith('IMGLESS')),'com foto')
json.dump({'items':items,'order':order,'src':src},open('merge.json','w'),ensure_ascii=False)
print(Counter(src.values()).most_common())
