import json,re,glob,os,html
TR='/root/.claude/projects/-home-claude-religioteca/a3eb2253-36bb-5033-a204-bee710637dc6/tool-results/'
out='/home/claude/trabalho/lg/wb.json'
W={}; pages={}
for f in glob.glob(TR+'mcp-Firecrawl-firecrawl_scrape-*.txt')+glob.glob(TR+'toolu_*.txt'):
    try: d=json.load(open(f))
    except Exception: continue
    url=d.get('metadata',{}).get('sourceURL','')
    if 'watchbase.com' not in url: continue
    h=d.get('rawHtml') or ''
    cnt=re.findall(r'<h2>([\d,]+) Longines ([^<]*?) watches',h)
    fam=None
    blocks=re.findall(r'<a href="https://watchbase\.com/longines/([a-z0-9-]+)/([a-z0-9-]+)" class="item-block watch-block">(.*?)</a>',h,re.S)
    n=0
    for famslug,slug,b in blocks:
        m=re.search(r'<img[^>]*data-src="([^"]+)"[^>]*alt="([^"]*)"',b)
        if not m: continue
        img,alt=m.group(1),html.unescape(m.group(2))
        r=re.search(r'\(([^()]+)\)\s*$',alt)
        ref=r.group(1) if r else slug.upper()
        key=re.sub(r'[^A-Z0-9]','',ref.upper()).replace('O','0')
        if key not in W: n+=1
        W.setdefault(key,{'ref':ref,'alt':alt,'img':img.replace('/watch/md/','/watch/lg/'),'fam':famslug,'url':f'https://watchbase.com/longines/{famslug}/{slug}'})
    pages[url]=(cnt[0] if cnt else None, len(blocks), n)
B='https://cdn.watchbase.com/watch/lg/longines/'
for ref,alt,fam,img in [l.split(';') for l in open('/home/claude/trabalho/lg/wb_manual.txt').read().strip().split('\n')]:
    key=re.sub(r'[^A-Z0-9]','',ref.upper()).replace('O','0')
    slug=ref.lower().replace('.','-')
    W.setdefault(key,{'ref':ref,'alt':'Longines '+alt+' ('+ref+')','img':B+fam+'/'+slug+'-'+img+'.jpg','fam':fam,'url':f'https://watchbase.com/longines/{fam}/{slug}'})
    pages.setdefault('https://watchbase.com/longines/'+fam,(None,0,0))
json.dump(W,open(out,'w'),ensure_ascii=False,indent=0)
for u,v in sorted(pages.items()): print(u,v)
print('total',len(W))
