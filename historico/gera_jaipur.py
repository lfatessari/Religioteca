import re,collections
P='https://jaipur.watch/products/'
H=[l.rstrip('\n').split('|') for l in open('/home/claude/trabalho/jaipur_handles.txt')]
extra=[('stamp-watch-4','STAMP WATCH',40000),('blue-penny-stamp-watch','BLUE PENNY STAMP WATCH',130000),('iabk05','Imperial III Automatic Watch',45000),('iabk07','Imperial III Automatic Watch',45000),
('fil02','Filigree II Automatic Wristwear',45000),('fil03','FILIGREE III RED',30000),('fil04','FILIGREE III GREEN',30000),('the-royal-baagh-rbw03','THE ROYAL BAAGH',65000),('the-royal-baagh-rbw02','THE ROYAL BAAGH',65000),
('hc01','Indian Pegasus Watch',23000),('black-fire-opal-wristwear','Black Fire Opal Wristwear',60000),('nandi-art-pichwai-watch','Nandi Art - Pichwai Watch',30000),('copy-of-nandi-art-pichwai-watch','Nandi Art - Pichwai Watch',30000),
('holy-cow-pichwai-watch','Holy Cow - Pichwai Watch',22000),('lord-shiv-parivar-automatic-watch-silver','Lord Shiv Parivar Automatic Watch Silver',65000),('radha-in-the-moon-light-automatic-watch','Radha In The Moon Light Automatic Watch',65000)]
seen={h[0] for h in H}
for e in extra:
    if e[0] not in seen: H.append([e[0],e[1],str(e[2])])
IMG={'timeless-mirage-b02':'https://jaipur.watch/cdn/shop/files/TM_Front_Blue_2000X2000_a0a345de-29cc-402f-a6dd-6a43821ec426.png?v=1726043873',
'jumping-hour-watch-blue-46mm-copy':'https://jaipur.watch/cdn/shop/files/1_e35918f1-81fc-4e4e-8b90-925dbc0fbd3a.png?v=1790131643',
'black-fire-opal-wristwear-silver':'https://cdn.shopify.com/s/files/1/0565/0150/2134/files/3_2b2068c7-e0a2-4a38-89b1-bdd5a1e5707d.jpg?v=1773895503',
'the-one-7':'https://jaipur.watch/cdn/shop/files/24_b6d22349-e557-4135-822d-6ee461f88178.jpg?v=1752561805',
'the-one':'https://jaipur.watch/cdn/shop/files/29_1e8b49ff-e278-40b2-ae50-e11831ef1083.jpg?v=1752562351',
'hc08':'https://jaipur.watch/cdn/shop/files/6_1.png?v=1777633196','stamp-watch-4':'https://jaipur.watch/cdn/shop/files/B_MaroonGold.jpg?v=1790146757',
'stamp-watch-automatic':'https://jaipur.watch/cdn/shop/files/4_14581985-e384-47ee-90be-a11205c8bd22.png?v=1767425236',
'maharana-pratap-stamp-watch-automatic':'https://jaipur.watch/cdn/shop/files/Pratap.jpg?v=1790131992',
'blue-penny-stamp-watch':'https://jaipur.watch/cdn/shop/files/PennyBlue_GG.png?v=1728667817',
'imperial-iv-automatic-wristwear-ibe03':'https://jaipur.watch/cdn/shop/files/IBE03_1.jpg?v=1739426719',
'imperial-iv-automatic-wristwear-ibe01':'https://jaipur.watch/cdn/shop/files/IBE01_1.jpg?v=1739426351',
'imperial-iv-automatic-wristwear-ibe02':'https://jaipur.watch/cdn/shop/files/IBE02_1.jpg?v=1739426532',
'imperial-v-automatic-wristwear':'https://jaipur.watch/cdn/shop/files/38_f8aed172-e81c-467b-b962-600c91b93743.png?v=1789369921',
'iabk05':'https://jaipur.watch/cdn/shop/files/ImperialIII_dc1590a6-bac1-42f9-9d04-bc3775b5ce9a.jpg?v=1686905012',
'iabk07':'https://jaipur.watch/cdn/shop/products/GeorgeEmpireCoinChrome-PlainBackground.jpg?v=1673805495',
'imperial-i-2013-re-issue':'https://jaipur.watch/cdn/shop/files/ImperialI2013Re-Issue_4.jpg?v=1773216619',
'fil02':'https://jaipur.watch/cdn/shop/products/EkAanaGreenDial-PlainBackground.jpg?v=1673803686',
'hc01':'https://jaipur.watch/cdn/shop/products/187-550x550w.png?v=1790141170','hc07':'https://jaipur.watch/cdn/shop/files/07.png?v=1789361862',
'hc04':'https://jaipur.watch/cdn/shop/files/24_b7d0ef78-875c-4458-8606-27c895f378af.png?v=1789206237',
'bw15':'https://jaipur.watch/cdn/shop/files/2000X2000_0018_FRONTGOLDARABIC.jpg?v=1731673750',
'the-eternal-wristwear-hc12':'https://jaipur.watch/cdn/shop/files/31_ed738e63-c1cf-41a3-9a36-a452f704ef4f.png?v=1789205217',
'the-eternal-opal-wristwear':'https://jaipur.watch/cdn/shop/files/35_c14354d1-194d-4353-b99b-6b638c08ba12.png?v=1789205348',
'fil03':'https://jaipur.watch/cdn/shop/files/Filigree_Front_R_cdb23701-a06c-4c63-9b9a-8f0c13b4f2a5.png?v=1729512600',
'fil04':'https://jaipur.watch/cdn/shop/files/Filigree_Front_G_5f70ad86-f023-40be-9835-56e9094ad460.png?v=1729512572',
'lord-shiv-parivar-automatic-watch-silver':'https://jaipur.watch/cdn/shop/files/ShivParivar_SIlver_500X500_7d9f708d-5ca9-43b8-b891-4ec66d69e267.jpg?v=1790137674',
'krishna-automatic-watch':'https://jaipur.watch/cdn/shop/files/WhatsAppImage2023-08-14at11.26.44AM.jpg?v=1691992814',
'hans-damayanti-automatic-watch':'https://jaipur.watch/cdn/shop/files/HansDamayanti.jpg?v=1691212681',
'silver-engraved-watch-copy-1':'https://jaipur.watch/cdn/shop/files/Hand_Engraved_1.jpg?v=1756709886',
'filigree-iv-red':'https://jaipur.watch/cdn/shop/files/Filigree_IV_red.png?v=1758618250','filigree-iv-black':'https://jaipur.watch/cdn/shop/files/Filigree_IV_Black.png?v=1758618120',
'bw01':'https://jaipur.watch/cdn/shop/files/Untitled_design_6.jpg?v=1790135737','pocket-watch':'https://jaipur.watch/cdn/shop/products/POCKET-WATCH-1.png?v=1620750452',
'bw02':'https://www.ablogtowatch.com/wp-content/uploads/2025/01/Jaipur-Roman-Baag-india-rupee-dial-watch-5.jpg',
'the-majestic-elephant-ring-watch':'https://akm-img-a-in.tosshub.com/businesstoday/images/story/202510/68e8cc2ae4c9e-gaurav-mehtas-elephant-ring-watch-100437144-16x9.jpg',
}
SPEC={
'BAAGH':'Moeda indiana de 1947 com o tigre no mostrador (1 rupia no Baagh/Roman/Devanagari; meia rupia no Baagh III), caixa de 43 mm de aço 316L, Miyota 8215 automático, safira, 5 ATM.',
'BAAGH II':'The Baagh 2 (2024): moeda de 1/4 de rupia "Bagh" de 1947, caixa tonneau, mostrador de esmalte em mosaico, Miyota 6T28 automático; 50 peças por estilo e cor.',
'PREMIUM BAAGH':'Gaurav Mehta Signature Series (2026): tigre dourado sobre paisagem em pedra (turquesa, olho de tigre, aventurina ou abalone), khadi; 5 versões limitadas a 100 peças; versão de topo em aço 904L com Sellita SW200, as demais com Miyota.',
'IMPERIAL IV':'Moeda de meia rupia de prata de Jorge VI (1938–45), 42 mm, aço 316L, safira dos dois lados, Miyota 8215 automático; cores Eclipse Black, Royal Blue e Forest Green; numerado; ₹ 55.000 (2025).',
'GATES':'Gates of India: caixa giratória de dupla face (portal Lotus ou Leheriya de um lado, monumento do outro), dois movimentos de quartzo Seiko VX00 (dois fusos); 38,4 mm, aço 316L; ₹ 50.000.',
'KWW':'Kings Wristwear IV: moeda britânica da Índia no mostrador; ₹ 50.000.',
'EKAM':'Coleção Ekam (moeda), automático; ₹ 55.000.',
'ETERNAL':'Moeda One Pice (1950–55, cavalo a galope), 42 mm x 14 mm, aço 316L, safira, Seiko NH35A automático.',
'PICE':'The Pice Heritage (2025): moeda One Pice (1943–47 / 1950–55), mostrador martelado com numerais devanágari, 40 mm, aço, Miyota 2033 quartzo, alças móveis; ₹ 30.000.',
'RRV':'Coleção Raja Ravi Varma (2023, 10º aniversário da marca): pintura de Ravi Varma licenciada pelo Kilimanoor Palace Art Trust impressa sob o vidro, 40 mm, aço 316L, Miyota 9015 automático, coroa com safira; 112 peças no total; ₹ 65.000.',
'BRIDES':'Coleção feminina Brides of Jaipur (2024).',
'RING':'Relógio-anel; ₹ 15.000.',
}
def code(h):
    m=re.fullmatch(r'(bw\d+|ekam\d+|ring\d+|hc\d+|onepice\d+|fil\d+m?|iabk\d+)',h)
    if m: return h.upper()
    m=re.search(r'-(bw\d+|pbtur0\d|pbabel|pbaven|pbtig|kww\d+|ib[ek]\d+|ign\d+|goi[a-z]+\d?|rbw\d+|hc\d+|g\d\d|r\d\d|p\d\d|rg\d\d|b\d\d|ked\d+|stmpa\d+|fil\d+m?)$',h)
    if m: return m.group(1).upper()
    if h=='hc09-bmw': return 'HC09-BMW'
    if h=='black-fire-opal-wristwear-silver': return 'HC18'
    return ''
def title(t):
    t=t.replace(' / ',' | ')
    if t.isupper(): t=t.title().replace(' Iv',' IV').replace(' Iii',' III').replace(' Ii',' II').replace(' V ',' V ').replace(' Mop',' MOP').replace('Mg Select X Jwc','MG Select x JWC').replace(' Of ',' of ').replace(' In ',' in ')
    t=t.replace('|','–').replace(' Iv',' IV').replace(' Iii',' III').replace(' Ii ',' II ')
    if t.endswith(' Ii'): t=t[:-3]+' II'
    if t.endswith(' V'): pass
    return t
def spec(t):
    u=t.upper()
    if 'PREMIUM BAAGH' in u: return SPEC['PREMIUM BAAGH']
    if 'BAAGH II' in u and 'DIAMOND' not in u: return SPEC['BAAGH II']
    if 'BAAGH' in u and 'ROYAL' not in u and 'DIAMOND' not in u and 'ENGRAVED' not in u: return SPEC['BAAGH']
    if 'IMPERIAL IV' in u: return SPEC['IMPERIAL IV']
    if 'GATES OF INDIA' in u: return SPEC['GATES']
    if 'KINGS WRISTWEAR IV' in u: return SPEC['KWW']
    if u=='EKAM': return SPEC['EKAM']
    if 'ETERNAL' in u and 'DIAMOND' not in u: return SPEC['ETERNAL']
    if 'PICE HERITAGE' in u: return SPEC['PICE']
    if 'AUTOMATIC WATCH' in u and any(k in u for k in ['LORD','GODDESS','HANS','DAMAYANTI','RADHA','TARA','SHIVAJI','MOHINI','AVATAR','DHRUV']): return SPEC['RRV']
    if any(k in u for k in ['ENVIKA','BLOSSOM','GOLDEN EMBRACE','REGAL MAJESTY','TIMELESS MIRAGE']): return SPEC['BRIDES']
    if u=='RING WATCH': return SPEC['RING']
    return ''
EXTRA_E={'timeless-mirage-b02':'Relógio-pulseira, mostrador azul pintado à mão, Miyota 2025 quartzo.',
'jumping-hour-watch-blue-46mm-copy':'Hora saltante; caixa tonneau 41 x 30 mm de aço 316L, mostrador de pedra (malaquita, olho de tigre, aventurina ou lápis-lazúli) com guilloché, automático, safira, 5 ATM.',
'black-fire-opal-wristwear-silver':'Opala e aventurina com madrepérola negra, 42 mm, aço 316L, Seiko NH35A automático.',
'stamp-watch-4':'Selo real de Jorge VI do estado principesco de Nabha, 1½ anna, marrom; 34 x 30,2 mm, aço 316L, Ronda 1062 quartzo.',
'blue-penny-stamp-watch':'Selo Two Pence Blue (Grã-Bretanha, 1840–41), 34 x 30,2 mm, aço 316L, Ronda 1062 quartzo; ₹ 130.000.',
'maharana-pratap-stamp-watch-automatic':'Selo de 10 rupias de Maharana Pratap, 34 x 30,3 mm, aço 316L, Miyota 6T28 automático; ₹ 50.000.',
'iabk05':'Moeda de meia rupia de prata da Índia britânica (1939–45), 41 mm, Miyota 8215 automático; acabamento dourado.',
'iabk07':'Moeda de meia rupia de prata da Índia britânica (1939–45), 41 mm, Miyota 8215 automático; acabamento cromado.',
'imperial-i-2013-re-issue':'Reedição do primeiro Imperial (2013): moeda de 1 rupia de Jorge VI (1938–45), 37 mm, aço 316L, Miyota 8215 automático; ₹ 55.000. A loja tem 4 versões sem nome distinto.',
'fil02':'Moeda de 1 anna de Jorge VI (1938–47) em desenho de filigrana, mostrador verde, 41 mm, Miyota 8215 automático; 100 peças.',
'fil03':'Moeda de 1 anna (1938–40), 38 mm, aço 316L, Miyota 2033; ₹ 30.000 (2024).','fil04':'Moeda de 1 anna (1938–40), 38 mm, aço 316L, Miyota 2033; ₹ 30.000 (2024).',
'filigree-iv-red':'Moeda de 2 naya paisa (1957–63), 38 mm, aço 316L, Miyota 2026 quartzo; ₹ 30.000 (2025).','filigree-iv-black':'Moeda de 2 naya paisa (1957–63), 38 mm, aço 316L, Miyota 2026 quartzo; ₹ 30.000 (2025).',
'filigree-iv-green':'Moeda de 2 naya paisa (1957–63), 38 mm, Miyota quartzo; ₹ 30.000 (2025).',
'hc01':'Moeda de 1 paisa "Galloping Horse" (1950–55), mostrador de fibra de carbono com numerais hindi, 43 mm.',
'the-royal-baagh-rbw03':'One Piece Heritage Edition; mostrador floral, caixa de 42 mm, Miyota 8215 automático.',
'silver-engraved-watch-copy-1':'Mostrador gravado à mão (cada peça diferente), caixa Royal Baagh de 42 mm, Miyota 8215 automático; ₹ 100.000.',
'the-baagh-hand-engraved-watch':'Mostrador gravado à mão; ₹ 85.000.',
'nandi-art-pichwai-watch':'Mostrador pintado à mão no estilo pichwai (tema Nandi), 43 mm, aço, Miyota quartzo ou automático 9015; ₹ 30.000.',
'holy-cow-pichwai-watch':'Mostrador pintado à mão no estilo pichwai (tema Holy Cow), 43 mm, aço, coroa dourada, Miyota quartzo ou automático; ₹ 22.000.',
'pocket-watch':'Relógio de bolso: caixa de 50 mm banhada a ouro, mostrador esqueleto, Seagull de corda manual.',
'the-majestic-elephant-ring-watch':'Relógio-anel de ouro 18 k com esmalte verde e diamantes polki; a tampa em forma de elefante se abre sobre um mostrador de madrepérola (2025); ₹ 1.121.000.',
'onepice02':'Moeda One Pice; ₹ 23.000.','bw02':'Moeda de 1 rupia de 1947, 43 mm x 14 mm, aço polido, Miyota 8215 automático; o modelo usado pelo primeiro-ministro Narendra Modi.',
'pocket':'',}
GROUP={}  # titles sem código agrupados
lines=[];done=set()
for h,t,pr in H:
    c=code(h); t2=title(t)
    if t2.upper()=='THE PICE HERITAGE (HC07)': t2='The Pice Heritage'
    if h=='baagh-iv-steel': t2='Baagh IV Steel'
    if h=='baagh-iv-golden': t2='Baagh IV Gold'
    if c:
        key=(t2,c)
    else:
        key=(t2,'')
    GROUP.setdefault(key,[]).append(h)
out=[]
for (t2,c),hs in GROUP.items():
    h=hs[0]; img=next((IMG[x] for x in hs if x in IMG), P+h)
    e=EXTRA_E.get(h) or next((EXTRA_E[x] for x in hs if x in EXTRA_E),'') or spec(t2)
    if not e: e=''
    if len(hs)>1:
        e=(e+' ' if e else '')+f'A loja oficial tem {len(hs)} versões com este nome e sem código ou nome próprio publicado (moedas, selos ou cores diferentes): '+', '.join(P+x for x in hs[:6])+('…' if len(hs)>6 else '')+'.'
    if img.startswith(P): e=(e+' ' if e else '')+'Foto não alcançada: a coluna C traz o link da página do produto.'
    out.append((t2,c,img,e.replace('|','/')))
# extras sem handle (imprensa/gumroad)
out+= [('Kings Wristwear II','','https://www.latestly.com/agency-news/business-news-jaipur-watch-company-launches-a-new-coin-based-watch-kings-wristwear-ii-3224936.html','Moeda One Pice (1/64 de rupia, 1943–47, com furo no centro), 43 mm, Ronda 702 suíço com disco móvel; preto (ouro e prata) e salmão em 50 peças, verde Sacramento em 25 peças de cada; ₹ 40.000 (c. 2022). Foto não alcançada: a coluna C traz o link da matéria.'),
('Kings Wristwear III','','https://public-files.gumroad.com/16ta8rkcctalgoxoz91gnjen29ao','Moeda de 1 paisa com mecanismo de disco móvel, 42 mm, Miyota 2033; ₹ 35.000 (loja da marca no Gumroad, item KWW08).'),
('Imperial (1ª coleção)','','https://d12d6l12s3d372.cloudfront.net/Imperial_Watch_Collection_by_Jaipur_Watch_Company_1_e1423639675780_4470327f99.jpg','Primeira coleção da marca: moeda de Jorge VI usada dos dois lados, aço, automático, safira, coroa com safira; seis variações, feito sob encomenda (Man\'s World, 2015).'),
('Postage Stamp Watch – edição limitada de 10 peças','','https://businessworld.in/article/jaipur-watch-company-launches-unique-postage-stamp-watch-181027','Caixa de ouro de 32,5 x 27,5 mm e 4,6 mm de espessura, selo real de Jorge VI de 3 pies (1937–40) no mostrador, movimento suíço ultrafino, gravação de lótus; ₹ 1.40.000 (2020). Foto não alcançada: a coluna C traz o link da matéria.'),
]
import os
with open('/home/claude/trabalho/dados_Jaipur_Watch_Company.txt','w') as f:
    for t2,c,img,e in out: f.write(f'{t2}|{c}|{img}|{e}\n')
print(len(out), sum(1 for o in out if not o[2].startswith(P)))
names=collections.Counter((o[0],o[1]) for o in out); print([k for k,v in names.items() if v>1])
