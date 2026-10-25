import re, json
img={}; desc={}
for l in open('catena_img.txt'):
    if not l.strip(): continue
    c,u,e=l.rstrip('\n').split('|'); img[c]=u; desc[c]=e
rows={}  # code -> [name, code, url, E]
order=[]
def gender(g): return {'Men':'Masculino','Women':'Feminino','Unisex':'Unissex'}.get(g,'')
def nm(t):
    t=t.replace('Swiss Made','').replace('Swiss','').replace('Watch','').replace('Limited Edition','')
    t=re.sub(r'\s+',' ',t).strip()
    return t or 'Clássico'
def add(name,code,url,e):
    k=code.upper()
    if k in rows: 
        if not rows[k][2] or 'catawiki.com/en/l' in rows[k][2] or 'ebay.com/itm' in rows[k][2]:
            if url and ('assets' in url or 'finncdn' in url or 'ebayimg' in url or 'lot-art' in url): rows[k][2]=url
        return
    rows[k]=[name,code,url,e]; order.append(k)
# catawiki raw
for l in open('catena_raw.txt'):
    t,c,g,y,u=l.rstrip('\n').split('|')
    if c in ('CAH026',): continue
    n=nm(t)
    if c.startswith('SSH001'): n='Swiss Space – edição limitada de 999 peças'
    if c in img: url=img[c]; e=gender(g)+'. '+desc[c]
    else: url=u; e=f'{gender(g)}. {t} ({y}); visto em leilão da Catawiki (link do anúncio).'
    add(n,c,url,e)
for l in open('catena_finn.txt'):
    p=l.rstrip('\n').split('|')
    if p[0]=='IMG':
        k=p[1].upper()
        if k in rows: 
            if 'catawiki.com/en/l' in rows[k][2] or 'ebay.com/itm' in rows[k][2]: rows[k][2]=p[2]
        continue
    if p[0]=='VINTAGE':
        add('Vintage retangular banhado a ouro 12 k','',p[2],'Feminino. Caixa retangular preta e dourada, banhada a ouro 12 k, desenho dos anos 1970 (anúncio no FINN.no).'); continue
    t,c,g,y,u=p
    n=nm(t)
    if c.startswith('SSH001'): n='Swiss Space – edição limitada de 999 peças'
    e=desc.get(c) or f'{t} ({y}); anúncio de leilão no FINN.no.'
    add(n,c,img.get(c,u),gender(g)+'. '+e)
fam={'A807':'Clássico','B804':'Diamond','A913':'Clássico','B891':'Clássico'}
for l in open('catena_flickr.txt'):
    c,u=l.rstrip('\n').split('|')
    add(fam[c[:4]],c,u,'Foto do catálogo publicada pela loja Gemini Watches no Flickr (por volta de 2010).')
for l in open('catena_extra.txt'):
    n,c,u,e=l.rstrip('\n').split('|')
    if c=='622h': continue
    add(n,c,u,e)
add('Ferradura','D691-1','https://www.ebay.com/itm/137025950564','Visto só no título de anúncio do eBay ("Catena Horseshoe D691-1"; link do anúncio).')
for l in open('catena_zeno.txt'):
    n,c,h=l.rstrip('\n').split('|')
    n=n.replace('Ladies Catena gold bar Credit Suisse 1 gr Chinese lacquer','Barra de ouro Credit Suisse 1 g com laca chinesa (feminino)').replace('Ladies Catena gold bar Credit Suisse 1 gr','Barra de ouro Credit Suisse 1 g (feminino)').replace('Ladies Catena 566','566 (feminino)').replace('Catena ','')
    e='Estoque antigo vendido pela Zeno-Watch Basel; visto só na lista da loja (link da página do produto).'
    if 'Barra de ouro' in n: e='Mostrador com barra de ouro de 1 g do Credit Suisse. '+e
    if c=='583W': e='Tamanhos 583W-32, 583W-30 e 583W-26. '+e
    add(n,c,'https://www.zeno-watch.ch/collections/catena/products/'+h,e)
# names must be unique: name - code unique by code anyway; check names without code
out=[]
seen=set()
for k in order:
    n,c,u,e=rows[k]
    key=(n+' - '+c) if c else n
    assert key not in seen,key; seen.add(key)
    e=e.replace('|','/').strip()
    if e.startswith('. '): e=e[2:]
    out.append('|'.join([n,c,u,e]))
open('dados_Catena.txt','w').write('\n'.join(out)+'\n')
print(len(out))
