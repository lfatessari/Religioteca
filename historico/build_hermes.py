# acumulador: cada item = (nome, codigo, url, caract)
CS='https://www.collectorsquare.com/en/watches/hermes/'
def cs(path): return CS+path
D1='https://www.1stdibs.com/buy/hermes-watches'; D3='https://www.1stdibs.com/buy/hermes-watch/?page=3'; D4='https://www.1stdibs.com/buy/hermes-watch/?page=4'; DS='https://www.1stdibs.com/buy/hermes-sellier-watch/'
V1="Visto só em anúncio da CollectorSquare (link do anúncio). "
V2="Visto só no título de anúncio da 1stDibs (link da página de busca). "
R=[]
def a(n,c,u,e): R.append((n,c,u,e))
a("Cape Cod","CC1.190",cs("cape-cod/cape-cod/hermes-cape-cod-in-white-gold-ref-cc1-190-circa-2000-395349.html"),V1+"Ouro branco, c. 2000.")
a("Passe-Passe","PP1.210",cs("passe-passe/passe-passe/hermes-passe-passe-in-stainless-steel-ref-hermes-pp1-210-circa-2008-414705.html"),V1+"Aço, c. 2008.")
a("Heure H","HH1.210",cs("heure-h/heure-h/hermes-heure-h-medium-model-in-stainless-steel-ref-hermes-hh1-210-circa-2010-432151.html"),V1+"Aço, modelo médio.")
a("Cape Cod","CC1.210",cs("cape-cod/cape-cod/hermes-cape-cod-watch-in-steel-ref-hermes-cc1-210-circa-2000-435587.html"),V1+"Aço, c. 2000.")
a("Heure H","HH1.110",cs("heure-h/heure-h/hermes-heure-h-watch-small-model-in-steel-ref-hermes-hh1-110-circa-2020-435542.html"),V1+"Aço, modelo pequeno, quartzo, c. 2020.")
a("Cape Cod","CC3.730",cs("cape-cod/cape-cod/hermes-cape-cod-watch-large-model-in-steel-ref-hermes-cc3-730-circa-2021-433823.html"),V1+"Aço, modelo grande, c. 2021.")
a("Barenia","BA1.510",cs("barenia/barenia/hermes-barenia-in-stainless-steel-ref-hermes-ba1-510-circa-2000-429027.html"),V1+"Aço, c. 2000.")
a("Arceau","AR5.220",cs("arceau/arceau/hermes-arceau-watch-in-gold-plated-and-steel-ref-hermes-ar5-220a-circa-2000-435665.html"),V1+"Aço e banho de ouro, c. 2000 (anúncio grafa AR5.220a).")
a("Arceau","AR5.210",cs("arceau/arceau/hermes-arceau-steel-watch-ref-hermes-ar5-210-circa-2010-435666.html"),V1+"Aço, c. 2010.")
a("Belt","BE1.210",cs("belt/belt/hermes-belt-in-stainless-steel-ref-hermes-be1-210-circa-2000-428985.html"),V1+"Aço, c. 2000.")
a("Cape Cod","CC1.250",cs("cape-cod/cape-cod/hermes-cape-cod-in-stainless-steel-ref-hermes-cc1-250-circa-2010-429017.html"),V1+"Aço, c. 2010.")
a("Cape Cod Tonneau","CT1.210",cs("cape-cod/cape-cod-tonneau/hermes-cape-cod-tonneau-watch-in-steel-ref-hermes-ct1-210-circa-2000-435412.html"),V1+"Aço, c. 2000.")
a("Clipper","CL4.210",cs("clipper/clipper/hermes-clipper-in-stainless-steel-ref-hermes-cl4-210-circa-2000-432760.html"),V1+"Aço, 24 mm, quartzo, c. 2000.")
a("Heure H","HH1.510",cs("heure-h/heure-h/hermes-heure-h-watch-medium-size-in-steel-ref-hermes-hh1-510-circa-2010-435675.html"),V1+"Aço, modelo médio, c. 2010.")
a("Heure H","HH1.530",cs("heure-h/heure-h/hermes-heure-h-watch-large-model-in-steel-ref-hermes-hh1-530-circa-2010-433820.html"),V1+"Aço, modelo grande, c. 2010.")
a("Cape Cod Nantucket","CC3.210",cs("cape-cod/cape-cod-nantucket/hermes-cape-cod-nantucket-watch-in-steel-ref-hermes-cc3-210-circa-2010-435577.html"),V1+"Aço, modelo pequeno, c. 2010.")
a("Cape Cod","CC1.710",cs("cape-cod/cape-cod/hermes-cape-cod-watch-large-model-in-steel-ref-hermes-cc1-710-circa-2010-436236.html"),V1+"Aço, modelo grande, automático, c. 2010.")
a("Cape Cod","CC2.710",cs("cape-cod/cape-cod/hermes-cape-cod-watch-large-model-in-steel-ref-hermes-cc2-710-circa-2010-435582.html"),V1+"Aço, modelo grande, quartzo, c. 2010.")
a("Kelly 2","KT1.210",cs("kelly-2/kelly-2/hermes-kelly-2-in-stainless-steel-ref-hermes-kt1-210-circa-2000-432767.html"),V1+"Aço, c. 2000.")
a("Heure H","HH1.131",cs("heure-h/heure-h/hermes-heure-h-watch-small-model-in-steel-ref-hermes-hh1-131-circa-2025-435541.html"),V1+"Aço, modelo pequeno, c. 2025.")
a("Cape Cod Tonneau","CT1.710",cs("cape-cod/cape-cod-tonneau/hermes-cape-cod-tonneau-watch-in-steel-ref-hermes-ct1-710-circa-2010-435578.html"),V1+"Aço, c. 2010.")
a("Arceau","AR5.710",cs("arceau/arceau/hermes-arceau-watch-in-steel-ref-hermes-ar5-710-circa-2010-435674.html"),V1+"Aço, automático, c. 2010.")
a("Médor","ME2.110",cs("medor/medor/hermes-medor-steel-watch-ref-hermes-me2-110-circa-2010-436057.html"),V1+"Aço, c. 2010.")
a("Arceau","AR3.220",cs("arceau/arceau/hermes-arceau-watch-in-gold-plated-steel-ref-hermes-ar3-220-436321.html"),V1+"Aço com banho de ouro.")
a("Arceau","AR3.210",cs("arceau/arceau/hermes-arceau-watch-in-steel-ref-hermes-ar3-210-circa-2000-435664.html"),V1+"Aço, c. 2000.")
a("Cape Cod","CC1.810",cs("cape-cod/cape-cod/hermes-cape-cod-watch-size-xl-in-steel-ref-hermes-cc1-810-circa-2010-435662.html"),V1+"Aço, tamanho XL, c. 2010.")
a("Faubourg","FG1.171",cs("faubourg/faubourg/hermes-faubourg-watch-in-rose-gold-ref-hermes-fg1-171-circa-2010-436866.html"),V1+"Ouro rosa, c. 2010.")
a("Tandem","TA1.210",cs("tandem/tandem/hermes-tandem-in-stainless-steel-ref-hermes-ta1-210-circa-2000-432766.html"),V1+"Aço, c. 2000.")
a("Tandem","TA1.296",cs("tandem/tandem/hermes-tandem-watch-in-white-gold-ref-hermes-ta1-296-circa-2010-429258.html"),V1+"Ouro branco, c. 2010.")
a("Heure H","HH1.801",cs("heure-h/heure-h/hermes-heure-h-watch-in-gold-plated-and-steel-ref-hermes-hh1-801-circa-2017-422481.html"),V1+"Aço e banho de ouro, c. 2017.")
a("Paprika","PA1.210",cs("paprika/paprika/hermes-paprika-in-stainless-steel-ref-hermes-pa1-210-circa-2000-427692.html"),V1+"Aço, c. 2000.")
a("Heure H","RS1.205",cs("heure-h/heure-h/hermes-heure-h-in-stainless-steel-and-stainless-steel-ref-hermes-rs1-205-circa-2010-428998.html"),V1+"Aço, c. 2010 (referência como no anúncio).")
a("Kelly","KE1.210",cs("kelly/montre-kelly/hermes-kelly-watch-in-steel-ref-hermes-ke1-210-circa-2000-436477.html"),V1+"Aço, c. 2000.")
a("Kelly (Kelly Cadenas)","KE1.201",cs("kelly/montre-kelly/hermes-kelly-watch-gold-plated-ref-hermes-ke1-201-circa-1990-436473.html"),V1+"Aço com banho de ouro, cadeado, c. 1990.")
a("Arceau","AR6.410",cs("arceau/arceau/hermes-arceau-watch-in-steel-ref-hermes-ar6-410-circa-2012-435673.html"),V1+"Aço, c. 2012.")
a("Heure H","HH1.810",cs("heure-h/heure-h/hermes-heure-h-in-stainless-steel-ref-hermes-hh1-810-431055.html"),V1+"Aço, quartzo.")
a("Heure H","HH1.201",cs("heure-h/heure-h/hermes-heure-h-watch-small-model-in-steel-and-gold-plated-ref-hermes-hh1-201-circa-2010-436468.html"),V1+"Aço e banho de ouro, modelo pequeno (21 mm), quartzo.")
a("Cape Cod Nantucket","NA2.110",cs("cape-cod/cape-cod-nantucket/hermes-cape-cod-nantucket-steel-watch-ref-hermes-na2-110-circa-2010-435583.html"),V1+"Aço, c. 2010.")
a("Cape Cod Nantucket","NA1.250",CS+"?page=2","Visto só no título de anúncio (só para membros) da CollectorSquare (link da página da lista). Prata, c. 1996.")
a("Pullman","PU2.210",CS,"Visto só no título de anúncio (só para membros) da CollectorSquare (link da página da lista). Aço, c. 2000.")
# 1stDibs
a("Heure H Mini","HH1.190",D1,V2+"Ouro branco 18k com diamantes, pulseira de crocodilo.")
a("Clipper H1 Grande Date","CP1.710",D1,V2+"Aço, 44 mm, automático, pulseira de aligátor.")
a("Heure H","HH1.191",D1,V2+"Ouro branco 18k com diamantes.")
a("Heure H","HH1.102",D1,V2+"Aço com banho de ouro, 20 x 25 mm, diamante, anos 1990.")
a("Heure H Mini","W053094WW00",D1,V2+"Ouro rosa 18k, 21 x 17 mm, 84 diamantes.")
a("Faubourg Joaillerie","W049640WW00",D1,V2+"Ouro branco 18k e diamantes, 16,3 mm, mostrador azul.")
a("Sesame Squelette","SM1.790",D1,V2+"Ouro branco 18k, 36 mm, esqueletizado, automático, anos 2000.")
a("Loquet","L01.201",D1,V2+"Aço com banho de ouro, bracelete, quartzo.")
a("Harnais","HA3.410",D1,V2+"Aço, quartzo.")
a("Clipper Date Automatique","CP2.810",D1,V2+"Aço, automático.")
a("Clipper Diver","CL2.910",D1,V2+"Aço, quartzo.")
a("Clipper Chronographe","CP2.941",D1,V2+"Titânio e aço, automático, data.")
a("Clipper Chronographe Lady","CP2.430",D3,V2+"Aço, diamantes, mostrador de madrepérola, quartzo (anúncio grafa CP2.430.212/1C5).")
a("Médor","W028322WW00",D3,V2+"Aço, 23 mm, pulseira de couro.")
a("Médor","W028321WW00",D3,V2+"Aço, 23 mm, pulseira de couro.")
a("Heure H","HH1.291",D3,V2+"Ouro branco 18k com diamantes, 30 x 24 mm, quartzo.")
a("Dressage Chronographe","DR5.910",D3,V2+"Aço, 40,5 mm, automático (anúncio grafa DR5.910.220/MHA).")
a("Slim d'Hermès","CA2.271",D3,V2+"Ouro rosa 18k, 32 mm, luneta de diamantes (anúncio grafa CA2.271.212/ZZ8C).")
a("Arceau","AR4.810",D3,V2+"Aço, 41 mm, pulseira Barenia.")
a("Arceau","AR5.786",D3,V2+"Ouro amarelo e diamantes, 38 mm.")
a("Heure H","HH1.585",D4,V2+"Ouro 18k (amarelo ou rosa).")
a("Arceau Squelette","AR2.710",D4,V2+"40 mm, automático (anúncio grafa 'Skerret').")
a("Clipper","CL5.785",D4,V2+"Ouro amarelo 18k, 36 mm.")
a("Cape Cod","CC1.230",D4,V2+"Aço, quartzo (anúncio grafa CC1.230.213.WW7T).")
a("Cape Cod","CC1.288",D4,V2+"Ouro amarelo 18k, 23 x 23 mm, luneta de diamantes.")
a("Sellier","SE4.210",DS,V2+"Aço, mostrador branco, quartzo.")
a("Sellier","SE3.720",DS,V2+"Aço e ouro 18k, 34 mm, quartzo.")
a("Clipper","CL4.220","https://www.thewatchcompany.com/clipper-cl4220-ss-gp-ivory-24mm-hermes-cl4220-ivory-govwqeg0.html","Visto só em anúncio da The Watch Company (link do anúncio). Aço e banho de ouro, 24 mm, mostrador marfim.")
a("Arceau","W044824WW00","https://www.thewatchbox.com/fr/fr/shop/Hermes-Arceau-W044824WW00.html","Visto só em anúncio da WatchBox (link do anúncio). Aço, 40 mm, mostrador azul, quartzo, data, 30 m.")
MP="Foto e dados da Mr Porter. "
a("Arceau Automatique","W055574WW00","https://www.mrporter.com/variants/images/18706561955937385/in/w2000_q80.jpg",MP+"Aço, 40 mm x 9,3 mm, calibre automático H1837 (45 h), mostrador opalino prateado em espinha de peixe, pulseira de aligátor preta, 30 m.")
a("Arceau Automatique","W055562WW00","https://www.mrporter.com/variants/images/13452677150447004/in/w2000_q80.jpg",MP+"Aço, 40 mm, calibre automático H1837, mostrador opalino prateado em espinha de peixe, pulseira de aligátor marrom, 30 m.")
a("Arceau Automatique","W055547WW00","https://www.mrporter.com/variants/images/13452677152107498/in/w2000_q80.jpg",MP+"Aço, 40 mm, calibre automático H1837, mostrador marfim e cinza-claro, pulseira de aligátor azul, 30 m.")
a("H08 Automatique Graphène","W057303WW00","https://www.mrporter.com/variants/images/11452292647421708/in/w2000_q80.jpg",MP+"Grafeno (composto) e borracha, 39 mm, automático.")
a("Slim d'Hermès Titane","W052845WW00","https://www.mrporter.com/variants/images/20346390235370710/in/w2000_q80.jpg",MP+"Titânio, 39,5 mm x 2,6 mm, calibre automático H1950 (42 h), mostrador antracite caracolado, ponteiro de segundos laranja, 30 m.")
NP="Foto e dados da Net-a-Porter. "
a("Arceau Soleil","W053348WW00","https://www.net-a-porter.com/variants/images/6630340699185345/in/w2000_q60.jpg",NP+"Aço, 36 mm, 0,34 ct de diamantes, quartzo, mostrador laqueado azul degradê gravado a laser, pulseira de aligátor azul, 30 m.")
a("Nantucket Dual Time","W053748WW00","https://www.net-a-porter.com/variants/images/17411127376576986/in/w2000_q60.jpg",NP+"Aço, 39 mm, 0,27 ct de diamantes, quartzo com módulo GMT, mostrador de aventurina azul e laca, pulseira de aligátor azul-marinho.")
a("Nantucket TPM","W049573WW00","https://www.net-a-porter.com/en-hk/shop/product/hermes-timepieces/jewelry-and-watches/watches/nantucket-17mm-very-small-18-karat-rose-gold-mother-of-pearl-watch/13452677151377111","Visto na Net-a-Porter (link da página; foto não obtida). Ouro rosa 18k, 17 mm, bracelete de ouro, quartzo, mostrador de madrepérola.")
a("Galop d'Hermès GM","W047892WW00","https://www.net-a-porter.com/en-us/shop/product/hermes-timepieces/jewelry-and-watches/watches/galop-d-hermes-40mm-large-18-karat-rose-gold-and-alligator-watch/25185454456470394","Visto na Net-a-Porter (link da página; foto não obtida). Ouro rosa 18k, 40 mm, quartzo, mostrador opalino prateado granulado, pulseira de aligátor vermelho-rubi.")
a("Galop d'Hermès GM","W047887WW00","https://www.net-a-porter.com/variants/images/25185454456470374/in/w2000_q60.jpg",NP+"Aço, 40 mm, 0,66 ct de diamantes, quartzo, mostrador opalino prateado granulado, pulseira de aligátor azul-safira.")
a("Faubourg Double Tour","W049177WW00","https://www.net-a-porter.com/en-ch/shop/product/hermes-timepieces/jewelry-and-watches/watches/faubourg-double-tour-15mm-mini-18-karat-rose-gold-and-diamond-watch/17411127376576976","Visto na Net-a-Porter (link da página; foto não obtida). Ouro rosa 18k, 15 mm, bracelete de duas voltas, luneta com 0,10 ct de diamantes, quartzo.")
a("Nantucket Serti Joaillier PM","W056606WW00","https://www.net-a-porter.com/en-us/shop/product/hermes-timepieces/jewelry-and-watches/watches/nantucket-serti-joaillier-29mm-small-stainless-steel-alligator-and-diamond-watch/36856120585388386","Visto na Net-a-Porter e no site oficial (link da página; foto não obtida). Aço, 29 mm, 186 diamantes (0,58 ct), quartzo, mostrador laqueado preto, pulseira de aligátor azul-marinho.")
a("Heure H au Carré PM","W053242WW00","https://www.net-a-porter.com/variants/images/25185454456521521/in/w2000_q60.jpg",NP+"Aço, 21 mm, quartzo, mostrador laqueado preto com 0,126 ct de diamantes, pulseira de aligátor preta.")
LP="Visto na Lepage (link da página; foto não obtida). "
a("Galop d'Hermès MM","W053768WW00","https://www.lepage.fr/en/22845-hermes-galop-hermes-medium-model-watch-set-with-quartz-silver-dial-black-leather-strap-32-mm-053768ww.html",LP+"Modelo médio, 32 mm, quartzo, mostrador prateado, pulseira de couro, 30 m.")
a("Galop d'Hermès MM","W058955WW00","https://feldmarwatch.com/wp-content/uploads/2026/08/W058955WW00.jpg","Foto da Feldmar; dados da Lepage. Modelo médio, 32 mm, quartzo, mostrador de madrepérola, pulseira de couro cinza, 30 m.")
a("Galop d'Hermès MM","W058957WW00","https://www.lepage.fr/en/20671-hermes-galop-hermes-medium-model-watch-set-with-quartz-aventurine-dial-and-hawk-s-eye-black-leather-strap-32-mm-058957ww.html",LP+"Modelo médio, 32 mm, quartzo, mostrador de aventurina, pulseira de couro preto, 30 m.")
a("Galop d'Hermès GM","W047898WW00","https://www.lepage.fr/en/20670-hermes-galop-hermes-large-model-watch-set-with-quartz-silver-dial-grey-leather-strap-40-mm-047898ww.html",LP+"Modelo grande, 40 mm, quartzo, mostrador prateado, pulseira de couro cinza, 30 m.")
a("Galop d'Hermès MM","W053750WW00","https://www.lepage.fr/en/20669-hermes-galop-hermes-medium-model-watch-set-with-quartz-silver-dial-black-leather-strap-32-mm-053750ww.html",LP+"Modelo médio, 32 mm, quartzo, mostrador prateado, pulseira de couro preto, 30 m.")
a("Galop d'Hermès MM","W053774WW00","https://www.lepage.fr/en/22847-hermes-galop-d-hermes-moyen-model-quartz-silver-dial-brown-leather-strap-32-mm-053774ww.html",LP+"Modelo médio, 32 mm, quartzo, mostrador prateado, pulseira de couro marrom, 30 m.")
a("Galop d'Hermès MM","W053770WW00","https://www.lepage.fr/en/24272-hermes-galop-d-hermes-medium-model-quartz-silver-dial-etoupe-leather-strap-32-mm-w053770ww00.html",LP+"Modelo médio, 32 mm, quartzo, mostrador prateado, pulseira de couro etoupe, 30 m.")
a("Arceau GM","W043404WW00","https://www.lepage.fr/53466-zoom_default/hermes-arceau-grand-modele-quartz-watch-white-lacquered-dial-taupe-leather-strap-36-mm.jpg","Foto e dados da Lepage. Aço, 36 mm, quartzo, mostrador laqueado branco, ponteiros azulados, pulseira Barenia taupe, safira, 30 m.")
a("Arceau PM","W040135WW00","https://www.lepage.fr/53405-zoom_default/hermes-arceau-petit-modele-quartz-watch-white-matte-dial-brown-leather-strap-28-mm.jpg","Foto e dados da Lepage. Aço, 28 mm, quartzo, mostrador branco fosco, ponteiros azulados, pulseira Barenia natural, safira, 30 m.")
a("Slim d'Hermès","CA2.210","https://www.lepage.fr/80708-zoom_default/hermes-slim-ca2210-quartz-32-mm-full-set-2018.jpg","Foto e dados da Lepage (usado, 2018). Aço, 32 mm x 7 mm, quartzo, mostrador prateado jateado, bracelete de aço, 30 m.")
a("Médor","W028326WW00","https://www.prestigetime.com/images/watches/112/2132/w028326WW00/028326WW00_main.jpg","Foto e dados da Prestige Time. Aço, 23 x 23 mm, quartzo, mostrador prateado, pulseira de couro laranja, safira, 30 m (também ME3.210.282/SW93).")
a("Kelly","KE4.110","https://cdn.shopify.com/s/files/1/0266/7141/5373/files/hermes-kelly-ke4-110b-ladies-stainless-steel-white-dial-quartz-hermes-1253531605.png?v=1786129271","Foto da Wrist Aficionado. Caixa em forma de cadeado em aço polido, mostrador branco, quartzo, bracelete de aço de duas fileiras (anúncio grafa KE4.110B).")
a("Carré H XL","W045778WW00","https://www.manfredijewels.com/cdn/shop/files/hermes-carre-h-extra-large-watch-watches-manfredi-jewels-637.jpg?v=1695360277","Foto e dados da Manfredi Jewels. Aço, 38 mm de largura, calibre automático manufatura H1912 (50 h), mostrador cinza-escuro raiado, pulseira Barenia natural, 30 m.")
a("Carré H – edição limitada de 173 peças (2010)","","https://quillandpad.com/wp-content/uploads/2018/01/Hermes-Carre-H-2010.jpg","Foto da Quill & Pad. Titânio jateado, 36,5 x 36,5 mm, calibre Girard-Perregaux 3200, 2010.")
a("Carré H (2018) – mostrador preto, segundos vermelhos","","https://quillandpad.com/wp-content/uploads/2018/01/Hermes-Carre-H-9W0B5509.jpg","Foto da Quill & Pad. Aço, 38 x 38 mm, calibre automático manufatura H1912 (50 h).")
a("Carré H (2019) – mostrador preto, segundos vermelhos, pulseira Barenia preta","","https://en.worldtempus.com/sites/default/files/media/article/hermes/ecarre_h_black_barenia_red-_burnishing_photo-article.jpg","Foto da Worldtempus (03/05/2019). Aço polido e jateado, 38 x 38 mm, automático, mostrador guilhochado, números luminescentes.")
a("Carré H (2019) – segundos amarelos, pulseira Barenia natural","","https://en.worldtempus.com/sites/default/files/media/article/hermes/hermes-carre_h_natural_barenia_yellow_burnishing_image-article.jpg","Foto da Worldtempus (03/05/2019). Aço polido e jateado, 38 x 38 mm, automático, mostrador guilhochado cinza-antracite.")
a("H08 Squelette – azul","W408556WW00","https://hermes.watchonista.com/node/500510","Visto na Watchonista (link da página). Titânio com DLC, 39 mm, calibre automático esqueletizado H1978 S, borracha azul, 100 m, 2026.")
JE="Foto da The Jewellery Editor. "
a("Médor PM – pirâmides com pavê de diamantes, aligátor preto","","https://media.thejewelleryeditor.com/cdn-cgi/image/width=640,height=640,fit=cover,gravity=0.5x0.5,format=auto/old-47808-HermesMedorWatches013.jpg",JE+"Relógio secreto: o mostrador fica sob a pirâmide maior; aço, 499 diamantes, quartzo, mostrador opalino prateado.")
a("Médor – pulseira rosa, pirâmides de ouro rosa com diamantes","","https://media.thejewelleryeditor.com/cdn-cgi/image/width=640,height=640,fit=cover,gravity=0.5x0.5,format=auto/old-47797-HermesMedorWatches002.jpg",JE+"Quartzo, mostrador opalino prateado.")
a("Médor (1993) – Barenia natural, pirâmides ródio","","https://media.thejewelleryeditor.com/cdn-cgi/image/width=640,height=640,fit=cover,gravity=0.5x0.5,format=auto/old-47805-HermesMedorWatches010.jpg",JE+"Modelo de lançamento, 1993, quartzo.")
SB="Foto e dados de leilão da Sotheby's. "
a("Arceau L'Heure de la Lune – edição limitada de 100 peças","AR1.890A","https://sothebys-md.brightspotcdn.com/dims4/default/7c8fa05/2147483647/strip/true/crop/2000x2000+0+0/resize/4096x4096!/quality/90/?url=http%3A%2F%2Fsothebys-brightspot.s3.amazonaws.com%2Fmedia-desk%2F16%2Fb5%2Fce3fc6574d87ac2acc2277fad817%2Fge2104-bzxjt-1.jpg",SB+"Ouro branco 18k, 43 mm, calibre automático H1837, mostrador de aventurina e madrepérola, c. 2019.")
a("Arceau – mostrador de esmalte cloisonné (ateliê Anita Porchet), edição limitada","AR6.A90C","https://sothebys-md.brightspotcdn.com/dims4/default/df79c6b/2147483647/strip/true/crop/2500x2500+0+0/resize/4096x4096!/quality/90/?url=http%3A%2F%2Fsothebys-brightspot.s3.amazonaws.com%2Fmedia-desk%2Fde%2F2a%2F3a2887054bc78ffdbdf5eb69311c%2Fn12174-dn3fs-01-cropped.jpg",SB+"Ouro branco 18k, 34 mm, calibre automático H1912, c. 2015.")
a("Arceau Le Temps Suspendu – platina, edição limitada","AR8.965","https://sothebys-md.brightspotcdn.com/dims4/default/572c7fc/2147483647/strip/true/crop/2500x2500+0+0/resize/4096x4096!/quality/90/?url=http%3A%2F%2Fsothebys-brightspot.s3.amazonaws.com%2Fmedia-desk%2Fda%2F64%2Fea04f823440a91d03561a316cfb3%2Fn12023-djm5f-02-cropped.jpg",SB+"Platina, 43 mm, automático ETA 2892-A2 com módulo, mostrador guilhochado preto, c. 2014.")
a("Arceau Le Temps Suspendu","AR8.910","https://sothebys-md.brightspotcdn.com/dims4/default/289bd8e/2147483647/strip/true/crop/4724x4724+0+0/resize/4096x4096!/quality/90/?url=http%3A%2F%2Fsothebys-brightspot.s3.amazonaws.com%2Fmedia-desk%2F93%2F15%2F571b58c7406392c500b7f63b4916%2Fge2114-c3998-1.jpg",SB+"Aço, 43 mm, automático ETA 2892-A2, data retrógrada e suspensão do tempo, mostrador prateado, c. 2012.")
a("Arceau Chronographe","AR4.910","https://images-catalog.antiquorum.swiss/images/384/lots/46/46.jpg","Foto e dados de leilão da Antiquorum. Aço, 42 mm, cronógrafo automático (calibre 2894-2), c. 2010.")
a("Arceau Petite Lune","AR7M.530","https://images-catalog.antiquorum.swiss/images/319/lots/78/78.jpg","Foto e dados de leilão da Antiquorum. Aço com 62 diamantes, 38 mm, automático H1837, mostrador de madrepérola com data e fases da lua, c. 2015.")
a("Arceau – edição limitada de 110 peças (2º Saut Hermès no Grand Palais)","","https://media.app.artisio.co/media/cb69651c-b560-4bed-88f6-b6f199770432/inventory/9f1dacd3-ad28-4546-82b1-fec02ac42b98/1ca8e766-413b-4bf0-8411-bbe9b4c906cf/0001_FWzlLj_lg.jpeg","Foto e dados de leilão da Aguttes. Aço, 39 mm, automático, c. 2010.")
a("Arceau Squelette – 30 anos do Arceau, edição limitada de 171 peças","","https://dist.phillips.com/auction-assets/NY060224/203646_001.jpg","Foto e dados de leilão da Phillips (2024). Ouro branco 18k, cerca de 40 mm, automático esqueletizado, fundo transparente, pulseira de aligátor vermelho.")
a("Arceau Le Temps Suspendu – ouro rosa","AR8.970","https://medias.collectorsquare.com/images/products/218961/00pp-hermes-arceau-le-temps-suspendu-in-pink-gold-ref-ar8-970-vers-2010.jpg","Foto da CollectorSquare. Ouro rosa, 43 mm, automático, safira, c. 2010.")
a("Arceau Le Temps Suspendu Fleurs d'Indiennes – série limitada de 5 peças","MO-AR8.790","https://cms.gphg.org/uploads/gphg2011_hermes_11_0627_arceau_fleursdindiennes_1_e3fdb040d5.jpg","Foto e dados do GPHG (2011). Ouro branco, 41 mm x 9,4 mm, automático com suspensão do tempo, mostrador guilhochado em espinha de peixe, 30 m.")
a("Arceau Le Temps Suspendu – ouro rosa, madrepérola, 38 mm","AR7.471","https://cms.gphg.org/uploads/gphg2013_050713_hermes_arceau_le_temps_suspendu_01_acd90bbafb.jpg","Foto e dados do GPHG (2013). Ouro rosa, 38 mm x 11,42 mm, base manufatura H1912 com módulo de horas e minutos retrógrados, mostrador de madrepérola, 30 m.")
a("Arceau Le Temps Suspendu – ouro rosa, mostrador azul raiado (2025)","","https://en.worldtempus.com/sites/default/files/styles/medium/public/2025-04/80340_0.jpg.jpeg?itok=K4TMiUlz","Foto e dados da Worldtempus. Ouro rosa, 42 mm, automático (45 h), data, pulseira azul, 30 m.")
a("Le Temps Suspendu 43 mm Platine Baguette","","https://en.worldtempus.com/sites/default/files/styles/medium/public/media/product/hermes-arceau-le-temps-suspendu-43mm-platine-baguette-face-view.jpg.jpeg?itok=9RdBSIHW","Foto e dados da Worldtempus (fora de produção). Platina, 43 mm, automático (42 h), mostrador azul, 30 m.")
a("H08 – ouro rosa e titânio, mostrador preto e dourado","W059581WW00","https://monochrome-watches.com/wp-content/uploads/2023/02/Hermes-H08-Watch-Black-and-Gold-Hands-On-Review-5.jpg","Foto e dados da Monochrome (2023). 39 x 39 mm, aro de ouro rosa, luneta de cerâmica preta, fundo de titânio DLC, automático H1837 (50 h), 100 m.")
a("H08 Titane (2025)","","https://monochrome-watches.com/wp-content/uploads/2025/09/2025-Hermes-H08-Titanium-and-Bleu-Saint-Cyr-review-3.jpg","Foto e dados da Monochrome (2025). Titânio, 39 x 39 mm, automático H1837 (50 h), segundos com ponta laranja, 100 m.")
a("H08 Titane Bleu Saint-Cyr (2025)","","https://monochrome-watches.com/2025-sporty-chic-hermes-h08-returns-in-titanium-bleu-saint-cyr-review-price/","Visto na Monochrome (link do artigo). Titânio, luneta de cerâmica preta, números e ponteiros azul Saint-Cyr, 39 x 39 mm, automático H1837, 100 m.")
a("Slim d'Hermès (2015) – aço","","https://monochrome-watches.com/wp-content/uploads/2015/09/Slim-dHermès-Time-Only-Watch-3.jpg","Foto e dados da Monochrome (2015). Aço, 39,5 mm, calibre automático H1950 com micro-rotor (2,6 mm), tipografia de Philippe Apeloig.")
CC="Visto só em anúncio da CollectorSquare (link do anúncio). "
a("Clipper","CL6.710","https://a.1stdibscdn.com/mens-hermes-clipper-stainless-steel-watch-cl6710-for-sale/1121189/j_87492811581147962248/8749281_master.jpg?width=768","Foto da 1stDibs. Aço, 36 mm, quartzo, data, safira, anos 1990.")
a("Clipper Grande Date H1","CP1.710","https://a.1stdibscdn.com/auth-hermes-watch-clipper-grande-date-h1-ss-croco-strap-new-for-sale/v_42492/v_304397721788795640331/v_27282142_1757020392735_bg_processed.jpg?width=240","Foto da 1stDibs. Aço, 44 mm, automático, pulseira de aligátor preta.")
a("Nomade","","https://a.1stdibscdn.com/hermes-nomade-mens-37mm-uncommon-auto-quartz-watch-stainless-steel-for-sale/j_43332/j_293710421778509985561/j_29371042_1778509985600_bg_processed.jpg?width=240","Foto da 1stDibs. Aço, 37 mm, quartzo automático (autoquartz), início dos anos 2000.")
a("Pullman","PU2.210","https://a.1stdibscdn.com/genuine-hermes-pullman-stainless-steel-25mm-round-clipper-quartz-watch-silver-for-sale/j_41232/j_270598621754629011609/j_27059862_1754629012603_bg_processed.jpg?width=240","Foto da 1stDibs (anúncio sem referência); referência vista na CollectorSquare. Aço, 25 mm, quartzo, anos 1990.")
a("Clipper Diver Lady","","https://a.1stdibscdn.com/hermes-clipper-ladies-quartz-divers-watch-stainless-steel-for-sale/j_43332/j_296657921781626163531/j_26764942_1751904433485_bg_processed.jpg?width=240","Foto da 1stDibs. Aço, quartzo, início dos anos 2000.")
a("Clipper Lady – mostrador de madrepérola","","https://a.1stdibscdn.com/hermes-clipper-ladies-quartz-watch-with-mother-of-pearl-dial-stainless-steel-for-sale/j_43332/j_293409721778167157432/j_29340972_1778167157471_bg_processed.jpg?width=240","Foto da 1stDibs. Aço, quartzo, mostrador de madrepérola.")
a("Clipper Chronographe Quartz","","https://a.1stdibscdn.com/hermes-clipper-mens-ladies-unisex-chronograph-quartz-watch-stainless-steel-for-sale/j_43332/j_294054821778774776347/j_29405482_1778774776387_bg_processed.jpg?width=240","Foto da 1stDibs. Aço, cronógrafo a quartzo, início dos anos 2000.")
a("Cape Cod Automatique 41 mm – pulseira Double Tour","","https://a.1stdibscdn.com/archivesE/upload/j_37762/j_312585521794495292937/57a8355d-bb57-4cd6-a087-2c85b506f8e7/1794495278040_u308_1035736_1_bg_processed.jpeg?width=240","Foto da 1stDibs. Aço, 41 mm, automático.")
a("Carré Ashe","T12.710","https://a.1stdibscdn.com/archivesE/upload/j_13003/j_310983521793672861141/a6c1e746-5fee-4edd-b1b0-c91b836372c8/image_2_bg_processed.png?width=240","Foto da 1stDibs. Aço, 38 mm, automático, mostrador cinza-escuro com números arábicos.")
a("Ponteiro único (vintage, anos 1950)","","https://a.1stdibscdn.com/archivesE/upload/j_41232/j_303265721787854479672/657edd35-fa9a-435b-97a7-a9103c7e0f8f/1787854460461_u239_946835_1_bg_processed.jpeg?width=240","Foto da 1stDibs. Aço, mostrador preto, corda manual, c. anos 1950.")
a("Heure H Mini Double Tour","","https://a.1stdibscdn.com/hermes-stainless-steel-h-mini-double-tour-20mm-for-sale/j_9323/j_298913921783717763511/j_29891392_1783717763687_bg_processed.jpg?width=240","Foto da 1stDibs. Aço, 20 mm, quartzo, mostrador branco, pulseira de duas voltas.")
a("Clipper Automatique","CP2.810","https://www.analogshift.com/cdn/shop/files/AS10023_40992121_HERMES_CLIPPER_CP2.81AS10023_40992121_HERMES_CLIPPER_CP2.810-7.jpg?v=1726102343&width=500","Foto da Analog/Shift. Aço, 39 mm, automático, mostrador prateado, data.")
a("Clipper Chrono","CL1.910","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper-chrono/hermes-clipper-chrono-in-stainless-steel-ref-hermes-cl1-910-circa-2000-427657.html",CC+"Aço, c. 2000.")
a("Clipper","CL6.430","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper/hermes-clipper-watch-in-stainless-steel-ref-cl6-430-circa-2000-304685.html",CC+"Aço, c. 2000.")
a("Clipper","CL5.210","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper/hermes-clipper-watch-in-stainless-steel-ref-cl5-210-circa-2000-370507.html",CC+"Aço, c. 2000.")
a("Clipper","CC1.220","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper/hermes-clipper-watch-in-stainless-steel-and-gold-plated-ref-cc1-220-circa-1990-370750.html",CC+"Aço e banho de ouro, c. 1990 (referência como no anúncio).")
a("Clipper","CL4.285","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper/hermes-clipper-watch-in-18k-yellow-gold-ref-cl4-285-circa-2000-344085.html",CC+"Ouro amarelo 18k, c. 2000.")
a("Clipper","CL7.710","https://www.collectorsquare.com/en/watches/hermes/clipper/hermes-clipper--wristlet-watch-watch-in-stainless-steel-ref-cl7-710-circa-2000-335518.html",CC+"Aço, c. 2000.")
a("Clipper Chrono","CL2.315","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper-chrono/hermes-clipper-chrono-in-stainless-steel-ref-hermes-cl2-315-circa-2000-425104.html",CC+"Aço, c. 2000.")
a("Clipper Chrono","CL1.321","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper-chrono/hermes-clipper-chrono-in-stainless-steel-and-gold-plated-ref-hermes-cl1-321-circa-2000-424100.html",CC+"Aço e banho de ouro, c. 2000.")
a("Clipper Chrono","CL2.916","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper-chrono/hermes-clipper-chrono-watch-in-stainless-steel-ref:-cl2.916-circa-2000-321080.html",CC+"Aço, c. 2000.")
a("Clipper Chronographe","CL2.915","https://www.collectorsquare.com/en/watches/hermes/clipper/clipper-chrono/hermes-chronographe-clipper-in-stainless-steel-ref-:-cl2.915-circa-2010-265623.html",CC+"Aço, c. 2010.")
a("Cape Cod Automatique","CD7.810","https://www.analogshift.com/cdn/shop/files/AS10229_40992197_HERMES_CAPECODMEN_CD7.810-5.jpg?v=1743176571&width=500","Foto da Analog/Shift. Aço, 33 mm, automático, mostrador cinza com data às 6, fundo transparente, c. 2023.")
a("Cape Cod","W059599WW00","https://www.the1916company.com/pre-owned/hermes/cape-cod/5043397/","Visto só em anúncio da The 1916 Company (link do anúncio).")
a("Médor","ME1.201","https://www.collectorsquare.com/en/watches/hermes/medor/medor/hermes-medor-watch-gold-plated-ref-hermes-me1-201-circa-1990-435120.html",CC+"Banho de ouro, c. 1990.")
a("Médor","ME1.250","https://www.collectorsquare.com/en/watches/hermes/medor/medor/hermes-medor-watch-in-silver-ref-me1-250-circa-2000-330927.html",CC+"Prata, c. 2000.")
TRR="Visto só no título de anúncio da The RealReal (link da página da lista). "
for n in ["Clipper Power Reserve","Croisière","Klikti","Profile","Windsor","Kelly Lock","Faubourg Manchettes","Cape Cod Chaîne d'Ancre Joaillier","Arceau Petite Lune Ciel Étoilé","Clipper Chrono Maxi","Rallye","Slim d'Hermès – Hermès × Hodinkee, edição limitada","Médor – edição limitada","Cape Cod TGM"]:
    a(n,"","https://therealreal.com/designers/hermes/watches",TRR)
P="Visto só em artigo de imprensa (link do artigo). "
for n,u,e in [
("Arceau Lift Tourbillon","https://watchesbysjx.com/2013/10/presenting-the-first-flying-tourbillon-from-hermes-the-arceau-lift-with-specs-and-price.html","Primeiro turbilhão voador da Hermès, 2013."),
("Arceau Lift Tourbillon Répétition Minutes","https://watchesbysjx.com/2020/09/hermes-arceau-lift-tourbillon-minute-repeater.html","Peça única, 2020."),
("Dressage L'Heure Masquée","https://watchesbysjx.com/2014/03/baselworld-2014-introducing-the-hermes-dressage-lheure-masquee-a-dual-time-zone-with-a-secret-hour-hand-with-specs-and-price.html","Dois fusos, ponteiro de horas escondido, 2014."),
("Arceau Cheval d'Orient","https://watchesbysjx.com/2014/10/hermes-introduces-french-lacquer-dials-with-the-arceau-cheval-dorient-with-pricing.html","Mostrador de laca francesa, 2014."),
("Slim d'Hermès Quantième Perpétuel (2015)","https://watchesbysjx.com/2015/06/hands-on-with-the-slim-dhermes-perpetual-calendar-plus-original-photos-price.html","Calendário perpétuo, 2015."),
("Slim d'Hermès Cheval Ikat","https://watchesbysjx.com/2019/12/slim-d-hermes-cheval-ikat.html","2019."),
("Slim d'Hermès Astrologie Nouvelle","https://watchesbysjx.com/2019/12/hermes-astrologie-nouvelle-pegase-paysage-watch.html","Mostrador de marchetaria de madeira, 2019."),
("Slim d'Hermès Pégase Paysage","https://watchesbysjx.com/2019/12/hermes-astrologie-nouvelle-pegase-paysage-watch.html","Mostrador de marchetaria de madeira, 2019."),
("Slim d'Hermès Les Zèbres de Tanzanie","https://watchesbysjx.com/2018/10/hermes-leather-marquetry-watches.html","Mostrador de marchetaria de couro, 2018."),
("Arceau Cavales","https://watchesbysjx.com/2018/10/hermes-leather-marquetry-watches.html","Mostrador de marchetaria de couro, 2018."),
("Arceau Robe du Soir","https://www.ablogtowatch.com/hermes-arceau-robe-du-soir-cavales-slim-dhermes-les-zebres-de-tanzanie-watches/","2018."),
("Arceau 78","https://watchesbysjx.com/2018/12/hermes-arceau-78.html","Lançado no SIHH 2019; 40 mm, aço com luneta de titânio, quartzo (anúncio da 1stDibs)."),
("Arceau Cheval Cosmique","https://www.watchadvice.com.au/4792/2020-hermes-arceau-cheval-cosmique-released/","2020."),
("Arceau Wow","https://www.watchadvice.com.au/12840/hermes-horloger-arceau-wow/","2023."),
("Slim d'Hermès Minuit au Faubourg","https://www.watchadvice.com.au/11975/hermess-slim-dhermes-minuit-au-faubourg/","2022."),
("Arceau Grand Tralala Brides et Mors","https://revolutionwatch.com/hermes-arceau-grand-tralala-brides-et-mors/","2024."),
("Arceau Mon Premier Galop","https://revolutionwatch.com/hermes-arceau-mon-premier-galop/","Cavalo pintado e bordado no mostrador, 2024."),
("Arceau Duc Attelé","https://revolutionwatch.com/hermes-arceau-duc-attele/","Turbilhão central e repetição de minutos; o relógio mais complicado da Hermès até então, 2024."),
("Arceau Cheval Fusion","https://revolutionwatch.com/twin-peaks-hermes-arceau-squelette-and-arceau-cheval-fusion/","2020."),
("Arceau Cavalier en Formes","https://monochrome-watches.com/introducing-hermes-arceau-cavalier-en-formes-tourbillon-minute-repeater-gianpolo-pagni-specs-price-pics/","Turbilhão e repetição de minutos, desenho de Gianpaolo Pagni."),
("Arceau Belles du Mexique","https://www.ablogtowatch.com/new-release-hermes-arceau-belles-du-mexique-watches/","2023."),
("Arceau Chrono Titane","https://www.ablogtowatch.com/hermes-arceau-chrono-titane-watch/","Titânio, 2017."),
("Clipper Diver H1 200 m","https://www.ablogtowatch.com/i-admit-it-i-have-a-weakness-for-fashion-brands-and-the-release-of-the-2008-hermes-clipper-200m-diver-watch-does-not-help/","2008."),
("Clipper Chronographe Automatique (2010)","https://www.ablogtowatch.com/hermes-clipper-automatic-chronograph-watch-for-2010/","2010."),
("Sertie Neige","https://www.ablogtowatch.com/hermes-sertie-neige-ladies-watch/","Feminino, cravejado, 2010."),
("Slim d'Hermès GMT (2018)","https://www.ablogtowatch.com/hermes-slim-d-hermes-gmt-watch/","2018."),
("Hermès Cut Le Temps Suspendu","https://www.ablogtowatch.com/new-release-hermes-cut-le-temps-suspendu-watch/","2025."),
("Arceau Art (2025)","https://www.ablogtowatch.com/new-release-hermes-arceau-art-watches/","2025."),
("H08 Chronographe","https://wornandwound.com/hermes-expands-their-h08-collection-with-sleek-new-three-handers-and-an-impressive-chronograph/","2023."),
("H08 fibra de vidro Bleu de Malte","https://monochrome-watches.com/hermes-h08-bleu-de-malte-and-blanc-chantilly-glass-fibre-case-editions-2026-review-price/","Caixa de fibra de vidro, 2026."),
("H08 fibra de vidro Blanc Chantilly","https://monochrome-watches.com/hermes-h08-bleu-de-malte-and-blanc-chantilly-glass-fibre-case-editions-2026-review-price/","Caixa de fibra de vidro, 2026."),
("Cape Cod Titane Automatique (2026)","https://monochrome-watches.com/2026-hermes-cape-cod-titanium-automatic-review-price/","Titânio, automático, 2026."),
("Arceau L'Heure de la Lune – mostradores de meteorito, lápis-lazúli e pérola azul","https://www.ablogtowatch.com/herm%d1%90s-arceau-lheure-de-la-lune-watch-in-new-meteorite-lapis-and-blue-pearl-dials/","2020."),
("Slim d'Hermès L'Heure Impatiente","https://monochrome-watches.com/hermes","Complicação 'hora impaciente'."),
("Heure H Double Jeu","https://en.worldtempus.com/article/watches/trends-and-style/hermes-heure-h-double-jeu-26359.html","Visto no título do artigo da Worldtempus."),
]:
    a(n,"",u,(("Peça única. "+P+e) if "Peça única" in e else P+e))
D1b="Visto só no título de anúncio da 1stDibs (link da página de busca). "
for n,e in [("Carrick","Aço e ouro 18k, automático (também versão feminina e banhada a ouro)."),("Glissade","Ouro amarelo 18k, 20 mm, quartzo, 2003."),("Pursang Dame","Ouro 18k, anos 1990."),("Ruban","Ouro amarelo 18k, 26 a 33 mm, quartzo."),("Mors","Ouro amarelo e branco 18k, anos 1970."),("Loquet Clic-Clac","Metal dourado e esmalte, bracelete rígido."),("Barenia Ronde","Pulseira de couro.")]:
    a(n,"",D1,D1b+e)
