import json,re
P=json.load(open('/home/claude/trabalho/lg/prod.json'))
X=json.load(open('/home/claude/trabalho/lg/extra.json')) if __import__('os').path.exists('/home/claude/trabalho/lg/extra.json') else {}
FIX={'HYDROCONQUEST':'HydroConquest','DOLCEVITA':'DolceVita','PRIMALUNA':'PrimaLuna','ULTRA‑CHRON':'Ultra-Chron','ULTRA-CHRON':'Ultra-Chron','GMT':'GMT','BIGEYE':'BigEye','MAJETEK':'Majetek','LONGINES':'Longines','DE':'de','ODERMATT':'Odermatt','FLYBACK':'Flyback'}
def tc(s):
    out=[]
    for w in s.split():
        out.append(FIX.get(w, w.capitalize() if not w.isdigit() else w))
    t=' '.join(out)
    t=re.sub(r'-([a-z])',lambda m:'-'+m.group(1).upper(),t)
    return t
lines=[]
for sku,v in sorted(P.items(), key=lambda kv:(kv[1]['model'],kv[0])):
    m=re.search(r'Ø\s*([\d.]+)\s*mm',v['name'] or '')
    e=[]
    if v.get('color'): e.append(f"Mostrador {v['color'].replace('|','/')}.")
    if m: e.append(f"Caixa de {m.group(1).replace('.',',')} mm.")
    if v.get('price'):
        cur={'USD':'US$','GBP':'£'}.get(v.get('cur'),v.get('cur'))
        pais={'USD':'dos EUA','GBP':'do Reino Unido'}.get(v.get('cur'),'')
        e.append(f"Preço no site oficial {pais}: {cur} "+f"{int(v['price']):,}".replace(',','.')+" (nov/2026).")
    e.append('Modelo atual do catálogo oficial (longines.com).')
    lines.append(f"{tc(v['model'])}|{sku}|{v['image']}|{' '.join(e)}")
for sku,v in X.items():
    lines.append(f"{v['nome']}|{sku}|{v['img']}|{v['e']}")
import os
if os.path.exists('/home/claude/trabalho/lg/vintage.json'):
    for sku,v in json.load(open('/home/claude/trabalho/lg/vintage.json')).items():
        lines.append(f"{v['nome']}|{v['code']}|{v['img']}|{v['e']}")
if os.path.exists('/home/claude/trabalho/lg/outros.txt'):
    lines+= [l for l in open('/home/claude/trabalho/lg/outros.txt').read().split('\n') if l.strip()]
open('/home/claude/trabalho/dados_Longines.txt','w').write('\n'.join(lines)+'\n')
print(len(lines)); print('\n'.join(lines[:3])); print(lines[-1])
