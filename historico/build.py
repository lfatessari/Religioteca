import re,glob,sys
# fontes de dados: raw_all.txt (CODE|C|desc|src) e jt_*.txt (urls do jamtangan, uma por linha)
STOP=set('men man mens ladies lady women woman womens couple unisex black silver blue white green red brown gold rose grey gray yellow pink purple orange navy beige cream dark dial skeleton digital automatic chronograph chrono sport analog stainless steel leather rubber strap mesh silicone special limited edition series bundling extra and the of luke darth obiwan boba mandalorian r2d2 grogu padawan jedi kenobi maul vader star death watch quartz multifunction classic passion square rectangular glitter gunmetal mother pearl mop titanium carbon ceramic sapphire full tone two dual moon phase nato canvas transparent camo multicolor multi colour color tosca champagne bronze copper army tan maroon light open heart tourbillon gl pattern with gift set sillicone sunray baby cotton macaron 25th panda tiffany acetate st anniversary v2 dress tank lb'.split())
def split_code(c):
    c=re.sub(r'[\s\-]','',c.upper())
    if c.startswith('AC'): c=c[2:]
    m=re.match(r'^([0-9][0-9A-Z]{3}|S\d{3})(.*)$',c)
    if not m: return None
    b,a=m.group(1),m.group(2)
    CORES={'BR','SS','IP','RG','TB','EP','GP','TR','UR','CA','IG','TE','GU','RO','CB','BU','BP','TU','GA','CU','TP','UB','GE','ZB','BN','GC','SB'}
    if len(a)>=4 and a[0] in 'BLRN' and a[1:3] in CORES: return b,'',a
    if a.startswith('XXV'): return b,'XXV',a[3:]
    if len(a)>=2 and a[:2].isalpha(): return b,a[:2],a[2:]
    return b,'',a
rows={}
def add(code,C,desc,src,coll=''):
    sp=split_code(code)
    if not sp: return
    b,t,r=sp; key=b+t+r
    if key in rows:
        old=rows[key]
        # preferir foto direta (cdn) a link de pagina
        if ('/p/' in old['C'] or '/products/' in old['C']) and not ('/p/' in C or '/products/' in C): old['C']=C
        if len(desc)>len(old['desc']): old['desc']=desc
        if coll and not old['coll']: old['coll']=coll
        return
    rows[key]=dict(b=b,t=t,r=r,C=C,desc=desc,src=src,coll=coll)
for l in open('/home/claude/trabalho/raw_all.txt'):
    p=l.rstrip('\n').split('|')
    if len(p)<4: continue
    add(p[0],p[1],p[2],p[3],p[4] if len(p)>4 else '')
COLL={'-tank-':'Classic Steel Tank','macaron':'Classic Steel Macaron Series','25th-anniversary':'25th Anniversary – edição limitada','classic-slim':'Classic Slim','green-ocean':'Green Ocean','slim-elegance':'Slim Elegance','-tank-':'Classic Steel Tank','primo-steel':'Primo Steel','asteria':'Asteria','x-star-wars':'Star Wars','classic-steel':'Classic Steel','passion':'Passion','smart-gen-3':'AC Smart Gen 3','special-edition':'Special Edition','-digi-ac':'AC DiGi','25th-anniversary':'25th Anniversary','primo':'Primo','sapphire':'Sapphire','ring':'Ring Watch','reminiscence':'Reminiscence'}
for f in sorted(glob.glob('/home/claude/trabalho/jt_*.txt')):
    for u in open(f):
        u=u.strip()
        if 'jamtangan.com' not in u and 'tokopedia.com' not in u: continue
        slug=u.split('/')[-1].replace('.html','').replace(' ','-').replace('%20','-').replace('%C2%A0','-').replace('(','-').replace(')','')
        m=re.search(r'(?:^|-)ac-([0-9][0-9a-z]{3}|s\d{3})-(.*)$',slug)
        if not m: continue
        base=m.group(1); toks=m.group(2).split('-')
        code=[]
        lim=3 if toks and toks[0]=='xxv' else 2
        for t in toks:
            if t in STOP or re.fullmatch(r'\d{4,}',t) or t=='+': break
            code.append(t)
            if len(code)==lim: break
        if not code: continue
        full=(base+''.join(code)).upper()
        pre=slug[:m.start()].replace('alexandre-christie','').strip('-')
        coll=''
        for k,v in COLL.items():
            if k in slug: coll=v; break
        rest=' '.join(toks[len(code):]); rest=re.sub(r'\s\d{4,}$','',rest)
        sp=split_code(full)
        if not sp: continue
        b,t,r=sp
        if 'jamtangan' in u and r:
            rr=re.sub(r'(\D)(\d)$',r'\1-\2',r)
            img=f'https://assets.jamtangan.com/images/product/alexandre-christie/ACF-{b}-{t}{rr}/1l_800x800.jpg'
        else: img=u
        add(full,img,pre.replace('-',' ')+' '+rest,'jamtangan' if 'jamtangan' in u else 'tokopedia',coll)
print(len(rows),file=sys.stderr)
TR=[('chronograph','Cronógrafo'),('chrono','Cronógrafo'),('automatic','Automático'),('mechanical','Automático'),('multifunction','Multifunção'),('multi-function','Multifunção'),('multi ','Multifunção'),('digital','Digital'),('smart','Smartwatch')]
def desc_pt(d,coll):
    d=' '+d.lower()+' '
    out=[]
    for k,v in TR:
        if k in d and v not in out: out.append(v)
    if 'couple' in d or 'pack of 2' in d: out.append('par (casal)')
    elif re.search(r'\b(women|ladies|lady|womens)\b',d): out.append('feminino')
    elif re.search(r'\b(men|man|mens)\b',d): out.append('masculino')
    elif 'unisex' in d: out.append('unissex')
    mm=re.search(r'(\d\d)\s?mm',d)
    if mm: out.append(mm.group(1)+' mm')
    if 'quartz' in d and 'quartzo' not in out: out.append('quartzo')
    if 'sapphire' in d: out.append('vidro de safira')
    if 'skeleton' in d: out.append('mostrador esqueletizado')
    if 'titanium' in d: out.append('titânio')
    if 'carbon' in d: out.append('carbono')
    if 'open heart' in d: out.append('mostrador open heart')
    if 'mother of pearl' in d or ' mop' in d: out.append('mostrador de madrepérola')
    if 'glitter' in d: out.append('mostrador com glitter')
    if 'ceramic' in d: out.append('cerâmica')
    if 'leather' in d: out.append('pulseira de couro')
    elif 'rubber' in d: out.append('pulseira de borracha')
    elif 'silicone' in d: out.append('pulseira de silicone')
    elif 'mesh' in d: out.append('pulseira de malha')
    elif 'stainless steel strap' in d or ' steel' in d: out.append('aço inoxidável')
    s=', '.join(out)
    return (s[0].upper()+s[1:]+'.') if s else ''
out=open('/home/claude/trabalho/dados_alexandre-christie.txt','w')
for key in sorted(rows, key=lambda k:(rows[k]['b'],rows[k]['t'],rows[k]['r'])):
    x=rows[key]
    # pular codigos parciais quando ha variante completa
    if x['src']=='watchreport':
        out.write("Night Vision|AC 9202|"+x['C']+"|Automático Miyota 8217 com data e indicação de 24 horas, caixa de 48 mm, tubos de trítio, vidro mineral abaulado, 50 m, pulseira de couro marrom; resenha de 2016.\n"); continue
    if len(x['r'])<3 and any(k2!=key and k2.startswith(key) for k2 in rows): continue
    coll=x['coll']
    if not coll:
        dl=x['desc'].lower()
        for k,v in [('classic steel','Classic Steel'),('passion','Passion'),('panther x','Panther X'),('asteria','Asteria'),('reminiscence','Reminiscence')]:
            if k in dl: coll=v
    base_nm=f"AC {x['b']}{(' '+x['t']) if x['t'] else ''}"
    nome=(base_nm+' '+coll) if ('–' in coll) else ((coll+' ' if coll else '')+base_nm)
    cod=f"AC {x['b']} {x['t']} {re.sub(r'(\D)(\d)$',r'\1-\2',x['r'])}".replace('  ',' ').strip() if x['r'] else ''
    if len(x['r'])<3:
        cod=''
        nome=nome+(x['r'] if x['r'] else '')+' – '+(desc_pt(x['desc'],coll).rstrip('.').lower() or 'variante')
    e=desc_pt(x['desc'],coll)
    if x['C'].startswith('https://www.nykaafashion') or '/p/' in x['C'] or 'kamalwatch.com/products' in x['C'] or 'tokopedia.com' in x['C'] or 'skywatches.com.sg/' in x['C'] and '/products/' in x['C'] or 'tatacliq.com/' in x['C'] and '/p-' in x['C'] or 'zalora' in x['C']:
        e=(e+' ' if e else '')+'Visto só no título da página do produto (link da página).'
    out.write(f"{nome}|{cod}|{x['C']}|{e}\n")
out.close()
