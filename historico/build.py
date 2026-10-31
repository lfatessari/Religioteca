import sys
img=dict(l.rstrip('\n').split('|',1) for l in open('img.tsv') if l.strip())
car={}
try: car=dict(l.rstrip('\n').split('|',1) for l in open('car.tsv') if l.strip())
except: pass
out=[];seen=set()
for l in open('prod.tsv'):
    if not l.strip(): continue
    h,t,c,e=l.rstrip('\n').split('|')
    if h in seen: continue
    seen.add(h)
    url=img.get(h) or ('https://shop.diywatch.club/products/'+h)
    e=car.get(h,e)
    if not img.get(h) and not h.startswith('http'):
        e=(e+'. ' if e else '')+'Foto não coletada: link da página do produto na loja oficial'
    out.append(f'{t}|{c}|{url}|{e}')
open('parcial_DIY Watch Club_relogios.txt','w').write('\n'.join(out)+'\n')
print(len(out))
