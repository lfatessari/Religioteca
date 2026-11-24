import json,re,sys,os
M='jh_master.json'
def norm(r):
    r=r.upper().replace(' ','')
    m=re.match(r'^0*(\d+)[/\-\.]?(\d{4})[\.\-]?(\d{2})$',re.sub(r'[^\d/\.\-]','',r))
    if m: return f"{int(m.group(1))}/{m.group(2)}.{m.group(3)}"
    return re.sub(r'[^A-Z0-9]','',r)
def load():
    return json.load(open(M)) if os.path.exists(M) else {}
def save(d): json.dump(d,open(M,'w'),ensure_ascii=False,indent=0)
def add(d,name,ref,img,e,src):
    k=norm(ref) if ref else 'N:'+name.lower()
    if k in d:
        if not d[k]['img'] and img: d[k]['img']=img
        return 0
    d[k]={'name':name,'ref':k if ref else '','img':img,'e':e,'src':src}; return 1
def oembed(path,src,d,brand='Junghans'):
    t=json.load(open(path))
    raw=t.get('rawHtml') or t.get('markdown')
    o=json.loads(raw); n=0
    for p in o['products']:
        title=p['title']; sku=(p['offers'][0].get('sku') or '') if p['offers'] else ''
        m=re.search(r'(\d{2,3}/\d{4}\.\d{2})',title+' '+sku)
        ref=m.group(1) if m else ''
        name=re.sub(r'^Junghans\s+','',title); name=re.sub(r'\s*\d{2,3}/\d{4}\.\d{2}.*$','',name).strip(' -')
        img=p.get('thumbnail_url','') or ''
        if img.startswith('//'): img='https:'+img
        if not ref: continue
        n+=add(d,name,ref,img,'',src)
    return n,len(o['products'])
def pjson(path,src,d):
    raw=json.load(open(path))['rawHtml']
    raw=re.sub(r'^<[^{]*','',raw); raw=raw[:raw.rfind('}')+1]
    o=json.loads(raw); n=0; sem=[]
    for p in o['products']:
        title=p['title']; skus=' '.join((v.get('sku') or '') for v in p.get('variants',[]))
        body=re.sub('<[^>]+>',' ',p.get('body_html') or '')
        m=re.search(r'(\d{2,3})\s*/\s*(\d{4})\s*\.\s*(\d{2})',title+' '+skus+' '+body)
        ref=''.join(m.groups()) and f"{m.group(1)}/{m.group(2)}.{m.group(3)}" if m else ''
        name=re.sub(r'^Junghans\s+','',title,flags=re.I); name=re.sub(r'\s*\(?\d{2,3}\s*/\s*\d{4}\.\d{2}.*$','',name).strip(' -–')
        img=p['images'][0]['src'] if p.get('images') else ''
        if not ref: sem.append(title); continue
        n+=add(d,name,ref,img,'',src)
    return n,len(o['products']),sem
def twp(path,src,d):
    h=json.load(open(path))['rawHtml']; n=0; tot=0; seen=set()
    for m in re.finditer(r'href="(https://www\.thewatchpages\.com/watches/junghans-([a-z0-9\-]+?)-(\d{1,3})-(\d{6})(?:-\d)?/?)"',h):
        url,slug,a,b=m.groups()
        if url in seen: continue
        seen.add(url); tot+=1
        seg=h[m.end():m.end()+3000]
        im=re.search(r'(https://cdn\.thewatchpages\.com/app/uploads/[^"\s?]+\.(?:jpe?g|png|webp))',seg)
        nm=re.search(r'alt="Junghans ([^"]+)"',seg)
        name=nm.group(1).strip() if nm else slug.replace('-',' ').title()
        ref=f"{int(a)}/{b[:4]}.{b[4:]}"
        n+=add(d,name,ref,im.group(1) if im else '','',src)
    return n,tot
def dump(d):
    with open('parcial_junghans_relogios.txt','w') as f:
        for k,v in d.items(): f.write(f"{v['name']}|{v['ref']}|{v['img']}|{v['e']}\n")
