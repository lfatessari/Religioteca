import json
rows=[tuple(r) for r in json.load(open('rows.json'))]
def add(n,c,e): rows.append((n,c,'',e))
m3="Quartzo Ronda 708 com fase da lua; 34 mm, mostrador efeito areia vulcânica, aço 316L, 100 m"
dia="Caixa cravejada de diamantes (o site oferece versões com 12 e 64 diamantes); "+m3
for c in "A151UAA-AG-MA150 A151UAA-TF-BP0886TF A151UAA-SP-MA150 A151UAA-AG-BP0886BU A151UAA-SP-BP0886TM A151UAA-TF-MA150 A151UAA-VL-BP0886VL A151UAA-VL-MA150 A151SAA-VL-MA150 A151SAA-VL-BP0886VL A151SAA-TF-MA150 A151SAA-TF-BP0886TF A151SAA-SP-MA150 A151SAA-SP-BP0886TM A151SAA-AG-BP0886BU A151SAA-AG-MA150".split():
  add("M03-3 Moon Phase Diamonds",c,dia)
# fix diamond names
rows=[(("M03-3 Moon Phase Diamonds",c,i,dia) if n.startswith("M03-3 Moon Phase – caixa") else (n,c,i,e)) for n,c,i,e in rows]
m2="41 mm, 11,9 mm, aço 316L, safira, 50 m"
for c in "A740T-3K-BP22740NAN A740T-1N-BP22740NAN A740T-RK-BP22740NAN A740T-2V-BP22740NAN A740T-PN-BP22740NAN".split():
  add("M02 Toni Art – edição limitada pintada à mão",c,"Caixa pintada à mão por Toni Art; "+m2)
for c in "A740C-ZA-GG2710N A740C-NM-GG2710N A740C-VA-GG2710N A740C-ZA-GG2710U A740C-ZA-BP22740UAU A740C-ZA-BMA22740A A740C-VA-BP22740NAN A740C-VA-BMA22740A A740C-NM-BMA22740A A740C-NM-BP22740NAN".split():
  add("M02-5 Date",c,"Automático (base SW-200, 38 h); mostrador escovado vertical; "+m2)
for c in "A740A-RN-BP22740MAM A740A-RN-P140MR2 A740A-RN-BMA22740A A740A-BU-BP22740UAU A740A-BU-P140BU2 A740A-BU-BMA22740A A740A-AG-BP22740MAM A740A-AG-BP22740NAN A740A-AG-P140MR2 A740A-AG-P140NR2 A740A-AG-BMA22740A A740A-NR-BP22740NAN A740A-NR-P140NR2 A740A-NR-BMA22740A".split():
  add("M02-5 Date",c,"Automático (base SW-200, 38 h); mostrador guilloché; "+m2)
for c in "A740L-RN-BP22740MAM A740L-RN-P140MR2 A740L-RN-BMA22740A A740L-BU-BP22740UAU A740L-BU-P140BU2 A740L-BU-BMA22740A A740L-AG-BP22740MAM A740L-AG-P140MR2 A740L-AG-BP22740NAN A740L-AG-P140NR2 A740L-AG-BMA22740A A740L-NR-BP22740NAN A740L-NR-P140NR2 A740L-NR-BMA22740A".split():
  add("M02-5 Moonphase",c,"Automático AN280 (base SW-280, 38 h) com fase da lua; mostrador guilloché; "+m2)
add("O.H.M. L06","L06","Corda manual AN501, base UT-176 (1951) restaurado em 2006; pequenos segundos; tiragens de 300 (18 rubis) e 125 (17 rubis) peças")
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=0);print(len(rows),len({r[1] for r in rows}))
