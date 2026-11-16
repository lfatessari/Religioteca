# handle -> list of (sufixo, imagem, carac) ; sem entrada = linha única com a foto base
V = {
'lumin-g100': [('Silver','G100-NEW-SS.png?v=1768533103'),('Grey','G100-NEW-G.png?v=1775786375')],
'lighthouse-n': [('Silver','lighthousebrownstrap_1.png?v=1780457797'),('Gold','lighthouse_new_color8_6aa1bada-6ddb-45ea-bcc2-847fe7ea465f.png?v=1784688500'),('Gold Silver','lighthouse_new_color2.png?v=1784615923'),('Silver Classic - Ship I','Lighthouse-classic.png?v=1790652257')],
'radar': [('Silver-Green','Radar-sg_1.png?v=1792400729'),('Black-Green','Black-G.png?v=1787126572'),('Black-Red','radarwatch_1.png?v=1787126625')],
'desktop-95': [('Blue','90sPC925.png?v=1790675509'),('White','90sPCwhite_cac10f48-019d-4d1c-a8b7-57d33188b4de.png?v=1793685828')],
'melt-tank': [('Silver','2_2cc607af-f0f6-4c0b-8373-c12ef70edcbd.png?v=1765038785'),('Gold','Gold-2.png?v=1782977238'),('Black','Melt_tank5.png?v=1785492818'),('Silver II','Melt_tank1.png?v=1785492818'),('Gold II','Melt_tank6_78347a0b-947a-481d-9554-2638c226773b.png?v=1785493238')],
'r200': [('Silver','R2002.png?v=1785735865'),('Gold','R200_Gold.png?v=1789959194')],
'r100-1': [('Silver','R100-Silver.png?v=1789957944'),('Gold','R100_Gold.png?v=1789958407')],
'g400': [('Silver-Green','G400Silver-Green_5b5ab6f2-8fc4-460d-bcf2-e5cc1b153fb3.png?v=1778305653'),('Silver-Red','G400Silver-Red_65f139fb-e3fb-4a14-b078-c8a49c800341.png?v=1778305653'),('Grey-Red','G400Grey.png?v=1778305653'),('Gold-Red','G400Gold.png?v=1778305655'),('Gold-Green','G400Gold-Green_a0bac8e8-3a37-462a-a8c4-20f4702675ca.png?v=1778305653')],
'g200': [('Silver-Red','G200silver-Front_view.png?v=1769767748'),('Gold-Red','G200-Gold_1.png?v=1769768152'),('Silver-Green','Silver-G.png?v=1778207553'),('Black-Red','Black-G200_3.png?v=1769768152')],
}
C = {
'lumin-g100':'Caixa de liga de zinco, 38 × 46,5 mm, 13 mm de espessura; movimento digital eletrônico Benlydesign; 30 m.',
'lighthouse-n':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.',
'radar':'Caixa de liga de zinco, 38 × 46,5 mm, 13 mm; digital eletrônico; 50 m.',
'desktop-95':'Mostrador que imita a área de trabalho do Windows 95. Caixa de aço 316L, 39 × 44,5 mm, 10 mm; quartzo suíço; 50 m.',
'after-100-years-limited-edition':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.',
'recure':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.',
'fighter-limited-edition':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.',
'melt-tank':'Caixa de aço 316L, 30 × 37 mm, 13 mm; quartzo Miyota; 30 m.',
'base-moon':'Caixa de aço 316L, 39 × 46,5 mm; quartzo suíço; 50 m.',
'sleep-mission':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.',
'sleepy':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.',
'r200':'Caixa de aço 316L, 30 × 37 mm, 13 mm; Miyota 2025; vidro de safira; 30 m.',
'r100-1':'Caixa de aço 316L, 39 × 47 mm; Miyota 2025; 30 m.',
'g400':'Caixa de aço, 38 × 46,5 mm, 13 mm; movimento digital eletrônico próprio; 50 m.',
'g200':'Caixa de liga de zinco, 38 × 46,5 mm; digital eletrônico; 30 m.',
}
LIM = {'desktop-95':500,'after-100-years-limited-edition':500,'recure':500,'fighter-limited-edition':500,'base-moon':500,'sleep-mission':500,'g200':1000}
V.update({
'time-gallery':[('Bronze Gold','BronzeGold.png?v=1779702221'),('Silver - ponteiro branco','TG-Silver-Hand.png?v=1786588199'),('Silver - ponteiro preto','TG-Silver-Black-Hand.png?v=1786588199'),('Gold','Gold_65fd4237-5068-4a70-990d-ac2352b67252.png?v=1785377170')],
'planet-dashboard-ii':[('Moon','Moon-Hand-Black_strap.png?v=1787106748'),('Earth','Earth_dd96203e-53c1-4049-92a5-d1f03a5fbbbb.png?v=1784777421'),('Mars','Mars_2_7681a597-e799-4261-81ac-06166089906e.png?v=1784777666'),('Vintage Chart','VintageChart_a048b7d9-398b-4809-8fdf-9012d8df9ab2.png?v=1784777126'),('Black Hole','Black-hole.png?v=1784777629'),('Jupiter','Jupiter_2.png?v=1784777796')],
'escape':[('Steel','digital-2.png?v=1778123566'),('Gold','gold-l.png?v=1778125375')],
'm4':[('Silver','Silver-M4.png?v=1780990718'),('Black','M4-Black.png?v=1780989773'),('Gold','M4-G.png?v=1767165138'),('Red','M4-Red.png?v=1780989773'),('Steel Matte','M4-steel.png?v=1780989773')],
'steel-tank':[('White','white_4cff00f5-5a1b-4176-9a50-3001a42696dc.png?v=1776735417'),('Yellow','yellow_f53b997a-3266-4b6e-8542-c9e7b1f90648.png?v=1776735428')],
})
C.update({
'time-gallery':'Hora saltante. Caixa de aço 316L, 32 × 42 mm, 9 mm; automático TY2709; 50 m.',
'planet-dashboard-ii':'Caixa de aço 316L, 43 × 25 mm; dois movimentos de quartzo; 30 m.',
'escape':'Caixa de liga de zinco, 50 × 80 mm, 13 mm; movimento digital eletrônico próprio; 30 m.',
'm4':'Caixa de aço 316L, 49 × 51 mm; quartzo; 30 m.',
'steel-tank':'Hora saltante. Caixa de aço 316L, 39 × 46,5 mm, 10 mm; automático TY2709; 50 m.',
})
LIM.update({'time-gallery':1000,'escape':1000})
V.update({
'redline-1':[('Silver-Red','Redline_Front_view.png?v=1780641691'),('Silver-Blue','redline_15.png?v=1788168077'),('Silver-Green','redline_16.png'),('Black-Red','redline-black_1.png?v=1788156331'),('Black-Green','redline_3_de0d5733-c924-4ba7-bb70-fa1b3b0f6715.png?v=1788170840'),('Gold','redline-gold_4_1aeed65b-a925-4140-a451-b22fc142f415.png?v=1790738630')],
'mk2':[('Silver-Red','MK2-SR.png?v=1775532898'),('Silver-Green','MK2-S-Green.png?v=1775532898'),('Gold-Red','MK2-GR.png?v=1775532898'),('Black-Red','MK2-BR.png?v=1775532898'),('Silver-White','MK2-SW.png?v=1775532898'),('Black-Green','MK2-B-Green.png?v=1775532898')],
'magnet-orbit':[('Earth','EA8A7726.png?v=1786676433'),('Moon','EA8A7725.jpg?v=1786676383'),('Mars','EA8A7723.jpg?v=1786676383'),('Jupiter','benlywatch-Magnet-ORi-Jupiter.png?v=1776750813'),('Saturn','benlywatch-Magnet-ORi-SATURN.png?v=1776750813')],
})
C.update({
'redline-1':'Caixa de metal, 43,2 × 40 mm; movimento digital próprio com LED vermelho; 30 m.',
'mk2':'Caixa de liga, 45 × 40 mm; movimento eletrônico Benlydesign com tela OLED; 50 m.',
'mk3':'Silver-Red. Caixa de liga, 45 × 40 mm, 14 mm; movimento eletrônico com tela OLED; 50 m.',
'magnet-orbit':'Caixa de cobre, 42 × 49 mm, 13 mm, fundo de aço 316L; quartzo Miyota; 30 m.',
'retro-letter':'Caixa de metal, 36 × 43,2 mm, 9 mm; digital próprio; 30 m.',
})
LIM.update({'mk2':3000})
V.update({
'y2k-metal-unique-digital-watch-x6000s':[('X6000S Shiny','IMG_1031_478a4b00-8ada-49a1-b969-c596f345fbc0.png?v=1764838366'),('X6000S Matte','IMG_1053.png?v=1764838366'),('X6000 Black','IMG_1054_9c9057e7-fec5-41aa-bad2-9ec89b8d1e02.png?v=1764838366')],
'flavor':[('Coffee','coffee-fa.png?v=1788849195'),('Orange','Orange_cfc8148a-a9ab-4ea5-85d1-1c7acd82e177.png?v=1789980068'),('Mint Lemon','Lemon112.png?v=1789980695'),('Grapefruit','Grapefruit_1.png?v=1785137542'),('Avocado','Avocado_1.png?v=1785137575'),('Chili','Chili_3.png?v=1785137595')],
'pulse-matrix':[('Steel','getpulsematrix_1.png?v=1789526993'),('Silver','getpulsematrix_4.png?v=1789526993'),('Gold','getpulsematrix_3.png?v=1789526993'),('Steel-Green','getpulsematrix_2.png?v=1789526993'),('Silver-Green','getpulsematrix_5.png?v=1789526993')],
'g300-limited-edition':[('Silver-Red','G300_3.png?v=1780545028'),('Gold-Red','G300-GOLD_1.png?v=1780545142')],
})
C.update({
'y2k-metal-unique-digital-watch-x6000s':'Caixa de aço, 31 × 34 mm; movimento digital eletrônico próprio; 30 m.',
'flavor':'Caixa de aço 316L, 43 × 25 mm, 11 mm; quartzo; 30 m.',
'pulse-matrix':'Caixa de aço, 40 × 44 mm, 13 mm; movimento digital eletrônico Benlydesign; 30 m.',
'lighthouse-mechanical-limited-edition':'Caixa de aço 316L, 39 × 46,5 mm, 10 mm; automático japonês 9015; 50 m.',
'g300-limited-edition':'Caixa de liga de zinco, 38 × 46,5 mm, 13 mm; movimento digital eletrônico próprio; 30 m.',
})
LIM.update({'flavor':3000,'lighthouse-mechanical-limited-edition':1000,'g300-limited-edition':1000})
Q='Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; 50 m.'
for h in ['f1-0-0001s','sallon-limited-edition','prison-break-limited-edition','octopus-treasure','orchard-dream-limited-edition']: C[h]=Q; LIM[h]=500
C['ukiyoe-limited-edition']='Caixa de aço 316L, 39 × 44,5 mm, 10 mm; quartzo suíço; 50 m.'; LIM['ukiyoe-limited-edition']=500
V['band-80']=[('Orange','BAND80orange-steel.png?v=1786678190'),('Beach','BAND80_rainbow.png?v=1786678190'),('Red','BAND80_red-steel.png?v=1786678191')]
C['band-80']='Caixa de liga de zinco, 38 × 45 mm, 13 mm, fundo de aço; movimento digital eletrônico próprio; 30 m.'
C['vacation-away-from-work']=Q; LIM['vacation-away-from-work']=500
V['kyosi']=[('Silver','ALTER-N_4bd9d2a4-0049-4f44-8178-e82e7c24f7c5.png?v=1766736930'),('Orange','o.png?v=1767778573'),('Gold','g_cadcd293-2677-44eb-89b1-1a77716cd3a3.png?v=1767778573'),('Rose Gold','rg_a00778fc-2910-4a7e-9d25-e159a887461e.png?v=1767778573'),('Black','b_2658b7af-7a78-46d7-86b9-297083379e61.png?v=1767778573')]
C['kyosi']='Caixa de aço 316L, 35 × 46,5 mm, 13 mm; quartzo Miyota; 30 m.'
Q2='Caixa de aço 316L, 39 × 44,5 mm, 10 mm; quartzo suíço; 50 m.'
C['last-picnic']=Q2; LIM['last-picnic']=500
C['dreamwave']=Q2; C['melt-time']=Q2
C['torch']='Caixa de aço 316L, 39 × 46,5 mm, 10 mm; quartzo suíço; vidro de safira; 50 m.'; LIM['torch']=500
V['alien-drop']=[('Black-Green','AD_1.png?v=1789436355'),('Black-Blue','AD-11.png?v=1791797007'),('Cream','AD_2.png?v=1789436355'),('Silver-Blue','AD_3.png?v=1789436356'),('Silver-Green','AD-22.png?v=1791797007')]
C['alien-drop']='Caixa de aço, 36 × 45 mm, 12 mm; quartzo suíço; 50 m.'; LIM['alien-drop']=1000
V['t10']=[('Silver','T10_3.png?v=1787302198'),('Black','T10_1.png?v=1787302198'),('Gold','T10_2.png?v=1787302198')]
C['t10']='Caixa de aço, 42 × 50 mm, 13 mm; movimento digital eletrônico próprio; 30 m.'; LIM['t10']=1000
C['loch-hunt']=Q; LIM['loch-hunt']=500
V['time-frame-limited-edition']=[('Silver-Black','03-black-silver.png?v=1792136503'),('Rose Gold-Black','04-black-rose-gold.png?v=1792136503'),('Classic Silver','05-white-silver.png?v=1792136519'),('Classic Rose Gold','06-white-rose-gold.png?v=1792136519')]
C['time-frame-limited-edition']='Hora saltante. Caixa de aço 316L, 32 × 42 mm, 9 mm; automático TY2709; 50 m.'; LIM['time-frame-limited-edition']=1000
C['sakura-journey']=Q2; LIM['sakura-journey']=500
C['friends-limited-edition']='Caixa de aço 316L, 39 × 46,5 mm; quartzo suíço; 50 m.'; LIM['friends-limited-edition']=500
V['race-timer']=[('Silver','raceTimer_7f8f6705-0164-4271-8906-a9ced4b3bda6.png?v=1789006886'),('Black','rt-black.png?v=1789006888')]
C['race-timer']='Caixa de liga de zinco, 40 × 45 mm, 12 mm; movimento digital eletrônico Benlydesign; 30 m.'
C['built-from-above-built-from-above']=Q2
