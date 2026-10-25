import sys,subprocess
# uso: python3 a.py FONTE "NOME" [passada] < MODEL|IMG[|desc]  (linha com 4 campos = Nome|COD|IMG|desc)
src,name=sys.argv[1],sys.argv[2]; pas=sys.argv[3] if len(sys.argv)>3 else '1'
out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    p=l.split('|')
    if len(p)>=4: out.append(l)
    else:
        while len(p)<3: p.append('')
        out.append(f'{name}|{p[0]}|{p[1]}|{p[2]}')
r=subprocess.run(['python3','add.py',src,pas],input='\n'.join(out),text=True,capture_output=True)
print(r.stdout,r.stderr)
