# uso: python3 upg.py <<< "COD|img"   -> troca C (e tira o aviso 'Visto só...') de linhas cujo C não é imagem
import sys,re
def norm(c): return re.sub(r'(\d)A$',r'\1',re.sub(r'[^A-Z0-9]','',c.upper()).replace('O','0'))
up={norm(l.split('|')[0]):l.strip().split('|')[1] for l in sys.stdin if l.strip()}
L=open('parcial_Gucci_relogios.txt').read().splitlines();n=0;out=[]
isimg=lambda u: bool(re.search(r'\.(jpe?g|png|webp|avif)(\?|$)',u,re.I))
for l in L:
  p=l.split('|')
  k=norm(p[1]) if p[1] else None
  if k in up and not isimg(p[2]):
    p[2]=up[k]; p[3]=re.sub(r'\s*Visto só [^.]*\.','',p[3]).strip(); n+=1
  out.append('|'.join(p))
open('parcial_Gucci_relogios.txt','w').write('\n'.join(out)+'\n'); print('trocadas',n)
