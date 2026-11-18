# uso: python3 add.py fonte_url passada <<< "Nome|COD|img|car" linhas
import sys,re
url,pas=sys.argv[1],sys.argv[2]
def norm(c): return re.sub(r'(\d)A$',r'\1',re.sub(r'[^A-Z0-9]','',c.upper()).replace('O','0'))
R='parcial_Gucci_relogios.txt';F='parcial_Gucci_fontes.txt'
ex={}
try:
  for l in open(R):
    p=l.rstrip('\n').split('|'); ex[norm(p[1]) if p[1] else p[0]]=l
except FileNotFoundError: pass
novos=0;out=open(R,'a')
for l in sys.stdin:
  l=l.strip()
  if not l: continue
  p=l.split('|'); assert len(p)==4,l
  k=norm(p[1]) if p[1] else p[0]
  if k in ex: continue
  ex[k]=l; out.write(l+'\n'); novos+=1
open(F,'a').write(f'{pas}|{url}|{novos}\n')
print('novos',novos,'total',len(ex))
