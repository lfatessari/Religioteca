import re
def lep(u):
    s=u.rsplit('/',1)[1][:-5]
    m=re.search(r'-w?(\d{6})ww(00)?$',s); ref='W'+m.group(1)+'WW00'
    s=re.sub(r'^\d+-hermes-','',s[:m.start()])
    t=s
    col=[('heureh','Heure H'),('heure-h','Heure H'),('h-hour','Heure H'),('hour-h','Heure H'),('cape-cod-chaine-d-ancre-joaillier','Cape Cod Chaîne d\'Ancre Joaillier'),('cape-cod','Cape Cod'),('arceau-petite-lune','Arceau Petite Lune'),('arceau-chronographe-titane','Arceau Chronographe Titane'),('arceau-78','Arceau 78'),('arceau','Arceau'),('nantucket','Nantucket'),('faubourg-polka','Faubourg Polka'),('faubourg','Faubourg'),('cut','Hermès Cut'),('slim-d-hermes','Slim d\'Hermès'),('dressage','Dressage'),('h08','H08')]
    name=next(v for k,v in col if t.startswith(k))
    for k,v in [('mini-model','TPM'),('tres-petit','TPM'),('small-model','PM'),('petit-model','PM'),('petit-modele','PM'),('medium-model','MM'),('moyen-model','MM'),('large-model','GM'),('grand-model','GM'),('grand-modele','GM'),('tres-grand','TGM')]:
        if k in t: name+=' '+v; break
    feats=[]
    W=t
    for k,v in [('automatic','automático'),('quartz','quartzo'),('pvd','PVD'),('titanium','titânio'),('titane','titânio'),('rose-gold','ouro rosa'),('yellow-gold','ouro amarelo'),('white-gold','ouro branco'),('diamond','diamantes'),('set','cravejado'),('mother-of-pearl','mostrador de madrepérola'),('malachite','mostrador de malaquita'),('aventurine','mostrador de aventurina'),('nephrite-jade','mostrador de jade nefrita'),('obsidian','mostrador de obsidiana'),('skeleton','mostrador esqueletizado'),('double-tour','pulseira de duas voltas'),('double-turn','pulseira de duas voltas'),('steel-bracelet','bracelete de aço'),('rubber','pulseira de borracha'),('croco','pulseira de crocodilo'),('fabric','pulseira de tecido')]:
        if k in W and v not in feats: feats.append(v)
    if 'set' in W and 'diamantes' in feats: feats.remove('cravejado')
    mm=re.search(r'(\d+(?:-x-\d+)?|395)-mm',t); tam=''
    if mm: tam=mm.group(1).replace('-x-',' x ').replace('395','39,5')+' mm'
    cor=re.search(r'(white|silver|black|blue|pink|gold|anthracite|rose-gold)(-lacquered|-matte|-opaline)?-dial',t)
    cs={'white':'branco','silver':'prateado','black':'preto','blue':'azul','pink':'rosa','gold':'dourado','anthracite':'antracite','rose-gold':'ouro rosa'}
    strap=re.search(r'(brown|black|blue|taupe|etaupe|etoupe|orange|red|green|pink|white|yellow|grey|purple|naples-yellow|gold-brown|swift-green|swift-etoupe|dark-brown|silver)(?:-croco|-crocodile|-calf)?-(?:leather|calfskin)',t)
    e="Visto na Lepage (link da página da loja). "+(("Caixa de "+tam+", ") if tam else "")+", ".join(feats)
    if cor: e+=", mostrador "+cs[cor.group(1)]
    if strap: e+=", pulseira de couro "+{'brown':'marrom','black':'preto','blue':'azul','taupe':'taupe','etaupe':'etoupe','etoupe':'etoupe','orange':'laranja','red':'vermelho','green':'verde','pink':'rosa','white':'branco','yellow':'amarelo','grey':'cinza','purple':'roxo','naples-yellow':'amarelo Nápoles','gold-brown':'marrom dourado','swift-green':'Swift verde','swift-etoupe':'Swift etoupe','dark-brown':'marrom-escuro','silver':'prateado'}[strap.group(1)]
    return name,ref,u,e.rstrip(', ')+'.'
