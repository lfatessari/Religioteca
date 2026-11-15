import re,sys
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper().replace('O','0'))
rows={};order=[]
def add(n,c,i,e,prio):
    k=norm(c) if c else n.lower()
    if k in rows:
        if prio>rows[k][4]: rows[k]=[n,c,i,e,prio]
        return
    rows[k]=[n,c,i,e,prio];order.append(k)
# extra: opened pages with photo (prio 3)
for fn in ("extra.txt","gg_rows.txt"):
  for l in open(fn):
    if l.strip(): n,c,i,e=l.rstrip('\n').split('|'); add(n,c,i,e,3)
for l in open('p1.txt'):
    n,c,u=l.strip().split('|'); add(n,c,u,'Visto só na lista da loja Watchard (link da página do produto).',1)
lines={'classic':'Appella Classic','diamonds':'Appella Diamonds','diamond':'Appella Classic Diamond','chronograph':'Appella Chronograph','chronograf':'Appella Classic Chronograph','multifunction':'Appella Multifunction','moonphase':'Appella Moonphase','automatic':'Appella Automatic','skeleton':'Appella Skeleton Automatic'}
for l in open('slugs.txt'):
    s=l.strip()
    m=re.match(r'appella-(.*?)-?(l\d+)-([a-z0-9]+)-watch',s)
    pre,a,b=m.groups(); ref=(a+'.'+b).upper()
    nm='Appella '+' '.join(w.capitalize() for w in pre.split('-')) if pre else 'Appella'
    nm=nm.replace('Chronograf','Chronograph')
    add(nm.strip(),ref,'https://watchard.com/'+s,'Visto só no endereço da página do produto na loja Watchard (link da página).',0)
try:
    for l in open('pages.txt'):
        if l.strip(): n,c,u=l.strip().split('|')[:3]; add(n,c,u,'Visto só na página do produto (link da página).',0.5)
except FileNotFoundError: pass
with open('parcial_Appella_relogios.txt','w') as f:
    for k in order:
        n,c,i,e,_=rows[k]; f.write(f'{n}|{c}|{i}|{e}\n')
print(len(order))
