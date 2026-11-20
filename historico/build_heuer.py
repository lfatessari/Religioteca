import sys;sys.path.insert(0,'/home/claude/trabalho')
import importlib, heuer_base, heuer_fotos
from heuer_base import RAW,MOV
from heuer_fotos import F
OTD='https://onthedash.com/docs/Master_Reference_Table.htm'
extra=[l.rstrip('\n').split('|') for l in open('/home/claude/trabalho/heuer_extra.txt',encoding='utf-8') if l.strip()] if __import__('os').path.exists('/home/claude/trabalho/heuer_extra.txt') else []
out=[];nofoto=0
for r in [l.split('|') for l in RAW.strip().split('\n')]:
  nome,ref,anos,mov,caixa,mostr=r
  nome=nome.replace('Mergulho','Diver')
  code='' if ref=='sem ref' else ref
  foto=F.get(f'{r[0]}|{ref}') or F.get(ref)
  m=MOV[mov]
  e=f"{mostr[0].upper()+mostr[1:]}. Caixa {caixa}"+(f"; movimento {m}" if m else "")+f". Anos de catálogo: {anos}."
  if not foto:
    foto=OTD; nofoto+=1
    e+=" Foto não achada: link da tabela de referências da OnTheDash."
  out.append(f"Heuer {nome}|{code}|{foto}|{e}".replace('Heuer Heuer','Heuer') if False else f"{nome}|{code}|{foto}|{e}")
for x in extra: out.append('|'.join(x))
open('/home/claude/trabalho/dados_Heuer.txt','w',encoding='utf-8').write('\n'.join(out)+'\n')
open('/home/claude/trabalho/parcial_Heuer_relogios.txt','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out),'sem foto:',nofoto)
