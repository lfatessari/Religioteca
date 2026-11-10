# converte "ref | descrição WatchBase" -> linha raw "Nome ref | link | E"
import sys,re
MAT=[('Stainless Steel Bracelet','aço inoxidável'),('Stainless Steel','aço inoxidável'),('Red Gold','ouro vermelho'),('White Gold','ouro branco'),('Rose Gold','ouro rosa'),('Yellow Gold','ouro amarelo'),('Platinum','platina'),('Titanium','titânio'),('Ceramic','cerâmica'),('Steel','aço inoxidável'),('Bronze','bronze')]
COR={'Silver':'prateado','Black':'preto','Blue':'azul','Grey':'cinza','Gray':'cinza','White':'branco','Green':'verde','Salmon':'salmão','Brown':'marrom','Red':'vermelho','Skeleton':'esqueletizado','Black-Skeleton':'preto esqueletizado','Silver-Arabic':'prateado com algarismos arábicos','Frosted Silver':'prateado fosco (frosted)','Frosted Copper':'cobre fosco (frosted)','Rainbow':'arco-íris','Paved':'cravejado','China SKP':'edição SKP (China)','Diamond':'com diamantes','Champagne':'champanhe','Anthracite':'antracite','Purple':'roxo','Yellow':'amarelo','Orange':'laranja','Rhodium':'ródio','Pink':'rosa','Cold Enamel':'esmalte a frio','Cold Enamel Brown':'esmalte a frio marrom','MOP - Diamond':'madrepérola com diamantes','Silver Screen':'prateado ("panda")','MOP':'madrepérola','Tahiti MOP':'madrepérola do Taiti','Blue MOP':'madrepérola azul','Rose':'rosa','Guilloche Limited Edition':'guilloché (edição limitada)','Hand-Engraved':'gravado à mão','China':'edição China','Baguette':'com diamantes baguete','Year of the Dragon':'edição Ano do Dragão','Tribute to Dresden':'homenagem a Dresden'}
PUL={'Alilgator':'pulseira de couro de aligátor','Alligator':'pulseira de couro de aligátor','Calf':'pulseira de couro de bezerro','Rubber':'pulseira de borracha','Bracelet':'bracelete de metal','Synthetic':'pulseira sintética','Fabric':'pulseira de tecido','Satin':'pulseira de cetim','Nubuck':'pulseira de nobuck','Textile':'pulseira têxtil','Leather':'pulseira de couro','Louisiana Alligator':'pulseira de aligátor'}
FE={'Pin':'fivela simples','Short Folding':'fecho dobrável curto','Foldiong':'fecho dobrável','Folding':'fecho dobrável','pin':'fivela simples'}
def conv(ref,desc,link):
    d=desc.strip()
    idx=None
    for k,_ in MAT:
        i=d.find(' '+k)
        if i>0 and (idx is None or i<idx[0]): idx=(i,k)
    if not idx: return f'{d} {ref} | {link} | '
    nome=d[:idx[0]].strip(); rest=d[idx[0]:].strip()
    parts=[p.strip() for p in re.split(r'\s*/\s*|\s+-\s+',rest) if p.strip()]
    mat=dict(MAT).get(parts[0],parts[0]) if parts else ''
    ex=[]
    for p in parts[1:]:
        if p in COR: ex.append(('m',COR[p]))
        elif p in PUL: ex.append(('p',PUL[p]))
        elif p in FE: ex.append(('f',FE[p]))
        elif p.startswith('Black / Rubber') or p=='Black': ex.append(('m','preto'))
    t='Caixa de '+mat
    ms=[v for k,v in ex if k=='m']; ps=[v for k,v in ex if k=='p']; fs=[v for k,v in ex if k=='f']
    if ms: t+=', mostrador '+' '.join(ms)
    if ps: t+=', '+ps[0]
    if fs: t+=', '+fs[0]
    return f'{nome} {ref} | {link} | {t}. Visto só na lista do WatchBase (link da página da família).'
src,link,out=sys.argv[1:4]
with open(out,'w') as w:
    w.write(f'#SRC 1 {src}\n')
    for l in open('/dev/stdin'):
        if '|' not in l: continue
        r,d=l.split('|',1); w.write(conv(r.strip(),d.strip(),link)+'\n')
