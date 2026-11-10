import sys,re
R='https://b0650f7f058d5f70d743-97d5bb3f4194bc3eff7a94253e4a4e28.ssl.cf1.rackcdn.com/'
MAT=[('Stainless Steel','aço inoxidável'),('Rose Gold','ouro rosa'),('Red Gold','ouro vermelho'),('White Gold','ouro branco'),('Yellow Gold','ouro amarelo'),('Platinum','platina'),('Steel','aço inoxidável'),('Bicolor','bicolor (aço e ouro)')]
CORES={'Silver':'prateado','Black':'preto','Blue':'azul','Grey':'cinza','Gray':'cinza','White':'branco','Green':'verde','Brown':'marrom','Gold':'dourado','Rose':'rosa','Purple':'roxo','Red':'vermelho','Champagne':'champanhe','Salmon':'salmão'}
def tr(d):
    out=[]
    m=re.search(r'(\d+(?:[.,]\d+)?)\s*(?:x[\d.]+)?mm',d); 
    mat=next((p for k,p in MAT if k in d),None)
    s='Caixa de '+mat if mat else ''
    if m: s+=(' de ' if s else 'Caixa de ')+m.group(1).replace('.',',')+' mm'
    if 'Diamond Bezel' in d: s+=', luneta com diamantes'
    dm=re.search(r'([A-Za-z ]+?) (?:Skeleton |Guilloche |Galvanized |Cotes de Geneve |MOP |Ruthenium |Carbon )*Dial',d)
    if dm:
        w=dm.group(1).split()[-1]
        if w in CORES: s+=', mostrador '+CORES[w]
    if re.search(r'Skeleton Dial',d): s+=' esqueletizado'
    if 'MOP' in d: s+=' de madrepérola'
    if 'Bracelet' in d: s+=', bracelete de metal'
    elif 'Rubber' in d: s+=', pulseira de borracha'
    elif 'Fabric' in d: s+=', pulseira de tecido'
    elif re.search(r'Crocodile|Alligator|Leather|Calfskin',d): s+=', pulseira de couro'
    lm=re.search(r'Limited to (\d+)',d)
    if lm: s+=f', edição limitada de {lm.group(1)} peças'
    return (s+'.') if s else ''
src=sys.argv[1]; out=sys.argv[2]
with open(out,'w') as w:
    w.write(f'#SRC 1 {src}\n')
    for l in sys.stdin:
        if '|' not in l: continue
        ref,nome,desc,img=[x.strip() for x in l.split('|')]
        if not img.startswith('http'): img=R+img
        w.write(f'{nome} {ref} | {img} | {tr(desc)}\n')
