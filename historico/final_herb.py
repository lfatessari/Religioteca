import json,re,html
FR={'acier':'aço','noir':'preto','bleu':'azul','vert':'verde','blanc':'branco','gris':'cinza','or':'ouro','rose':'rosa','jaune':'amarelo','cuir':'couro','nacre':'madrepérola','argent':'prata','argenté':'prateado','marron':'marrom','taupe':'taupe','champagne':'champanhe','doré':'dourado','dorée':'dourada','rouge':'vermelho','orange':'laranja','caoutchouc':'borracha','textile':'tecido','titane':'titânio','céramique':'cerâmica','kaki':'cáqui','bordeaux':'bordô','beige':'bege','violet':'violeta','miel':'mel','camel':'caramelo','cognac':'conhaque','brun':'marrom','turquoise':'turquesa','maille':'malha','milanaise':'milanesa','diamants':'diamantes','sertie':'cravejada','squelette':'esqueleto','mat':'fosco','forgé':'forjado','forge':'forjado','carbone':'carbono','inoxydable':'inoxidável','glacier':'glacial','sable':'areia','corail':'coral','lune':'lua','phase':'fase','de':'de','la':'a','&':'e','et':'e','316l':'316L','fkm':'FKM','pvd':'PVD','dlc':'DLC','arctic':'ártico','ice':'gelo','quartz':'quartzo','automatique':'automático','chronographe':'cronógrafo','mécanique':'mecânico','petite':'pequeno','seconde':'segundo','bracelet':'pulseira','cadran':'mostrador','tour':'volta','double':'dupla','rosé':'rosé','vintage':'vintage','lumineux':'luminoso','émail':'esmalte','bronze':'bronze','perles':'pérolas','perle':'pérola','grand':'grande','date':'data','gmt':'GMT','gold':'ouro','steel':'aço','black':'preto','blue':'azul','green':'verde','white':'branco','grey':'cinza','silver':'prata'}
def tr(s): return ' '.join(FR.get(w.lower(),w.lower()) for w in s.split())
def tc(s):
    small={'de','du','des','et','la','le','à','en'}
    return ' '.join((x if (x in small and i) else ('Ve' if x=='ve' else x[:1].upper()+x[1:])) for i,x in enumerate(s.lower().split()))
norm=lambda s: re.sub(r'[^A-Z0-9]','',s.upper()).replace('O','0')
mov={'quartz':'quartzo','automatique':'automático','mecanique':'mecânico','solaire':'solar'}
gen={'homme':'masculino','femme':'feminino','mixte':'unissex'}
rows=[];seen=set()
def add(nome,cod,img,e):
    k=norm(cod) if cod else 'N:'+nome.lower()
    if k in seen: return
    seen.add(k); rows.append(f"{nome}|{cod}|{img}|{e.replace('|','/')}")
for p in json.load(open('herb_all.json')):
    if p['product_type']!='Montre': continue
    sku=p['variants'][0]['sku'].strip(); parts=[x.strip() for x in p['title'].split(' - ')]
    nome=tc(' '.join(parts[:2]))
    body=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',p['body_html'] or '')))
    tags=p['tags'] if isinstance(p['tags'],list) else p['tags'].split(', ')
    t={}
    for x in tags:
        if ':' in x: k,v=x.split(':',1); t.setdefault(k,[]).append(v)
    lim=re.search(r'(?:édition|série) limitée (?:à |de )?(\d[\d ]*)',body,re.I)
    if lim: nome+=f' – edição limitada de {lim.group(1).strip()} peças'
    elif re.search(r'(?:édition|série) limitée',body,re.I): nome+=' – edição limitada'
    e=[]
    if parts[2:]: e.append('Versão: '+tr(parts[-1])+'.')
    if 'genre' in t: e.append('Modelo '+'/'.join(gen.get(g,g) for g in t['genre'])+'.')
    if 'mouvement' in t: e.append('Movimento '+', '.join(mov.get(m,m) for m in t['mouvement'])+'.')
    d=re.search(r'(\d{2}(?:[.,]\d)?(?: ?x ?\d{2}(?:[.,]\d)?)?)\s?mm',body)
    if d: e.append(f'Caixa de {d.group(1)} mm.')
    if 'materiau-boitier' in t: e.append('Caixa em '+tr(t['materiau-boitier'][0].replace('-',' '))+'.')
    if 'bracelet' in t: e.append('Pulseira de '+tr(t['bracelet'][0].replace('-',' '))+'.')
    if re.search(r'saphir',body,re.I): e.append('Vidro de safira.')
    wr=re.search(r'(\d+)\s?(?:mètres|m)\s?\((\d+) ?(?:bar|ATM)',body,re.I) or re.search(r'étanche[^.]{0,40}?(\d+)\s?(?:mètres|m\b)',body,re.I)
    if wr: e.append(f'Resistente a {wr.group(1)} m.')
    e.append(f"Preço no site oficial: € {float(p['variants'][0]['price']):.0f}.")
    img=p['images'][0]['src'] if p['images'] else 'https://herbelin.com/products/'+p['handle']
    add(nome,sku,img,' '.join(e))
FAMS=[('newport-carbon-titanium','Newport Carbon Titanium'),('newport-yacht-club','Newport Yacht Club'),('newport-heritage','Newport Heritage'),('newport-slim','Newport Slim'),('newport-diver','Newport Diver'),('newport-trophy','Newport Trophy'),('newport-classics','Newport Classics'),('newport-edition-limitee','Newport – edição limitada'),('newport-limited-edition','Newport – edição limitada'),('newport','Newport'),('cap-camarat-square','Cap Camarat Square'),('cap-camarat-diver','Cap Camarat Diver'),('cap-camarat-squelette','Cap Camarat Squelette'),('cap-camarat','Cap Camarat'),('coffret-antares','Coffret Antarès'),('case-michel-herbelin-antares','Coffret Antarès'),('case-herbelin-antares','Coffret Antarès'),('antares','Antarès'),('art-deco-1925','Art Déco 1925'),('art-deco','Art Déco'),('5eme-avenue','Ve Avenue'),('v-avenue','Ve Avenue'),('ve-avenue','Ve Avenue'),('city-vegan','City Vegan'),('city-lady','City Lady'),('city','City'),('classiques-24h','Classiques 24h'),('classiques','Classiques'),('classique','Classique'),('epsilon','Epsilon'),('equinoxe','Équinoxe'),('galet','Galet'),('fil','Fil'),('inspiration','Inspiration'),('luna-mini','Luna Mini'),('luna','Luna'),('lady-h','Lady H'),('octogone','Octogone'),('perles','Perles'),('trophy-inland','Trophy Inland'),('trophy','Trophy')]
def fam(slug):
    s=re.sub(r'^(montre-)?(michel-)?herbelin-','',slug)
    for k,v in FAMS:
        if s.startswith(k) or ('-'+k+'-') in '-'+s: return v,s
    return 'Michel Herbelin',s
for ref,slug,u,img in json.load(open('lp_new.json')):
    img=img.split(' ')[0]
    f,s=fam(slug); typ=''
    for k,v in (('chronograph','Chronographe'),('chrono','Chronographe'),('moon-phase','Phase de Lune'),('phase-de-lune','Phase de Lune'),('skeleton','Squelette'),('automatic','Automatique'),('automatique','Automatique'),('mechanical','Mécanique'),('quartz','Quartz')):
        if k in s and k.split('-')[0].lower() not in f.lower(): typ=v; break
    nome=f+(' '+typ if typ and 'Coffret' not in f else '')
    lim=re.search(r'(?:limited-edition|edition-limitee)[^0-9]*?(?:numbered-)?(\d{2,4})-(?:copies|exemplaires|pieces)',s)
    if lim: nome+=f' – edição limitada de {lim.group(1)} peças'
    elif ('limited-edition' in s or 'edition-limitee' in s) and 'edição limitada' not in nome: nome+=' – edição limitada'
    desc=s.rsplit('-'+ref.lower()[:5],1)[0].replace('-',' ')
    add(nome,ref,img,'Visto na loja Lepage (França), revendedor oficial: "'+desc+'".')
for ref,name,u,img in json.load(open('oc_new.json')):
    name=' '.join(name.split()[:next((i for i,w in enumerate(name.split()) if w in ('pvd','bico','1n','brac','bangle')),99)])
    add(tc(name.replace('5e avenue','Ve Avenue').replace('5eme avenue','Ve Avenue')),ref,img,'Visto na loja Ocarat (França); referência fora do catálogo atual do site oficial.')
for ref,f,u,img,n in json.load(open('c24_new.json')):
    nm=f or ('Classic' if 'Classic' in n else 'Newport Date Automatique' if '1666' in ref else 'Relógio feminino')
    add(nm,ref,img,'Visto em anúncio na Chrono24: "'+html.unescape(n)[:120]+'".')
man={'Attalage':('Attalage','', 'Feminino, quartzo, aço com banho de ouro; anos 1990, feito na França (anúncio Chrono24).'),
'J Class J-CLASS':('Newport J-Class Chrono Réserve de Marche','','Cronógrafo com indicação de reserva de marcha (anúncio Chrono24).'),
'J Class Day':('Newport J-Class Day Date GMT Réserve de Marche','','Dia, data, GMT e reserva de marcha (anúncio Chrono24).'),
'DIVER Buceador':('Diver (anos 1970)','','Mergulhador vintage dos anos 1970 (anúncio Chrono24).'),
'safari valjoux':('Safari Chronographe Automatique','','Cronógrafo automático com calibre Valjoux 7750 (anúncio Chrono24).'),
'Chronos':('Chronos','','Peça antiga sem uso (NOS), com caixa e papéis (anúncio Chrono24).'),
'Automatique 1680':('Classic Automatique','1680','Automático (anúncio Chrono24).'),
'Grand Sport':('Newport Grand Sport – edição limitada','','Mergulhador "Swiss Made", 100 ATM (anúncio Chrono24).'),
'Newport connect':('Newport Connect','','Relógio híbrido (conectado), feminino (anúncio Chrono24).'),
'Kharga':('Kharga','','Visto só em anúncio na Chrono24.'),
'Ref. 34468':('Newport Chronographe Bicolor','34468','Cronógrafo bicolor (anúncio Chrono24).'),
'Newport 1657':('Newport Automatique','1657','Automático, 38 mm (anúncio Chrono24).'),
'Grand Large':('Grand Large','8230 T','Vintage dos anos 1980, estilo de luneta octogonal (anúncio Chrono24).'),
'Tank Paris':('Tank Paris','','Mecânico, mostrador com algarismos arábicos, peça antiga sem uso (anúncio Chrono24).'),
'Yacht Club Squelette':('Newport Yacht Club Squelette – edição limitada de 500 peças','','Automático esqueleto; exemplar 107/500 à venda (anúncio Chrono24).'),
'Paris ref 2813':('Paris','2813','Vintage dos anos 1980, corda manual Peseux 7001, caixa fina (anúncio Chrono24).'),
'17040 Paris':('Paris','17040','Visto só em anúncio na Chrono24.')}
sel=json.load(open('c24_sel.json'))
for k,(nm,cod,e) in man.items():
    if k in sel: add(nm,cod,sel[k][2],e)
import glob,os
for fx in sorted(glob.glob('extras*.txt')):
    for l in open(fx):
        if l.strip(): n,c,i,e=l.rstrip('\n').split('|'); add(n,c,i,e)
open('dados_Herbelin.txt','w').write('\n'.join(rows)+'\n')
print(len(rows))
