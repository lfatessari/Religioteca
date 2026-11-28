import json,sys,re,glob,os
TR='/root/.claude/projects/-home-claude-religioteca/a3eb2253-36bb-5033-a204-bee710637dc6/tool-results/'
out='/home/claude/trabalho/lg/prod.json'
P=json.load(open(out)) if os.path.exists(out) else {}
pages=json.load(open('/home/claude/trabalho/lg/pages.json')) if os.path.exists('/home/claude/trabalho/lg/pages.json') else {}
for f in glob.glob(TR+'mcp-Firecrawl-firecrawl_scrape-*.txt'):
    try: d=json.load(open(f))
    except Exception: continue
    h=d.get('rawHtml') or ''
    url=d.get('metadata',{}).get('sourceURL','')
    ld=re.findall(r'<script type="application/ld\+json"[^>]*>(\{"@context":"https://schema.org","@type":"Product".*?)</script>',h)
    n=0
    for s in ld:
        try: j=json.loads(s)
        except Exception: continue
        sku=j.get('sku')
        if not sku: continue
        if sku in P and ('/en-us/' in P[sku]['src'] or '/en-us/' not in url): continue
        if sku not in P: n+=1
        P[sku]={'name':j.get('name'),'model':j.get('model'),'color':j.get('color'),'image':j.get('image'),'price':(j.get('offers') or {}).get('price'),'cur':(j.get('offers') or {}).get('priceCurrency'),'src':url}
    if ld: pages[url]=pages.get(url) or n
json.dump(P,open(out,'w'),ensure_ascii=False,indent=0)
json.dump(pages,open('/home/claude/trabalho/lg/pages.json','w'),indent=0)
print('total',len(P)); 
for u,n in sorted(pages.items()): print(u,n)
