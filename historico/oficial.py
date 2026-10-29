# Dados do site oficial coverwatches.com (out/2026)
O='https://coverwatches.com/cdn/shop/files/'
P='https://coverwatches.com/products/'
A='https://almuftahcenter.com/cdn/shop/files/{}-1.jpg'
rows=[]
def add(nome,ref,img,e): rows.append((nome,ref,img,e))
# Alston Gent Co216
cores={1:'mostrador preto, prateado',2:'mostrador prata, todo prateado',3:'mostrador azul, prateado',4:'mostrador verde, prateado',5:'mostrador preto, bicolor prata/dourado',6:'mostrador prata, bicolor prata/dourado',7:'mostrador azul, bicolor prata/dourado',8:'mostrador verde, bicolor prata/dourado',9:'mostrador preto, bicolor prata/rosé',10:'mostrador prata, bicolor prata/rosé'}
for n,c in cores.items():
    r=f'Co216.{n:02d}'
    img={7:O+'Co216.07-579430.jpg'}.get(n, O+r+'.jpg' if n in (1,3,5,9) else P+f'co216-{n:02d}-cover-alston-gent')
    add('Alston Gent',r,img,'Aço, '+c+('' if n in (1,3,5,7,9) else '; foto não exibida na listagem (link da página do produto)'))
for n,c in cores.items():
    r=f'Co217.{n:02d}'
    img=O+r+'.jpg' if n in (1,3,5,7,9) else P+f'co217-{n:02d}-cover-alston-ladies'
    add('Alston Lady',r,img,'Aço, '+c+('; feminino' if n in (1,3,5,7,9) else '; feminino; foto não exibida na listagem (link da página do produto)'))
mg={1:'mostrador preto, prateado',2:'todo prateado',3:'mostrador azul, prateado',4:'mostrador verde, prateado',5:'mostrador prata, bicolor prata/dourado',6:'mostrador azul, bicolor prata/dourado',7:'mostrador verde, bicolor prata/dourado',8:'mostrador prata, bicolor prata/rosé',9:'mostrador azul, bicolor prata/rosé',10:'mostrador verde, bicolor prata/rosé'}
for n,c in mg.items():
    r=f'Co214.{n:02d}'
    img=O+r+'.jpg' if n in (1,2,6,8,9) else P+f'co214-{n:02d}-cover-marville-gent'
    add('Marville Gent',r,img,'Aço, '+c+('' if n in (1,2,6,8,9) else '; foto não exibida na listagem (link da página do produto)'))
ml={1:'mostrador preto, prateado',2:'todo prateado',3:'mostrador azul, prateado',4:'mostrador verde, prateado',5:'mostrador azul-claro, prateado',6:'mostrador prata, bicolor prata/dourado',7:'mostrador azul, bicolor prata/dourado',8:'mostrador verde, bicolor prata/dourado',9:'mostrador prata, bicolor prata/rosé',10:'mostrador azul, bicolor prata/rosé',11:'mostrador verde, bicolor prata/rosé'}
for n,c in ml.items():
    r=f'Co215.{n:02d}'
    img=O+r+'.jpg' if n in (1,2,3,7,10) else P+f'co215-{n:02d}-cover-marville-lady'
    add('Marville Lady',r,img,'Aço, '+c+'; feminino'+('' if n in (1,2,3,7,10) else '; foto não exibida na listagem (link da página do produto)'))
cm={1:'mostrador branco, pulseira de couro azul, prateado',2:'mostrador azul, pulseira de couro preta, prateado',3:'mostrador azul, pulseira de couro marrom, prateado',4:'mostrador cinza, pulseira de couro preta, prateado',5:'mostrador branco, pulseira de couro preta, dourado',6:'mostrador branco, pulseira de couro marrom, rosé',7:'mostrador azul, pulseira de couro marrom, rosé'}
for n,c in cm.items():
    r=f'Co202.{n:02d}'
    img=O+r+'.jpg' if n in (2,3,4,5,7) else P+f'co202-{n:02d}-cover-chapman-moon-stars'
    add('Chapman Moon & Stars',r,img,'Aço, fase da lua, '+c+('' if n in (2,3,4,5,7) else '; foto não exibida na listagem (link da página do produto)'))
cc={1:'mostrador preto, prateado',2:'prateado',3:'mostrador azul, prateado',4:'mostrador verde, prateado',5:'mostrador preto, pulseira de couro',6:'mostrador azul, pulseira de couro',7:'mostrador verde, pulseira de couro',8:'mostrador champanhe, pulseira de couro',9:'caixa rosé, mostrador azul, pulseira de couro'}
for n,c in cc.items():
    r=f'Co220.{n:02d}'
    img=O+r+'.jpg' if n in (3,4,6,7,9) else A.format(f'CO220-{n:02d}') if n in (2,5,8) else P+f'co220-{n:02d}-cover-chapman-chrono-ii'
    add('Chapman Chrono II',r,img,'Aço, cronógrafo, '+c)
ic={1:'mostrador preto, prateado',2:'mostrador azul, prateado',3:'mostrador preto, bicolor',4:'mostrador azul, bicolor',5:'mostrador verde, bicolor',6:'mostrador prata, prateado (41 mm, 9 mm, safira, quartzo suíço Ronda 5040.D, 100 m)',7:'mostrador azul-claro, marrom',8:'dourado bicolor'}
im={4:O+'co212.04-772642.png',5:O+'co212.05-270680.png'}
for n,c in ic.items():
    r=f'Co212.{n:02d}'
    img=O+r+'.jpg' if n in (6,7,8) else im.get(n, P+f'co212-{n:02d}-cover-iconosteel-chrono')
    add('Iconosteel Chrono',r,img,'Aço, cronógrafo, '+c)
i3={1:'mostrador preto, prateado',2:'mostrador azul, prateado',3:'mostrador preto, bicolor prata/dourado',4:'mostrador azul, bicolor prata/dourado',5:'mostrador verde, bicolor prata/dourado',6:'mostrador azul-claro, prateado',7:'mostrador azul, prateado',8:'mostrador "dune" (areia), bicolor',9:'dourado, bicolor'}
for n,c in i3.items():
    r=f'Co213.{n:02d}'
    img=O+r+'.jpg' if n in (6,7,8,9) else (O+'co213.05-631691.png' if n==5 else P+f'co213-{n:02d}-cover-iconosteel')
    add('Iconosteel',r,img,'Aço, '+c)
il={1:'mostrador perolado branco, prateado',2:'mostrador perolado azul, prateado',3:'mostrador verde, bicolor dourado',4:'mostrador verde-claro, bicolor dourado',5:'dourado, bicolor',6:'todo dourado'}
for n,c in il.items():
    r=f'Co223.{n:02d}'
    img=O+r+'.jpg' if n!=1 else A.format('CO223-01')
    add('Iconosteel Lady',r,img,'Aço, '+c+'; feminino')
ns={1:'mostrador preto, prateado',2:'prateado',3:'mostrador azul-claro, prateado',4:'mostrador preto, dourado (30,2 x 22 mm, 6,8 mm, safira, quartzo Ronda 762, 50 m)',5:'mostrador prata, dourado',6:'mostrador champanhe, dourado'}
for n,c in ns.items():
    r=f'Co222.{n:02d}'
    img=O+r+'.jpg' if n!=1 else P+'co222-01-cover-noble-square'
    add('Noble Square',r,img,'Aço, quadrado, '+c+'; feminino')
cd={1:'prateado',2:'mostrador azul-claro, prateado',3:'mostrador prata, bicolor dourado',4:'mostrador azul, bicolor dourado',5:'mostrador verde, bicolor dourado',6:'bicolor rosé'}
for n,c in cd.items():
    r=f'Co221.{n:02d}'
    img=O+r+'.jpg' if n!=1 else P+'co221-01-cover-cardea-crystal'
    add('Cardea Crystal',r,img,'Aço com cristais, '+c+'; feminino')
vm={1:'mostrador perolado azul, prateado',2:'mostrador perolado branco, bicolor (30 mm, 8,3 mm, safira, quartzo Ronda 763, 50 m)',3:'mostrador perolado verde, bicolor',4:'mostrador perolado branco, bicolor rosé',5:'mostrador perolado branco, dourado'}
for n,c in vm.items():
    r=f'Co224.{n:02d}'; add('Valentina Mini',r,O+r+'.jpg','Aço, '+c+'; feminino')
jm={1:('mostrador perolado branco, prateado','co218.01-514556.png'),2:('mostrador perolado azul, prateado','co218.02-166227.png'),3:('mostrador perolado branco, bicolor prata/dourado','co218.03-680031.png'),4:('mostrador perolado verde, bicolor prata/dourado','co218.04-375132.png'),5:('mostrador perolado branco, bicolor prata/rosé','co218.05_56f571a4-3dff-43a2-aa66-54145f2d22f2-392140.png')}
for n,(c,f) in jm.items():
    add('Jumeira Crystals',f'Co218.{n:02d}',O+f,'Aço com cristais, '+c+'; feminino')
ad={1:('mostrador perolado azul, prateado','co210.01-477804.png'),2:('mostrador perolado branco, prateado','co210.02-648468.png'),3:('mostrador perolado verde, prateado','co210.03-495025.png'),4:('mostrador perolado branco, bicolor dourado','co210.04-766349.png'),5:('mostrador perolado branco, bicolor rosé','co210.05-181815.png')}
for n,(c,f) in ad.items():
    add('Andara Diamond',f'Co210.{n:02d}',O+f,'Aço com diamantes, '+c+'; feminino')
vc={1:('mostrador preto, prateado','Co207.01-330458.png'),2:('mostrador de madrepérola branca, prateado',None),3:('mostrador de madrepérola branca, dourado',None),4:('mostrador verde, dourado',None),5:('mostrador de madrepérola branca, pulseira de couro marrom','co207.05-875339.png'),6:('mostrador de madrepérola branca, prateado, pulseira de couro','co207.06-453741.png'),7:('mostrador de madrepérola branca, dourado, pulseira de couro','co207.07-590088.png'),8:('mostrador verde, pulseira de couro verde','co207.08-770071.png')}
hv={2:'co207-02-cover-valentina-chrono-mother-of-pearl-watch-white-silver',3:'co207-03-cover-valentina-chrono-mother-of-pearl-watch-white-gold',4:'co207-04-cover-valentina-chrono-mother-of-pearl-watch-green-gold'}
for n,(c,f) in vc.items():
    img=O+f if f else P+hv[n]
    add('Valentina Chrono',f'Co207.{n:02d}',img,'Aço, cronógrafo, '+c+'; feminino'+('' if n in (2,3,4,5) else '; referência deduzida da foto da listagem'))
sd={1:('todo prateado (28 mm, 7 mm, vidro mineral K1 com camada de safira, quartzo Ronda 763, 50 m)',None),2:('mostrador azul, prateado','co203.02-651552.png'),3:('mostrador prata, bicolor',None),4:('mostrador verde, bicolor prata/dourado','co203.04-601105.png'),5:('mostrador prata, bicolor',None),6:('mostrador azul, bicolor prata/rosé','co203.06-185372.png'),7:('mostrador rosa, prateado','co203.07-946349.png'),8:('mostrador azul-claro, prateado','co203.08-200278.png')}
for n,(c,f) in sd.items():
    img=O+f if f else (A.format(f'CO203-{n:02d}') if n in (1,3) else P+'co203-05-cover-sandara')
    add('Sandara Crystal',f'Co203.{n:02d}',img,'Aço com cristais, '+c+'; feminino')
ldo={1:('mostrador perolado branco, prateado','coa8.01_df0f71cd-f734-4fb1-b67b-3d574246fe54-937296.png'),2:('mostrador perolado branco, bicolor prata/dourado','coa8.02-905830.png'),3:('mostrador perolado branco, bicolor prata/rosé','coa8.03-251990.png')}
for n,(c,f) in ldo.items():
    add('Lady Diamond Open Heart',f'CoA8.{n:02d}',O+f,'Automático com abertura (open heart), diamantes, '+c+'; feminino')
ar={1:'mostrador preto, pulseira de aço',2:'mostrador azul, pulseira de aço',3:'mostrador areia ("dune"), pulseira de aço',4:'mostrador preto, pulseira de couro',5:'mostrador azul, pulseira de couro',6:'mostrador areia, pulseira de couro',7:'mostrador bordô, pulseira de couro'}
for n,c in ar.items():
    r=f'CoA225.{n:02d}'
    img=O+r+'.jpg' if n in (3,4,5,6,7) else P+f'coa225-{n:02d}-cover-arena'
    add('Arena Automatic',r,img,'Automático, aço, '+c)
lv={1:('mostrador prata, bicolor prata/dourado','COVER_Lovis_Square_Watch_Silver_Dial_Bicolor_Gold_Co229.01.jpg'),2:('mostrador verde-claro, bicolor prata/dourado','Co229.02COVER_Lovis_Square_Watch_Light_Green_Dial_Bicolor_Gold_Co229.02.jpg'),3:('mostrador prata, bicolor prata/rosé','COVER_Lovis_Square_Watch_Silver_Dial_Bicolor_Rosegold_Co229.03.jpg'),4:('mostrador prata, dourado','COVER_Lovis_Square_Watch_Silver_Dial_Gold_Co229.04.jpg'),5:('mostrador verde, dourado',None),6:('todo dourado','COVER_Lovis_Square_Watch_Full_Gold_Co229.06.jpg')}
for n,(c,f) in lv.items():
    add('Lovis',f'Co229.{n:02d}',O+f if f else P+'cover-lovis-square-watch-green-dial-gold','Aço, quadrado, '+c+'; feminino; lançamento 2026'+('; referência deduzida da sequência' if n==5 else ''))
um={1:('prateado','COVER_Urban_Muse_Faceted_Diamond_Watch_Silver_Co228.01.jpg'),2:('mostrador azul, prateado','COVER_Urban_Muse_Faceted_Diamond_Watch_Blue_Silver_Co228.02.jpg'),3:('mostrador rosa, prateado','COVER_Urban_Muse_Faceted_Diamond_Watch_Rose_Silver_Co228.03.jpg'),4:('mostrador prata, bicolor dourado','COVER_Urban_Muse_Faceted_Diamond_Watch_Silver_Bicolor_Gold_Co228.04.jpg'),5:('mostrador verde, bicolor dourado',None),6:('mostrador prata, bicolor rosé','COVER_Urban_Muse_Faceted_Diamond_Watch_Silver_Bicolor_Ros_Gold_Co228.06.jpg')}
for n,(c,f) in um.items():
    add('Urban Muse Faceted Diamond',f'Co228.{n:02d}',O+f if f else P+'cover-urban-muse-faceted-diamond-watch-green-bicolor-gold','Aço, vidro facetado, diamantes, '+c+'; feminino; lançamento 2026'+('; referência deduzida da sequência' if n==5 else ''))
ep={1:('mostrador branco, prateado','COVER_Eternal_Pearl_Diamond_Ladies_Watch_Co227.01.jpg'),2:('mostrador azul, prateado','Blue_Dial_and_Silver_Stainless_Steel_Bracelet_Swiss_elegant_diamond_watch_COVER_Eternal_Pearl_Diamond_Ladies_Watch_Blue_Silver_Co227.02.jpg'),3:('mostrador branco, dourado','COVER_Eternal_Pearl_Diamond_Ladies_Watch_White_Gold_Co227.03.jpg'),4:('mostrador verde, dourado','COVER_Eternal_Pearl_Diamond_Ladies_Watch_Green_Gold_Co227.04.jpg'),5:('mostrador branco, rosé','COVER_Eternal_Pearl_Diamond_Ladies_Watch_White_Rose_Gold_Co227.05.jpg')}
for n,(c,f) in ep.items():
    add('Eternal Pearl Diamond',f'Co227.{n:02d}',O+f,'Aço, diamantes, mostrador perolado '+c+'; feminino; lançamento 2026')
al={1:('prateado','COVER_Altea_Curved_Case_Watch_Silver_Co226.01.jpg'),2:('mostrador azul, prateado','COVER_Altea_Curved_Case_Watch_Blue_Silver_Co226.02.jpg'),3:('bicolor dourado','Watch_Bicolor_Gold_Co226.03.jpg'),4:('dourado','Co226.04.jpg'),5:('mostrador verde, dourado','Co226.05.jpg'),6:('bicolor prata/rosé',None)}
for n,(c,f) in al.items():
    add('Altea Curved Case',f'Co226.{n:02d}',O+f if f else P+'cover-altea-curved-case-bicolor-silver-rose-gold','Aço, caixa curva, '+c+'; feminino; lançamento 2026'+('; referência deduzida da sequência' if n==6 else ''))
