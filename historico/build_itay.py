U='https://www.itay-noy.com/wp-content/uploads/'
R=[]
def a(n,c,i,e): R.append((n,c,i if i.startswith('http') else U+i,e))
# Jewish Heritage
JH='Coleção Jewish Heritage do site oficial.'
id42='Aço 316L, 42,4 × 10,4 mm, safira, fundo aberto, 5 ATM. Automático (rotor com rolamento), 38 h, data. Mostrador com numerais hebraicos.'
a('Identity Hebrew - mostrador azul-marinho - edição limitada de 99 peças','HEB.NAVY','2024/05/HEB.NAVY_.jpg',id42+' '+JH)
a('Identity Hebrew - mostrador dourado - edição limitada de 99 peças','HEBREW.G','2024/05/HEB.G-front.png',id42+' Também listado como HEB.GD 42.4MM na coleção Jewish Heritage.')
a('Identity Hebrew - mostrador verde - edição limitada de 99 peças','HEB.GN','2024/05/HEBREW.GRN_.png',id42+' '+JH)
a('Identity Hebrew - edição limitada de 99 peças','IDHebrew','2024/05/HEB.jpg','Aço 316L, 42,4 × 10,5 mm, safira, fundo aberto, 50 m. ETA 2824-2 automático (horas, minutos, segundos, data). Mostrador preto esmaltado com letras hebraicas e padrão de Estrela de Davi; centro esqueletizado e rotor personalizado. Cerca de US$ 2.000 em 2011. No site oficial: HEBREW.')
a('Identity Arabic - edição limitada de 99 peças','IDArabic','2018/12/ARAB-front.png','Aço 316L, 42,4 × 10,5 mm, safira, fundo aberto, 50 m. ETA 2824-2 automático, data. Mostrador preto com numerais arábicos orientais. No site oficial: ARABIC.')
a('Identity Roman - edição limitada de 99 peças','IDROM','2018/12/ROM-front.png','Aço 316L, 42,4 × 10,5 mm, safira, fundo aberto. Automático, data. Numerais romanos. No site oficial: ROME.')
a('Identity Greek - edição limitada de 99 peças','GREEK','2018/12/GREEK-front.png','Aço 316L, 42,4 × 10,4 mm, safira, fundo aberto, 5 ATM. Automático, 38 h, data. Numerais gregos.')
a('Identity Japanese - edição limitada de 99 peças','IDJapan','2018/12/JAP-front.png','Aço 316L, 42,4 × 10,5 mm, safira, fundo aberto, 50 m. ETA 2824-2 automático, data. Mostrador preto esmaltado com numerais japoneses; coroa às 3h30. No site oficial: JAPANESE.')
a('Identity Chinese - edição limitada de 99 peças','IDChinese','2018/12/CHINA-front.png','Aço 316L, 42,4 × 10,5 mm, safira, fundo aberto, 50 m. ETA 2824-2 automático, data. Numerais chineses e motivo de dragão (um blog de 2013 o chama "Identity Chinese (Red)"). No site oficial: CHINESE.')
sh='Aço 316L, 40 × 8,4 mm, safira, fundo aberto, 5 ATM. Calibre IN.S200/INS240 (Sellita SW240 modificado) automático, 38 h, data e dia. Dias da semana em hebraico sobre padrão de Estrela de Davi; o sétimo dia é o Shabat.'
a('Seven-Day Cycle Shabbat - mostrador preto - edição limitada de 77 peças','SHABBAT.BK','2023/07/sdc.5.png',sh+' 2023; US$ 4.900.')
a('Seven-Day Cycle Shabbat - mostrador azul e dourado - edição limitada de 77 peças','SHABBAT.BL&GD','2024/05/SHABBAT.ROYAL_.png',sh+' '+JH)
a('Seven-Day Cycle Shabbat - mostrador verde e dourado - edição limitada de 77 peças','SHABBAT.GN&GD','2024/05/SHABBAT.GRN_.png',sh+' '+JH)
m36='Aço 316L, 36 × 10,2 mm, safira, fundo aberto, 5 ATM, mostrador esmaltado. Automático, 42 h.'
a('Medium Size Hebrew 36 - preto - edição limitada de 99 peças','HEBREW36.B','2018/12/HEB-1.png',m36+' Numerais hebraicos. Também na coleção Jewish Heritage (HEB.BK 36MM).')
a('Ladies Hebrew 36 - dourado - edição limitada de 99 peças','HEBREW36.G','2019/01/HEBREW36.png',m36+' Numerais hebraicos. Também na coleção Jewish Heritage (HEB.GD 36MM).')
a('Ladies Hebrew 36 - vermelho - edição limitada de 99 peças','HEBREW36.R','2021/07/HEBRED-1.png',m36+' Numerais hebraicos. Também na coleção Jewish Heritage (HEB.RD 36MM).')
fm='Aço 316L, 40 × 44 mm, 6,24 mm de altura, safira, fundo aberto, 5 ATM. Calibre IN.VMF5400 (Vaucher) automático extrafino com microrrotor, 48 h, 29 rubis. Data lida num círculo de 31 fendas.'
a('Full Month Hebrew - Moon - edição limitada de 18 peças','HEB MONTH.MN','2024/05/FM.MOON_.HEB_.png',fm+' Numerais hebraicos com fases da lua. '+JH)
a('Full Month Hebrew - mostrador branco - edição limitada de 18 peças','HEB MONTH.WT','2018/11/full-month4.png',fm+' Numerais hebraicos. '+JH)
a('Full Month Hebrew - mostrador azul - edição limitada de 18 peças','HEB MONTH.BL','2024/05/FM.HEB_.BL_.png',fm+' Numerais hebraicos. '+JH)
a('Square Hebrew - preto','SQUARE.HEB.BK','2024/05/SQUARE.BK_.png','Caixa quadrada, numerais hebraicos. '+JH)
a('Square Hebrew - dourado','SQUARE.HEB.GD','2024/05/SQUARE.GD_.png','Caixa quadrada, numerais hebraicos. '+JH)
a('Hebrew Stars & Moon','HEB STARS & MOON','2024/05/HEB-STARSMOON-Front.png','Numerais hebraicos com estrelas e lua. '+JH)
a('Alef Beit 38 mm','ALEF BEIT','2024/05/AB-2.jpg','Letras do alfabeto hebraico; 38 mm. '+JH+' A página própria da coleção Alef Beit não abriu.')
a('Time After Time 38 mm - edição limitada de 88 peças','TAT','2026/10/TAT.jpg','Hora saltante. Aço 316L, 38 × 11,8 mm, safira, fundo aberto, 10 ATM. Calibre IN.S200JH com módulo de hora saltante, 38 h, 25 rubis. Coleção mais nova do site (2026).')
a('Holy Land 1000 - edição limitada','HOLY LAND 1000','2018/11/HLFRONT-2.png','Aço 316L, 44 × 12 mm. Calibre 6498-1 esqueletizado de corda manual, 38 h, indicador de reserva de marcha. O site diz edição de 99 peças no texto e de 40 na descrição. Esgotado.')
a('Holy Land 2026 - preto - edição limitada','HOLY LAND 2026','2018/11/HL.BLACK-Front-2026.png','Aço 316L, 44 × 12 mm. Calibre 6498-1 esqueletizado de corda manual, 38 h, indicador de reserva de marcha. Versão preta de 2026 (também "HOLILAND" na coleção Jewish Heritage).')
sdc='Aço 316L de 3 partes, 40 × 8,4 mm, safira, fundo aberto, 5 ATM. Calibre IN.S200 (Sellita SW240 modificado) automático, 38 h, data e dia. 2023; US$ 4.900 (CHF 4.800 no GPHG).'
a('Seven-Day Cycle Rest Day - mostrador branco - edição limitada de 77 peças','SDC-REST.W','2023/07/sdc4.png','Dias 1 a 7 vazados; o dono escolhe o dia de descanso. '+sdc+' No site oficial: RESTDAY.WT. Concorreu no GPHG 2023.')
a('Seven-Day Cycle Rest Day - mostrador azul - edição limitada de 77 peças','RESTDAY.BL','2023/07/sdc.4.png','Dias 1 a 7 vazados; dia de descanso personalizável. '+sdc)
a('Seven-Day Cycle - mostrador branco - edição limitada de 77 peças','SEVEN-DAY CYCLE.WT','2023/07/sdc.3-1.png','Nomes dos dias da semana vazados, data às 6 h. '+sdc)
a('Seven-Day Cycle - mostrador azul - edição limitada de 77 peças','SEVEN-DAY CYCLE.BL','2023/07/sdc.2.png','Nomes dos dias da semana vazados, data às 6 h. '+sdc)
tq='Aço 316L 44 × 12 mm, safira nos dois lados, 5 ATM. Calibre IN.AR (Alfred Rochat, base ETA 6498) de corda manual, 46 h. Quatro discos giratórios, um por quarto do dia, mostram as horas. 2022; US$ 6.800 / CHF 6.800. Concorreu no GPHG 2022 (ref. TQ).'
for c,i,d in [('TIME QUARTERS.YL','2022/04/TQ.YL_.png','mostrador preto com discos amarelos'),('TIME QUARTERS.RD','2022/04/TQ.RD_.png','mostrador preto com discos vermelhos'),('TIME QUARTERS.GN','2022/04/TQ.GR_.png','mostrador preto com discos verdes'),('TIME QUARTERS.4C','2022/04/TQ.4C.png','mostrador de quatro cores')]:
    a(f'Time Quarters - {d} - edição limitada de 24 peças',c,i,tq)
ry='Mostrador inspirado na grade do motor e reserva de marcha como marcador de combustível. Aço 316L 41,6 × 44,6 × 10,6 mm, safira, fundo aberto, 5 ATM. Calibre 6498-1 esqueletizado preto de corda manual, 38 h. 2020; US$ 5.150.'
a('Rally - edição limitada de 99 peças','RALLY.BK','2020/11/RALLY.BK_.png',ry)
a('Rally PVD - edição limitada de 99 peças','RALLY.BK.PVD','2020/11/RALLYPVD.png',ry+' Caixa com PVD preto.')
fr='Peça única. Mostrador esqueletizado com padrão fractal; série de 8 peças únicas que não serão repetidas. Aço 316L com PVD preto, 40 × 44 mm, 6,24 mm de altura, safira, fundo aberto, 5 ATM. Calibre IN.VMF5400 (Vaucher) automático extrafino com microrrotor, 48 h, data. Agosto de 2020; CHF 9.990 no GPHG 2020 (ref. FRAC2020), US$ 11.800. Esgotado.'
for k,i in enumerate(['FRAC-1.jpg','FRAC2-1.jpg','FRAC3.jpg','FRAC4.jpg','FRAC5.jpg','FRAC6.jpg','FRAC7.jpg','FRAC8.jpg'],1):
    a(f'Fractal {k:02d}',f'FRACTAL{k:02d}','2020/08/'+i,fr)
nf='Peça única. Mostrador laqueado à mão com ouro 24k que mostra a cidade vista do avião à noite; pequenos segundos em forma de hélice às 10 h; fundo de safira em forma de janela de avião. Aço 316L com PVD preto, 44 × 12 mm, 5 ATM. Calibre 6497-1 esqueletizado e rutenizado, corda manual, 38 h. 2020; US$ 16.800.'
for city,img,st in [('Jerusalem','watch-NFjerisalem.png',' Esgotado. Concorreu no GPHG 2020 (ref. NF-JER 1/1).'),('Cairo','watch-NFcairo.png',''),('Las Vegas','watch-NFlasvegas.png',''),('Seoul','watch-NFseoul.png',''),('Athens','watch-NFathens.png',''),('Berlin','watch-NFberlin.png',' Esgotado.'),('Beijing','watch-NFbeijing.png',''),('Taipei','watch-NFtaipei.png',' Esgotado.'),('Melbourne','watch-NFmelbourne.png',''),('Denver','watch-NFdenver.png','')]:
    a(f'Night Flight {city}','NF-JER' if city=='Jerusalem' else '','2020/08/'+img,nf+st)
ro='12 janelas espalhadas mostram as horas em ordem anti-horária; disco central repete a hora. Aço 316L 44 × 12 mm, safira, fundo aberto, 5 ATM. Calibre IN.AR / IN.IP13 (Unitas modificado) de corda manual. Baselworld 2019; US$ 6.800.'
a('ReOrder - mostrador branco - edição limitada de 24 peças','REORDER.WT','2019/02/REORDER.WT_-1.jpg',ro)
a('ReOrder - mostrador azul - edição limitada de 24 peças','REORDER.BL','2019/02/REORDER.BL_.NS_.jpg',ro)
a('ReOrder - mostrador dourado - edição limitada de 24 peças','REORDER.GD','2019/02/REORDER.GD_-2.jpg',ro+' Esgotado.')
fm2=fm+' 2018; US$ 9.800.'
a('Full Month - mostrador azul - edição limitada de 18 peças','FULL MONTH.BL','2018/11/FM.BL_.jpg',fm2+' Esgotado.')
a('Full Month - mostrador branco - edição limitada de 18 peças','FULL MONTH.WT','2018/11/FM.W.jpg',fm2+' Esgotado.')
a('Full Month - mostrador preto - edição limitada de 18 peças','','https://wornandwound.com/library/uploads/2018/09/Itay-Noy-Full-Month-6.jpg',fm2+' Citado só pela Worn & Wound (2018); não aparece no site oficial.')
a('Full Month Moon - edição limitada de 18 peças','FULL MONTH.MN','2018/11/FM.jpg','Os 31 números do mês trocados por 31 fases da lua. '+fm2+' Esgotado.')
tt='Discos coloridos giratórios fazem o papel do ponteiro das horas; o dono escolhe qual disco marca a hora. Aço 316L 44 × 12 mm, safira, fundo aberto, 5 ATM. Calibre IN.IP13 / IN.AR de corda manual.'
a('Time Tone - mostrador azul - edição limitada de 24 peças','TONE.BL','2018/11/TT.BL_.jpg',tt+' Azul com banho de ouro. 2017; US$ 5.600.')
a('Time Tone - mostrador preto - edição limitada de 24 peças','TONE.BK','2018/11/TT.BK_.jpg',tt+' Preto com banho de rutênio. 2017; US$ 5.600.')
a('Time Tone Color Wheel (Color Wheel Hour) - edição limitada de 24 peças','TONE.CW','2018/11/TT-CW-1.png','12 aberturas sobre um disco com 12 cores. '+tt+' 2021; US$ 5.600. Peças numeradas no mostrador.')
ct='Signos do zodíaco no disco das horas. Aço 316L 44 × 12 mm, safira, fundo aberto, 5 ATM, mostrador com banho de ouro e rutênio. Calibre IN.AR de corda manual, 46 h. 2017.'
a('Celestial Time Western - edição limitada de 24 peças','CT.EU','2018/11/CT.EU_.png','Zodíaco ocidental. '+ct)
a('Celestial Time Chinese - edição limitada de 24 peças','CT.CH','2018/11/CT.CH_.png','Zodíaco chinês. '+ct)
cg='Duas engrenagens giram em volta do ponteiro das horas: uma mostra as 24 horas e a outra 8 fases do dia ("Dynamic Dial"); não é cronógrafo. Aço 316L 44 × 12 mm, 5 ATM. Calibre de corda manual (Isoprog 13 / IN.AR), 42-46 h. 2016; US$ 5.800.'
a('Chrono Gears - mostrador preto - edição limitada de 24 peças','CHRONO GEARS.BK','2018/11/CG.BK_.FRONT_.EDIT_.png',cg)
a('Chrono Gears - mostrador azul - edição limitada de 24 peças','CHRONO GEARS.BL','2018/11/CG.ROYAL_.FRONT_.EDIT_.png',cg+' Esgotado.')
om='"Memento mori" que mostra as engrenagens em movimento. Aço 316L 44 × 12 mm, safira, fundo aberto, 5 ATM, mostrador com banho de ouro e rutênio. Calibre 6497-1 esqueletizado de corda manual, 38 h. 2016.'
for c,i,d in [('OPEN MIND-F.BK','OM.F.FRONT_.BK_.EDIT_.png','F preto'),('OPEN MIND-F.BL','OM.F.FRONT_.BL_.EDIT_.png','F azul'),('OPEN MIND-S.BK','OM.S.FRONT_.BK_.EDIT_.png','S preto'),('OPEN MIND-S.BL','OM.S.FRONT_.BL_.EDIT_.png','S azul')]:
    a(f'Open Mind {d} - edição limitada de 99 peças',c,'2018/11/'+i,om)
pt='Mostrador dividido em dia (6h-18h) e noite. Aço 316L de 3 partes, 41,6 × 44,6 × 10,6 mm, safira nos dois lados, coroa às 4 h, 5 ATM. Calibre IN.DD&6498-1 de corda manual, 38 h. Baselworld 2015; US$ 4.800.'
a('Part Time Sun & Moon - mostrador branco - edição limitada de 24 peças','PART TIME.SM.W','2018/11/PT.SM_.W.jpg','Janelas de sol e lua. '+pt)
a('Part Time Sun & Moon - mostrador azul - edição limitada de 24 peças','PART TIME.SM.BL','2018/11/PT.SM_.BL_.jpg','Janelas de sol e lua. '+pt)
a('Part Time Day & Night - mostrador preto - edição limitada de 24 peças','PART TIME DN.BK','2018/11/PT.DN_.BK_.jpg',pt+' Esgotado.')
a('Part Time Day & Night - mostrador azul - edição limitada de 24 peças','PART TIME DN.BL','2018/11/PT.DN_.BL_.jpg',pt+' Esgotado.')
a('Part Time AM PM - mostrador azul e preto','DN.BL&BK','https://cdn.sanity.io/images/j0ua8uvr/production/9ae044c1bd389b5993aff4c89350135696ba7ab3-2400x2400.jpg','Mostrador dinâmico em dois tons, azul e preto. Aço 41,6 × 44,6 × 10,6 mm. Calibre IN.DD&6498-1 de corda manual. Quinta cor, lançada depois das 4 de 2015 (leilão Loupe This, lote 2385, 2023).')
pv='Mostrador esqueletizado com mapa-múndi ou símbolos religiosos. Aço 316L 42,4 × 10,4 mm, safira, fundo aberto, 5 ATM. Automático, 42 h, data. Esgotado.'
for c,i in [('POV-1','2026/08/2.png'),('POV-2','2026/08/1.png'),('POV-3','2026/08/3.png'),('POV-R','2026/08/4.png'),('POV-R.RD','2026/08/7.png')]:
    a(f'Point of View {c[4:]} - edição limitada de 99 peças',c,i,pv)
hs='Caixa quadrada de aço 316L 42,4 × 42,4 × 11,6 mm, safira, fundo aberto, 5 ATM. TechnoTime TT651-24H automático (2º fuso, dia/noite 24 h, grande data), 42 h. 2013; US$ 6.900.'
a('Hyper Cityscape - edição limitada de 24 peças','CITYSCAPE','2018/11/CITYSCAPE.jpg',hs)
a('Hyper Cityscape - negativo - edição limitada de 24 peças','','https://www.ablogtowatch.com/wp-content/uploads/2013/04/Itay-Noy-Hyper-Scape-2.jpg','Versão em tons invertidos (noite), citada pela aBlogtoWatch (2013); não aparece no site oficial. '+hs)
a('Hyper Landscape - edição limitada de 24 peças','LANDSCAPE','2018/11/LANDSCAPE.jpg',hs)
a('Hyper Landscape - negativo - edição limitada de 24 peças','','https://www.ablogtowatch.com/wp-content/uploads/2013/04/Itay-Noy-Hyper-Scape-5.jpg','Versão em tons invertidos (noite), citada pela aBlogtoWatch (2013); não aparece no site oficial. '+hs)
mk='Caixa quadrada de aço 316L 42,4 × 42,4 × 11,6 mm, safira, fundo aberto, 5 ATM. TechnoTime TT651-24H automático (2º fuso, dia/noite 24 h, grande data), 42 h.'
a('Mask 01 - edição limitada de 24 peças','MASK01','2018/12/MASK02.jpg',mk+' No site, a foto do MASK01 tem o nome de arquivo MASK02.')
a('Mask 02 - edição limitada de 24 peças','MASK02','2018/12/MASK01.jpg',mk+' No site, a foto do MASK02 tem o nome de arquivo MASK01.')
dl='Aço 316L 41,6 × 44,6 × 10,6 mm, safira, fundo aberto, 5 ATM. Calibre 6498-1 de corda manual, 38 h, pequenos segundos.'
for c,i,d in [('DiaLOG-ROM','DLG.R.jpg','numerais romanos'),('DiaLOG-ROM.L','DLG.RL_.jpg','numerais romanos (L)'),('DiaLOG-NUM','DLG.N.jpg','numerais arábicos'),('DiaLOG-NUM.L','DLG.NL_.jpg','numerais arábicos (L)')]:
    a(f'DiaLOG - {d} - edição limitada de 99 peças',c,'2018/11/'+i,dl)
xr='Mostrador esmaltado gravado como uma radiografia do movimento. Aço 316L 41,6 × 44,6 × 10,6 mm, safira, fundo aberto, 5 ATM. Calibre 6497-1/6498-1 de corda manual, 38 h, pequenos segundos. Lançado em 2011.'
a('X-Ray B - edição limitada de 99 peças','X-RAY.B','2018/12/X-RAY-B.jpg',xr)
a('X-Ray S - edição limitada de 99 peças','X-RAY.S','2018/12/X-RAY-S.jpg',xr)
a('X-Ray G - edição limitada de 99 peças','X-RAY.G','2018/12/X-RAY.G.jpg',xr)
a('X-Ray - edição limitada de 99 peças','XRAY6497INVG','https://www.luxuriousmagazine.com/wp-content/uploads/2011/04/itay-noy-xray-collection.jpg','Aço, 41,5 × 10,6 mm, safira, fundo aberto, 50 m. ETA 6497-1 de corda manual. Mostrador prateado. Referência do WatchBase e da Majestix; pode corresponder a uma das versões do site oficial.')
sk='Aço 316L 41,6 × 44,6 × 10,6 mm, safira, fundo aberto, 5 ATM. Calibre 6497-1 esqueletizado de corda manual, 38 h, pequenos segundos.'
a('Skeleton S - edição limitada de 99 peças','SKELETON.S','2018/12/SKEL.B-new.jpg',sk)
a('Skeleton G - edição limitada de 99 peças','SKEL6497G','2018/12/SKEL.G.FRONT-new.jpg',sk+' Movimento banhado a ouro. No site oficial: SKELETON.G.')
mx='Aço 316L, 42,4 × 10,4 mm, safira, fundo aberto, 5 ATM, mostrador esmaltado. ETA 2824-2 automático, 38 h, data.'
a('Maximalism Max 01 - edição limitada de 99 peças','MAX01','2018/12/MAX-01-NO-STITCH.jpg',mx)
a('Maximalism Max 02 - edição limitada de 99 peças','MAX02','2018/12/MAX-02-NO-STITCH.jpg',mx+' Mostrador preto com numerais romanos e abertura que mostra parte do movimento.')
a('Maximalism Max 03 - edição limitada de 99 peças','MAX03','2018/12/MAX-03-NO-STITCH.jpg',mx)
a('Maximalism Max 04 - edição limitada de 99 peças','MAX04','2018/12/MAX-04-NO-STITCH-WIP.jpg',mx+' Mostrador preto com índices de traço e ponto.')
a('Maximalism Max 05 - edição limitada de 99 peças','MAX05','https://majestixcollection.com/watches/itay-noy-max-05-max05/','Visto só na lista de relógios da Majestix (link da página); pode corresponder ao MAX-DOTS do site oficial.')
a('Maximalism Max 06 - edição limitada de 99 peças','MAX06','https://majestixcollection.com/wp-content/uploads/2023/06/Itay-Noy-Max-06-MAX06.jpg',mx+' Referência do WatchBase e da Majestix; pode corresponder ao MAX-DOTS do site oficial.')
a('Maximalism Max Dots - edição limitada de 99 peças','MAX-DOTS','2018/12/MAX-DOTS-F.png',mx+' Pulseira marrom.')
a('Maximalism Max Deco - edição limitada de 99 peças','MAX06DECO','2018/12/MAX-DECO-F.png',mx+' No site oficial: MAX-DECO.')
for c,i,d in [('ARABIC36.B','2018/12/ARAB.png','Arabic 36 - preto'),('ROMAN36.B','2018/12/ROM1.png','Roman 36 - preto'),('JAPANESE36.B','2018/12/JAP.png','Japanese 36 - preto'),('CHINESE36.B','2018/12/CHIN.png','Chinese 36 - preto'),('FRACTAL01.B','2018/12/FRAC01.png','Fractal 01 36 - preto'),('FRACTAL02.B','2018/12/FRAC02.png','Fractal 02 36 - preto')]:
    a(f'Medium Size {d} - edição limitada de 99 peças',c,i,m36+(' No site oficial o código é só FRACTAL01/FRACTAL02/CHINESE.' if 'FRAC' in c or 'CHIN' in c else ''))
for c,i,d in [('ARABIC36.R','ARAB.36R.jpg','Arabic 36 - vermelho'),('ROMAN36.R','ROM.36R.jpg','Roman 36 - vermelho'),('CHINESE36.R','CHAINESE.36R.jpg','Chinese 36 - vermelho'),('JAPANESE36.R','JAP.R36.jpg','Japanese 36 - vermelho'),('FRACTAL01.R','FRAC01.R.jpg','Fractal 01 36 - vermelho'),('FRACTAL02.R','FRAC02.R.jpg','Fractal 02 36 - vermelho'),('ARABIC36.G','ARABIC36.png','Arabic 36 - dourado'),('ROMAN36.G','ROMAN36.png','Roman 36 - dourado'),('CHINESE36.G','CHINESE36.png','Chinese 36 - dourado'),('JAPANESE36.G','JAPANESE36.png','Japanese 36 - dourado'),('FRACTAL01.G','FRACTAL01.png','Fractal 01 36 - dourado'),('FRACTAL02.G','FRACTAL02.png','Fractal 02 36 - dourado')]:
    a(f'Ladies {d} - edição limitada de 99 peças',c,'2019/01/'+i,m36+(' No site: CHAINESE36.R.' if c=='CHINESE36.R' else ' No site: CHANESE36.G.' if c=='CHINESE36.G' else ''))
cs='Mostrador esmaltado com foto aérea de uma praça de cidade. Aço 316L 42,4 × 10,4 mm, safira, fundo aberto, 5 ATM. Automático, 38 h, data. Cerca de 2007-2009. Esgotado.'
a('City Square Kikar Hamedina, Tel Aviv - edição limitada de 99 peças','','2026/08/Hamedina-Front.png',cs)
a('City Square Columbus Circle, NYC - edição limitada de 99 peças','','2026/08/Columbus-Front.png',cs)
a('City Square Piazza San Pietro, Rome - edição limitada de 99 peças','','2026/08/San-Pietro-Front.png',cs)
a("City Square Place de l'Étoile, Paris - edição limitada de 99 peças",'','2026/08/lEtoile-Front.png',cs)
a('City Square Trafalgar Square, London','','https://s3files.core77.com/blog/images/0itaynoy.jpg','Mostrador com foto aérea da praça. Citado pela Core77 (2009) e por Meredith Price (2007); não aparece no site oficial. Foto da coleção.')
du='Relógio reversível de duas faces: duas caixas de aço 316L 42,4 mm empilhadas, 13-14 mm, coroas às 3h30 e 8h30, safira. 2009; US$ 3.800. O site oficial fala em edição de 99 peças com dois movimentos mecânicos; a aBlogtoWatch (2009) cita dois quartzos ETA 995.112. Esgotado.'
a('Duality Exposed-Concealed - edição limitada de 99 peças','','2026/08/DUALITY-2.png',du)
a('Duality Modern-Classical - edição limitada de 99 peças','','2026/08/DUALITY-6.png',du)
a('Duality Everyday-Holiday - edição limitada de 99 peças','','2026/08/DUALITY-1.png',du)
a('Duality Decorative-Informative','','https://www.ablogtowatch.com/wp-content/uploads/2009/04/itay-noy-duality-decorative-informative-2.jpg',du.replace(' Esgotado.','')+' Citado pela aBlogtoWatch (2009); não aparece no site oficial.')
a('Netline - edição limitada de 99 peças','','https://www.luxuriousmagazine.com/the-x-ray-and-netline-collection-from-itay-noy/','Esqueleto com grade sobre o mostrador e recortes circulares que mostram o movimento gravado; corda manual suíço. Lançado em 2011, peças numeradas. Visto só no texto do artigo (link da página).')
a('Reflective','','https://meredithprice.com/me/Innovations/Itaynoy.html','Tema de cidade e trânsito ("Reflective City Square"). Citado em 2007. Visto só no texto (link da página).')
a('Second Time','','https://archive.israel21c.org/?p=2864','Relógios antigos refeitos com mostradores de fotos e ponteiros parados na hora em que pararam. Anos 2000 (citado em 2007). Visto só no texto (link da página).')
names=[r[0] for r in R]; import collections
d=[k for k,v in collections.Counter(names).items() if v>1]; assert not d,d
assert not any('|' in x for r in R for x in r)
open('/home/claude/trabalho/dados_ItayNoy.txt','w').write('\n'.join('|'.join(r) for r in R)+'\n')
print(len(R))
