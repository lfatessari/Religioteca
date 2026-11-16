exec(open('variantes.py').read())
CDN='https://benlydesignwatch.com/cdn/shop/files/'
out=[]
for l in open('base_benly.tsv'):
    nome,h,img=l.rstrip('\n').split('|')
    lim=LIM.get(h); suf=f' – edição limitada de {lim} peças' if lim else ''
    car=C.get(h,'')
    if h in V:
        for s,i in V[h]: out.append(f'{nome} {s}{suf}||{CDN}{i}|{car}')
    else: out.append(f'{nome}{suf}||{CDN}{img}|{car}')
for x in open("extras.txt"):
    if x.strip(): out.append(x.rstrip("\n"))
open('parcial_Benlydesign_relogios.txt','w').write('\n'.join(out)+'\n'); print(len(out))
