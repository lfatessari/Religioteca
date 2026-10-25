import sys,re
# entrada: CODE|nome ; saída para a.py com link da página
P=sys.argv[1]; pref=sys.argv[2]; V=sys.argv[3]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    c,*r=l.split('|')
    c=re.sub(r'(U?EF|ER|DR|DF|JF|PR|CR)$','',c.strip())
    nm=pref+' '+re.match(r'^([A-Z]+-?[A-Z]*\d+)',c).group(1) if re.match(r'^([A-Z]+-?[A-Z]*\d+)',c) else pref
    print(f'{nm}|{c}|{P}|{V}')
