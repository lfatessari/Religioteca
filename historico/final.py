import re,collections
W='/home/claude/trabalho/'
L=[]
for f in ['raw_exq.txt','raw_all.txt']:
    for l in open(W+f):
        p=l.rstrip('\n').split('|')
        if len(p)<3: continue
        t,r,i=p[0].strip(),p[1].strip(),p[2].strip()
        t=re.sub(r'^Bremont\s+','',t)
        L.append([t,r.upper(),i,p[3] if len(p)>3 else ''])
STRAP=['-L-S','-R-S','-N-S','-LS','-RS','-B','-BR','/BR','-S']
def base(r):
    r=r.upper().replace(' ','-')
    if r in ('ALT1-B',): return r
    for s in STRAP:
        if r.endswith(s) and len(r)>len(s)+3: return r[:-len(s)]
    return r
def ck(r): return re.sub(r'[^A-Z0-9]','',base(r))
ALIAS={  # compact base -> canonical compact
 'MBIIBKORANGE':'MBIIBKOR','MBIIOR':'MBIIBKOR','MBIIWHBLUE':'MBIIWHBL','MBIIORWH':'MBIIWHOR',
 'MBIIGN':'MBIIBKGN','MBIIGRWH':'MBIIWHGN','MBIIAN':'MBIIBKAN','MBIIANWH':'MBIIWHAN',
 'MBIIIBKOR':'MBIIIOR','U2SS':'U2','U2BL':'U2BL','U2DLC':'U2DLC','U22':'U22','U251':'U251JET',
 'ALT1ZT':'ALT1ZTBK','ALT1PBL':'ALT1PBL','ALT1CPBK':'ALT1CPB','ALT1CPWH':'ALT1CPW',
 'ALTWHBLCHALGROVE':'ALT1WTBL','S2000':'S2000BK','S302BKNATO':'S302','S302BK':'S302',
 'W APEXIIHBR':'WAPEXII','WAPEXIIHBR':'WAPEXII','WAPEXIIBKR':'WAPEXII','WAPEXIIBRSHB':'WAPEXII',
 'WATERMANR':'WATERMAN','HMAFARGONAUTD':'ARGONAUT','HMAFARROWD':'ARROW','HMAFBROADSWORDD':'BROADSWORD',
 'SOLOCRBR':'SOLOCR','SOLOWHSI':'SOLOWHSI','SOLO37BKSI':'SOLO37BKSI','SOLO37SIRG':'SOLO37SIRG',
 'SOLO37S1RG':'SOLO37SIRG','SOLO37SIBR':'SOLO37SI','BB1SSWH':'1WH','BB1TIGMTBKBR':'BB1TIGMTBK',
 'ARGONAUTBZSAR':'ARGONAUTBZSAR','U2LE':'U2LE','HAWKINGRG':'HAWKINGRG','TN38NDSSTQ':'TN38NDSSTQ',
 'MBIISSBKCOP11P':'MBIISSBKCOP11P','S500BLBR':'S500BL','S500BRBLUE':'S500BL',
 'ALT1ZDG':'ALT1ZDG','ALT1WTWHKINGSMAN':'ALT1WTWHKINGSMAN',
}
NAMEMAP={ # name key -> canonical compact or DROP or NEW (keep as name group)
 'terranova38turquoise':'TN38NDSSTQ','u2argyllejet':'U2JETARGYLLE','u251jet':'U251JET',
 'williamsracingboxset':'WRBOX','williamsracingboxsetediolimitadade50conjuntos':'WRBOX',
 'alt1p2':'DROP','supermarines302bluegreen':'S302BLGN','argonaut':'ARGONAUT',
 'enduranceediolimitada':'ENDURANCE','broadsword':'BROADSWORD','supermarines301':'S301BK',
 'supermarines302oceanediolimitada':'S302GR','supermarines501black':'S501BK',
 'supermarinechronographblack':'SMARINECHRONOBK','supermarinechronojet':'SMARINECHRONOJET',
 'argonautbronzeblack':'ARGONAUTBZBK','argonautazure':'ARGONAUTBL',
 'bamfordauroraediolimitadacolaboraobamforddepartment':'S502DLCBAMFORD','altitudembmeteororangeblack':'ALT42MTTIBKOR',
 'altitudembmeteororangesilver':'ALT42MTTISIOR','supermarines300':'DROP','alt1p2jet':'ALT1P2JET',
 'supernovamidnight':'SUPERNOVAMNB','argonautbronzeblue':'ARGONAUTBZSAR','argonautbronzebluedial':'ARGONAUTBZSAR',
 'supermarinewatermanapexediolimitada':'WATERMANAPEX','furyblack':'FURYBKSS','furyblue':'FURYBLSS',
 'williamsracingwr22':'WR22SS','alt1cgriffon':'ALT1CGRIFFON','mbiii':'DROP','supernovapitch':'SUPERNOVAPIN',
 'broadswordbronzetobacco':'BROADSWORDBZTO','supermarines2000':'DROP','supermarinedescentiisteel':'DESCENTII',
 'mbsavanna':'MBSAVANNA','mbiisavanna':'MBSAVANNA','supermarinechronographblue':'SMARINECHRONOBL',
 'supernovaalbus':'SUPERNOVAALN','supermarines302jet':'S302JET','supermarines500watermanediolimitada':'WATERMAN',
 'alt1c':'DROP','mbii':'DROP','aircomach2':'DROP','solo43':'DROP','alt1zt':'ALT1ZTBK','u2':'U2',
 'supermarines500blue':'S500BL','boeingmodel247steel':'DROP','battleofbritaincollectionboxedsetediolimitada80aniversriodabatalhadainglaterra':'BOB',
 'supermarines302gmt':'DROP','longitude':'DROP','dambusterediolimitada':'DAMBUSTER','1918ediolimitada':'DROP',
 'h4herculesplatinumediolimitada':'H4PT','h4herculesplatinumediolimitadade75peasmadeiraoriginaldosprucegoose':'H4PT',
 'terranova35mmjumpinghourbluenightfrosted904l':'TN35FROSTED','terranova35mmjumpinghourfrosted':'TN35FROSTED',
 'terranova35mmjumpinghourfrostedediolimitadade150peas':'TN35FROSTED','terranova35mmjumpinghourfrostedpink':'TN35PINK',
 'terranova35mmjumpinghourfrostedpinkediolimitadade200peas':'TN35PINK','terranova35mmjumpinghourburgundy':'TN35JHSSBG',
 'supernova41mmchronographhawkingedition':'SN41CHRDLCHWK','supernova41mmchronographhawkingeditionediolimitadade600peas':'SN41CHRDLCHWK',
 'kingsmanchronographedioespecialfilmekingsman':'DROP','jaguardtype':'DTYPEBL','solo34ajmotherofpearl':'SOLO34AJMP',
 'supermarines302black':'S302','jaguaretype60thanniversaryboxsetdropeverythinggreenediolimitadade60peas60aniversriodoetype':'ETYPE60THGNSS',
 'mbiseparapilotosejetadoscomassentomartinbaker':'MB1','altitudembmeteortimezonesairforceblue':'METEORTZ',
 'ionbirdcolaboraorollsroyce':'IONBIRD','broadswordrecon':'BROADSWORDRECON','alt1wtblue':'ALT1WTBL',
 'supermarinedescentiititanium':'DESCENTIITI','supermarinedescentiibronze':'DESCENTIIBZ','broadswordjet':'BROADSWORDJET',
 'argonautbronzebluedia':'ARGONAUTBZSAR','solo34ajblack':'SOLO34AJBK','mbisparapilotosejetadoscomassentomartinbaker':'MB1','1918steelediolimitada':'1918SS','1918steelediolimitadade275peascentenriodaraf':'1918SS','alt1wtkingsman':'ALT1WTKINGSMAN',
}
def nkey(t):
    t=t.lower(); t=re.sub(r'\b(on|bracelet|strap|leather|rubber|nato|watch|pilot|the|dial)\b','',t)
    return re.sub(r'[^a-z0-9]','',t)
G=collections.OrderedDict()
for t,r,i,src in L:
    if r:
        k=ck(r); k=ALIAS.get(k,k)
    else:
        nk=nkey(t); k=NAMEMAP.get(nk,'N:'+nk)
    if k=='DROP': continue
    G.setdefault(k,[]).append((t,r,i,src))
import pickle; pickle.dump(G,open(W+'G.pkl','wb'))
print(len(G))
for k,v in G.items():
    if k.startswith('N:'): print(k, '|', v[0][0])
