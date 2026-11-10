import json,re,glob,os
os.chdir('/home/claude/trabalho')
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper().replace('O','0'))
M={}  # key -> dict(nome,cod,img,e,src)
def add(nome,cod,img,e='',src='',force_img=False,kx=''):
    k=(norm(cod) if cod else 'N:'+nome.lower())+kx
    if k in M:
        r=M[k]
        if (not r['img'] or force_img) and img: r['img']=img
        if not r['e'] and e: r['e']=e
        return False
    M[k]=dict(nome=nome,cod=cod,img=img,e=e,src=src); return True
# 1) official store collection pages (short names)
short={}
for f in sorted(glob.glob('raw/fc_all_p*.json')):
    for x in json.load(open(f))['json']['p']:
        short[norm(x['r'])]=(x['t'].strip(),x['r'].strip(),x['i'].split('&width')[0])
for l in open('raw/fc_all_p1_manual.txt'):
    r,t=l.strip().split('|'); short.setdefault(norm(r),(t,r,''))
# long titles from products.json / oembed (give size + movement)
longt={}
for f in ['raw/gw_pj1.txt','raw/gw_all_p4.txt']:
    for l in open(f):
        t,i=l.strip().split('|'); r=t.split()[-1]; longt[norm(r)]=(t,i.split('?')[0])
for l in open('raw/gw_airman.txt'):
    pass
def e_from_long(t):
    m=re.search(r"(\d+)mm\s+(Automatic|Quartz)?",t)
    if not m: return ''
    s=f"Caixa de {m.group(1)} mm"
    if m.group(2)=='Automatic': s+=', movimento automático'
    elif m.group(2)=='Quartz' or 'Quartz' in t: s+=', movimento de quartzo'
    if 'Bronze' in t: s+=', caixa de bronze'
    return s+'.'
keys=set(short)|set(longt)
for k in sorted(keys):
    if k in short: t,r,i=short[k]
    else:
        lt=longt[k][0]; r=lt.split()[-1]
        t=re.sub(r"^Glycine (Men's|Women's|Unisex) ","",lt); t=re.sub(r"\s+\d+mm.*$","",t)
        i=''
    if k in longt:
        e=e_from_long(longt[k][0]); i=i or longt[k][1]
    else:
        mm=re.search(r'\b(36|39|40|42|43|44|46|48)\b',t); e=''
    t=t.replace(' (sold out)','')
    t=re.sub(r'\\\\?GL\d+$','',t).strip()
    if not i and not any(x in t for x in ('Field','Box Ceramic')): i=f'https://www.glycinewatches.com/cdn/shop/files/{r}.png'
    add(t,r,i,e,'oficial')
# airman page fallback images
for l in open('raw/gw_airman.txt'):
    n,c,i,e=l.rstrip('\n').split('|')
    add(n,c,i,e,'oficial-airman')
# extras curated by hand
if os.path.exists('extras.txt'):
    for l in open('extras.txt'):
        if not l.strip() or l.startswith('#'): continue
        p=l.rstrip('\n').split('|'); n,c,i,e=p[:4]
        add(n,c,i,e,'extra',kx=(p[4] if len(p)>4 else ''))
if __name__=='__main__':
    import sys
    print(len(M))
    with open('dados_Glycine.txt','w') as f:
        for k,r in M.items(): f.write(f"{r['nome']}|{r['cod']}|{r['img']}|{r['e']}\n")
