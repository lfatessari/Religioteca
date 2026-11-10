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
out={};order=[];fontes=[]
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
        key=code.replace('-','').replace('.','') if code else 'N:'+name.lower()
        i=img(i) if i.startswith('http') else ''
        if key in out:
            o=out[key]
            if not o[2] and i: o[2]=i
            if not o[3] and e: o[3]=e
            if len(name)>len(o[0]) and code: pass
            continue
        out[key]=[name,code,i,e];order.append(key)
    if src: fontes.append((src[0],src[1],len(order)-n0))
with open('/home/claude/trabalho/parcial_Glashutte_Original_fontes.txt','w') as w:
    for p,u,n in fontes: w.write(f'{p}|{u}|{n}\n')
print(len(fontes),'fontes')
with open('/home/claude/trabalho/parcial_Glashutte_Original_relogios.txt','w') as w:
    for k in order: w.write('|'.join(out[k])+'\n')
print(len(order),'relogios;',sum(1 for k in order if out[k][1]),'com codigo;',sum(1 for k in order if out[k][2]),'com foto')
