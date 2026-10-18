import re,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r"\(.*?\)|–.*$","",s)
    s=s.replace('artya','').replace("'",'').replace('saphir','sapphire').replace('crystal','sapphire').replace('&','and')
    s=re.sub(r'\bthe\b|\bwatch\b|\bedition\b','',s)
    return re.sub(r'[^a-z0-9]','',s)
rows=[]
for l in open('parcial_artya_relogios.txt'):
    n,c,i,e=l.rstrip('\n').split('|'); rows.append([n,c,i,e,'p'])
for l in open('extra_relogios.txt'):
    n,c,i,e=l.rstrip('\n').split('|')
    if e=='DUP': continue
    rows.append([n,c,i,e,'x'])
site_map={'chorus-minute-repeater-tourbillon':'Chorus Minute Repeater Tourbillon','minute-repeater-platinum':'Minute Repeater Platinum',
 'delicacy-tourbillon':'Butterfly Delicacy Tourbillon','race-250gto-choco':'250 GTO Choco','shining-star-tourbillon':'Shining Star Tourbillon Set',
 'wolf-tourbillon':'Wolf Tourbillon','sculpted-gold-tourbillon':'Sculpted Gold Tourbillon','raging-skull':'Son of a Gun "Raging Skull"',
 'race-red-oz':'Race Red OZ','race-mahogany':'Race Mahogany – edição limitada','race-blue-bbs':'Race Blue BBS'}
byname={r[0]:r for r in rows}
for l in open('oficial_p1_2.txt'):
    n,s=l.rstrip('\n').split('|'); u='https://www.artya.com/product-page/'+s
    if '(site)' in n:
        if s in site_map:
            r=byname[site_map[s]]; r[2]=u; r[3]=re.sub(r' ?Sem foto direta: link do artigo do Master Horologer\.| ?Visto só na página do produto \(link da página\)\.','',r[3]).strip()
            r[3]=(r[3]+' ' if r[3] else '')+'Foto na página oficial do produto (link da página).'
        continue
    for k,v in (('(2)','– 2ª versão'),('(3)','– 3ª versão')): n=n.replace(k,v)
    rows.append([n,'',u,'Foto na página oficial do produto (link da página).','o'])
# collisions
from collections import defaultdict
g=defaultdict(list)
for r in rows: g[norm(r[0])].append(r)
for k,v in g.items():
    if len(v)>1: print(k,'::',' || '.join(f"{x[4]}:{x[0]}" for x in v))
import pickle;pickle.dump(rows,open('rows.pkl','wb'))
print(len(rows))
