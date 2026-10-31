import re,json
img=dict(l.rstrip('\n').split('|',1) for l in open('img.tsv') if l.strip())
car=dict(l.rstrip('\n').split('|',1) for l in open('car.tsv') if l.strip())
remove={'gift-set-diy-watchmaking-kit-nh72-dive-watch-with-sapphire-dial-dwc-d02s',
'gift-set-diy-watchmaking-kit-pilot-watch-with-date-vintage-strap-f01-standard-lume',
'gift-set-diy-watchmaking-kit-nh34-gmt-dive-watch-seiko-gmt-movement-ceramic-coke-gmt-bezel-dwc-d03',
'new-year-deal-lucky-bag-dive-watch-diy-kit-with-complete-tools-and-components',
'diy-watch-gift-for-a-couple-watch-experience-mosel-silver-vintage-dress-watch-w-miyota-movement',
'gift-set-skeleton-couple-watch-kit-miyota-citizen-8n24-anthracite-movement-mosel-series',
'diy-watch-gift-for-a-couple-watch-experience-blue-dial-skeleton-vintage-dress-watch-w-miyota-8n24',
'42mm-blue-type-b-bezel-dive-watch-kit-d05-maxi-superlume-dial-with-c3-lume-copy',
'diy-watchmaking-kit-38-5mm-mosel-series-blue-dial-skeleton-vintage-dress-watch-w-miyota-8n24-copy'}
rename={'best-deal-lucky-bag-38mm-expedition-gmt-watch-diy-kit-with-complete-tools-and-components':'38mm Expedition GMT Watch Kit (vendido como Lucky Bag)'}
coll=set(l.split('|')[0] for l in open('prod.tsv').read().splitlines()[:68])
rows=[];seen=set()
for l in open('prod.tsv'):
    if not l.strip(): continue
    h,t,c,e=l.rstrip('\n').split('|')
    if h in remove or h in seen: continue
    seen.add(h)
    t=rename.get(h,t)
    t=re.sub(r'^\[([^\]]+)\]\s*',r'\1 – ',t)
    rows.append([h,t,c])
# strip movement parentheses if unique
def strip(t): return re.sub(r'\s*\((?:TMI|Seiko|Miyota)[^)]*\)','',t).strip()
cand=[strip(t) for h,t,c in rows]
keys=[(x+'|'+r[2]).lower() for x,r in zip(cand,rows)]
from collections import Counter
cnt=Counter(keys)
out=[]
for (h,t,c),x,k in zip(rows,cand,keys):
    name=x if cnt[k]==1 else t
    name=name.replace('|','/')
    u=img.get(h) or ('https://shop.diywatch.club/products/'+h if not h.startswith('x-') else '')
    e=car.get(h,'')
    if not e: e='Kit para montar'
    if not img.get(h): e+='. Foto não coletada (a página da loja não expôs a imagem à leitura automática): link da página do produto na loja oficial'
    if 'Starter Bundle' in name or 'Modding' in name: e+='. Vendido como pacote com peças extras (pulseiras, luneta, inserto ou ferramenta)'
    out.append(f'{name}|{c}|{u}|{e}')
names=[o.split('|')[0]+o.split('|')[1] for o in out]
assert len(names)==len(set(names)), [n for n,v in Counter(names).items() if v>1]
open('dados_DIY Watch Club.txt','w').write('\n'.join(out)+'\n')
print(len(out), sum(1 for h,_,_ in rows if img.get(h)))
json.dump(sorted(coll),open('coll.json','w'))
