import sys,subprocess,re
# uso: python3 b.py FONTE "NOME" [passada] < (1a linha prefixo; depois [MODEL|]path[|desc]) ; linha "N:nome" muda o nome
src,name=sys.argv[1],sys.argv[2]; pas=sys.argv[3] if len(sys.argv)>3 else '1'
lines=[l.strip() for l in sys.stdin if l.strip()]
pre=lines[0].split('|')[-1]
out=[]
for l in lines[1:]:
    if l.startswith('N:'): name=l[2:]; continue
    p=l.split('|')
    if p[0]=='MODEL' or '/' not in p[0] and len(p)>1 and '/' in p[1]: m=p[0]; path=p[1]; desc=p[2] if len(p)>2 else ''
    else: m=''; path=p[0]; desc=p[1] if len(p)>1 else ''
    if m in ('','MODEL'):
        seg=path.split('/')[3]
        m=seg.upper().replace('--','-')
    nm=name
    if name.startswith('AUTO:'):
        mm=re.match(r'^([A-Z]+-?[A-Z]*\d+)',m)
        nm=name[5:]+' '+(mm.group(1) if mm else m.split('-')[0])
    out.append(f'{nm}|{m}|{pre}{path}|{desc}')
r=subprocess.run(['python3','add.py',src,pas],input='\n'.join(out),text=True,capture_output=True)
print(r.stdout,r.stderr)
