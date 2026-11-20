import re,urllib.parse
exec(open('build_hermes.py').read())
def core(c):
    m=re.fullmatch(r'W?0?(\d{5,6})WW(00)?',c.replace(' ','').upper())
    if m: return 'W'+m.group(1).zfill(6)
    return re.sub(r'[^A-Z0-9]','',c.upper()).replace('O','0')
seen={};out=[]
for n,c,u,e in R:
    k=core(c) if c else n
    if k in seen: continue
    seen[k]=1; out.append([n,(('W'+core(c)[1:]+'WW00') if c and core(c).startswith('W') and re.fullmatch(r'W\d{6}',core(c)) else c),u,e])
# oficiais
def nome_slug(u):
    s=urllib.parse.unquote(u.rstrip('/').split('/')[-1])
    ref=re.search(r'(W\d{6}WW00)',s).group(1)
    s=s[:s.rfind(ref)].strip('-')
    return s,ref
SIZES={'mini-model':'TPM','small-model':'PM','medium-model':'MM','large-model':'GM','very-small':'TPM'}
for u in open('urls_hermes.txt').read().split():
    s,ref=nome_slug(u)
    if core(ref) in seen: continue
    seen[core(ref)]=1
    mm=re.search(r'(\d+(?:\.\d+)?)-?mm',s.replace('395mm','39.5mm')); tam=(mm.group(1).replace('.',',')+' mm') if mm else ''
    if '29-x-29' in s: tam='29 x 29 mm'
    base=s
    for t in ['-watch','-워치','워치']: base=base.replace(t,'')
    base=re.sub(r'-?(mini-model|small-model|medium-model|large-model|watchlarge-model|large|pm)?-?\d+(\.\d+)?-?(x-29)?-?mm.*$','',base)
    base=re.sub(r'-?(mini-model|small-model|medium-model|large-model|pm)$','',base)
    nm={'arceau':'Arceau','cape-cod':'Cape Cod','cape-cod-automatique':'Cape Cod Automatique','hermes-h08':'H08','heure-h':'Heure H','heure-h-automatique':'Heure H Automatique','slim-d-hermes':"Slim d'Hermès",'slim-dhermes':"Slim d'Hermès",'slim-d-hermes-squelette':"Slim d'Hermès Squelette",'slim-dhermes-squelette':"Slim d'Hermès Squelette",'slim-d-hermes-squelette-lune':"Slim d'Hermès Squelette Lune",'slim-d-hermes-quantieme-perpetuel':"Slim d'Hermès Quantième Perpétuel",'slim-d-hermes-gmt':"Slim d'Hermès GMT",'kelly':'Kelly','faubourg':'Faubourg','hermes-cut':'Hermès Cut','galop-d-hermes':"Galop d'Hermès",'medor':'Médor','medor-joaillerie':'Médor Joaillerie','arceau-petite-lune':'Arceau Petite Lune','arceau-le-temps-suspendu':'Arceau Le Temps Suspendu','arceau-double-h':'Arceau Double H','arceau-aventurine-etoilee':'Arceau Aventurine Étoilée','arceau-squelette':'Arceau Squelette','arceau-le-temps-voyageur':'Arceau Le Temps Voyageur','arceau-chronographe':'Arceau Chronographe','arceau-l-heure-de-la-lune':"Arceau L'Heure de la Lune"}
    if 'ナンタケット' in s: name='Nantucket PM'
    elif 'arceau-double-h-' in s and '34mm' in s: name='Arceau Double H MM'
    else: name=nm.get(base.lower(),base)
    if name==base: print('?? slug',s)
    mod=[v for k2,v in SIZES.items() if k2 in s]
    if mod and name!='Nantucket PM': name+=' '+mod[0]
    out.append([name,ref,u,"Visto no site oficial hermes.com (link da página do produto; a foto não foi obtida porque o site não abre para leitura automática). "+(("Caixa de "+tam+".") if tam else "")])
open('parcial_Hermes_relogios.txt','w').write('\n'.join('|'.join(x) for x in out)+'\n')
print(len(out))
