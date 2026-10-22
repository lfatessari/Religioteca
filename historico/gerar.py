import pickle,re
W='/home/claude/trabalho/'
G=pickle.load(open(W+'G.pkl','rb'))
HANDLE={'TN','ROSE','WATERMAN','ENDURANCE','DESCENT','WF-SS','WF-RG','DH-88-SS','DH-88-RG','CODEBREAKER-SS','CODEBREAKER-RG','VICTORY-SS','VICTORY-RG',
 'KINGSMAN-SS','KINGSMAN-RG','KINGSMAN-DLC','HRR-SE-MEMBER','HRR-SE-WINNER','HRR-SE-COMPETITOR','MW-II-FLYING-TIGER',
 'REGATTA-AC-35-RG','NORTON-V4RR','BB100','U-2-LE','1947-COLLECTION-NO1','1947-COLLECTION-NO3','HMAF-COLLECTORS','1918-RG',
 'SOLO-32-LC-WH','SOLO-32-AJ-BK','SOLO-32-AJ-WH','SOLO-32-LC-RG','SOLO-32-AJ-RG','MBII-BK','MB1','U22','U2','P-51','EP120','BROMPTON-CHEANEY',
 'ALT1-WT KINGSMAN','ALT1-WT-WH-KINGSMAN','ALT1-B-KINGSMAN','ALT1-C-TWG','S302','S2000','HAWKING-LADIES-SS','HAWKING-RG-R-S','LONGITUDE-RG-R','LONGITUDE-WG-R'}
PRI=['off','righttime','wf_cb','longit','le_misc','p2','p3','mono','t1916','fix','gear','wb','exq','']
def prio(src):
    for n,p in enumerate(PRI):
        if src.startswith(p): return n
    return len(PRI)
def imgscore(u):
    if not re.search(r'\.(jpg|jpeg|png|webp)',u,re.I): return 9
    if 'cdn.shopify.com/s/files/1/0024/5084/9907' in u or 'bremont.com/cdn' in u: return 0
    if 'righttime.com' in u: return 1
    if 'exquisitetimepieces' in u: return 2
    return 3
def clean(t,refs):
    t=re.sub(r'^Bremont\s+','',t)
    for r in sorted(refs,key=len,reverse=True):
        if r: t=re.sub(re.escape(r),'',t,flags=re.I)
    t=re.sub(r'\b(on|On)\s+(Leather |Rubber |NATO |Nato )?(Bracelet|Strap|strap)\b','',t)
    t=re.sub(r'\b(Leather|Rubber|NATO|Nato) Strap\b','',t)
    t=re.sub(r'\s{2,}',' ',t).strip(' -')
    return t
OV={'SOLO34LCWH':'Solo 34 LC White','WR45':'WR-45','BCS2':'BC Day Date Chronometer','P51':'P-51 – edição limitada','ROSE':'The Rose – edição especial, England Rugby (RFU)','AC2':"America's Cup 2",'AC1':"America's Cup 1",'DESCENT':'Supermarine Descent – edição especial','ALT1B':'ALT1-B','U22':'U-22','EP120':'EP120 – edição limitada de 120 peças (peças do Spitfire EP120)','ALT42MTGRTIGR':'Altitude MB Meteor Stealth Grey','TN40JHSSBK':'Terra Nova 40.5 Jumping Hour Black','SM43DTSSWH':'Supermarine 500M Polar White',
 'SM43DTBKCERWH':'Supermarine Full Ceramic Polar White','ALT42PERTIBL':'Altitude Perpetual Calendar GMT','SM43DTSSBK':'Supermarine 500M Black',
 'ALT42MTTIBKBK':'Altitude MB Meteor Black','ALT42CHRGSSBK':'Altitude Chronograph GMT Black','ALT42MTTISITI':'Altitude MB Meteor Silver',
 'ALT39DTSSBK':'Altitude 39 Date Black','ALT39DTSSSI':'Altitude 39 Date Silver','ALT42CHRGSSSI':'Altitude Chronograph GMT Silver',
 'TN40PWRBZBR':'Terra Nova 40.5 Power Reserve Bronze','TN40DTBZGN':'Terra Nova 40.5 Date Bronze Green','TN42CHRBZGN':'Terra Nova 42.5 Chronograph Bronze',
 'TN40DTSSBR':'Terra Nova 40.5 Date Caramel','SM40GMTSSBLBK':'Supermarine 300M GMT "Glacier" Blue','SM40GMTSSGNBK':'Supermarine 300M GMT "Tundra" Green',
 'SM43DTGNCERGN':'Supermarine Full Ceramic Jungle Green – edição limitada','SM43DTBKCERBK':'Supermarine Full Ceramic Tactical Black',
 'SM40DTSSBK':'Supermarine 300M Date Black','SM40DTBIBR':'Supermarine 300M Date Bi-Colour','SM40NDSSBL':'Supermarine 300M Blue',
 'SM40NDSSGN':'Supermarine 300M Green','TN38NDSSWH':'Terra Nova 38 White','TN38NDSSBK':'Terra Nova 38 Black','TN38NDSSPK':'Terra Nova 38 Pink – edição limitada',
 'MBIIWHBL':'Martin-Baker MBII White Blue','ALT1ZT51':'ALT1-ZT/51','SOLO37BKSI':'Solo 37 Black Silver','MBIIWH':'MBII White','SOLOPB':'Solo 43 Polished Black',
 'SOLO37SIRG':'Solo 37 Silver Rose Gold Numerals','SOLOWH':'Solo 43 White','SOLO37RG':'Solo 37 Rose Gold','ACRSS':"America's Cup Regatta",
 'SOLOWHSI':'Solo 43 White Silver','ALT1WTBL':'ALT1-WT World Timer Blue','ACRII':"America's Cup AC-R-II",'SOLO34AJWH':'Solo 34 AJ White',
 'MBIIBKOR':'Martin-Baker MBII Black Orange','SOLO34AJMP':'Solo 34 AJ Mother of Pearl','MBIIBKJET':'Martin-Baker MBII Jet',
 'BROMPTONCHEANEY':'Bremont x Brompton x Cheaney – edição limitada de 200 peças, colaboração Brompton × Cheaney',
 'BROADSWORDBZSO':'Broadsword Bronze Sotek','ALT1CCR':'ALT1-C Cream','ARROW':'Armed Forces Arrow','ALT1CGRIFFON':'ALT1-C Griffon',
 'S500BL2018':'Supermarine S500 Blue (2018)','BROADSWORDBZTO':'Broadsword Bronze Tobacco','ALT1CPB':'ALT1-C Polished Black','BROADSWORDBZSL':'Broadsword Bronze Slate',
 'ALT1P2BL':'ALT1-P2 Blue','SOLO43CR':'Solo 43 Cream','JMKIIWH':'Jaguar MKII White','ALT1CPW':'ALT1-C Polished White','AIRCOM2AN':'AIRCO Mach 2 Anthracite',
 'HAWKINGSS':'Hawking Steel – edição limitada de 388 peças','JMKIIBK':'Jaguar MKII Black','S2000YL':'Supermarine S2000 Yellow','SOLO43WS':'Solo 43 White Silver',
 'AIRCOM1BK':'AIRCO Mach 1 Black','MBIISSWHCOP11R':'Martin-Baker MBII White (configurador)','MBIISSBKCOP11P':'Martin-Baker MBII Black (configurador)',
 'S500BKGN':'Supermarine S500 Black Green','MB1':'MBI – só para pilotos ejetados com assento Martin-Baker','MBIIWHAN':'MBII White Anthracite','MBIIIAN':'MBIII Anthracite',
 'MBIIBKAN':'MBII Black Anthracite','MBIIBKGN':'MBII Black Green','MBIIWHGN':'MBII White Green','MBIIIBR':'MBIII Bronze','MBIIWHOR':'MBII White Orange',
 'MBIIIOR':'MBIII Orange','FURYBKSS':'H1 Generation Fury Black','TN38NDSSTQ':'Terra Nova 38 Turquoise','S501BK':'Supermarine S501 Black','S301BK':'Supermarine S301 Black',
 'S302GR':'Supermarine S302 Ocean GMT Grey – edição limitada','ARGONAUT':'Armed Forces Argonaut','BROADSWORD':'Armed Forces Broadsword','ENDURANCE':'Endurance – edição especial',
 'ARGONAUTBZSAR':'Argonaut Bronze Sargasso','ARGONAUTBZBK':'Argonaut Bronze Black','ARGONAUTBL':'Argonaut Azure','S502BK':'Supermarine S502 Black',
 'U251JET':'U-2/51-JET','WRBOX':'Williams Racing Box Set – edição limitada de 50 conjuntos','DTYPEBL':'Jaguar D-Type','WAPEXII':'Supermarine Waterman Apex II – edição limitada',
 'MAYAP':'Maya Pink','ALT1PBK':'ALT1-P Pilot Black','ALT1PBL':'ALT1-P Pilot Blue','S302':'Supermarine S302 Black','METEORTZ':'Altitude MB Meteor Time Zones Air Force Blue',
 'TN35FROSTED':'Terra Nova 35mm Jumping Hour Frosted – edição limitada de 150 peças','TN35PINK':'Terra Nova 35mm Jumping Hour Frosted Pink – edição limitada de 200 peças',
 'TN35JHSSBG':'Terra Nova 35mm Jumping Hour Burgundy','SN41CHRDLCHWK':'Supernova 41mm Chronograph Hawking Edition – edição limitada de 600 peças',
 'SN41CHRSSBK':'Supernova 41mm Chronograph','S2000BK':'Supermarine S2000 Black','1918SS':'1918 Steel – edição limitada de 275 peças, centenário da RAF',
 'WATERMAN':'Supermarine S500 Waterman – edição especial','DESCENTII':'Supermarine Descent II','HAWKINGRG':'Hawking Rose Gold – edição limitada de 88 peças',
 'ALT1C2CRSS':'ALT1-C Cream (2ª geração)','ALT1P2JET':'ALT1-P2 Jet','S302JET':'Supermarine S302 Jet','SMARINECHRONOBK':'Supermarine Chronograph Black',
 'SMARINECHRONOJET':'Supermarine Chronograph Jet','SMARINECHRONOBL':'Supermarine Chronograph Blue','MBIIKCLEBK':'MBII King Charles III – edição limitada',
 'MBIIBLORANGE':'Martin-Baker MBII Blue Orange','S502JETVINTAGE':'Supermarine S502 Jet','S502DLCBAMFORD':'Supermarine S502 Bamford Aurora – edição limitada, colaboração Bamford Watch Department',
 'MBSAVANNA':'MB Savanna','U2':'U-2 Black','ALT1WTKINGSMAN':'ALT1-WT Kingsman – edição especial, filme "Kingsman"','ALT1WTWHKINGSMAN':'ALT1-WT Kingsman White – edição especial, filme "Kingsman"',
 'ALT1BKINGSMAN':'ALT1-B Kingsman – edição especial, filme "Kingsman"','S301ALT1T2018':'Felix the Cat (2018) – edição limitada',
 'WR22SS':'Williams Racing WR-22','ALT1ZDG':'ALT1-Z Zulu Green','ETYPE60THGNSS':'Jaguar E-Type 60th Anniversary Green – edição limitada de 60 peças, 60º aniversário do E-Type',
 'LONGITUDESS':'Longitude Steel – edição limitada de 150 peças','H4HERCULESSS':'H-4 Hercules Steel – edição limitada de 300 peças (madeira original do "Spruce Goose")',
 'DAMBUSTER':'Dambuster – edição limitada de 232 peças','HMAFCOLLECTORS':'HMAF Commemorative Watch Box Set','IONBIRD':'ionBird – colaboração Rolls-Royce',
 'BROADSWORDRECON':'Broadsword Recon – edição limitada','ALT42MTTIBKOR':'Altitude MB Meteor Orange Black','ALT42MTTISIOR':'Altitude MB Meteor Orange Silver',
 'TN38JHDLCCC':'Terra Nova 38 Jumping Hour Stealth Black (DLC)','TN38JHSSCC':'Terra Nova 38 Jumping Hour','SOLO34AJBK':'Solo 34 AJ Black','SOLO37SI':'Solo 37 Silver',
 'ALT42CHRVTISM':'Altitude Chronograph Pulsograph Valjoux 23 – edição limitada de 40 peças','SOLO43ARGYLLE':'Argylle GMT – edição limitada, colaboração Argylle',
 'U2JETARGYLLE':'U-2 Argylle Jet – edição limitada, colaboração Argylle','BOB':'Battle of Britain Collection Boxed Set – edição limitada, 80º aniversário da Batalha da Inglaterra',
 'SUPERNOVAALN':'H1 Generation Supernova Albus','SUPERNOVAMNB':'H1 Generation Supernova Midnight','SUPERNOVAPIN':'H1 Generation Supernova Pitch','FURYBLSS':'H1 Generation Fury Blue',
}
out=[];stats={'link':0}
for k,v in G.items():
    v=sorted(v,key=lambda x:prio(x[3]))
    refs=[x[1] for x in v if x[1]]
    # display code
    code=''
    for r in refs:
        b=r
        for s in ['-L-S','-R-S','-N-S','-LS','-RS','-B','-BR','/BR','-S']:
            if b.endswith(s) and len(b)>len(s)+3 and b!='ALT1-B': b=b[:-len(s)]; break
        if r in HANDLE or b in HANDLE: continue
        code=b; break
    name=OV.get(k) or clean(v[0][0],refs)
    if not name or name.startswith('–'): name=re.sub(r'^Bremont\s+','',v[0][0])
    if k=='S302': code='S302-BK'
    imgs=sorted([x[2] for x in v if x[2]],key=imgscore)
    img=imgs[0] if imgs else ''
    e=[]
    if '1947 Collection' in name: e.append('Peça única. Mostrador pintado à mão por Ronnie Wood; caixa de ouro branco 18k de 42 mm; parte da 1947 Collection, série de 47 peças únicas')
    if 'militar restrita' in name: e.append('Venda restrita a membros da unidade')
    allrefs=sorted({x for x in refs if x and x!=code and x not in HANDLE})
    if allrefs: e.append('Outras referências/variantes de pulseira: '+', '.join(allrefs[:8]))
    hand=sorted({x for x in refs if x in HANDLE})
    if hand and not code: e.append('Código da página oficial/loja: '+', '.join(hand[:3]))
    if not img or imgscore(img)==9:
        stats['link']+=1
        e.append('Foto não encontrada; link da página/anúncio onde o modelo aparece')
    E='. '.join(e)
    if E and not E.endswith('.'): E+='.'
    name=name.replace('|','/'); E=E.replace('|','/')
    out.append(f"{name}|{code}|{img}|{E}")
# dedupe identical display names
seen={}
final=[]
for l in out:
    n,c=l.split('|')[:2]
    key=(n+' - '+c) if c else n
    if key in seen:
        p=l.split('|'); p[0]=p[0]+' (variante)'; l='|'.join(p)
    seen[key]=1; final.append(l)
open(W+'dados_Bremont.txt','w').write('\n'.join(final)+'\n')
print(len(final),'linhas; só link:',stats['link'])
