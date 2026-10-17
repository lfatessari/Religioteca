import sys,re
def norm(r): return re.sub(r'[^A-Z0-9]','',r.upper())
known=set()
for f in ['raw_shop.txt','hidden_raw.txt']:
    for l in open(f): known.add(norm(l.split('|')[1]))
try:
    for l in open('extra.txt'): known.add(norm(l.split('|')[1]))
except FileNotFoundError: pass
for r in sys.argv[1:]:
    print(r, 'JA' if norm(r) in known else 'NOVO')
