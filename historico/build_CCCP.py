import re, glob, os
os.chdir('/home/claude/trabalho')
FAM = {'7001':'Sputnik 1','7002':'Sputnik 1','7003':'Yuri Gagarin','7004':'Kashalot','7005':'Kashalot','7006':'Kashalot','7007':'Kashalot','7008':'Kashalot','7009':'St. Petersburg','7010':'Shchuka','7011':'Shchuka','7012':'Shchuka','7013':'Aviator Yak-15','7014':'Aviator Yak-15','7015':'Golden Soviet Submarine','7017':'Delta','7018':'Typhoon','7019':'Heritage','7020':'Heritage','7021':'Heritage','7022':'Aurora','7024':'Chistopol','7025':'Monino','7026':'Sputnik-2','7027':'Kashalot','7028':'Sputnik-2','7029':'Golden Soviet Submarine','7030':'Shchuka','7031':'Shchuka','7032':'Golden Soviet Submarine','7033':'Shchuka','7035':'Aviator Yak-15','7036':'Heritage','7037':'Heritage','7038':'Balaklava','7039':'Kashalot','7040':'Badygin','7041':'Aurora','7042':'Aleksandrov','7043':'Black Sea','7044':'Friedmann','7045':'Arkhipov','7046':'Gorshkov','7047':'Arkhipov','7048':'Kamchatka','7049':'Shchuka','7050':'Gromov','7051':'Gorky','7052':'Gurevich','7053':'Russia Timezone','7054':'Spasskaya','7055':'Fadeyev','7056':'Vlasov','7057':'Gorshkov','7058':'Chakhava','7059':'MiG-21','7060':'Soyuz-Apollo','7063':'Mirny','7065':'Neujmin','7067':'Soyuz','7068':'Spetsnaz','7069':'Naval Kiev','7070':'Kirov','7071':'Gurevich','7072':'Typhoon','7073':'Naval Viktor','7074':'Mriya','7075':'Tolstoy','7077':'Kamzolkin','7079':'Chkalov','7080':'Tsiolkovsky','7081':'Alfa 200 Diver','7082':'Tupolev','7086':'Buran Tritium','7089':'Proton','7090':'Togliatti','7094':'Barrakuda','7095':'Kondor','7097':'Comrade','7098':'Sputnik','7099':'Leonov','7100':'Leonov','7101':'MiG-21','7104':'Lissitzky'}
LE = {'7069':' – edição limitada de 300 peças','7080':' – edição limitada de 300 peças'}
for k in ['7059','7060','7065','7067','7068','7071','7077','7086','7094','7099','7101','7003']: LE[k]=' – edição limitada'
LE_codes = {'CP-7001-02':' – edição limitada','CP-7001-04':' – edição limitada','CP-7002-02':' – edição limitada','CP-7002-03':' – edição limitada','CP-7095-33':' – edição limitada'}
TR = {'black':'preto','blue':'azul','green':'verde','red':'vermelho','white':'branco','grey':'cinza','gray':'cinza','silver':'prateado','gold':'dourado','brown':'marrom','steel':'aço','cream':'creme','beige':'bege','champagne':'champanhe','orange':'laranja','navy':'azul-marinho','sand':'areia','granite':'granito','rose':'rosé','ip-black':'IP preto','ip-gold':'IP dourado','smoky':'fumê','yellow':'amarelo','gunmetal':'grafite','tan':'caramelo','rosegold':'ouro rosé'}
def tr(s):
    out=[]
    for w in s.lower().split():
        out.append(TR.get(w,w))
    return ' '.join(out)

COR={'black':'preto','blue':'azul','green':'verde','red':'vermelho','white':'branco','grey':'cinza','silver':'prateado','gold':'dourado','brown':'marrom','cream':'creme','beige':'bege','biege':'bege','champagne':'champanhe','orange':'laranja','dark':'escuro','light':'claro','dual':'bicolor','tone':'','multi':'multicolorido','color':'','map':'com mapa','metallic':'metálico','gunmetal':'grafite','rose':'ouro rosé','tan':'caramelo','skeleton':'esqueleto','semi':'semi','mesh':'de malha','rubber':'de borracha','leather':'de couro','stainless':'de aço','steel':''}
def jt_desc(t):
    t=t.replace('semi skeleton','semi-esqueleto').replace('rose gold','rose')
    if ' dial ' not in t+' ': return ''
    d,p=(t+' ').split(' dial ',1)
    dw=[COR.get(w,w) for w in d.split()]
    pw=[COR.get(w,w) for w in p.replace('strap','').split()]
    mats=[w for w in pw if w.startswith('de ')]; cores=[w for w in pw if not w.startswith('de ') and w]
    dial='Mostrador '+' '.join(w for w in dw if w)
    pul='pulseira '+' '.join(mats+cores)
    return (dial+', '+pul).replace('  ',' ').strip()

rec = {}  # code -> dict
def add(code, src, color='', foto='', page='', e=''):
    code=code.upper()
    r=rec.setdefault(code,{'cor':'','foto':'','page':'','e':'','src':set()})
    r['src'].add(src)
    if color and not r['cor']: r['cor']=color
    if foto and not r['foto']: r['foto']=foto
    if page and not r['page']: r['page']=page
    if e and not r['e']: r['e']=e
# explicit photos/specs
for l in open('fotos_extra.txt'):
    c,u=l.strip().split('|',1); add(c,'foto',foto=u)
for l in open('parcial_CCCP_relogios.txt'):
    n,c,i,e=l.rstrip('\n').split('|')
    if not c: continue
    if len(c)==7: continue  # CP-7018 genérico
    isimg = re.search(r'\.(jpe?g|png|webp)',i,re.I)
    add(c,'manual',foto=i if isimg else '',page='' if isimg else i,e=e)
for f in ['aw_p1.txt','aw_p2.txt']:
    for l in open(f):
        n,c,i,e=l.rstrip('\n').split('|'); add(c,'allwatches',foto=i,e=e)
# jamtangan
jt=set()
for l in open('jt_titulos.txt'):
    m=re.search(r'cp(\d{4})(\w{2})\b',l)
    if not m: continue
    code=f'CP-{m.group(1)}-{m.group(2).upper()}'; jt.add(code)
    rest=l[m.end():].strip()
    rest=re.sub(r'^(automatic|chronograph|diver 1000m automatic)\s+(men|man)?\s*','',rest).replace('limited edition','').strip()
    rest=re.sub(r'^(men|man)\s+','',rest)
    add(code,'jamtangan',e='Mostrador/pulseira: '+rest)
for c in jt:
    add(c,'jt',foto=f'https://assets.jamtangan.com/images/product/cccp/{c}/1l_800x800.jpg')
# site
for f in glob.glob('site_*.txt'):
    for l in open(f):
        l=l.strip()
        if '|' not in l: continue
        left,h=l.rsplit('|',1)
        m=re.match(r'cp-(\d{4})-(\w{2})',h)
        if not m: continue
        code=f'CP-{m.group(1)}-{m.group(2).upper()}'
        color=''
        if ' / ' in left:
            fam=FAM.get(m.group(1),'').upper()
            cl=left
            for name in [fam,'GOLDEN SOVIET SUBMARINE','ALFA 200 DIVER','BURAN TRITIUM AUTOMATIC LIMITED EDITION','BARRAKUDA LIMITED EDITION','SOYUZ-APOLLO','RUSSIA TIMEZONE','AVIATOR YAK-15','SPUTNIK 1','SPUTNIK-2','BLACK SEA','TSIOLKOVKSKY','TOGLIATTI','KONDOR','CCCP']:
                if name and name in cl.upper():
                    cl=cl[:cl.upper().index(name)].strip(); break
            color=cl
        page = f'https://www.cccptime.com/products/{h}' if f!='site_watchescom.txt' else ''
        add(code,'site',color=color,page=page)
# ashford codes
for l in open('ash_codes.txt'):
    c=l.strip()
    if c: add(c,'ashford',page=f'https://www.ashford.com/products/cccp-{c.lower()}')
# p2 titles
for l in open('p2_titulos.txt'):
    n,c,s=l.rstrip('\n').split('|')
    if 'h2hub' in s:
        pg=f'https://www.h2hubwatches.com/collections/cccp'
    elif 'ashford' in s: pg=f'https://www.ashford.com/products/cccp-{c.lower()}'
    elif 'conteenium' in s: pg='https://conteenium.com/brand/cccp-watch/'
    elif 'watches.com' in s: pg='https://www.watches.com/collections/all/cccp'
    elif 'amazon.co.uk' in s: pg='https://www.amazon.co.uk/CCCP-CP-7022-22-Display-Japanese-Automatic/dp/B00LMZLYDO'
    elif 'amazon' in s: pg='https://www.amazon.com/CCCP-CP-7006-03-Kashalot-Black-Automatic/dp/B00OC344HQ'
    elif 'jomashop' in s: pg='https://www.jomashop.com/cccp-watch-cp-7005-03.html'
    elif 'camel' in s: pg='https://camelcamelcamel.com/CCCP-CP-7017-02-Display-Japanese-Automatic/product/B00FWM0QIC'
    elif 'ebay' in s and '7019' in c: pg='https://www.ebay.com/itm/256483185952'
    elif 'ebay' in s and '7082' in c: pg='https://www.ebay.com/p/7059212456'
    elif 'ebay' in s: pg='https://www.ebay.com/itm/364478231593'
    elif 'youtube' in s: pg='https://www.newfashionwatch.com/cccp/1448-cccp-heritage-analog-display-automatic-self-wind-cp-7019-01-unisex-s-watch.html'
    else: pg=''
    add(c,'p2',page=pg)
# extra codes from search titles in pass1/2
extra={'CP-7043-02':'https://www.amazon.com/CCCP-Black-Automatic-Silver-Blue/dp/B081RWWPC6','CP-7044-02':'https://www.ebay.com/p/20034396570','CP-7044-03':'https://www.ashford.com/products/cccp-cp-7044-03','CP-7046-33':'https://www.ebay.com/p/5042368243','CP-7059-04':'https://www.jomashop.com/cccp-mig-21-black-dial-mens-watch-cp-7059-04.html','CP-7059-01':'https://www.ashford.com/products/cccp-cp-7059-01','CP-7082-33':'https://www.ebay.com/p/7059212456','CP-7081-11':'https://www.jomashop.com/cccp-naval-alfa-200-diver-black-stainless-steel-black-dial-mens-watch-cp-7081-11.html','CP-7071-02':'https://www.timepiece.com/cccp-aviation-gurevich-black-dial-mens-watch-cp-7071-02.html','CP-7089-11':'https://www.mainspringboutique.com/products/cp-7089-11-proton','CP-7067-02':'https://www.mainspringboutique.com/products/cp-7067-02-soyuz','CP-7079-44':'https://mainspringboutique.com/products/cp-7079-44-chkalov','CP-7079-11':'https://mainspringboutique.com/products/cp-7079-11-chkalov','CP-7079-22':'https://www.mainspringboutique.com/products/cp-7079-22-chkalov','CP-7099-11':'https://www.mainspringboutique.com/products/cp-7099-11-leonov','CP-7072-01':'https://www.mainspringboutique.com/products/cp-7072-01-typhoon','CP-7072-04':'https://mainspringboutique.com/products/cp-7072-04-typhoon','CP-7071-03':'https://www.mainspringboutique.com/products/cp-7071-03-gurevich','CP-7014-01':'https://www.amazon.in/CCCP-CP-7014-01-Aviator-Stainless-Leather/dp/B00FWM180C','CP-7075-33':'https://www.mainspringboutique.com/products/cp-7075-33-tolstoy','CP-7029-03':'https://www.ebay.com/p/11037380438','CP-7068-11':'https://www.watches.com/products/cccp-spetsnaz-automatic-black-ss-cp-7068-11','CP-7065-11':'https://www.watches.com/collections/all/products/cccp-neujmin-automatic-black-ss-cp-7065-11','CP-7056-33':'https://www.watches.com/products/cccp-vlasov-automatic-black-cp-7056-33','CP-7056-22':'https://www.watches.com/products/cccp-vlasov-automatic-blue-cp-7056-22','CP-7077-66':'https://www.watches.com/products/cccp-heroes-kamzolkin-automatic-red-cp-7077-66','CP-7071-04':'https://watches.com/products/cccp-aviation-gurevich-automatic-blue-cp-7071-04','CP-7071-05':'https://www.watches.com/products/cccp-aviation-gurevich-automatic-green-cp-7071-05','CP-7101-02':'https://www.watches.com/products/cccp-mig-21-automatic-red-cp-7101-02','CP-7080-06':'https://www.watches.com/products/cccp-tsiolkovsky-automatic-black-cp-7080-06','CP-7021-11':'https://www.watches.com/collections/cccp-watches/products/black-steel-cp-7021-11-heritage','CP-7042-01':'https://www.watches.com/collections/cccp-watches/products/cccp-aleksandrov-automatic-silver-black-cp-7042-01','CP-7080-01':'https://www.watches.com/collections/cccp-watches/products/cccp-tsiolkovsky-automatic-silver-brown-cp-7080-01'}
for c,u in extra.items(): add(c,'busca',page=u)
# specs from fetched pages (by family, only for exact codes fetched -> already in manual e). family-level info for E when code page fetched:
CAL = {'CP-7010-02':'Quartzo suíço ISA 2330/103, caixa de 43,5 mm e 11 mm, 50 m','CP-7020-08':'Calibre Slava 2427 automático, caixa de aço com IP preto de 43 mm e 14,5 mm, pulseira de couro preta, 50 m','CP-7025-05':'Automático NH35 (TMI), caixa de 38 mm e 14 mm com IP dourado, mostrador vermelho, 100 m; a Ashford chama de Sputnik-2 e a H2Hub de Monino','CP-7055-04':'Calibre Slava H3265 automático, caixa de 40 mm, mostrador verde, 30 m','CP-7090-22':'Calibre Slava 2427N automático (40 h), caixa de aço de 43 mm, mostrador azul, pulseira de aço, 50 m','CP-7041-03':'Automático NH35 (TMI), caixa de aço de 46 mm e 14,5 mm, pulseira de couro verde, 100 m','CP-7036-03':'Linha Heritage Gospoda; calibre Slava 2427 automático, caixa de 43 mm e 14,5 mm, mostrador marrom, 50 m','CP-7035-05':'Calibre Slava 2427N automático, caixa de 44 mm, mostrador preto, 50 m','CP-7051-03':'Calibre Slava H335 automático, caixa de 42 mm, mostrador azul, 50 m','CP-7054-06':'Caixa retangular de aço de 39 mm, calibre Slava H3265 automático (40 h), mostrador verde, couro verde, 30 m','CP-7050-33':'Calibre Slava H335 automático, caixa de aço de 40 mm e 13 mm, mostrador cinza, pulseira de aço, 50 m','CP-7057-03':'Calibre Slava 2427N automático (40 h), caixa de aço de 43 mm, mostrador dourado, couro verde, 50 m','CP-7028-01':'Quartzo VD51 (TMI), caixa de aço de 43 mm e 15 mm, mostrador preto, couro preto, 50 m','CP-7005-05':'Linha Kashalot Submarine; quartzo Miyota OS21, caixa de aço de 47 mm e 17 mm, couro preto, 100 m','CP-7044-01':'Automático NH35 (TMI), caixa de 42 mm e 14 mm, couro preto, 50 m','CP-7043-04':'Automático com data, caixa de aço com IP preto de 42 mm e 14 mm, mostrador verde, 10 ATM','CP-7045-04':'Automático Seiko NH35, caixa de 42 mm, 50 m','CP-7048-22':'Calibre Slava automático com data, caixa de aço de 43 mm e 14 mm, mostrador preto, 10 ATM','CP-7101-02':'Calibre Slava automático com data, caixa de aço de 47,5 mm, mostrador vermelho, 5 ATM','CP-7024-01':'Automático, caixa prateada de 38 mm, couro preto, 50 m','CP-7058-04':'Caixa retangular de 42 mm e 15 mm, calibre Slava automático (40 h), mostrador branco e cinza, 30 m','CP-7058-02':'Caixa retangular de 42 mm e 15 mm, calibre Slava automático (40 h), mostrador azul e cinza, 30 m','CP-7019-03':'Calibre Slava automático (40 h), caixa de 43 mm e 14 mm, mostrador cinza, 50 m','CP-7104-04':'Caixa de aço de 43 mm e 13 mm, automático, fundo transparente, mostrador branco, couro preto, 100 m','CP-7029-02':'Cronógrafo de quartzo japonês com data, caixa de 43,5 mm e 12 mm, mostrador marrom, couro marrom, 5 ATM','CP-7069-11':'Mergulhador de 54 mm e 18 mm, calibre Slava automático, mostrador preto, pulseira de aço, 1000 m','CP-7026-0D':'Automático, caixa de 43 mm, mostrador esqueleto azul, couro marrom, 5 ATM','CP-7073-01':'Mergulhador de 54 mm e 18 mm, calibre Slava automático com data, mostrador azul, couro azul-escuro, 1000 m','CP-7074-44':'Caixa de 40 mm e 12 mm, calibre Slava automático, mostrador verde, pulseira de aço, 10 ATM','CP-7001-04':'Caixa de aço com IP dourado de 44 mm e 16 mm, calibre Slava 2437 de 27 rubis e dois tambores, 50 m'}
FOTO_ASH = {'CP-7010-02':'https://www.ashford.com/cdn/shop/files/CP-7010-02_F.jpg?v=1749740453','CP-7020-08':'https://www.ashford.com/cdn/shop/files/CP-7020-08_F.jpg?v=1749740452','CP-7025-05':'https://www.ashford.com/cdn/shop/files/CP-7025-05_F.jpg?v=1749740459','CP-7055-04':'https://www.ashford.com/cdn/shop/files/CP-7055-04_F.jpg?v=1749740465','CP-7090-22':'https://www.ashford.com/cdn/shop/files/CP-7090-22_F.jpg?v=1748471278','CP-7041-03':'https://www.ashford.com/cdn/shop/files/CP-7041-03_F.jpg?v=1749740463','CP-7036-03':'https://www.ashford.com/cdn/shop/files/CP-7036-03_F.jpg?v=1749740458','CP-7035-05':'https://www.ashford.com/cdn/shop/files/CP-7035-05_F.jpg?v=1749740462','CP-7051-03':'https://www.ashford.com/cdn/shop/files/CP-7051-03_F.jpg?v=1749740466','CP-7054-06':'https://www.ashford.com/cdn/shop/files/CP-7054-06_F.jpg?v=1749740468','CP-7050-33':'https://www.ashford.com/cdn/shop/files/CP-7050-33_F.jpg?v=1749740469','CP-7057-03':'https://www.ashford.com/cdn/shop/files/CP-7057-03_F_9a67523a-f2be-4e52-9b2b-b5d6ed09bce5.jpg?v=1792500205'}
lines=[]
for code in sorted(rec, key=lambda c:(c[3:7],c[8:])):
    r=rec[code]; fam=FAM.get(code[3:7])
    if not fam: print('SEM FAMILIA',code,r['src']); continue
    foto = FOTO_ASH.get(code) or r['foto']
    e_parts=[]
    if code in CAL: e_parts.append(CAL[code])
    elif r['e'] and not r['e'].startswith('Mostrador/pulseira'): e_parts.append(r['e'])
    if r['cor']: e_parts.append('Variante no site oficial: '+tr(r['cor'].replace('Rose Gold','rosegold')))
    elif r['e'].startswith('Mostrador/pulseira') and code not in CAL: e_parts.append(jt_desc(r['e'].replace('Mostrador/pulseira: ','')))
    if not foto and ('ashford' in r['src'] or r['page'].startswith('https://www.ashford.com/products/')):
        foto=f'https://www.ashford.com/cdn/shop/files/{code}_F.jpg'
        e_parts.append('Foto pelo padrão de imagens da Ashford (conferido em 12 fichas da loja)')
    if not foto:
        foto=r['page']; e_parts.append('Foto não encontrada; link da página do produto')
    if not foto: print('SEM C',code); continue
    e=' . '.join(p for p in e_parts if p).replace(' . ','. ')
    if e and not e.endswith('.'): e+='.'
    e=e[0].upper()+e[1:] if e else ''
    nome = fam + (LE_codes.get(code) or LE.get(code[3:7],''))
    lines.append(f'{nome}|{code}|{foto}|{e}'.replace('\n',' '))
# codeless extras
lines.append('Aurora 1917 (série Slava, 2012)||https://assets.catawiki.nl/assets/2026/7/23/a/b/f/abf16d06-7e21-4833-af65-3d80f93f9135.jpg|Automático; versão antiga anunciada como "CCCP 1917 Aurora Automatic" (visto em leilão da Catawiki).')
lines.append('Korolev – edição limitada de 140 peças||https://catawiki.com/de/l/88337083-cccp-korolev-limited-edition-1-140-space-race-automatic-slava-rare-ingen-mindstepris-maend-ny|Calibre Slava automático; visto só no título de um leilão da Catawiki (link da página).')
open('dados_CCCP.txt','w').write('\n'.join(lines)+'\n')
print(len(lines))
