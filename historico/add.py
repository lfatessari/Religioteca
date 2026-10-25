import sys,re,os
src=sys.argv[1]; passada=sys.argv[2] if len(sys.argv)>2 else '1'
R='parcial_casio_relogios.txt'; F='parcial_casio_fontes.txt'
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper().replace('O','0'))
def isimg(u): return bool(re.search(r'\.(png|jpe?g|webp|gif)(\?|$)',u,re.I))
d={}
if os.path.exists(R):
    for l in open(R):
        p=l.rstrip('\n').split('|')
        if len(p)==4: d[norm(p[1]) if p[1] else norm(p[0])]=p
new=0;upd=0
for l in sys.stdin:
    l=l.strip()
    if not l or l.startswith('#'): continue
    p=[x.strip() for x in l.split('|')]
    while len(p)<4: p.append('')
    p=p[:4]
    p[2]=re.sub(r'\.transform/.*$','',p[2])
    k=norm(p[1]) if p[1] else norm(p[0])
    if k in d:
        o=d[k]
        if '–' in p[0] and '–' not in o[0]: o[0]=p[0]; upd+=1
        if p[2] and isimg(p[2]) and not isimg(o[2]):
            o[2]=p[2]; o[3]=p[3] or re.sub(r'Visto só.*$','',o[3]).strip(); upd+=1
        elif not o[3] and p[3]: o[3]=p[3]
        continue
    d[k]=p; new+=1
open(R,'w').write(''.join('|'.join(v)+'\n' for v in d.values()))
open(F,'a').write(f'{passada}|{src}|{new}\n')
print('novos',new,'fotos melhoradas',upd,'total',len(d))
