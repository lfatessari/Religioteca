import sys,re
src,fam,out=sys.argv[1:4]
seen=set()
with open(out,'w') as w:
    w.write(f'#SRC 3 {src}\n')
    for t in sys.stdin.read().split():
        m=re.match(r'([a-z0-9-]+)/((?:[12]-\d{2}|100|\d{2})(?:-\d{2}){4})(-[0-9a-f]{1,3})?\.(png|jpg)$',t)
        if not m: continue
        ref=m.group(2)
        if ref in seen: continue
        seen.add(ref)
        w.write(f'{fam} {ref} | https://cdn.watchbase.com/watch/glashutte-original/{t} | \n')
print(len(seen))
