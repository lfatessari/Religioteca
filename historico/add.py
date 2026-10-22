import sys,re
# stdin: title | ref | img   -> appends to raw_all.txt as title|ref|img|fonte
fonte=sys.argv[1]
out=open('/home/claude/trabalho/raw_all.txt','a')
for l in sys.stdin:
    p=[x.strip() for x in l.split(' | ')]
    if len(p)<2: continue
    while len(p)<3: p.append('')
    t,r,i=p[:3]
    if r.lower() in ('n/a','none','-'): r=''
    if r.startswith('bremont-') or ' ' in r or 'slug' in r: r=''
    i=re.sub(r'crop=center&height=1&','',i); i=re.sub(r'&width=1\b','&width=1200',i)
    if i.startswith('http') and 'width=' not in i and 'cdn/shop' in i: i+=('&' if '?' in i else '?')+'width=1200'
    out.write(f'{t}|{r}|{i}|{fonte}\n')
