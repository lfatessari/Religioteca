import sys,re
# filtra linhas Nome|COD|img|desc: descarta se já existe código que começa com COD (série já coberta)
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper().replace('O','0'))
ex=[norm(l.split('|')[1]) for l in open('parcial_casio_relogios.txt') if l.count('|')>=3 and l.split('|')[1]]
for l in sys.stdin:
    p=l.rstrip('\n').split('|')
    if len(p)<4: continue
    n=norm(p[1])
    if any(e.startswith(n) for e in ex): continue
    print(l.rstrip('\n'))
