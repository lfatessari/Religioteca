import glob,re,json,os
os.chdir('/home/claude/trabalho')
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper())
R={}  # norm -> dict
def add(code,line,desc,url,src,title=''):
    k=norm(code) or ('T:'+title)
    if k=='T:': return
    d=R.setdefault(k,{'code':code,'line':'','desc':'','url':'','src':src,'title':''})
    if line and not d['line']: d['line']=line
    if desc and len(desc)>len(d['desc']): d['desc']=desc
    if url and (not d['url'] or ('relogioscondor' in d['url'] and 'img' in url)): d['url']=url
    if title and not d['title']: d['title']=title
    if '/' in code and '/' not in d['code']: d['code']=code
PDFURL={}
for f in sorted(glob.glob('pdf_*.txt')):
    for l in open(f):
        p=l.rstrip('\n').split('|')
        if len(p)==3: add(p[0],p[1],p[2],'',f)
        elif len(p)==2: add(p[0],p[1].split(',')[0],p[1],'',f)
for f in ['raw_site.txt','raw_site2.txt','raw_site3.txt','raw_site4.txt']:
    if os.path.exists(f):
        for l in open(f):
            c,t,u=l.rstrip('\n').split('|')[:3]; add(c,'','',u,f,t)
if os.path.exists('raw_other.txt'):
    for l in open('raw_other.txt'):
        p=l.rstrip('\n').split('|')
        add(p[0],'',p[3] if len(p)>3 else '',p[2],'other',p[1])
for l in open('raw_search.txt'):
    p=l.rstrip('\n').split('|'); add(p[0],'',p[3],p[2],'search',p[1])
IMG={}
for l in open('img.txt'):
    p=l.rstrip('\n').split('|'); IMG[norm(p[0])]=p[1]; add(p[0],'','',p[1],'img',p[2])
for k,v in IMG.items(): R[k]['url']=v
json.dump(R,open('merged.json','w'),ensure_ascii=False,indent=0)
with open('parcial_Condor_relogios.txt','w') as o:
    for k,d in R.items(): o.write(f"{d['line'] or d['title']}|{d['code']}|{d['url']}|{d['desc']}\n")
print(len(R))
