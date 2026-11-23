import re,sys,collections
files=sys.argv[1:]
def norm(r): return re.sub(r'[^A-Z0-9]','',r.upper()).replace('O','0') if r else ''
MAT=[('white gold','ouro branco'),('rose gold','ouro rosa'),('red gold','ouro vermelho'),('yellow gold','ouro amarelo'),('gold & diamonds','ouro com diamantes'),('gold and diamonds','ouro com diamantes'),('steel & diamonds','aço com diamantes'),('gold & steel','ouro e aço'),('platinum','platina'),('titanium','titânio'),('ceramic','cerâmica'),('steel','aço'),('gold','ouro'),('sapphire case','caixa de safira')]
def pt(spec):
    s=spec; out=[]
    m=re.search(r'(\d\d)\s?mm',s)
    if m: out.append(f'Caixa de {m.group(1)} mm')
    low=s.lower()
    for en,p in MAT:
        if en in low:
            out.append(p); low=low.replace(en,'')
            break
    if 'automatic' in low: out.append('automático')
    if 'manual' in low: out.append('corda manual')
    if 'quartz' in low: out.append('quartzo')
    d=re.search(r'([a-z ,/&-]+?) dial',low)
    if d and d.group(1).strip() not in ('n/a','n/s'): out.append('mostrador '+d.group(1).strip().split(',')[-1].strip())
    DIC=[('slate grey','cinza-ardósia'),('mother-of-pearl','madrepérola'),('mother of pearl','madrepérola'),('grand feu enamel','esmalte Grand Feu'),('petrified algae','alga petrificada'),('ebony wood','ébano'),('grey','cinza'),('gray','cinza'),('blue','azul'),('black','preto'),('white','branco'),('silvered','prateado'),('silver','prateado'),('ivory','marfim'),('onyx','ônix'),('aventurine','aventurina'),('enamel','esmalte'),('opaline','opalino'),('rhodium','ródio'),('cream','creme'),('meteorite','meteorito'),('champagne','champanhe'),('dark','escuro'),('deep','profundo'),('red','vermelho'),('with','com'),('and','e'),('fuchsia','fúcsia'),('spectrolite','espectrolita'),('rutile','rutilo'),('psilomelane','psilomelano'),('jade','jade'),('imperial','imperial'),('cuprite','cuprita'),('engraved','gravado'),('guilloche','guilhochê'),('spessartine','espessartita'),('yellow','amarelo'),('lapis lazuli','lápis-lazúli'),('sapphire','safira'),('opal','opala'),('paillonné','com paillons'),('hand-painted','pintado à mão'),('pink','rosa'),('green','verde'),('arabic','arábico'),('center','centro')]
    for i,o in enumerate(out):
        if o.startswith('mostrador '):
            d=o
            for en,p in DIC: d=re.sub(r'\b'+re.escape(en)+r'\b',p,d)
            out[i]=d
    t=', '.join(out)
    return (t[0].upper()+t[1:]+'.') if t else ''
items=collections.OrderedDict(); byname={}
for f in files:
    for l in open(f,encoding='utf-8'):
        if not l.strip(): continue
        n,r,i,s=(l.rstrip('\n').split('|')+['','','',''])[:4]
        r=r.strip().upper().rstrip('.'); n=n.strip()
        if i and not i.startswith('http'): i=f'https://www.exquisitetimepieces.com/cdn/shop/files/{i}.jpg'
        i=re.sub(r'\?v=\d+$','',i)
        flags=[]; 
        while re.match(r'^(PU|LE\d+);',s): fl,s=s.split(';',1); flags.append(fl)
        key=norm(r) if r else 'N:'+n.lower()
        if key in items:
            it=items[key]
            if not it['img'] and i: it['img']=i
            if len(s)>len(it['spec']): it['spec']=s
            it['flags']|=set(flags); continue
        items[key]=dict(n=n,r=r,img=i,spec=s,flags=set(flags))
# name uniqueness for no-ref items
rows=[];seen=collections.Counter()
for k,it in items.items():
    if not it['img']:
        if it['r']=='J029037141':
            it['img']='https://www.the1916company.com/pre-owned/jaquet-droz/'; it['pre']='Visto só na lista de usados da The 1916 Company (link da página).'
        else:
            it['img']='https://essential-watches.com/jaquet-droz-allwatches'; it['pre']='Visto só na lista de modelos da loja Essential Watches, sem foto (link da página).'
    n=it['n']; le=[f for f in it['flags'] if f.startswith('LE')]
    if le and 'edição limitada' not in n: n+=f' – edição limitada de {le[0][2:]} peças'
    e=pt(it['spec'])
    if it.get('pre'): e=it['pre']+' '+e
    if 'PU' in it['flags']: e='Peça única. '+e
    rows.append([n,it['r'],it['img'],e.strip()])
# disambiguate duplicate names without ref
c=collections.Counter((r[0],r[1]) for r in rows)
idx=collections.Counter()
out=[]
for r in rows:
    if c[(r[0],r[1])]>1:
        idx[(r[0],r[1])]+=1; m=re.search(r'(\d\d) mm',r[3])
        r[0]+=f' – {m.group(1)} mm' if m and idx[(r[0],r[1])]==1 else f' ({idx[(r[0],r[1])]})'
    out.append('|'.join(r))
noimg=[it for it in items.values() if it.get('pre')]
FIX=[('mostrador amarelo gold','mostrador de ouro amarelo'),('mostrador bordeaux esmalte Grand Feu','mostrador de esmalte Grand Feu bordô'),('mostrador brushed cinza','mostrador cinza escovado'),('mostrador alga petrificada','mostrador de alga petrificada'),('mostrador cuprita','mostrador de cuprita'),('mostrador k gold','mostrador de ouro 18k'),('mostrador k  hand-gravado','mostrador de ouro branco 18k gravado à mão'),('branco esmalte','de esmalte branco'),('marfim esmalte Grand Feu','de esmalte Grand Feu marfim'),('marfim esmalte','de esmalte marfim'),('preto esmalte','de esmalte preto'),('profundo azul','azul profundo'),('escuro cinza','cinza-escuro'),('slate com prateado centro','cinza-ardósia com centro prateado'),('safira e smoky quartz','de safira e quartzo fumê'),('preto carbon','de carbono preto'),('preto madrepérola','de madrepérola negra'),('imperial jade','de jade imperial'),('mostrador safira','mostrador de safira'),('mostrador esmalte','mostrador de esmalte'),('mostrador pintado à mão esmalte Grand Feu','mostrador de esmalte Grand Feu pintado à mão')]
txt='\n'.join(out)+'\n'
for a,b in FIX: txt=txt.replace(a,b)
open('/home/claude/trabalho/dados_Jaquet_Droz.txt','w').write(txt)
open('/home/claude/trabalho/sem_foto.txt','w').write('\n'.join(f"{it['n']}|{it['r']}|{it['spec']}" for it in noimg)+'\n')
print('com foto:',len(out),'sem foto:',len(noimg))
