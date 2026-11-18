# code: (titulo, url, img)
D = {}
def a(code, title, url, img=''):
    code=code.upper()
    if code in D:
        t,u,i = D[code]
        if img and not i: D[code]=(t,u,img)
        return
    D[code]=(title,url,img)
R='https://reach.dog/shop/gotham-watch/products/'
for code,slug,t in [
('GWC14103S','gotham-mens-silver-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14103s',"Stainless Steel Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14102G','gotham-mens-gold-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14102g',"Gold-Plated Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14102SB','gotham-mens-silver-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14102sb',"Silver-Tone Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14100G','gotham-mens-gold-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14100g',"Gold-Plated Mechanical Hand Wind Railroad Pocket Watch"),
('GWC18806G','gotham-mens-gold-tone-railroad-style-double-hunter-17-jewel-mechanical-pocket-watch-gwc18806g',"Gold-Tone Railroad Style Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18806S','gotham-mens-silver-tone-railroad-dial-double-hunter-17-jewel-mechanical-pocket-watch-gwc18806s',"Silver-Tone Railroad Dial Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC14103G','gotham-mens-gold-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14103g',"Gold-Plated Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14104BBK','gotham-mens-gun-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14104bbk',"Gun-Tone Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14104B','gotham-mens-gunmetal-mechanical-hand-wind-railroad-pocket-watch-gwc14104b',"Gunmetal Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14100S','gotham-mens-silver-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14100s',"Stainless Steel Mechanical Hand Wind Railroad Pocket Watch"),
('GWC18806SB','gotham-mens-silver-tone-railroad-dial-double-hunter-17-jewel-mechanical-pocket-watch-gwc18806sb',"Silver-Tone Railroad Dial Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18806B','gotham-mens-gun-tone-railroad-dial-double-hunter-17-jewel-mechanical-pocket-watch-gwc18806b',"Gun-Tone Railroad Dial Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC14111G','gotham-mens-gold-plated-stainless-steel-mechanical-hand-wind-railroad-pocket-watch-gwc14111g',"Gold Plated Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14108G','gotham-mens-gold-plated-stainless-steel-mechanical-hand-wind-railroad-style-pocket-watch-gwc14108g',"Gold-Plated Mechanical Hand Wind Railroad Style Pocket Watch"),
('GWC14124S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14124s',"Railway Classic Nostalgia Series Mechanical Pocket Watch"),
('GWC14111S','gotham-mens-stainless-steel-mechanical-hand-wind-railroad-pocket-watch-gwc14111s',"Stainless Steel Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14115G','gotham-mens-gold-plated-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14115g',"Railway Classic Nostalgia Series Gold Plated Mechanical Pocket Watch"),
('GWC14106S','gotham-mens-stainless-steel-mechanical-hand-wind-railroad-style-pocket-watch-gwc14106s',"Stainless Steel Mechanical Hand Wind Railroad Style Pocket Watch"),
('GWC14108S','gotham-mens-stainless-steel-mechanical-hand-wind-railroad-style-pocket-watch-gwc14108s',"Stainless Steel Mechanical Hand Wind Railroad Style Pocket Watch"),
('GWC14113S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14113s',"Railway Classic Nostalgia Series Mechanical Pocket Watch"),
('GWC14107S','gotham-mens-stainless-steel-analog-quartz-date-railroad-style-pocket-watch-gwc14107s-2',"Stainless Steel Analog Quartz Date Railroad Style Pocket Watch"),
('GWC14107SB','gotham-mens-stainless-steel-analog-quartz-date-railroad-style-pocket-watch-gwc14107sb',"Stainless Steel Analog Quartz Date Railroad Style Pocket Watch"),
('GWC14109SB','gotham-mens-stainless-steel-analog-quartz-date-luminous-pocket-watch-gwc14109sb',"Sport Series Stainless Steel Analog Quartz Date Pocket Watch"),
('GWC14125S','gotham-mens-stainless-steel-classic-series-brushed-covered-quartz-pocket-watch-gwc14125s',"Classic Series Brushed Covered Quartz Pocket Watch"),
('GWC14125SBU','gotham-mens-stainless-steel-classic-series-brushed-covered-quartz-pocket-watch-gwc14125sbu',"Classic Series Brushed Covered Quartz Pocket Watch"),
('GWC14109SG','gotham-mens-sport-series-stainless-steel-analog-quartz-date-pocket-watch-gwc14109sg',"Sport Series Stainless Steel Analog Quartz Date Pocket Watch"),
('GWC14123S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14123s',"Railway Classic Nostalgia Series Mechanical Pocket Watch"),
('GWC14140SR','gotham-womens-silver-tone-open-face-pendant-watch-with-chain-gwc14140sr',"Women's Silver-Tone Open Face Pendant Watch with Chain"),
('GWC14139GR','gotham-womens-gold-tone-open-face-pendant-watch-with-chain-gwc14139gr',"Women's Gold-Tone Open Face Pendant Watch with Chain"),
('GWC14138SR','gotham-womens-silver-tone-open-face-pendant-watch-with-chain-gwc14138sr',"Women's Silver-Tone Open Face Pendant Watch with Chain"),
('GWC18809SBU','gotham-mens-classic-silver-tone-polished-case-double-hunter-17-jewel-mechanical-pocket-watch-gwc18809sbu',"Classic Silver-Tone Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18804G','gotham-mens-gold-tone-double-cover-exhibition-mechanical-pocket-watch-gwc18804g',"Gold-Tone Double Cover Exhibition Mechanical Pocket Watch"),
('GWC18807G','gotham-mens-classic-gold-tone-polished-case-double-hunter-17-jewel-mechanical-pocket-watch-gwc18807g',"Classic Gold-Tone Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18808G','gotham-mens-classic-gold-plated-polished-case-double-hunter-17-jewel-mechanical-pocket-watch-gwc18808g',"Classic Gold Plated Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18807S','gotham-mens-classic-silver-tone-polished-case-double-hunter-17-jewel-mechanical-pocket-watch-gwc18807s',"Classic Silver-Tone Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18808S','gotham-mens-classic-silver-tone-polished-case-double-hunter-17-jewel-mechanical-pocket-watch-gwc18808s',"Classic Silver-Tone Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch"),
('GWC18810S','gotham-mens-classic-silver-tone-polished-case-double-hunter-17-jewel-mechanical-pocket-watch-gwc18810s',"Classic Silver-Tone Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch"),
]: a(code,t,R+slug)
W='https://i5.walmartimages.com/seo/'
a('GWC14112SBU',"Classic Series Stainless Steel Open Face 17 Jewel Mechanical Hand Wind Pocket Watch",'https://www.walmart.com/ip/5120579773', W+'Gotham-Classic-Series-Stainless-Steel-Open-Face-17-Jewel-Mechanical-Hand-Wind-Pocket-Watch-GWC14112SBU_47f7235a-fbfe-47f2-90dc-2ae525659088.4cf1b651038d279b22f1d7be9c0c7066.jpeg')
a('GWC14138GR',"Women's Gold-Tone Open Face Pendant Watch with Chain",'https://www.walmart.com/ip/16019166218',W+'Gotham-Women-s-Gold-Tone-Open-Face-Pendant-Watch-with-Chain-GWC14138GR_809941c5-84fc-4b89-81b1-6b88d23759ff.c79514f053f0c99c839947609ce8f9e3.jpeg')
a('GWC18807BBK',"Classic Gunmetal Plated Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch",'https://www.walmart.com/ip/16053504756',W+'Gotham-Men-s-Classic-Gunmetal-Plated-Polished-Case-Double-Hunter-17-Jewel-Mechanical-Pocket-Watch-GWC18807BBK_c0b15796-bd25-4c8b-85ae-fb11ec8db2d0.e6bd6f6cbb0d174740c0f2240a35612e.jpeg')
a('GWC14135SA',"Women's Silver-Tone Open Face Pendant Watch with Chain",'https://www.walmart.com/ip/19269555124',W+'Gotham-Women-s-Silver-Tone-Open-Face-Pendant-Watch-With-Chain-GWC14135SA_1ed96700-9c88-4854-99f7-2bd1ef642080.3719e07927bdf3f2f9d6c3906937c931.jpeg')
a('GWC14109S',"Sport Series Stainless Steel Analog Quartz Date Pocket Watch",'https://www.walmart.com/ip/15943570448',W+'Gotham-Men-s-Sport-Series-Stainless-Steel-Analog-Quartz-Date-Pocket-Watch-GWC14109S_592517f9-975b-48b5-8eb8-8186f0988881.d1e82dbe68bc9e7f6856a025e79f9693.jpeg')
WI='https://i5.walmartimages.com/asr/'
WP='https://www.walmart.com/ip/'
for code,t,ip,img in [
('GWC14125SBU',"Stainless Steel Analog Quartz Date Covered Pocket Watch",'16047911891',''),
('GWC14036BBK',"Classic 17 Jewel Half Hunter Mechanical Pocket Watch",'16224767426','59906d4a-fa03-42e4-9f07-030bed3075fd.e9c631c174f8004cfc82d58036cd43ef.jpeg'),
('GWC14109SB',"Sport Series Stainless Steel Analog Quartz Date Pocket Watch",'699432048','371025d9-aec1-48e6-b6a9-0d828163f1ff_1.fb5a42817bab2542e22e98e12740a658.jpeg'),
('GWC15044B',"Gun-Tone Railroad Polished Finish Covered Quartz Pocket Watch",'5930766323','93f0f8d5-0d69-45a2-8533-17849b2ba436.9b108c59dfeee436ab5bad89b5b999e4.jpeg'),
('GWC15044BBK',"Gun Metal Railroad Polished Finish Covered Quartz Pocket Watch",'5099894226','bf93d5b6-560a-4394-8ee5-9537889d9aa3.e48aebea244e555a012cd6ef5c781bb8.jpeg'),
('GWC14109BO',"Sport Series Gunmetal Stainless Steel Analog Quartz Date Pocket Watch",'16046708004','759939eb-6809-455d-863d-48ed0cc4ce91.f8c2507a2a222974590af7dda1d4ac21.jpeg'),
('GWC14135SR',"Women's Silver-Tone Open Face Pendant Watch with Chain",'19278356262','b0f53e67-465f-4028-b970-9e4669a13cd2.4d6413d5a0657bc8308a5e4ca17562d6.jpeg'),
('GWC14135SBA',"Women's Silver-Tone Open Face Pendant Watch with Chain",'19258608316','f977608c-6b07-4306-96fc-d7c1494d04ab.705e40e3fb588dffeeda4bd2de983e24.jpeg'),
('GWC15029B',"Gunmetal Thin Railroad Dial 24 Hour Open Face Quartz Pocket Watch",'15965214955','b4b3e6e1-524c-47e9-9089-7d8776fac981.bfe4abdffb8a19c418f0c6424a473494.jpeg'),
('GWC14135GA',"Women's Gold-Tone Open Face Pendant Watch with Chain",'19289910276','6753a022-9a6f-472c-af01-f91faa66b696.1ef587e86caa3d08e734599d93f84856.jpeg'),
('GWC15042S',"Silver-Tone Polished Finish Covered Quartz Pocket Watch with Chain",'171972502','16bdeff4-01aa-4d4f-8c03-0123165afea6.ad8ea175c364aa6db34f6a7db68af15d.jpeg'),
('GWC15044BR',"Gunmetal Railroad Polished Finish Hunter Quartz Pocket Watch",'5128904008','7714f82d-ae49-41e4-b194-44e76a1d0390.feb7e1a1040aa710406f837f44a834c2.jpeg'),
('GWC15029SBK',"Silver-Tone Slim Railroad 24 Hour Open Face Quartz Pocket Watch",'16228357876','b830df50-8dd3-447c-b749-706a5eb36818.ee4db6ed0c5690061249c0a29275959c.jpeg'),
]: a(code,t,WP+ip, WI+img if img else '')
a('GWC15026G',"Railroad Open Face Gold-Tone Analog Quartz Pocket Watch with Chain",WP+'106127156','https://i5.walmartimages.com/seo/Men-s-Railroad-Open-Face-Gold-Tone-Analog-Quartz-Pocket-Watch-with-Chain-GWC15026G_710efc42-a3ce-4416-b725-2c049832c3de.d6e89f0961c25702f085ef269a469b60.jpeg')
CAR={'GWC15026G':'Caixa de 44 mm banhada a ouro (latão), quartzo japonês, mostrador branco estilo ferroviário com marcação de 24 horas em vermelho; vem com corrente.',
     'GWC14104BBK':'Caixa de latão com banho cor grafite, 51 mm × 11,7 mm; movimento mecânico de corda manual com 17 rubis e pequenos segundos; mostrador preto estilo ferroviário com algarismos arábicos; vidro mineral.'}
for code,t,ip,img in [
('GWC14106BBK',"Gun-Plated Mechanical Hand Wind Railroad Style Pocket Watch",'15923464112','https://i5.walmartimages.com/seo/Gotham-Men-s-Stainless-Steel-Gun-Plated-Mechanical-Hand-Wind-Railroad-Style-Pocket-Watch-GWC14106BBK_29a4f74c-6cd1-4275-99f4-4bfc984d1bfa.fc8da7e194756d57be1acac1d56546cf.jpeg'),
('GWC14125G',"Classic Gold-Plated Analog Quartz Date Covered Pocket Watch",'16051502685',WI+'5bd088c6-d76a-400e-a9b1-4e2d75424dcf.45e7109a4854b0e27f620858d2132d89.jpeg'),
('GWC14110BBKX',"Railway Classic Gunmetal Analog Quartz Day/Date Hunter Pocket Watch",'15962665285',WI+'88827217-42de-4039-9f67-8c245aec7920.cecad537c5d011d3d4309eaa525dfa54.jpeg'),
('GWC14106S',"Stainless Steel Mechanical Hand Wind Railroad Style Pocket Watch",'15865650752',WI+'90ffd597-ec9e-4740-bbd0-a255f5abef88.46f53f2d4ae857b6f1bdf4812eaa4323.jpeg'),
('GWC14110S',"Railway Classic Stainless Steel Analog Quartz Day/Date Hunter Pocket Watch",'374275246',WI+'f68f9189-e37b-4f70-9687-5739631334e3.86d0125878293df6ac2132758385c211.jpeg'),
('GWC14125S',"Classic Series Brushed Covered Quartz Pocket Watch",'16046720798',WI+'7444ecdf-c4d3-41cf-918e-3aa4d7d0f8d0.39c1cd34bbc956b716f43bcee18c7121.jpeg'),
('GWC14106SB',"Stainless Steel Mechanical Hand Wind Railroad Style Pocket Watch",'15898922119',WI+'15c54ee1-a9e4-4a11-93d7-50f0e492e1cf.a73014e9e4fd46a521162240a0fc77db.jpeg'),
('GWC14107S',"Stainless Steel Analog Quartz Date Railroad Style Pocket Watch",'429786789',WI+'870a6a8b-fa90-4637-b1aa-80643a4f0eba_1.99be133239def377e92cf2b4d5029783.jpeg'),
('GWC14125SBU',"",'16047911891',WI+'cf3bfba9-9145-4981-be2f-f56139dba2e9.a3c8187a50e69cd611c3138a18e06a38.jpeg'),
('GWC14110BY',"Railway Classic Gunmetal Analog Quartz Day/Date Hunter Pocket Watch",'759940754',WI+'1c795020-c840-4c5e-addd-1a0896f6ee2f.b792ca92fbffd825a5d8dc1d49ee2922.jpeg'),
('GWC14040BBK',"Gunmetal 17 Jewel Mechanical Double Half Hunter Pocket Watch",'15881017987',WI+'6d58cbca-e090-4f02-ae18-9b776b5f2006.26f7b0cb5d7f59b8c0d3828c93e5654f.jpeg'),
('GWC15044BG',"Gunmetal Railroad Polished Finish Covered Quartz Pocket Watch",'5099876623',WI+'85be6743-1c00-4bb5-83dd-f7ded0060cad.0a4a9e3110b1d7c5f521da8d52fbc4df.jpeg'),
('GWC14109BBK',"Sport Series Gun-Plated Stainless Steel Analog Quartz Date Pocket Watch",'757146437','https://i5.walmartimages.com/seo/Gotham-Men-s-Sport-Series-Gun-Plated-Stainless-Steel-Analog-Quartz-Date-Pocket-Watch-GWC14109BBK_5edaa563-cc5e-4b86-abb1-d518b80fe371.9f7f7a0e169390f0c6fc1aa12781f029.jpeg'),
('GWC14101S',"Stainless Steel Analog Quartz Date Railroad Design Pocket Watch",'891846897',WI+'8ea7846d-4e75-4ec5-8bac-d8f5ac0dafb8.e9c26e72f268819c2b87a33b219edf96.jpeg'),
('GWC15029S',"Silver-Tone Slim Railroad 24 Hour Open Face Quartz Pocket Watch",'15881669552',WI+'dcd66618-4399-49bc-b487-98715d37caa7.23a20dc3f8227f72287458cd67829b52.jpeg'),
('GWC15042SM',"Silver-Tone Polished Finish Covered Quartz Pocket Watch with Chain",'167547673',WI+'68a23053-7fe1-4a7c-a2fc-44f2e63e6b3b_1.ce377677edf94fc07b1cf95869284cbc.jpeg'),
('GWC15042SG',"Silver-Tone Polished Finish Covered Quartz Pocket Watch with Chain",'184624971',WI+'c4ee6770-e126-406c-af86-bb91e64d7d6f_1.d53f2f9617e1cc3e08be0ef1ca7b1578.jpeg'),
('GWC15042BBK',"Gun Metal Black Dial Covered Quartz Pocket Watch with Chain",'143456191',''),
('GWC15042B',"Gun Metal White Dial Covered Quartz Pocket Watch with Chain",'115540060','https://i5.walmartimages.com/seo/Men-s-Gun-Metal-White-Dial-Covered-Quartz-Pocket-Watch-with-Chain-GWC15042B_18d976a7-8cae-4945-93e6-b38fdb91bc42_1.c62faa70ced7e7b4ba7911ca03e830c0.jpeg'),
('GWC14100BBK',"Gun-Tone Mechanical Hand Wind Railroad Pocket Watch",'496041436',''),
('GWC14110B',"Railway Classic Gunmetal Analog Quartz Day/Date Hunter Pocket Watch",'423699734',WI+'52d428a5-ec76-4f79-93fa-a8216fe9b875.ff9ed83e7d779453603ca7351f2f35aa.jpeg'),
('GWC15042SBL',"Silver-Tone Blue Dial Covered Quartz Pocket Watch with Chain",'107015154',WI+'e03955a6-a7e6-42f5-a87a-e68dd94fc754_1.cfc662c5af5ca88564d31fabb4719749.jpeg'),
('GWC15026B',"Railroad Open Face Gun Metal Analog Quartz Pocket Watch with Chain",'105488907',WI+'995d8609-0b21-4489-8051-cd9bb0c5c052.8c492687a78604f4b482cb657ca84ef9.jpeg'),
('GWC18804G',"Gold-Tone Double Cover Exhibition Mechanical Pocket Watch",'133362928','https://i5.walmartimages.com/seo/Men-s-Gold-Tone-Double-Cover-Exhibition-Mechanical-Pocket-Watch-GWC18804G_0a1ef733-a5b3-4a57-9643-4f402068db1b.9d21732e759e18aa1d784cc254d6bad1.jpeg'),
]: a(code,t,WP+ip,img)
CAR.update({'GWC14106BBK':'Caixa de aço inoxidável com banho grafite, 49 mm; mecânico de corda manual com 17 rubis; mostrador preto; vidro mineral; 30 m; vem com corrente.',
'GWC14109BBK':'Caixa de aço inoxidável com banho grafite, 49 mm × 11 mm; quartzo com data; mostrador preto; vidro mineral; 30 m.',
'GWC15042B':'Caixa com tampa (savonette) de liga metálica cor grafite, 47 mm × 14 mm; quartzo japonês; mostrador branco; corrente de 14 polegadas.'})
a('GWC18803S',"Silver-Tone Mechanical Double Cover Dual Time Pocket Watch",'https://www.desertcart.com.kw/products/10804373-gotham-mens-silver-tone-mechanical-double-cover-dual-time-pocket.md','https://m.media-amazon.com/images/I/71IAbFQtMkL.jpg')
a('GWC14050SBG',"Silver-Tone 17 Jewel Mechanical Double Hunter Pocket Watch",'https://www.desertcart.us/products/66240947-mens-silver-tone-17-jewel-mechanical-double-hunter-pocket-watch.md','https://images-na.ssl-images-amazon.com/images/I/51mzWSchOOL.jpg')
a('GWC14036G',"Gold-Tone 17 Jewel Mechanical Covered Pocket Watch",WP+'169707491','https://i5.walmartimages.com/seo/Men-s-Gold-Tone-17-Jewel-Mechanical-Covered-Pocket-Watch-GWC14036G_cf10e780-4a5a-48d3-8cf0-96c1f73e24c2.26a0ad22c65fbbafd6938d12cc957958.jpeg')
# só título de resultado de busca
for code,t,u in [
('GWC14040S',"17 Jewel Mechanical Double Half Hunter Pocket Watch",'https://manuals.plus/asin/B006K0VZ76'),
('GWC14112SB',"Classic Series Stainless Steel Open Face 17 Jewel Mechanical Hand Wind Pocket Watch",R+'gotham-classic-series-stainless-steel-open-face-17-jewel-mechanical-hand-wind-pocket-watch-gwc14112sb'),
('GWC14112S',"Classic Series Stainless Steel Open Face 17 Jewel Mechanical Hand Wind Pocket Watch",R+'gotham-classic-series-stainless-steel-open-face-17-jewel-mechanical-hand-wind-pocket-watch-gwc14112s'),
('GWC14112BBK',"Classic Series Gunmetal Plated Open Face 17 Jewel Mechanical Hand Wind Pocket Watch",R+'gotham-classic-series-gunmetal-plated-stainless-steel-open-face-17-jewel-mechanical-hand-wind-pocket-watch-gwc14112bbk'),
('GWC14109BY',"Sport Series Gunmetal Stainless Steel Analog Quartz Date Pocket Watch",R+'gotham-mens-sport-series-gunmetal-stainless-steel-analog-quartz-date-pocket-watch-gwc14109by'),
('GWC15027SG',"Silver-Tone Slim Railroad Open Face Quartz Pocket Watch",'https://www.ebay.de/itm/112161810249'),
('GWC15026S',"Silver-Tone Ultra Thin Railroad Open Face Quartz Pocket Watch",'https://newgoods.org.ru/buy/B006QAX9FQ'),
('GWC14140GA',"Women's Gold-Tone Open Face Pendant Watch with Chain",'https://www.ebay.de/itm/116632892970'),
('GWC18806BBK',"Gun-Tone Railroad Dial Double Hunter 17 Jewel Mechanical Pocket Watch",'https://www.desertcart.hu/products/96518422-gothammens-gun-tone-railroad-dial-double-hunter-17-jewel-mechanical'),
]: a(code,t,u)
CAR.update({'GWC18803S':'Mecânico de 17 rubis com segundo fuso horário; caixa prateada com dupla tampa e vidros minerais na frente e no fundo; ponteiros azul-cobalto; vem com corrente.',
'GWC14050SBG':'Mecânico de 17 rubis visível ao abrir as tampas; caixa prateada polida tipo double hunter (exibição); ponteiros azul-cobalto; vidro mineral.'})
E='https://www.ebay.de/itm/'
for code,t,i in [
('GWC15044BY',"Gunmetal Military Dial Hunter Quartz Pocket Watch",'127063938208'),
('GWC15044BBL',"Gunmetal Railroad Dial Covered Quartz Pocket Watch",'117436207660'),
('GWC14134GA',"Women's Gold-Tone Open Face Pendant Watch with Chain",'116974174951'),
('GWC14134GR',"Women's Gold-Tone Open Face Pendant Watch with Chain",'116983369878'),
('GWC15044SG',"Silver-Tone Railroad Dial Covered Quartz Pocket Watch",'117436254991'),
('GWC15042SP',"Silver-Tone Polished Covered Quartz Pocket Watch",'115495181048'),
('GWC14135GR',"Women's Gold-Tone Open Face Pendant Watch with Chain",'127623937549'),
('GWC15044SBL',"Silver-Tone Railroad Dial Covered Quartz Pocket Watch",'117436251725'),
('GWC14100BBK',"",'124544497272'),
('GWC15042BBK',"",'116600506782'),
]: a(code,t,E+i)
NS="Railway Classic Nostalgia Series Mechanical Pocket Watch"
for code,slug,t in [
('GWC14115S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14115s',NS),
('GWC14114S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14114s',NS),
('GWC14116S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14116s',NS),
('GWC14117S','gotham-mens-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14117s',NS),
('GWC14117G','gotham-mens-gold-plated-stainless-steel-mechanical-hand-wind-railway-classic-nostalgia-series-pocket-watch-gwc14117g',"Railway Classic Nostalgia Series Gold Plated Mechanical Pocket Watch"),
('GWC14111SB','gotham-mens-stainless-steel-mechanical-hand-wind-railroad-pocket-watch-gwc14111sb',"Stainless Steel Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14102S','gotham-mens-silver-tone-mechanical-hand-wind-railroad-pocket-watch-gwc14102s',"Stainless Steel Mechanical Hand Wind Railroad Pocket Watch"),
('GWC14108B','gotham-mens-gun-plated-stainless-steel-mechanical-hand-wind-railroad-style-pocket-watch-gwc14108b',"Gun-Plated Mechanical Hand Wind Railroad Style Pocket Watch"),
('GWC14109BO','gotham-mens-sport-series-gunmetal-stainless-steel-analog-quartz-date-pocket-watch-gwc14109bo',""),
]: a(code,t,R+slug)
a('GWC18806G','', '', 'https://m.media-amazon.com/images/I/71f+E1tiF4L._AC_SL1500_.jpg')
a('GWC14109BG',"Sport Series Gunmetal Stainless Steel Analog Quartz Date Pocket Watch",'https://www.desertcart.vn/products/262520945-gotham-mens-sport-series-gunmetal-stainless-steel-analog-quartz-date.md','https://m.media-amazon.com/images/I/71W9xdgTTGL.jpg')
CAR['GWC14109BG']='Caixa de aço inoxidável cor grafite, 49 mm × 11 mm; quartzo japonês com data; mostrador verde estilo militar; vidro mineral; 30 m; vem com corrente.'
a('GWC18806SB','','','https://i5.walmartimages.com/seo/Gotham-Men-s-Silver-Tone-Railroad-Dial-Double-Hunter-17-Jewel-Mechanical-Pocket-Watch-GWC18806SB_929487ce-f69f-4eda-9aa6-7bd7b6ed2ed3.5bf9c82af9534571bd8af616f09fe842.jpeg')
CAR['GWC18806SB']='Caixa de latão prateada, 54 mm, tipo double hunter; mostrador ferroviário; mecânico de corda manual com 17 rubis; vidro mineral.'
for code,t,ip,img in [
('GWC18807S','', '16026621662','eff26110-38e5-441b-8dbc-9cbd731812c7.2eaedc83963d31dd0cf0c01347b907eb.jpeg'),
('GWC14112S','', '20033254930','e13091ce-4e19-492d-b26e-cc5bd1c27070.7113d2746775be7c08d684d603ba9938.jpeg'),
('GWC18806B','', '20001012078','4b222842-35d2-426d-af91-e577703e2143.f8bc39a4a86f61972aa1f040fe445a27.jpeg'),
('GWC18808BBK',"Classic Gunmetal Plated Polished Case Double Hunter 17 Jewel Mechanical Pocket Watch",'15942203503','810ea146-9aa4-4b88-a2f1-ec4ac19dff8e.2ba60612cd501cd663fe7ec1d02360b3.jpeg'),
('GWC14051S',"Silver-Tone 17 Jewel Mechanical Double Cover Pocket Watch",'170274707','7602cd17-ba7e-4b96-983d-9cddd553fff3.d527830e666ac7394ab1cb2440c3c73a.jpeg'),
('GWC14110BO',"Railway Classic Gunmetal Analog Quartz Day/Date Hunter Pocket Watch",'679279187','9f89f9e6-9a18-4c5f-b098-0d90a259c990.46120bd55643b354d05ea4451f4c3ada.jpeg'),
('GWC15026S','', '102796776','6e613fa4-1221-49b8-b3cb-6725ab450c54.3223f2f5d2a5ee45076ac937a358df31.jpeg'),
('GWC18804S',"Double Hunter Silver-Tone Double Cover Exhibition Mechanical Pocket Watch",'111965388','53186354-012e-4eaf-bfb8-eadbcd6eaaf9_1.51469c670b83f39808d0dec10b7be614.jpeg'),
]: a(code,t,WP+ip,WI+img)
a('GWC15044BY','','','https://i5.walmartimages.com/seo/Gotham-Men-s-Gunmetal-Railroad-Polished-Finish-Covered-Quartz-Pocket-Watch-GWC15044BY_29349c19-74e1-4fc6-8c49-0660725efa63.b04ee476865a6cc717790b1b47304c6e.jpeg')
a('GWC021STX',"TimeOptics Talking Silver-Tone Day Date Alarm Expansion Bracelet Watch",WP+'15921100118','https://i5.walmartimages.com/seo/Men-s-Talking-Silver-Tone-Day-Date-Alarm-Expansion-Bracelet-Watch-GWC021STX_7beaebb4-1e5d-49be-88bc-a582c7af00ef.fba732bacd7a6ce29e1e8b25f745da0b.jpeg')
a('GWC128TBK',"TimeOptics Talking Two-Tone Day Date Alarm Leather Strap Watch",R+'timeoptics-mens-talking-two-tone-day-date-alarm-leather-strap-watch-gwc128tbk')
a('GWC021ST',"TimeOptics Talking Silver-Tone Day Date Alarm Flex Band Watch",'https://ebay.com/itm/112174562209')
CAR['GWC18806SB']='Caixa de latão cromado, 54 mm, tipo double hunter (gravável); mostrador preto estilo ferroviário; mecânico de corda manual com 17 rubis e pequenos segundos; vidro mineral; vem com corrente de 14 polegadas.'
CAR['GWC14108S']='Caixa de aço inoxidável de 49 mm; mecânico de corda manual com 17 rubis e pequenos segundos; mostrador estilo ferroviário; vidro mineral; 30 m; vem com corrente.'
for k in ('GWC021STX','GWC128TBK','GWC021ST'): CAR[k]='Relógio de pulso falante (anuncia hora e data em voz), com alarme; linha TimeOptics da Gotham Watch Co.'
