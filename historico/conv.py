import re,sys,glob,collections
PRE='https://images.squarespace-cdn.com/content/v1/56a9e12ac647ad08eb4453c7/'
MET=[('CARBONE','carbono'),('CARBON','carbono'),('CARB','carbono'),('SAPH','safira'),('ALU','alumínio'),('5N','ouro rosa 5N'),('3N','ouro amarelo 3N'),('OG','ouro branco'),('TT','titânio'),('AC','aço')]
def metal(img):
    f=img.split('/')[-1].upper().replace('%2B','+').replace('%252B','+')
    f=re.sub(r'\.(PNG|JPG|JPEG)$','',f)
    toks=[t for t in re.split(r'[-+._ ()%]',f) if t]
    for t in reversed(toks):
        for k,v in MET:
            if t==k: return v
    return ''
def load(files):
    rows=[]
    for fn in files:
        for l in open(fn,encoding='utf-8'):
            l=l.rstrip('\n')
            if not l.strip(): continue
            p=l.split('|')
            while len(p)<4: p.append('')
            c,r,i,d=p[:4]
            if not i.startswith('http'): i=PRE+i if i else ''
            rows.append([c,r,i,d])
    return rows
def build(rows):
    # dedupe identical image
    seen=set();out=[]
    for r in rows:
        if r[2] and r[2] in seen: continue
        seen.add(r[2]);out.append(r)
    g=collections.defaultdict(list)
    for r in out: g[(r[0],r[1])].append(r)
    res=[]
    for (c,ref),lst in g.items():
        mets=[metal(r[2]) if 'squarespace' in r[2] else '' for r in lst]
        cands=[]
        for k,r in enumerate(lst):
            m=mets[k]; d=r[3]
            bits=[x for x in [m, d if d and not d[0].isupper() else ''] if x]
            seen2=[];[seen2.append(b) for b in bits if b not in seen2]
            cands.append(', '.join(seen2))
        cnt=collections.Counter(cands); idx=collections.Counter()
        for k,r in enumerate(lst):
            m=mets[k]; d=r[3]
            name=c
            if len(lst)>1:
                suf=cands[k]
                if cnt[suf]>1 or not suf:
                    idx[suf]+=1; suf=(suf+', ' if suf else '')+f'variante {idx[suf]}'
                name=f'{c} – {suf}'
            e=''
            if d and d[0].isupper(): e=d
            parts=[]
            if m: parts.append('Caixa em '+m)
            if d and not d[0].isupper() and d!=m: parts.append(d)
            if parts:
                s='; '.join(parts)+'.'
                e=(e.rstrip('.')+'. '+s[0].upper()+s[1:]) if e else s[0].upper()+s[1:]
            code=ref if re.search(r'\d',ref) else ''
            if not code and ref!=c: name=ref if ref.lower().startswith(c.split(' –')[0].lower()[:6]) else f'{c} {ref}'
            res.append((name,code,r[2],e))
    return res
if __name__=='__main__':
    rows=load(sorted(glob.glob(sys.argv[1])))
    res=build(rows)
    names=collections.Counter(f'{a} - {b}' for a,b,_,_ in res)
    d=[k for k,v in names.items() if v>1]
    print('dups',d,file=sys.stderr)
    with open(sys.argv[2],'w',encoding='utf-8') as f:
        for a,b,c,e in res: f.write(f'{a}|{b}|{c}|{e}\n')
    print(len(res),file=sys.stderr)
