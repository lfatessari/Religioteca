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
    if not it['img']: continue
    n=it['n']; le=[f for f in it['flags'] if f.startswith('LE')]
    if le and 'edição limitada' not in n: n+=f' – edição limitada de {le[0][2:]} peças'
    e=pt(it['spec'])
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
noimg=[it for it in items.values() if not it['img']]
open('/home/claude/trabalho/dados_Jaquet_Droz.txt','w').write('\n'.join(out)+'\n')
open('/home/claude/trabalho/sem_foto.txt','w').write('\n'.join(f"{it['n']}|{it['r']}|{it['spec']}" for it in noimg)+'\n')
print('com foto:',len(out),'sem foto:',len(noimg))
