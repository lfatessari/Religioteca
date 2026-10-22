import re,sys
NAMES={'140':'Clubmaster Classic Chrono','240':'Clubmaster Classic HMS','142':'Clubmaster Sport Chrono','342':'Clubmaster Sport HMS','536':'Clubmaster Chic','642':'Clubmaster Diver','644':'Clubmaster Diver Pro','740':'Clubmaster Iconic Automatic','924':'Clubmaster Lady','842':'Clubmaster Traveler','2236':'Streamliner Kennedy Large','2030':'Streamliner Kennedy','2025':'Streamliner Kennedy Petite','1838':'Streamliner Kennedy Chrono','1936':'Streamliner Kennedy Auto','3640':'Streamliner Urban HMS Automatic','1740':'Clubmaster Legend Diver Automatic','1639':'Clubmaster Legend Petite Seconde Automatic','5639':'Clubmaster Legend Classic Automatic','5739':'Clubmaster Legend Open Automatic','6642':'Clubmaster Legend Compressor Automatic','4142':'Streamliner Gentleman Driver Chrono','2142':'Clubmaster Regatta Chrono'}
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper()).replace('O','0')
def guess(c):
    p=c.split('.')[0]
    for k in sorted(NAMES,key=len,reverse=True):
        if p.endswith(k): return NAMES[k]
    return 'Briston'
recs={};order=[]
for l in open('raw.txt',encoding='utf-8'):
    if not l.strip(): continue
    n,c,i,e,src=(l.rstrip('\n').split('|')+['']*5)[:5]
    c=c.strip().upper(); key=norm(c) if c else 'N:'+n.lower()
    r=recs.get(key)
    if not r:
        r={'n':n,'c':c,'i':i,'e':e}; recs[key]=r; order.append(key); continue
    if n and (not r['n']): r['n']=n
    pi=lambda u: u and not re.search(r'\.(jpe?g|png|webp)',u.lower())
    if i and (not r['i'] or (pi(r['i']) and not pi(i))): r['i']=i
    if e and (len(e)>len(r['e']) or 'link da página' in r['e']) and not ('link da página' in e and r['e'] and 'link da página' not in r['e']): r['e']=e
out=[]
for k in order:
    r=recs[k]; n=r['n'] or guess(r['c'])
    e=r['e']
    if re.search(r'\.(jpe?g|png|webp)',(r['i'] or '').lower()):
        e=re.sub(r';? ?(foto não aberta|visto)[^;]*\(link da página[^)]*\)','',e).strip(' ;') ; e=re.sub(r'^Visto na página do produto no site oficial','',e).strip(' ;')
    e=e[:1].upper()+e[1:] if e else ''
    out.append(f"{n}|{r['c']}|{r['i']}|{e}")
open(sys.argv[1] if len(sys.argv)>1 else 'parcial_Briston_relogios.txt','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out),'relógios;',sum(1 for x in out if re.search(r'\.(jpe?g|png|webp)',x.split('|')[2].lower())),'com foto')
