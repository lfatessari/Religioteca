import sys,re,glob,os
# raw files: REF|Name ; family slug from filename map
FAM={'wb_portugieser':'portugieser','wb_pilot':'pilot','wb_davinci':'da-vinci','wb_portofino':'portofino','wb_ingenieur':'ingenieur','wb_gst':'gst-aquatimer','wb_aquatimer':'aquatimer','wb_other':None}
MAT=[('Stainless Steel - Red Gold','aço e ouro vermelho'),('Stainless Steel / Rose Gold','aço e ouro rosa'),('Stainless Steel / Yellow Gold','aço e ouro amarelo'),('Stainless Steel Brushed','aço escovado'),('Stainless Steel','aço'),('Red Gold','ouro vermelho'),('Rose Gold','ouro rosa'),('White Gold','ouro branco'),('Yellow Gold','ouro amarelo'),('Armor Gold','Armor Gold'),('Platinum','platina'),('Ceratanium','Ceratanium'),('Titanium','titânio'),('Black Ceramic','cerâmica preta'),('White Ceramic','cerâmica branca'),('Ceramic','cerâmica'),('Bronze','bronze')]
COR={'Black':'preto','Silver':'prateado','White':'branco','Blue':'azul','Green':'verde','Grey':'cinza','Ardoise':'ardósia','Slate':'ardósia','Burgundy':'bordô','Brown':'marrom','Chocolate':'chocolate','Champagne':'champanhe','Salmon':'salmão','Dune':'areia (Dune)','Ice Blue':'azul-gelo','MOP':'madrepérola','Panda':'panda','Reverse Panda':'panda invertido','Silver - Blue':'prateado com detalhes azuis','Silver - Rose':'prateado com detalhes rosé','Silver - Gold Numerals':'prateado com números dourados','Silver - Blue Numerals':'prateado com números azuis','Black-Silver':'preto e prateado','Racing Green':'verde racing','Sunny Blue':'azul (Sunny Blue)','Peach Powder':'pêssego','Pink':'rosa','Black MOP':'madrepérola negra','Grey MOP':'madrepérola cinza','Blue MOP':'madrepérola azul','Pink MOP':'madrepérola rosa','Paved':'cravejado','Silver Embossed':'prateado gravado','Silver-Embossed':'prateado gravado','Black - Pilot':'preto (números de piloto)','Black - Breguet':'preto (números Breguet)','Silver - Breguet':'prateado (números Breguet)','White - Roman':'branco (romanos)','White - Railroad':'branco (minuteria ferroviária)','Black Breguet':'preto (Breguet)','Silver / Silver Numerals':'prateado'}
PUL={'Strap':'pulseira de couro','Bracelet':'bracelete de metal','Alligator':'pulseira de jacaré','Croco':'pulseira de crocodilo','Rubber':'pulseira de borracha','Calf':'pulseira de bezerro','Milanese':'bracelete milanês','Short Milanese':'bracelete milanês curto','Long Milanese':'bracelete milanês longo','Mesh':'bracelete milanês','Nappa':'pulseira de napa','Textile':'pulseira têxtil','NATO':'pulseira NATO','Leather':'pulseira de couro','Canvas':'pulseira de lona','Desmopan':'pulseira de Desmopan','Santoni':'pulseira Santoni','Feuille':'ponteiros folha','Diamond':'diamantes','Sector':'mostrador setorizado','Arabic':'números arábicos','Art Deco':'números art déco','Brown Croco':'crocodilo marrom','Black Croco':'crocodilo preto','Green Croco':'crocodilo verde','Blue Croco':'crocodilo azul','Red Croco':'crocodilo vermelho','Black Alligator':'jacaré preto','Brown Alligator':'jacaré marrom','Bordeaux Alligator':'jacaré bordô','Emerald':'esmeraldas','Ruby':'rubis','Sapphire':'safiras','Baguette':'diamantes baguete'}
LANG={'English':'inglês','German':'alemão','French':'francês','Italian':'italiano','Spanish':'espanhol'}
def parse(name):
    name=name.replace('’',"'").strip()
    mat=None
    for k,v in MAT:
        i=name.find(' '+k)
        if i<0: i=name.find('/ '+k)
        if i>=0:
            pre=name[:i].rstrip(' /'); post=name[i:].lstrip(' /')[len(k):]
            mat=v; break
    else:
        pre,post=(name.split(' / ',1)+[''])[:2] if ' / ' in name else (name,'')
    toks=[t.strip() for t in re.split(r' / ',post.strip(' /')) if t.strip()]
    e=[];extra=[]
    if mat: e.append('Caixa de '+mat)
    for t in toks:
        if t in COR: e.append('mostrador '+COR[t])
        elif t in PUL: e.append(PUL[t])
        elif t in LANG: e.append('mostrador em '+LANG[t])
        else: extra.append(t)
    b=pre + ((' – '+' / '.join(extra)) if extra else '')
    b=re.sub(r'\s+',' ',b).strip(' -/')
    return b, ('; '.join(e)+'.' if e else '')
def norm(r): return re.sub(r'[^A-Z0-9]','',r.upper().replace('O','0'))
OV={}
import os.path
if os.path.exists(sys.argv[1]+'/img_override.txt'):
    for l in open(sys.argv[1]+'/img_override.txt',encoding='utf-8'):
        if l.strip():
            p=l.rstrip('\n').split('|'); OV[norm(p[0])]=(p[1],p[2] if len(p)>2 else '')
out=[];seen=set()
for f in sorted(glob.glob(sys.argv[1]+'/wb_*.txt')):
    key=os.path.basename(f)[:-4]; fam=FAM.get(key)
    for l in open(f,encoding='utf-8'):
        l=l.strip()
        if not l: continue
        parts=l.split('|')
        ref,name=parts[0].strip(),parts[1].strip()
        img=parts[2].strip() if len(parts)>2 and parts[2].strip() else ''
        e_raw=parts[3].strip() if len(parts)>3 else None
        n=norm(ref)
        if n in seen: continue
        seen.add(n)
        b,e=parse(name)
        if e_raw is not None: b,e=name,e_raw
        if n in OV:
            img=OV[n][0]; e=(OV[n][1] or e).replace(' Foto: ver a ficha do WatchBase (link da página).','')
        elif img and 'wristler' in img and not e_raw:
            e='Visto só na lista de anúncios da Wristler (link da página).'
        if not img:
            slug=ref.lower().replace(' ','-')
            img=f'https://watchbase.com/iwc/{fam}/{slug}' if fam and re.fullmatch(r'iw\d{4}-\d{2}',slug) else f'https://watchbase.com/iwc/{fam}' if fam else ''
            e=(e+' ' if e else '')+'Foto: ver a ficha do WatchBase (link da página).'
        out.append(f'{b}|{ref}|{img}|{e}')
open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out))
