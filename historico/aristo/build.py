import re, json, collections
def norm(r): return re.sub(r'[^A-Z0-9]','',r.upper())
KW=[(r'\bAutomatic\b|\bAutomatik\b|\bAuto\b','automático'),(r'Quarz','quartzo'),(r'Handaufzug','corda manual'),
(r'Chrono','cronógrafo'),(r'Titan','titânio'),(r'Carbon','carbono'),(r'brüniert|burnished','aço brunido'),(r'Gold PVD|PVD gold','PVD dourado'),
(r'schwarz PVD|PVD Black|\bPVD\b','PVD preto'),(r'Damen|Lady','feminino'),(r'Taucher','mergulho'),(r'Flieger|Pilot|Beobachter|\bBeo\b|Navigator|B-Uhr','relógio de piloto'),
(r'RECORD|Rec-','movimento Longines Record 1959-2 dos anos 1970 recondicionado'),(r'AS 2072','movimento AS 2072 (Adolf Schild) de 1970'),(r'Aristomatic Plus','automático Aristomatic Plus (SW200 com rotor de tungstênio)'),
(r'unbranded','sem logotipo no mostrador'),(r'Bauhaus','estilo Bauhaus'),(r'Dessau','linha Dessau'),(r'U-Boot','estilo U-Boot'),(r'Milit','estilo militar'),(r'RLM','estilo RLM'),
(r'Marine|Navy','estilo marinha'),(r'Halbspange','meia-pulseira (Halbspange)'),(r'Schmuckband','pulseira-joia'),(r'Lederband','pulseira de couro'),(r'Milanaise','malha milanesa'),
(r'Bicolor','bicolor'),(r'Day Date|DayDate','dia e data'),(r'GMT','segundo fuso (GMT)'),(r'Taschenuhr','relógio de bolso'),(r'dégradé','mostrador degradê'),(r'Leuchtorange|Orange','luminescência laranja'),
(r'Kleine','versão menor'),(r'Tacho','escala taquimétrica'),(r'Silberuhr','prata'),(r'Edelstahl','aço inoxidável'),(r'Big Crown|XL','coroa/caixa grande'),(r'Luminor|Lumi','mostrador luminescente'),
(r'California','mostrador California'),(r'Retro','estilo retrô'),(r'Messerschmitt|\bME[- ]?262','linha Messerschmitt da Aristo'),(r'Ärzte','relógio de médico'),(r'Harley','movimento Ronda Harley 2538 com microrrotor')]
def ecar(name):
    out=[]
    for pat,t in KW:
        if re.search(pat,name) and t not in out: out.append(t)
    m=re.search(r'\b(3[4-9]|4[0-9]|55)\b(?! ?[A-Z]\d)',name)
    s=[]
    if m and not re.search(r'\b(250|1069|262|108|109|163)\b.*'+m.group(1),name): s.append(f'caixa de {m.group(1)} mm')
    out=s+out
    if not out: return ''
    t='; '.join(out); return t[0].upper()+t[1:]+'.'
def clean(name,ref):
    n=re.sub(r'^(ARISTO|Aristo)\s+','',name)
    if ref: n=re.sub(r'\s*'+re.escape(ref)+r'\s*',' ',n,flags=re.I)
    n=re.sub(r'\s+',' ',n).strip(' -')
    return n or name
LE={'3H2836VL':'edição limitada de 50 peças','3H1561L':'edição limitada de 30 peças','7H165':'edição limitada de 50 peças',
'7H16':'Manufaktur-Edition, 500 peças no total','7H18':'Manufaktur-Edition, 500 peças no total','3H98175-L':'edição limitada de 50 peças','3H98175-M':'edição limitada de 50 peças'}
LEE={'4H2538-M':'Movimento Ronda Harley 2538 de estoque antigo (a série AWARD de 2003 teve 500 peças). ',
'7H166':'Série Record 1959-2 limitada a 50 peças por tipo de mostrador (página "Specials" do site). ','4H209':''}
EXCL={'VOLLMER99','VOLLMER99B','VOLLMER99G','ARISTOUHRENBOXCARBON'}
rows=[]; seen={}
def add(n,r,img,e,src):
    k=norm(r) if r else 'NOREF:'+n
    if k in EXCL: return
    if r in ('H3','ME108-24DR'): k=k+n
    if k in seen: return
    seen[k]=1; rows.append((n,r,img,e,src))
for l in open('raw_shop.txt'):
    n,r,u,i=l.rstrip('\n').split('|')
    i=re.sub(r'-\d+x\d+(\.\w+)$',r'\1',i)
    b=clean(n,r)
    if r in LE: b+=' – '+LE[r]
    add(b,r,i,LEE.get(r,'')+ecar(n),'shop')
ERB={'Erbprinz GOLDSTADT GS-3':('Erbprinz Goldstadt 250','GS-3','https://www.erbprinz-aristo.de/images/GS_3.jpg','Erbprinz (marca de luxo da Aristo Vollmer, vendida só na Alemanha). Aço polido com bisel banhado a ouro 18 quilates; mostrador guilhochado com algarismos arábicos e ponteiros Breguet pretos; 43,5 mm, 11,5 mm; safira; 5 ATM; automático Aristomatic SW200; fundo de vidro grande; malha milanesa polida; 895 euros.'),
'Erprinz B3':('Erbprinz Baden-Baden','B3','https://www.erbprinz-aristo.de/images/b3.jpg','Erbprinz (marca de luxo da Aristo Vollmer, vendida só na Alemanha). Automático Aristomatic SW200; 42 mm; 550 euros.'),
'Erprinz H1':('Erbprinz Heidelberg','H1','https://www.erbprinz-aristo.de/images/H1.jpg','Erbprinz (marca de luxo da Aristo Vollmer, vendida só na Alemanha). Automático Aristomatic SW200; caixa quadrada de aço; 650 euros.')}
for l in open('hidden_raw.txt'):
    n,r,u,i=l.rstrip('\n').split('|')
    if r in ERB:
        b,rr,img,e=ERB[r]; add(b,rr,img,e+' Fora do catálogo atual (página oculta na loja oficial).','hidden'); continue
    if r=='ME-46BLAU Retro Diver': r='ME-46BLAU'
    b=clean(n,r)
    if r in LE: b+=' – '+LE[r]
    e=LEE.get(r,'')+ecar(n)
    e=(e+' ' if e else '')+'Fora do catálogo atual (página oculta na loja oficial).'
    add(b,r,i,e,'hidden')
for l in open('extra.txt'):
    p=l.rstrip('\n').split('|')
    n,r,i,e,src=p[0],p[1],p[2],p[3],p[4]
    add(n,r,i,e,src)
with open('../dados_aristo.txt','w') as f:
    for n,r,i,e,s in rows:
        assert '|' not in n+r+i+e
        f.write(f'{n}|{r}|{i}|{e}\n')
c=collections.Counter(s for *_,s in rows); print(len(rows)); print(c)
# check duplicate B
B=collections.Counter((n+' - '+r) if r else n for n,r,*_ in rows); print([k for k,v in B.items() if v>1])
json.dump(dict(c),open('counts.json','w'))
