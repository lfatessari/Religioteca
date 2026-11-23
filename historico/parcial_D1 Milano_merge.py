import re
of=[l.rstrip('\n').split('|') for l in open('oficial1.txt') if l.strip()]
fi={l.split('|')[0]:l.rstrip('\n').split('|') for l in open('fichas.txt') if l.strip()}
oc={l.split('|')[1]:l.rstrip('\n').split('|') for l in open('ocarat.txt') if l.strip()}
gi=[l.rstrip('\n').split('|') for l in open('giglio_raw.txt') if l.strip()]
gcode=lambda c: re.sub(r'^(D1-|D1|A-)','',c)
gi={gcode(x[1]):x for x in gi}
# códigos por nome (Giglio/Ocarat) para fichas que não abriram
mapa={'polycarbon-40-5mm-black-enamel':'PCBJ35','gilded-lunar-polychrono-watch':'PHBJ15','polychrono-40-5mm-shadow':'PHBJSH',
'polychrono-characoal-black':'PHBJ07','void-phantom-polychrono-watch':'PHBJ18','ultra-thin-bracelet-40-mm-scarabeo':'UTBJ37',
'ultra-thin-bracelet-40-mm-midnight':'UTBJ21','regun-mirage-ultra-thin-watch':'UTBJ41','ultra-thin-bracelet-40-mm-re-rosegold':'UTBJ42',
'ultra-thin-bracelet-40-mm-shadow':'UTBJSH','ultra-thin-40mm-black-dlc':'UTBJ31','groovy-green':'UHBJ03','classic-oxymor-ultra-thin-watch':'UHBJ06',
'dark-illusion-ultra-thin-watch':'UHBJ08','drift-diver-polycarbon-watch':'PDBJ02','carbon-diver-polycarbon-watch':'PDBJ01',
'steel-diver-polycarbon-watch':'PDBJ03','lagoon-diver-polycarbon-watch':'PDBJ04','black-mirror':'UTBU09','silver-gleam-ultra-thin-watch':'UTBL39',
'ultra-thin-30mm-ultimate-gray':'UTBL32','ultra-thin-30mm-edge':'UTBL34','ultra-thin-30mm-zephyr-silver':'UTBL30','tone-mellow':'UHBL03',
'silver-mellow':'UHBL01','polycarbon-37-mm-gun-mesh':'PCBU13','ring-ring-polycarbon-watch':'PCBU25','viridis-mdrj05':'MDRJ05','polycarbon-37-mm-akebia-mesh':'PCBU15'}
usados=set();linhas=[]
for nome,h,esp in of:
    f=fi.get(h);cod=(f[1] if f and f[1] else mapa.get(h,''))
    img=(f[2] if f and f[2] else '')
    e=(f[3] if f and f[3] else esp)
    if not img and cod in oc: img=oc[cod][2]
    if not img and cod=='PCBU15': img='https://images.ocarat.com/465352-cart_default/polycarbon-akebia-mesh-watch-pcbu15-d1-milano.jpg'
    if not img and cod in gi and gi[cod][2]: img='https://media-catalog.giglio.com/images/f_auto/t_prodPage/v1/products/%s/d1-milano.jpg'%gi[cod][2]
    nota=''
    if not img: img='https://d1milano.com/products/'+h; nota=' Foto não obtida: link da página do produto no site oficial.'
    if cod: usados.add(cod)
    e=e[0].upper()+e[1:] if e else ''
    linhas.append([nome,cod,img,(e+'.' if e else '')+nota])
# códigos de lojas que não apareceram no site oficial
for cod,x in oc.items():
    if cod in usados: continue
    usados.add(cod); linhas.append([x[0],cod,x[2],'Visto na loja Ocarat.'])
for cod,x in gi.items():
    if cod in usados: continue
    usados.add(cod)
    nm=x[0]
    if nm==x[1] or nm==cod:
        pf={'UC':'Ultra Thin 1980','UH':'Ultra Thin 1970','NC':'Polycarbon','AR':'Aura','MD':'Nylon – colaboração D1 × MAD Paris, edição limitada','CV':'Canva','SQ':'Square','UT':'Ultra Thin','PC':'Polycarbon'}
        nm=pf.get(cod[:2],'Modelo')
    img=('https://media-catalog.giglio.com/images/f_auto/t_prodPage/v1/products/%s/d1-milano.jpg'%x[2]) if x[2] else None
    pre={'au':'en-au','ca':'en-ca'}[x[3][:2]]
    cat={'au-woman_jewel':'accessories-woman_jewel','au-woman_watch':'accessories-woman_watch','au-clothing':'clothing-men_suit'}.get(x[3],'accessories-men_watch')
    pg='https://www.giglio.com/%s/%s-d1-milano-%s.html'%(pre,cat,x[1].lower())
    linhas.append([nm,cod,img or pg,('Linha deduzida do prefixo OL do código (provável Olivetti digital 36 mm). ' if cod.startswith('OL') else '')+'Visto na loja Giglio'+('' if img else ' só pelo título (link da página do produto)')+'.'])
for l in open('extra2.txt'):
    if l.strip():
        a=l.rstrip('\n').split('|'); linhas.append(a)
# nomes duplicados sem código
from collections import Counter
for l in linhas:
    l[1]=l[1] and ('D1-'+l[1] if not l[1].startswith('OL') else l[1])
c=Counter((l[0],l[1]) for l in linhas)
print('total',len(linhas),'dup',[k for k,v in c.items() if v>1])
print('sem codigo',[l[0] for l in linhas if not l[1]])
print('sem foto',sum('d1milano.com/products' in l[2] or 'giglio.com/en' in l[2] for l in linhas))
open('dados_D1 Milano.txt','w').write('\n'.join('|'.join(l) for l in linhas)+'\n')
