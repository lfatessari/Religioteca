# Constrói parcial_relogios a partir de raw/*.txt (linhas: titulo | imagem | caracteristicas opcional)
import re,glob,os,json
RX=re.compile(r'(?<![\d-])(\d-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}|\d{3}-\d{2}-\d{2}-\d{2}-\d{2}|\d{2}-\d{2}-\d{2}-\d{2}-\d{2})(?![\d-])')
def img(u):
    u=u.strip()
    m=re.match(r'(.*?)\?crop=center&height=1&v=(\d+)&width=1$',u)
    if m: return f'{m.group(1)}?v={m.group(2)}&width=1200'
    return u
def clean(t):
    t=re.sub(r'(?i)^\s*(glash[uü]e?tte original|go)\s+','',t.strip())
    return t
out={};order=[];fontes=[];SRCOF={}
def weak(u): return not re.search(r'\.(jpe?g|png|webp|avif|gif)(\?|$)|/image/upload/|img\.|cdn\.',u,re.I)
for f in sorted(glob.glob('/home/claude/trabalho/raw/*.txt'),key=os.path.getmtime):
    src=None;n0=len(order)
    for l in open(f,encoding='utf-8'):
        if l.startswith('#SRC'):
            _,pas,url=l.split(None,2); src=(pas,url.strip()); continue
        if '|' not in l or l.startswith('#'): continue
        p=[x.strip() for x in l.rstrip('\n').split('|')]
        while len(p)<3: p.append('')
        t,i,e=p[0],p[1],p[2]
        m=RX.search(t); code=m.group(1) if m else ''
        name=clean(RX.sub('',t)) if code else clean(t)
        name=re.sub(r'\s{2,}',' ',name).strip(' -–,')
        key=re.sub(r'\D','',code)[-10:] if code else 'N:'+name.lower()
        i=img(i) if i.startswith('http') else ''
        if key in out:
            o=out[key]
            if i and (not o[2] or (weak(o[2]) and not weak(i))): o[2]=i
            if not o[3] and e: o[3]=e
            if len(name)>len(o[0]) and code: pass
            continue
        out[key]=[name,code,i,e];order.append(key);SRCOF[key]=len(fontes)
    if src: fontes.append((src[0],src[1],len(order)-n0))
NM={}
import os as _o
if _o.path.exists('/home/claude/trabalho/nomes.txt'):
    for l in open('/home/claude/trabalho/nomes.txt',encoding='utf-8'):
        if '|' in l:
            c,n=l.rstrip('\n').split('|',1); NM[re.sub(r'\D','',c)[-10:]]=n
DROP=[l.rstrip('\n').split('|') for l in open('/home/claude/trabalho/drop.txt',encoding='utf-8') if '|' in l]
for nm,tc in DROP:
    kk='N:'+nm.lower()
    if kk in out:
        if tc:
            tk=re.sub(r'\D','',tc)[-10:]
            if tk in out and (not out[tk][2] or weak(out[tk][2])) and not weak(out[kk][2]): out[tk][2]=out[kk][2]
        del out[kk]; order.remove(kk)
FIX=[(r'(?i)\bpano ?matic ?lunar\b','PanoMaticLunar'),(r'(?i)\bpano ?matic ?calendar\b','PanoMaticCalendar'),(r'(?i)\bpano ?matic ?inverse\b','PanoMaticInverse'),(r'(?i)\bpano ?reserve\b','PanoReserve'),(r'(?i)\bpano ?inverse\b','PanoInverse'),(r'(?i)\bpano ?graph\b','PanoGraph'),(r'(?i)\bpano ?lunar ?tourbillon\b','PanoLunar Tourbillon'),(r'(?i)\bpano ?lunar ?inverse\b','PanoLunarInverse'),(r'(?i)\bpanomatic ?luna\b','PanoMatic Luna'),(r'(?i)\bpanomatic ?counter\b','PanoMatic Counter'),(r'^(?:Lady Collection |Ladies )','')]
def limpa(n):
    for a,b in FIX: n=re.sub(a,b,n)
    n=re.sub(r'\s+(?:on|with)\s+(?:Leather|Rubber|Bracelet|Strap|Synthetic|Nylon|Textil|Grey|Black|Blue|Orange|Exhibition|Solid).*$','',n)
    n=re.sub(r'\s*\((?:Rubber|Short Clasp Version)\)','',n)
    n=re.sub(r'\s+(?:Lush Forest Green|Reed Green|Stainless Steel|Midnight Blue|Rose Gold|Red Gold|White Gold|Platinum|Bi-Color|Steel|SS|Silver|Black|Blue|Green|White|Grey|Gray)(?: Dial)?(?=\s|$)','',n)
    n=re.sub(r'\s+\d{2}(?:\.\d)?\s?mm\b','',n)
    n=re.sub(r'\s+(?:Manual|Moonphase Skeleton)$','',n)
    return re.sub(r'\s{2,}',' ',n).strip(' -')
for k in order:
    o=out[k]
    mm=re.search(r'europeanwatch\.com/watch/.*-(\d{5})(?:\.html)?$',o[2]) or re.search(r'europeanwatch\.com/(\d{5})\.html$',o[2])
    if mm:
        o[2]=f'https://images.europeanwatch.com/images/{mm.group(1)[:2]}/{mm.group(1)}.jpg'
        o[3]=re.sub(r'Visto só no título do anúncio da European Watch \(link da página\)\.','Foto do anúncio da European Watch (vendido).',o[3])
    if o[1]: o[0]=limpa(o[0])
    o[3]=o[3].replace('mostrador com diamantes ','com diamantes, mostrador ')
    if k in NM: o[0]=NM[k]
    if o[2] and not weak(o[2]): o[3]=re.sub(r' ?Visto (?:só )?(?:na|no|em) [^()]*\((?:link d[ao] (?:página|anúncio)|foto não)[^)]*\)\.','',o[3]).strip()
with open('/home/claude/trabalho/parcial_Glashutte_Original_relogios.txt','w') as w:
    for k in order: w.write('|'.join(out[k])+'\n')
print(len(order),'relogios;',sum(1 for k in order if out[k][1]),'com codigo;',sum(1 for k in order if out[k][2]),'com foto')

from collections import Counter as _C
_cnt=_C(SRCOF[k] for k in order)
with open('/home/claude/trabalho/parcial_Glashutte_Original_fontes.txt','w') as w:
    for idx,(p,u,n) in enumerate(fontes): w.write(f'{p}|{u}|{_cnt.get(idx,0)}\n')
print(len(fontes),'fontes')
