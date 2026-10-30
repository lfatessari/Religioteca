import re
def san(ref):
    parts=ref.split('.')
    out=[parts[0]]
    for p in parts[1:]:
        out.append(p+'_' if re.fullmatch(r'[A-Za-z]{2,5}\d?',p) else p)
    return '.'.join(out)
def base(name,ref):
    s=('Damasko-'+name+'-'+ref).replace(' ','-')
    # sanitize whole string by dot parts (last part kept)
    parts=s.split('.')
    out=[parts[0]]+[ (p+'_' if re.fullmatch(r'[A-Za-z]{2,5}\d?',p) else p) for p in parts[1:]]
    return '.'.join(out)
# (watchbase name, ref, nome_planilha, codigo, E)
L='''DK 11|DK11|DK11|DK11|Modelo anterior; 42,8 mm; aço; mostrador branco; calibre de manufatura A35-1; luneta giratória de 12 horas.
DK 10 Black|DK10|DK10 Black|DK10|Modelo anterior; caixa preta.
DK 11 Black|DK11|DK11 Black|DK11|Modelo anterior; caixa preta.
DH 1.0|DH1.0|DH1.0|DH1.0|Modelo anterior; ETA 2836-2; aço, 40 mm; luneta de mergulho 0–60.
DK 15|DK15|DK15|DK15|Modelo anterior; 42,8 mm; aço; mostrador branco; calibre de manufatura A35-1; luneta de 12 horas.
DA 42 Black|DA42.black|DA42 Black|DA42.black|Modelo anterior; caixa preta.
DA 43 Black|DA43.black|DA43 Black|DA43.black|Modelo anterior; caixa preta.
DA 46 Black|DA46.black|DA46 Black|DA46.black|Modelo anterior; caixa preta.
DA 47 Black|DA47.black|DA47 Black|DA47.black|Modelo anterior; caixa preta.
DA 44 Black|DA44.black|DA44 Black|DA44.black|Modelo anterior; caixa preta.
DA 45 Black|DA45.black|DA45 Black|DA45.black|Modelo anterior; caixa preta.
DK 10|DK10|DK10|DK10|Modelo anterior.
DK 14|DK14|DK14|DK14|Modelo anterior.
DK 14 Black|DK14|DK14 Black|DK14|Modelo anterior; caixa preta.
DA 47|DA47|DA47|DA47|Modelo anterior.
DK 15 Black|DK15|DK15 Black|DK15|Modelo anterior; caixa preta.
DH2.0|DH2.0|DH2.0|DH2.0|Modelo anterior.
DH2.0 Black|DH2.0.black|DH2.0 Black|DH2.0.black|Modelo anterior; caixa preta.
DH3.0|DH3.0|DH3.0|DH3.0|Modelo anterior.
DH3.0 Black|DH3.0.black|DH3.0 Black|DH3.0.black|Modelo anterior; caixa preta.
DS30.blue|DS30.blue|DS30 Blue|DS30.blue|Mostrador azul.
DS30 Green|DS30.green|DS30 Green|DS30.green|Mostrador verde.
DS30.obo|DS30.obo|DS30 OBO|DS30.obo|
DS30 Ocean|DS30.ocean|DS30 Ocean|DS30.ocean|Mostrador Ocean.
DS30 Yellow|DS30.yellow|DS30 Yellow|DS30.yellow|Detalhes amarelos.
DA 343 Black|DA343.black|DA343 Black|DA343.black|Modelo anterior; caixa preta.
DA 20|DA20|DA20|DA20|Modelo anterior.
DA 34|DA34|DA34|DA34|Modelo anterior.
DA 34 Black|DA34.black|DA34 Black|DA34.black|Modelo anterior; caixa preta.
DA 35 Black|DA35.black|DA35 Black|DA35.black|Modelo anterior; caixa preta.
DA 35|DA35|DA35|DA35|Modelo anterior.
DA 36|DA36|DA36|DA36|Modelo anterior (antecessor do DK36).
DA 36 Black|DA36.black|DA36 Black|DA36.black|Modelo anterior; caixa preta.
DA 37|DA37|DA37|DA37|Modelo anterior.
DA 37 Black|DA37.black|DA37 Black|DA37.black|Modelo anterior; caixa preta.
DA 38|DA38|DA38|DA38|Modelo anterior.
DA 38 Black|DA38.black|DA38 Black|DA38.black|Modelo anterior; caixa preta.
DA 343|DA343|DA343|DA343|Modelo anterior.
DA 20 Black|DA20.black|DA20 Black|DA20.black|Modelo anterior; caixa preta.
DA 353|DA353|DA353|DA353|Modelo anterior.
DA 353 Black|DA353.black|DA353 Black|DA353.black|Modelo anterior; caixa preta.
DA 363|DA363|DA363|DA363|Modelo anterior; aço, 42 mm; ETA 2836-2, dia e data; 100 m; mostrador preto fosco com números arábicos.
DA 363 Black|DA363.black|DA363 Black|DA363.black|Modelo anterior; caixa preta.
DA 373|DA373|DA373|DA373|Modelo anterior.
DA 373 Black|DA373.black|DA373 Black|DA373.black|Modelo anterior; caixa preta.
DA 42|DA42|DA42|DA42|Modelo anterior.
DA 43|DA43|DA43|DA43|Modelo anterior.
DA 46|DA46|DA46|DA46|Modelo anterior.
DA 44|DA44|DA44|DA44|Modelo anterior.
DA 45|DA45|DA45|DA45|Modelo anterior.
DC 56 Si|DC56.si|DC56 Si|DC56.si|Modelo anterior; cronógrafo com espiral de silício.
DC 56 Si Black|DC56.si.black|DC56 Si Black|DC56.si.black|Modelo anterior; cronógrafo; caixa preta; espiral de silício.
DC 57 Si|DC57.si|DC57 Si|DC57.si|Modelo anterior; cronógrafo com espiral de silício.
DC 57 Si Black|DC57.si.black|DC57 Si Black|DC57.si.black|Modelo anterior; cronógrafo; caixa preta.
DC 58|DC58|DC58|DC58|Cronógrafo Valjoux 7750; 40 mm.
DC 58 Black|DC58.black|DC58 Black|DC58.black|Cronógrafo ETA 7750; aço com revestimento preto; 40 mm; luneta DAMEST.
DC 66|DC66|DC66|DC66|Cronógrafo Valjoux 7750 com luneta de mergulho 60 minutos; 43,8 mm.
DC 66 Black|DC66.black|DC66 Black|DC66.black|Cronógrafo; caixa preta; luneta de mergulho.
DC 66 Si|DC66.Si|DC66 Si|DC66.Si|Cronógrafo calibre 7750 Si; 43,8 mm; luneta de mergulho 0–60.
DC 66 Si Black|DC66.si.black|DC66 Si Black|DC66.si.black|Cronógrafo; caixa preta.
DC 67|DC67|DC67|DC67|Cronógrafo Valjoux 7750 com mostrador luminoso e luneta de mergulho.
DC 67 Si|DC67.si|DC67 Si|DC67.si|Cronógrafo calibre Damasko 7750 Si; 43,8 mm; luneta de 12 horas.
DC 67 Si Black|DC67.si.black|DC67 Si Black|DC67.si.black|Cronógrafo; caixa preta.
DC80 Bicolour|DC80.bicolour|DC80 Bicolour|DC80.bicolour|Cronógrafo C51-1; aço, 42 mm; luneta de 12 horas.
DC80 Green|DC80.green|DC80 Green|DC80.green|Cronógrafo; detalhes verdes.
DC80 Green Black|DC80.green.black|DC80 Green Black|DC80.green.black|Cronógrafo; caixa preta, detalhes verdes.
DC80 Green Orange|DC80.green.orange|DC80 Green Orange|DC80.green.orange|Cronógrafo; detalhes verdes e laranja.
DC80 Green Bicolour|DC80.green.bicolour|DC80 Green Bicolour|DC80.green.bicolour|Cronógrafo.
DC80 Yellow|DC80.yellow|DC80 Yellow|DC80.yellow|Cronógrafo; detalhes amarelos.
DC80 Yellow Black|DC80.yellow.black|DC80 Yellow Black|DC80.yellow.black|Cronógrafo; caixa preta, detalhes amarelos.
DC80 Yellow Bicolour|DC80.yellow.bicolour|DC80 Yellow Bicolour|DC80.yellow.bicolour|Cronógrafo.
DC82 Green|DC82.green|DC82 Green|DC82.green|Cronógrafo; detalhes verdes.
DK 105.blue|DK105.blue|DK105 Blue|DK105.blue|Linha Sporty Elegant; mostrador azul.
DK 105.anthracite|DK 105.anthracite|DK105 Anthracite|DK105.anthracite|Linha Sporty Elegant; calibre de manufatura H35-1; 42 mm; mostrador antracite.
DK 200|DK200|DK200|DK200|Linha Sporty Elegant.
DK 201|DK201|DK201|DK201|Linha Sporty Elegant.'''
with open('dados_majestix.txt','w') as f:
    for l in L.split('\n'):
        wn,ref,n,c,e=l.split('|')
        url='https://majestixcollection.com/wp-content/uploads/2023/06/'+base(wn,ref)+'.jpg'
        e=(e+' ' if e else '')+'Foto: Majestix Collection (base WatchBase).'
        f.write(f'{n}|{c}|{url}|{e}\n')
