import re,sys
def norm(c): return re.sub(r'[^0-9A-Z]','',c.upper().replace('O','0'))
def add(items, src, nota):
    L=open('parcial_Cover_relogios.txt').read().splitlines()
    exec(open('oficial.py').read(), g:={})
    have={norm(l.split('|')[1]) for l in L}|{norm(r[1]) for r in g['rows']}
    n=0
    for c,nm,u in items:
        c=c.replace('SET.','')
        k=norm(c)
        if k in have: continue
        have.add(k); n+=1
        e=nota
        if c.upper().startswith('CO10'): e+=' Sub-linha Crazy Seconds/edições temáticas.'
        if c.upper().startswith('SC'): e+=' Código no padrão SC (linha Trend), listado como Cover pela loja.'
        L.append(f"{nm}|{c}|{u}|{e}")
    open('parcial_Cover_relogios.txt','w').write('\n'.join(L)+'\n')
    open('parcial_Cover_fontes.txt','a').write(f"1|{src}|{n}\n")
    print(src,n,len(L))
