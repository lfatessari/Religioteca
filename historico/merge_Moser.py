import json,sys,re,os
M='master.json'
db=json.load(open(M)) if os.path.exists(M) else {}
def norm(r): return re.sub(r'[^0-9A-Z]','',r.upper().replace('O','0'))
def isimg(u): return bool(re.search(r'\.(jpe?g|png|webp|avif)(\?|$)',u,re.I)) or 'image' in u.lower()
def clean(u):
    u=u.replace('crop=center&height=1&','').replace('&width=1','&width=1200') if 'crop=center&height=1' in u else u
    return u
def add(ref,name,img,e=''):
    img=clean(img.strip()); ref=ref.strip(); name=name.strip()
    k=norm(ref) if ref else 'N:'+name.lower()
    if k in db:
        d=db[k]
        if img and isimg(img) and not isimg(d['img']): d['img']=img
        if e and not d['e']: d['e']=e
        return 0
    if name=='x': print('SKIP no-name new',ref); return 0
    db[k]={'ref':ref,'name':name,'img':img,'e':e}; return 1
n=0
for f in sys.argv[1:]:
    for l in open(f,encoding='utf-8'):
        if not l.strip(): continue
        p=l.rstrip('\n').split('|')
        if f.startswith('parcial') or f.startswith('dadosfmt'):  # Nome|COD|img|E
            n+=add(p[1],p[0],p[2],p[3] if len(p)>3 else '')
        else:  # ref|name|img|e
            n+=add(p[0],p[1],p[2],p[3] if len(p)>3 else '')
json.dump(db,open(M,'w'),ensure_ascii=False,indent=0)
print('novos',n,'total',len(db))
with open('parcial_Moser_relogios.txt','w') as o:
    for d in db.values(): o.write(f"{d['name']}|{d['ref']}|{d['img']}|{d['e']}\n")
