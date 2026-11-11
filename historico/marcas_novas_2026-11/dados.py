# -*- coding: utf-8 -*-
"""Dados das marcas novas (10/11/2026). Gera novas.json para inserir na aba Marcas."""
import json

CAMBIO = "Câmbio aproximado usado no preço médio: US$ 5,5 | € 6,1 | £ 7,2 | CHF 6,6 | SEK 0,55 | AUD 3,6 | AED 1,5 | INR 0,065."
BASE = "Incluída a pedido do usuário em 10/11/2026 (lista de marcas novas). Só a aba Marcas; relógios ainda não pesquisados."
PEND = ("Incluída a pedido do usuário em 10/11/2026 (lista de marcas novas). DADOS PENDENTES: o site oficial não foi localizado "
        "nesta sessão (a busca na web não retornou a marca, e o Instagram só abre pelo navegador do computador). "
        "Preencher a partir do link da bio do Instagram. Só a aba Marcas; relógios ainda não pesquisados.")

def faixa(p):
    if p is None: return None
    for n, lim in enumerate((1000, 5000, 10000, 20000, 40000, 70000, 100000, 350000, 600000), start=1):
        if p <= lim: return n
    return 10

M = []  # lista de marcas
def add(nome, pais=None, cidade=None, carac=None, preco=None, site=None, ig=None, hist=None, modelos=None, logo=None, obs=""):
    M.append({"A": nome, "B": pais, "C": cidade, "D": carac, "E": faixa(preco), "F": preco, "G": site, "H": ig,
              "I": hist, "J": modelos, "K": logo, "L": None,
              "M": (BASE if hist else PEND) + ((" " + obs) if obs else "") + ((" " + CAMBIO) if preco else "")})

# ---------------------------------------------------------------- com dados
add("1977", "França", "Ernolsheim-lès-Saverne",
    "Marca premium criada pela Pierre Lannier na Alsácia: automáticos em aço 904L com calibre France Ébauches, edições limitadas numeradas e o selo Origine France Garantie.",
    10535, "montres1977.com", None,
    "O nome é uma data: 1977 foi o ano em que Jean-Paul e Béatrice Burgun fundaram a Pierre Lannier, em Ernolsheim-lès-Saverne, na Alsácia. A ideia nasceu em 2022, quando a casa comemorou 45 anos com um relógio fabricado na França, vendido a 1.977 euros. Em 2023, o projeto virou uma marca própria, voltada ao segmento premium, sob a direção de Pierre Burgun, filho dos fundadores.\n\n"
    "A proposta é reunir o máximo possível de fabricação francesa. Os relógios são montados nos ateliês alsacianos da Pierre Lannier e usam um calibre automático da France Ébauches, feito em Maîche, no Doubs. A caixa é de aço 904L, o vidro é de safira e o fundo traz uma citação gravada.\n\n"
    "Segundo a marca e a Francéclat, a 1977 é a única marca de relógios com a certificação Origine France Garantie. As coleções têm nomes de pessoas — Edmond, Arsène e Roxane —, saem em séries limitadas e numeradas, com o ano gravado, e têm 10 anos de garantia.",
    "Edmond — automático de 40 mm, aço 904L, calibre France Ébauches FE1977-11 (44 h), 50 m, séries de 99 peças numeradas; cores azul, verde, preto, salmão, bordô e azul glacial; 1.677 €\n\n"
    "Arsène — cores azul, verde e laranja; 1.777 € (1.677 € com pulseira de borracha FKM)\n\n"
    "Arsène Edition Limitée — mostrador preto, 1.877 €; versão Carbone Forgé, 27 exemplares, 1.777 €\n\n"
    "Roxane — coleção feminina",
    None,
    "Marca achada pelo link enviado pelo usuário (montres1977.com, Edmond azul ref. 1977P01166). H vazio: Instagram oficial não confirmado. K vazio: logo não encontrado na página. Fontes: montres1977.com; international.franceclat.fr/brands-timepieces/1977; lejournaldesentreprises.com.")

add("Adriatica", "Suíça", "Minusio",
    "Marca suíça de preço acessível, quase toda a quartzo e com muitos modelos dourados, fabricada no Ticino e muito popular na Polônia e no Leste Europeu.",
    1650, "adriaticawatches.ch", "@adriatica_official",
    "Pouca gente fora do Leste Europeu conhece a Adriatica, mas na Polônia ela é quase sinônimo de relógio suíço acessível. A marca foi criada em 1931 pela Swiss Watch Company e tem ligação histórica com a Montilier Watch Co., fundada em 1852 perto de Morat. Em 1962, a fábrica foi para Biel/Bienne e Basileia, onde a produção se concentrou em relógios clássicos folheados a ouro.\n\n"
    "Foi nessa época que marinheiros começaram a levar os relógios para a Polônia, e a marca se espalhou pela região. A família Swiderski é dona da empresa desde 1991, segundo o diretor Thomas Swiderski disse à Europa Star. Desde o fim dos anos 1990, a produção é da PR&A Watch Sagl, no Ticino — primeiro em Dongio, hoje em Minusio.\n\n"
    "Na mesma entrevista, a empresa informou que cerca de 70% dos relógios custam entre 200 e 300 francos suíços e que 95% usam movimento a quartzo. A Adriatica é membro da Federação da Indústria Relojoeira Suíça desde 2006.",
    "Linha masculina — Tourbillon, Diving, Aviation e Portofino\n\nLinha feminina — Precious, Essence, Sophia e Milano\n\nAdriatica World Champion — coleção masculina citada no material de imprensa",
    "https://adriaticawatches.ch/themes/oak/assets/img/logo_adr.png",
    "Preço médio pela entrevista à Europa Star (70% das vendas entre CHF 200 e 300). Fontes: adriaticawatches.ch/en/content/6-history; europastar.com/1004088056.html; en.wikipedia.org/wiki/Adriatica.")

add("Aenigma Watches", "Itália", "Vale de Aosta", "Marca italiana do Vale de Aosta conhecida pelo SubX Monte Bianco, um relógio de mergulho em homenagem ao Monte Branco.",
    None, None, "@aenigma.watches.official",
    "A Aenigma vem do Vale de Aosta, a região alpina no noroeste da Itália, aos pés do Monte Branco. É dessa montanha — o pico mais alto dos Alpes, com 4.810 metros, na fronteira entre a Itália e a França — que saiu o relógio mais conhecido da marca, o SubX Monte Bianco.\n\n"
    "O sucesso do modelo levou a uma parceria com a também italiana Out Of Order: a edição OOO x Aenigma SubX Mont Blanc, limitada a 20 peças. Os fundadores e o ano de criação não foram encontrados em fonte pública nesta pesquisa.",
    "SubX Monte Bianco — relógio de mergulho em homenagem ao Monte Branco\n\nOOO x Aenigma SubX Mont Blanc Limited Edition — colaboração com a Out Of Order, 20 peças",
    None,
    "Dados parciais: só a página da colaboração com a Out Of Order foi lida (outoforderwatches.com/pages/ooo-x-aenigma). C traz a região (Vale de Aosta), não a cidade. G vazio: site oficial não localizado (aenigmawatches.com e .it não abrem). Fundadores, ano e preços a pesquisar.")

add("Aevig", "Holanda", "Roterdã (região)",
    "Microbrand holandesa de um só designer, com relógios-ferramenta de inspiração vintage dos anos 1950 a 1970 e mostradores de desenho gráfico próprio.",
    3580, "aevig.com", "@aevig",
    "Aevig quer dizer \"eterno\" em nórdico antigo, e a ideia de Chip Yuen era fazer relógios que não saíssem de moda. Nascido e criado na Holanda, com formação em artes e design industrial, ele descobriu o fórum Watchuseek ao pesquisar uma compra, desenhou dois relógios de projeto para a comunidade e, em 2013, abriu a própria marca.\n\n"
    "A estreia veio com dois modelos em pré-venda: o Huldra, um mergulhador automático de caixa-barril no estilo dos anos 1970, e o Corvid, um relógio de campo a quartzo. Depois vieram o Valkyr e o Balaur, um mergulhador de duas coroas com luneta interna que tinha começado como projeto do fórum em 2012.\n\n"
    "Hoje o catálogo tem também o Thor, de corda manual, e a linha Thule. A imprensa especializada costuma destacar o cuidado gráfico dos mostradores e os preços contidos para o nível de acabamento.",
    "Huldra — mergulhador automático de 200 m, caixa-barril, 599 €\n\nThule GMT — 699 €; Thule sportswatch — 549 €\n\nThor — social de corda manual, 499 €\n\nBalaur — mergulhador de duas coroas com luneta interna\n\nCorvid — relógio de campo (a quartzo na estreia, depois automático)\n\nValkyr — esportivo de aço",
    "https://aevig.com/wp-content/uploads/2015/03/Aevig-dot-logo-new.png",
    "Fontes: aevig.com; wornandwound.com/introducing-aevig-watches; thetimebum.com; watchpaper.com; chronofactum.com (cita a região de Roterdã).")

add("Aevum", "Japão", "Osaka",
    "Microbrand de um homem só, voltada a quem gosta de carros: relógios de titânio ultraleves e pulseiras de couro feitas à mão com desenho de banda de pneu.",
    None, "aevumtime.com", "@aevumtime",
    "A Aevum é obra de uma pessoa só: Bryan Farquharson, que leva para os relógios a experiência técnica do automobilismo. A marca nasceu no Canadá, com o Apex — nome tirado do ponto de tangência de uma curva de pista —, e se mudou para o Japão; o site hoje aponta Osaka e descreve os relógios como feitos à mão, numa garagem, para entusiastas de carros.\n\n"
    "As pulseiras de couro são cortadas, tingidas e costuradas pelo próprio Bryan, com um padrão que imita a banda de rodagem de um pneu. A linha atual é dominada por automáticos de titânio \"Super-lite\" e inclui colaborações com a Garage Hira e com a finlandesa Ando.",
    "Type-00 Titanium Automatic e Type-00 Super-lite Titanium GMT\n\nType-01 Super-lite Titanium Automatic\n\nType-02 Turbo Fan Titanium Automatic e Aevum x Ando Turbo Fan Super-lite\n\nAevum x Garage Hira Ippin Fordite Titanium Automatic e Garage Hira Overspray Monocompax\n\nThe Pure Ti, The Touge Racer e Advance Carbon Limited\n\nApex — primeiro modelo, da fase canadense",
    None,
    "E/F vazios: o site não mostrou os preços atuais na leitura automática (o Apex custava CAD 298–348 na estreia). K vazio: logo não encontrado. Fontes: aevumtime.com; carlthompson.co.uk (2024); watchpaper.com (review do Apex).")

add("Aft and Anchor Watch Co", "USA", "Mansfield (Texas)",
    "Marca texana de relógios de mergulho automáticos com nomes tirados da gíria da Marinha dos EUA, lançada com uma Founder Edition de 100 peças numeradas.",
    4120, "aftandanchorwatchco.com", "@aft_and_anchor",
    "Jason e Amber Huston criaram a Aft and Anchor em Mansfield, no Texas, com uma estreia de tiragem fechada: a Founder Edition soma 100 relógios numerados individualmente, divididos em quatro cores, e a marca avisa que eles serão aposentados em definitivo quando esgotarem.\n\n"
    "Os modelos são mergulhadores automáticos, e os nomes vêm do vocabulário da Marinha americana: 13 Buttons, Dixie Cup, Goat Locker e Salt & Steel. Cada um custa 749 dólares. O ano de fundação não aparece no site.",
    "13 Buttons Founder Edition — US$ 749\n\nDixie Cup Founder Edition — US$ 749\n\nGoat Locker Founder Edition — US$ 749\n\nSalt & Steel Founder Edition — US$ 749\n\n(100 peças numeradas no total, nas quatro cores)",
    "https://aftandanchorwatchco.com/cdn/shop/files/ChatGPT_Image_Jul_1_2026_06_27_13_PM.png?height=80&v=1782948513",
    "A ligação dos nomes com a gíria da Marinha dos EUA é leitura minha dos nomes dos modelos; conferir no site. Fonte: aftandanchorwatchco.com.")

add("ÁIGI", "Noruega", None,
    "Microbrand norueguesa nascida acima do Círculo Polar Ártico, com desenhos inspirados na luz do Ártico e nas estações de satélite do país, a preços acessíveis.",
    2480, "aigitime.com", "@aigitime",
    "ÁIGI significa \"tempo\" na língua do povo sámi, os indígenas do norte da Escandinávia. A marca foi fundada em 2017, acima do Círculo Polar Ártico, por três noruegueses apaixonados por relógios — Aleksander, Daniel e Christopher —, com a meta de oferecer acabamento de alto nível a um preço acessível.\n\n"
    "Todo o desenho é feito na Noruega, e a produção, no exterior, com aço inoxidável, vidro de safira e movimentos suíços ou japoneses. Os temas vêm do norte: o Satellite Ground Station tem o mostrador inspirado nas antenas de satélite e radar norueguesas e uma caixa no estilo dos relógios de pulseira integrada dos anos 1980.\n\n"
    "O Arctic GMT foi lançado por financiamento coletivo em 2023. O triângulo do logo e o lema \"Your Time Is Now\" acompanham todas as coleções, que saem em edições numeradas.",
    "Satellite Ground Station II — 39 mm, Miyota 9039, 100 m; a partir de US$ 479 no lançamento (versão dourada US$ 540 no site)\n\nArctic GMT — lançado no Kickstarter em 2023; US$ 560\n\nArctic Tide – Polar Night — US$ 865\n\nArctic Chrono II – Panda — US$ 360\n\nArctic Diver\n\nNorthern Lights e Glacier Rectangular — US$ 180 a 200",
    "https://aigitime.com/cdn/shop/files/Sort_logo_280x20_5e30903c-612c-455b-868b-431832fec8fb.png?v=1673348796&width=360",
    "C vazio: o site só diz 'acima do Círculo Polar Ártico, na Noruega'. Fontes: aigitime.com/pages/about-us; oracleoftime.com/aigi-satellite-ground-station-ii; masterhorologer.com (Arctic GMT).")

add("AIM Watches", "Emirados Árabes Unidos", "Dubai",
    "Relógios desenhados nos Emirados e fabricados na Suíça que levam dentro uma peça certificada de avião reaproveitada — de um Spitfire, de um A380 ou do Concorde.",
    29470, "aimwatches.com", "@aim.watches",
    "Cada relógio da AIM carrega um pedaço de avião de verdade. A marca, sediada em Dubai, reaproveita peças certificadas de aeronaves e as incorpora aos relógios, que são desenhados nos Emirados Árabes Unidos e fabricados na Suíça.\n\n"
    "As séries levam o nome dos aviões de origem: a LEGENDS Edition usa material de um Supermarine Spitfire, a ALPHA Series vem do Airbus A380 e a SUPERSONIC, anunciada como \"em breve\", do Concorde. Fundadores e ano de criação não aparecem na página inicial do site.",
    "LEGENDS Edition with Supermarine Spitfire — AED 14.140\n\nALPHA Series with A380 — AED 11.936\n\nSUPERSONIC Concorde — AED 32.869 (anunciado, em breve)",
    "https://aimwatches.com/cdn/shop/files/aim_logo_header_1.png?v=1790517503&width=5376",
    "Fundadores e ano não encontrados (a página 'about' não abriu). Fonte: aimwatches.com.")

add("Aion Watch", "Itália", None,
    "Relógio italiano de fibra de carbono impresso em 3D, com estrutura interna em colmeia patenteada e menos de 50 gramas com a pulseira.",
    None, "aionwatch.com", "@aion_watch",
    "A Aion faz um relógio que sai de uma impressora 3D. A marca italiana usa a tecnologia FDM com PLA reforçado com fibra de carbono e uma estrutura interna em colmeia, que ela diz ser patenteada. O resultado é uma caixa de cerca de 36 gramas — o relógio completo, com a pulseira, fica abaixo de 50 gramas.\n\n"
    "O modelo se chama Puro Elemento e está na terceira geração (MK3), \"realizzato in Italia\" segundo o site. Os fundadores, a cidade e o ano de criação não estão publicados na página.",
    "Puro Elemento MK3 — caixa de fibra de carbono impressa em 3D (FDM), cerca de 36 g",
    "https://static.wixstatic.com/media/7403ca_60cdc8f2b5ba48579ed17aef61bd0bab~mv2.png",
    "C, E e F vazios: o site não informa a cidade nem o preço (só fala em 'preço de lançamento'). Fonte: aionwatch.com.")

add("Alato", "Suécia", "Öjersjö (Gotemburgo)",
    "Microbrand sueca dos arredores de Gotemburgo, de um só designer, com automáticos de estética de engenharia em edições limitadas.",
    3390, "alato.se", "@alatoklockor",
    "A Alato nasceu de uma demissão. Pierre, o dono e designer, trabalhava como gerente de projetos na construção civil sueca e perdeu o emprego numa crise do setor; contou isso num fórum de colecionadores ao apresentar o primeiro desenho. Resolveu então aplicar o método de gerente de projetos a um relógio próprio, e registrou a marca ALATO, palavra que ele diz ter um significado pessoal.\n\n"
    "A empresa fica em Öjersjö, nos arredores de Gotemburgo. O site se apresenta como design sueco independente, de inspiração na engenharia, com movimentos mecânicos e edições limitadas. É o próprio Pierre quem responde aos clientes.\n\n"
    "O modelo mais comentado é o Arvet (\"herança\", em sueco), de 38 mm. A marca já apareceu no Micro-Brand Digest da Worn & Wound e está no diretório de marcas da Time+Tide.",
    "Arvet Automatic — 38 mm, 100 m; a partir de SEK 6.497\n\nTimescope Automatic — 39,8 mm, 100 m; a partir de SEK 7.499\n\nÖgonsten — 38 mm, 100 m; a partir de SEK 4.490",
    "https://www.alato.se/cdn/shop/files/ALATO_Logo_Footer.jpg?v=1764970446&width=760",
    "O site mostra 'SINCE 1990', sem explicar; não usei essa data como fundação da marca de relógios (a verificar). Sobrenome do fundador não encontrado. Fontes: alato.se/en; trustpilot.com/review/www.alato.se; watchcrunch.com (perfil Psalato).")

add("Alba", "Japão", "Tóquio",
    "Marca de entrada da Seiko Watch Corporation, com relógios a quartzo simples e baratos, linhas de personagens e a série RIKI, do designer Riki Watanabe.",
    None, "alba.jp", None,
    "A Alba é a marca de entrada da Seiko: relógios simples, a quartzo e de preço baixo, vendidos principalmente no Japão e em outros mercados da Ásia. Ela pertence à Seiko Watch Corporation, que mantém o site oficial da marca.\n\n"
    "O catálogo japonês se divide em linhas. A RIKI continua o trabalho do designer Riki Watanabe, com relógios de leitura fácil e desenho limpo. Há também a feminina ingenu, a ALBA QUARTZ, a linha CHARACTER, de personagens, e cronômetros esportivos.",
    "RIKI — linha do designer Riki Watanabe\n\ningenu — linha feminina\n\nALBA QUARTZ\n\nCHARACTER — relógios de personagens\n\nSTOP WATCH — cronômetros esportivos",
    "https://www.alba.jp/resources/img/logo.png",
    "A verificar (não confirmado em fonte aberta nesta sessão): ano de lançamento (costuma-se citar 1979) e a cidade (Tóquio é a sede da Seiko). H vazio: Instagram oficial não confirmado. E/F vazios: o site não mostrou preços. Fonte: alba.jp.")

add("Albedo Watches", "Holanda", "Horst",
    "Marca holandesa de venda direta com o lema \"Honest Horology\": safira e couro italiano de série, sem as margens do varejo tradicional.",
    2227, "albedowatches.com", "@albedowatches",
    "\"Honest Horology. No Compromises.\" é como a Albedo se apresenta. A marca foi fundada em 2022 em Horst, na Holanda, e conta que o criador ganhou a companhia do irmão, Sarkis, e do melhor amigo, Qais. A proposta é cortar as margens da indústria e entregar de série o que costuma ser opcional: vidro de safira e couro italiano de flor integral.\n\n"
    "A linha de entrada é a Solaris, um cronógrafo meca-quartzo com 100 metros de resistência à água, em três cores. O passo seguinte é o Albedo 1901, um cronógrafo mecânico em pré-venda.",
    "Albedo 1901 — cronógrafo mecânico, em pré-venda; 499,99 €\n\nSolaris Black, Blue e Silver — meca-quartzo, 100 m; 229,99 €",
    None,
    "O site não dá o nome do fundador. K vazio: logo não encontrado na leitura. Fonte: albedowatches.com.")

add("Alexandre Christie", "Indonésia", None,
    "Marca de grande volume, forte na Indonésia, com automáticos de movimento japonês, esqueletizados em titânio e a linha digital retrô AC Digi.",
    None, "alexandrechristie.com", "@alexandrechristieworld",
    "A Alexandre Christie diz ter mais de meio século de relojoaria. O catálogo é amplo e identificado por códigos \"AC\": há automáticos com movimentos japoneses, modelos esqueletizados como o AC 6295 em titânio, a linha digital unissex de ar retrô AC Digi e até um smartwatch, o AC Smart Gen 3.\n\n"
    "O site oficial não informa país, fundador nem ano na página inicial; a marca é conhecida sobretudo no mercado indonésio.",
    "AC 6295 MTR — automático esqueletizado em titânio\n\nAC 9205 MCR Carbon\n\nAC Digi — linha digital unissex de inspiração retrô\n\nAC Smart Gen 3 (AC S003) — smartwatch\n\nAC 2C42, AC 2377, AC 6680, AC 8714 — linhas sociais e esportivas",
    "https://alexandrechristie.com/cdn/shop/files/ac-logo-white.png?v=1768881903",
    "A verificar: país (Indonésia é o mercado principal e aparece só como indício no site), cidade, fundador e ano. E/F vazios: o site não mostrou preços. Fonte: alexandrechristie.com.")

add("Alkimos Watch Co.", "Austrália", None,
    "Microbrand da Austrália Ocidental com desenho marítimo inspirado no naufrágio do navio Alkimos, lançada com um GMT de 50 peças.",
    2516, "alkimoswatches.com.au", "@alkimoswatches",
    "O nome vem de um navio. O Alkimos naufragou na costa da Austrália Ocidental e seus destroços viraram referência local — e ponto de partida para o desenho marítimo desta microbrand australiana.\n\n"
    "O primeiro relógio é o Alkimos Ghostship GMT, uma edição limitada a 50 unidades, vendida a 699 dólares australianos. O site não informa a cidade, o fundador nem o ano de criação.",
    "Alkimos Ghostship GMT — edição limitada de 50 peças; AUD 699",
    None,
    "C vazio: o site não informa a cidade. K vazio: logo não encontrado. Fonte: alkimoswatches.com.au.")

add("Alp Watches", None, None,
    "Relógio automático de fibra de carbono que pesa 23 gramas, com calibre suíço desenvolvido pela Soprod.",
    None, "alpwatches.com", "@alp_watches",
    "O número que define a Alp é 23: é quanto pesa, em gramas, o ALP-1 — 27 gramas com a pulseira. A caixa é de fibra de carbono (a marca cita os materiais Carbon TSC e TFC) e o movimento é o AM1-S, um calibre automático Swiss made desenvolvido pela Soprod, com 40 horas de reserva de marcha.\n\n"
    "O relógio tem vidro de safira com tratamento antirreflexo na frente e no fundo e resiste a 45 metros. O site não informa país, fundadores nem preço na página inicial.",
    "ALP-1 Aurea — fibra de carbono, 23 g, calibre automático AM1-S (Soprod), 40 h, 45 m",
    None,
    "B, C, E e F vazios: o site não informa país, cidade nem preço na página lida. Fonte: alpwatches.com.")

add("Alpha-Leonis", "Suíça", "Vevey",
    "Marca suíça de Vevey, de venda direta sem intermediários, reconhecível pelo emblema de dupla lua crescente.",
    3557, "alpha-leonis.com", "@alpha.leonisgeneva",
    "A Alpha Leonis vende direto ao cliente, sem intermediários, e usa como emblema uma dupla lua crescente. O endereço da marca fica em Vevey, à beira do lago Léman, embora o perfil no Instagram leve o nome de Genebra.\n\n"
    "A coleção atual é a XR-72, com versões de nomes teatrais — Royal Blood, Frozen Majesty e Imperial Sand — e preços entre 507 e 597 francos suíços. O site não revela o nome do fundador nem o ano de criação.",
    "XR-72 Royal Blood — CHF 597\n\nXR-72 Frozen Majesty — CHF 512\n\nXR-72 Imperial Sand — CHF 507",
    "https://alpha-leonis.com/wp-content/uploads/2023/11/alphaleonis-logo.webp",
    "Fundador e ano não informados no site. Fonte: alpha-leonis.com.")

add("Alpharo", "Reino Unido", None,
    "Marca independente britânica que explora formas de caixa fora do padrão, com o lema \"Rethinking the shape of time\".",
    None, "alpharo.co.uk", "@alpharo_uk",
    "\"Repensar a forma do tempo\" é o lema da Alpharo, marca independente britânica da Alpharo Design Ltd. A proposta é misturar geometria, engenharia e imaginação para fazer relógios que fujam das convenções de formato.\n\n"
    "O primeiro relógio se chama simplesmente Model 1. O site não informa cidade, fundadores, ano nem preço na página inicial.",
    "Model 1 — primeiro relógio da marca",
    "https://alpharo.co.uk/cdn/shop/files/Alpharo_Full_Logo.svg",
    "C, E e F vazios: cidade e preço não informados na página lida. Fonte: alpharo.co.uk.")

add("Altanus Genève", "Itália", "Marcianise",
    "Marca de nome suíço e sede na Itália, com relógios acessíveis de estilo italiano: esqueletizados, de bolso, de mergulho e femininos finos.",
    2013, "altanus.com", "@altanus.geneve",
    "Apesar do \"Genève\" no nome, a Altanus tem sede em Marcianise, na província de Caserta, no sul da Itália, onde fica a Orologi Altanus Geneve S.r.l. A marca se apresenta como a união da relojoaria suíça com o estilo italiano.\n\n"
    "O catálogo é variado e de preço contido: relógios esqueletizados, modelos de bolso, mergulhadores e femininos de caixa fina, quase todos entre 160 e 600 euros. O site não informa fundador nem ano de criação na página inicial.",
    "Scheletrico 7030 — 290 €\n\nDiver Sub 00117 — 550 a 600 €\n\nTasca 7995 — relógio de bolso, 160 €\n\nSlim Donna 16107 — 290 a 298 €",
    "https://altanus.com/wp-content/uploads/2019/06/logo-altanus-1.png",
    "Fundador e ano não informados na página lida. Fonte: altanus.com.")

add("Amaros", "França", "Paris",
    "Jovem marca francesa com ateliê em Paris, estreando com um GMT automático fino, de 11,85 mm, e 100 metros de resistência à água.",
    None, "amaros-watches.com", "@amaros_watches",
    "A Amaros é uma marca francesa recente — o site fala em cerca de três anos de história — com ateliê em Paris. O primeiro relógio é o L'Odyssée GMT, um automático de segundo fuso horário com caixa de 11,85 mm de espessura e resistência à água de 10 ATM.\n\n"
    "O segundo modelo, La Seconde, está anunciado como \"em breve\". Os fundadores e os preços não aparecem na página inicial.",
    "L'Odyssée GMT — automático com GMT, 11,85 mm de espessura, 10 ATM\n\nLa Seconde — anunciado, em breve",
    None,
    "E/F vazios: preço não informado na página lida. Fundadores e ano exato não informados. K vazio. Fonte: amaros-watches.com.")

add("Analog Watch Co.", None, None,
    "Relógios de materiais naturais: madeira, mármore, cortiça, vinho e até musgo e flores no mostrador.",
    787, "analogwatchco.com", "@analogwatchco",
    "Na Analog Watch Co., o material é o assunto. A marca faz relógios e acessórios com madeira, mármore, cortiça, vinho e flores: há o Botanist, com musgo de rena no mostrador, o Chardonnay, a linha de mármore preto e os modelos que combinam couro e madeiras como blackwood e makore.\n\n"
    "Os preços ficam em torno de 120 a 150 dólares, com envio para o mundo todo. O site não informa cidade, fundadores nem ano de criação.",
    "Leather & Blackwood — US$ 150\n\nMakore & Red Sanders — US$ 150\n\nBlack Marble Classic — a partir de US$ 145\n\nChardonnay — a partir de US$ 150\n\nBotanist (Green Reindeer Moss) — a partir de US$ 120",
    "https://cdn.shopify.com/s/files/1/1193/6186/files/official_analog_logo_2017.png",
    "B e C vazios: o site não informa o país nem a cidade (os preços são em dólares). Fonte: analogwatchco.com.")

add("Anders & Co Timepieces", "Suécia", "Marstrand",
    "Marca sueca da ilha de Marstrand, com relógios de pequenas tiragens, caixas de inspiração vintage e mostradores de cores vivas.",
    5838, "andersandcotimepieces.com", "@andersandcotimepieces",
    "Marstrand é uma ilha de veraneio na costa oeste da Suécia, e é de lá que vem a Anders & Co. A marca faz relógios em lotes pequenos, com caixas de inspiração vintage e mostradores de cores vivas, em quantidades bem limitadas.\n\n"
    "As linhas são numeradas: o AC1 é um cronógrafo, o AC2 Volcán tem versão automática e outra, mais cara, de corda manual, e o AC3 leva o nome Lago. O site não informa o fundador nem o ano de criação.",
    "AC1 Chronograph — SEK 5.900 a 7.490\n\nAC2 Volcán — SEK 5.700 a 6.700\n\nAC2 Volcán Manual Wind — SEK 18.950\n\nAC3 Lago",
    "https://andersandcotimepieces.com/cdn/shop/files/IMG_5939_1_copy.png?v=1741016332&width=1001",
    "Preço médio puxado para cima pelo AC2 Volcán Manual Wind (SEK 18.950); os demais ficam perto de SEK 6.500 (≈ R$ 3.600, faixa 2). Fonte: andersandcotimepieces.com.")

add("AndoAndoAndo Design", "Finlândia", "Helsinque",
    "Estúdio de design finlandês-japonês que une a praticidade finlandesa ao minimalismo japonês, com relógios automáticos e peças bem-humoradas como o Cassette Tape Watch.",
    None, "andoandoando.com", "@andoandoando_design",
    "\"A Finnish-Japanese Design Company\": a AndoAndoAndo, com escritório em Helsinque desde 2021, se define pela soma da praticidade finlandesa com o minimalismo japonês. É um estúdio de design, e os relógios dividem o catálogo com objetos como relógios-pingente e suportes modulares.\n\n"
    "Há uma linha séria de automáticos — A-1, A-2 e o A-1b Singa — e outra francamente divertida, com o UFO Watch, o Cassette Tape Watch e o Vintage Computer Automatic Watch. A marca também assinou uma colaboração com a Aevum, o Turbo Fan Super-lite.",
    "A-1 Automatic, A-2 Auto e A-1b Auto Singa\n\nUFO Watch — 38 mm\n\nCassette Tape Watch\n\nVintage Computer Automatic Watch",
    "https://andoandoando.com/cdn/shop/files/a_logo_web.jpg?v=1613565219",
    "E/F vazios: preços não mostrados na página lida. Fundador não informado. Fonte: andoandoando.com.")

add("anemoic.", None, None,
    "Marca em pré-lançamento, com o lema \"Take a part of me\"; a loja ainda não tem relógios publicados.",
    None, "anemoicwatches.com", "@anemoic.watches",
    "A anemoic. — escrita assim, com minúscula e ponto final — ainda está em pré-lançamento. O site traz a pronúncia do nome (\"an-uh-moy-ik\"), o lema \"Take a part of me\" e uma loja em libras esterlinas, mas sem nenhum produto publicado até a data da pesquisa. País, fundadores e modelos ainda não foram divulgados no site.",
    None,
    "http://anemoicwatches.com/cdn/shop/files/20250323_Anemoic_Master_Logo_bd411952-75c7-40f9-897b-b8818c42b5d9.png?v=1784488309",
    "Marca em pré-lançamento: loja sem produtos ('No products found'), moeda GBP (indício de Reino Unido, não confirmado). Voltar depois. Fonte: anemoicwatches.com.")

add("Apogee Watches", "Suíça", None,
    "Marca Swiss made que estreia com o Grand Lac: titânio grau 5 na caixa e na pulseira, cronômetro certificado COSC e 300 metros de resistência à água.",
    15180, "apogee-watches.com", "@apogeewatches",
    "A Apogee estreia com uma ficha técnica ambiciosa. O Grand Lac tem caixa e pulseira de titânio grau 5, movimento certificado como cronômetro pelo COSC, resistência à água de 300 metros e Super-LumiNova grau X1.\n\n"
    "O desenho é creditado a Sergio Di Renzo e a Nicolas, do canal francês Chroniquemontres. O relógio sai em quatro cores e foi oferecido em pré-venda por 2.100 francos suíços, com preço de tabela de 2.300.",
    "Grand Lac — titânio grau 5, COSC, 300 m; cores Arctic White, Crystal Black, Ocean Blue e Tobacco Sunburst; CHF 2.300 (pré-venda CHF 2.100)",
    "https://static.wixstatic.com/media/5df617_e3386cceb8ec49bcaedeb16a351dc534~mv2.png",
    "C vazio: cidade não informada. Fundadores e ano não informados. Fonte: apogee-watches.com.")

add("Apose", "França", None,
    "Relógios minimalistas concebidos, fabricados e montados na França, com assistência feita pelo mesmo relojoeiro que montou a peça.",
    16775, "apose.fr", "@apose.officiel",
    "\"Cada relógio é concebido, fabricado e montado na França\", afirma a Apose. A marca aposta num desenho minimalista e num detalhe raro de pós-venda: a assistência é feita pelo próprio relojoeiro que montou o relógio.\n\n"
    "O catálogo gira em torno do N°3, declinado em versões como Douz, Radial e Pur, em aço ou com detalhes em ouro rosa, além de uma variante de 37 mm. Os preços vão de 2.700 a 2.950 euros.",
    "N°3 Douz (Or Rose & Noir, Ardoise) — 2.700 €\n\nN°3 Radial (Vert cendré, Noir Intégral) — 2.700 a 2.800 €\n\nN°3 Pur (Indigo, Noir de jais) — 2.700 a 2.950 €\n\nN°3 37 mm — 2.800 €\n\nN°3-100 Or Rose & Champagne — 2.700 €",
    "https://static.wixstatic.com/media/88675a_c71076af63cc4236a98cd229c481578b~mv2.png",
    "C vazio: o site não mostra endereço. Fundadores e ano não encontrados (a página 'à propos' não abriu). Fonte: apose.fr.")

add("Aquatico", "Hong Kong", "Kwun Tong",
    "Marca de Hong Kong de relógios de mergulho e de piloto em bronze, titânio e aço, muitos com iluminação por tubos de trítio suíços Trigalight.",
    None, "aquaticowatch.com", "@aquaticowatch",
    "\"Curiosidade embutida em cada relógio\" é o lema da Aquatico, marca com endereço em Kwun Tong, Hong Kong. A inspiração declarada vem do mar, do céu e da natureza, e a marca gosta de combinar pedra e metal nos mostradores.\n\n"
    "O forte são os relógios de mergulho e de piloto em bronze, titânio e aço, vários deles com iluminação própria por tubos de trítio suíços Trigalight, que brilham sem precisar de carga de luz. O site organiza o catálogo por faixas de preço: até 300, 500 e 1.000 dólares.",
    "Sea Recon Tritium, Ocean Diver Tritium e Sea Sentinel Tritium\n\nBronze Star (Tritium e Dive) e Super Bronze Tritium\n\nStorm Bay Full Bronze\n\nSuper Marine, Sea Raider e Bronze Raider\n\nHorizon Hawk — piloto\n\nAtlas Tritium, Ironblock Tritium, Steel Man e Dolphin Dive",
    None,
    "E/F vazios: a página não lista os preços (só as faixas até US$ 300, 500 e 1.000). Fundador e ano não informados. K vazio. Fonte: aquaticowatch.com.")

add("Aragon", "USA", None,
    "Relógios grandes e robustos de venda direta, com automáticos de mergulho, edições com mostrador de meteorito e até um turbilhão central.",
    None, "aragonwatch.com", "@aragonwatch",
    "A Aragon vende direto ao consumidor relógios grandes e de construção pesada. O catálogo vai do mergulho profissional ao exótico: o Virtuoso Titanium 9015 tem válvula de hélio e resiste a 1.000 metros, o Sea Charger Meteorite é uma edição limitada com mostrador de meteorito e o Divemaster Central Tourbillon LE leva um turbilhão ao centro do mostrador.\n\n"
    "O site não informa fundador, ano nem endereço na página inicial.",
    "Virtuoso Titanium 9015 Automatic — válvula de hélio, 1.000 m\n\nSea Charger Meteorite Automatic — edição limitada, mostrador de meteorito\n\nDivemaster Central Tourbillon LE",
    None,
    "A verificar (não confirmado em fonte aberta nesta sessão): país (USA, Flórida), fundador (Wing Liang) e a origem como Android Watch. E/F vazios: preços não mostrados. K vazio. Fonte: aragonwatch.com.")

add("Arcange Watches", "França", None,
    "Marca francesa de relógios com mostrador setorial e preço único, que acaba de passar ao movimento automático.",
    3935, "arcange-watches.com", "@arcangewatches",
    "\"Uma visão contemporânea da relojoaria francesa\": é assim que a Arcange se define. A marca trabalha com mostradores setoriais — aqueles divididos em anéis e faixas, típicos dos anos 1930 — em releitura atual, e a coleção mais recente adota movimento automático.\n\n"
    "Os três modelos em catálogo custam o mesmo, 645 euros: AS01 Polar Grey, AS03 Field e AS04 Paros Blue. Uma matéria de imprensa ligada no site menciona Reims, mas a cidade da marca não está confirmada.",
    "AS01 Polar Grey — 645 €\n\nAS03 Field — 645 €\n\nAS04 Paros Blue — 645 €",
    "https://arcange-watches.com/cdn/shop/files/logo-site.png?v=1751964086&width=1191",
    "C vazio: cidade não confirmada (um link de imprensa cita Reims). Fundadores e ano não informados. Fonte: arcange-watches.com.")

add("Arcus Watches", "Canadá", "Calgary",
    "Dupla de engenheiros canadenses que modifica movimentos por conta própria para criar complicações incomuns a preço acessível, como um cronógrafo monopulsante abaixo de mil dólares.",
    2954, "arcuswatch.com", "@arcus_watches",
    "A Arcus existe para fazer \"complicações relojoeiras únicas a preços acessíveis\". A marca de Calgary, no Canadá, é obra de dois engenheiros que pegam movimentos de prateleira e os modificam por conta própria — coisa rara entre as microbrands.\n\n"
    "O cartão de visitas foi o Tropos, um cronógrafo de corda manual com roda de colunas, baseado no Seagull ST19 e transformado em monopulsante (calibre AR-01), por menos de mil dólares; segundo a Watch Clicker, ele não chegou à produção. Veio então o Mesos, com uma função de leitura intermediária (start/read/reset), a US$ 475 e US$ 599 na versão monopulsante.\n\n"
    "Depois, o Exos Traveler trouxe ponteiro de horas saltante para viagens, e o site atual destaca o ExoStop.",
    "Mesos — cronógrafo Seagull ST19 modificado; US$ 475 (US$ 599 na versão monopulsante)\n\nTropos — cronógrafo monopulsante, calibre AR-01; não chegou à produção\n\nExos Traveler — horas saltantes para troca de fuso\n\nExoStop — modelo em destaque no site",
    None,
    "Preço médio pelos valores do Mesos na resenha da Watch Clicker (o site atual não mostrou preços). Nomes dos fundadores não encontrados. K vazio. Fontes: arcuswatch.com; wornandwound.com (Tropos e Mesos); watchclicker.com (Mesos e Exos Traveler).")

add("Arena Timepieces", "USA", None,
    "Marca americana de relógios-ferramenta mecânicos Swiss made com movimento Sellita, feitos para ambientes exigentes.",
    None, "arenatimepieces.com", "@arena_timepieces",
    "A Arena Timepieces, dos Estados Unidos, faz relógios-ferramenta mecânicos suíços pensados para ambientes exigentes, com foco em durabilidade, precisão e desenho funcional. O movimento é da Sellita.\n\n"
    "O modelo de estreia se chama The Vanitas. O site não informa cidade, fundadores, ano nem preço na página inicial.",
    "The Vanitas — relógio-ferramenta mecânico com movimento Sellita",
    None,
    "C, E e F vazios: cidade e preço não informados na página lida. K vazio. Fonte: arenatimepieces.com.")

add("ARES Watch Co.", "USA", None,
    "Relógios de mergulho e de campo montados à mão no noroeste dos EUA, numerados um a um, com garantia vitalícia e assistência própria.",
    12375, "areswatches.com", "@areswatchco",
    "Na ARES, cada relógio é montado à mão, recebe número de série individual e sai com garantia vitalícia. A marca americana, fundada e dirigida por Matt, trabalha no noroeste dos Estados Unidos (Pacific Northwest) e faz a própria assistência técnica.\n\n"
    "As linhas são diretas: DIVER-1, de mergulho, e FIELD-1, de campo, em versões a quartzo e automáticas, além de um GMT de edição limitada. O modelo de maior destaque é o Diver-1 Jack Carr Limited Edition, ligado ao escritor americano, vendido a 2.250 dólares.",
    "Jack Carr Limited Edition Diver-1 — US$ 2.250\n\nDIVER-1 Quartz\n\nFIELD-1 Quartz e FIELD-1 Automatic\n\nGMT Limited",
    None,
    "Preço médio: só o Jack Carr LE tinha preço na página (US$ 2.250); os modelos a quartzo devem custar menos — rever E/F. Sobrenome do fundador e ano não informados. K vazio. Fonte: areswatches.com.")

add("Arima Watches", "Alemanha", "Ludwigsburg",
    "Relógio Swiss made pensado a partir da pulseira: elos em degraus, fecho que se ajusta sozinho em até 4 mm e caixa de 9,8 mm.",
    7920, "arimawatches.com", "@arimawatches",
    "A Arima começou pelo lugar onde quase todo mundo termina: a pulseira. Kokilan e Joshua Don Bosco desenharam primeiro um bracelete de elos em degraus, com um fecho que se ajusta sozinho em até 4 milímetros, e só então o relógio em volta dele, com caixa de 9,8 mm de espessura.\n\n"
    "A empresa de Joshua, a Arima Watches UG, fica em Ludwigsburg, na Alemanha, e o relógio é Swiss made. O modelo de estreia é o Ascent, limitado a 150 peças numeradas, por 1.200 francos suíços.",
    "Ascent — Swiss made, 150 peças numeradas, caixa de 9,8 mm, bracelete em degraus com fecho autoajustável; CHF 1.200",
    None,
    "Ano de fundação não informado. K vazio. Fonte: arimawatches.com.")

add("Arpiem Watches", "França", None,
    "Automáticos franceses em séries limitadas, cada um em homenagem a uma lenda do automobilismo, com mostradores de três camadas e botões coloridos.",
    3160, "arpiem.fr", "@arpiem_watches",
    "Arpiem se lê como \"RPM\", e o assunto é mesmo motor. A marca francesa de Vincent Repoux faz automáticos em séries limitadas, e cada série homenageia uma lenda do esporte a motor — um circuito, um piloto, uma época.\n\n"
    "O Tribute TSR 4 lembra o circuito de Reims-Gueux, e o Racematic TSR 2 leva o nome do piloto Bob Wollek. Os mostradores são de \"três camadas\" e os botões, coloridos. Os preços vão de 349 a 639 euros.",
    "Racematic TSR 2 \"Bob Wollek\" — 639 €\n\nRide & Drive Time Control Orange — 589 €\n\nOverspeed \"White Face\" — 495 €\n\nTribute TSR 4 \"Reims - Gueux\" — 349 €",
    "https://arpiem.fr/cdn/shop/files/LOGO_MONOPLACE_1500_X_1000_SANS_FOND_e300852c-61d1-4d5c-aa98-2d5acce3af8f.png",
    "A leitura 'Arpiem = RPM' é interpretação minha do nome; conferir. C vazio: cidade não informada. Ano não informado. Fonte: arpiem.fr.")

add("Asterisk Watches", "USA", None,
    "Marca da equipe criadora da Xeric: um \"parquinho\" para colaborações com artistas, com relógios de horas saltantes sobre a NASA, parques nacionais e Charley Harper.",
    1760, "asteriskwatches.com", "@asteriskwatches",
    "\"Um parquinho para aventuras artísticas\": a Asterisk é o projeto paralelo das mentes criativas por trás da Xeric, e serve para o que não cabe na marca principal — colaborações com artistas e temas ilustrados.\n\n"
    "Há relógios sobre a corrida espacial (Apollo 11 Moonwalk, Gemini 4 Spacewalk, Space Shuttle), sobre parques nacionais americanos (Arches, Gates of the Arctic, Hawaii Volcanoes, Olympic) e uma série com as ilustrações de Charley Harper. Vários modelos usam horas saltantes com movimento automático. Os preços ficam entre 275 e 395 dólares.",
    "Charley Harper Turtleneck Automatic — US$ 395\n\nSpace Shuttle Jump Hour Automatic — US$ 350\n\nHawaii Volcanoes e Olympic Sunset Jump Hour Automatic — US$ 350\n\nThe Next Chapter — US$ 295\n\nApollo 11 Moonwalk e Gemini 4 Spacewalk — US$ 275\n\nArches Day Night e Gates of the Arctic Caribou — US$ 275",
    "https://asteriskwatches.com/cdn/shop/files/Asterisk-Official-Logo.svg",
    "País pela ligação com a Xeric (EUA); o site da Asterisk não mostra endereço — conferir. Fonte: asteriskwatches.com.")

add("Aubliq", "Coreia do Sul", "Goyang",
    "Marca coreana de design (\"Better living, by design\") que vende caixas e suportes para relógios — não foram encontrados relógios próprios.",
    None, "aubliq.com", "@aubliq",
    "A Aubliq, de Goyang, na Coreia do Sul, trabalha com o lema \"Better living, by design\". Na loja do site, porém, os produtos são acessórios para quem coleciona relógios — caixas de guarda da linha \"ATTENTION\" e suportes de mesa —, além de um incensário. Não foi encontrado nenhum relógio de pulso da marca.",
    "Sem relógios próprios no site. Produtos: Watch Storage Box \"ATTENTION\" (US$ 613 a 753) e Watch Stand (US$ 159 a 165)",
    None,
    "ATENÇÃO: pelo site, a Aubliq vende acessórios (caixas e suportes), não relógios. Avaliar se deve ficar na planilha (critério: só marcas que fazem relógios). Fonte: aubliq.com/shop.")

add("Auctor Horologium", None, None,
    "Relógio social automático suíço com mostrador transparente em camadas e um disco de números que gira sob um ponteiro fixo.",
    4945, "auctorwatches.com", "@auctorwatches_official",
    "No Auctor Zen, quem se move são os números. O relógio social da Auctor tem um mostrador transparente em camadas e um disco giratório de algarismos que passa por um ponteiro fixo — o contrário do habitual.\n\n"
    "A caixa é de aço 904L com revestimento PVD dourado, o vidro é de safira abaulada (box) e o movimento é automático suíço. A edição é limitada, em duas cores, Éclat e Noire, a 899 dólares. O site não informa país nem fundadores na página inicial.",
    "Auctor Zen (Éclat e Noire) — automático suíço, aço 904L com PVD dourado, edição limitada; US$ 899",
    "https://www.auctorwatches.com/cdn/shop/files/auctor-watches-logo.png?v=1779545788&width=600",
    "B e C vazios: país e cidade não informados na página lida. Fonte: auctorwatches.com.")

add("Audaz Watches", "Hong Kong", None,
    "Relógios de mergulho profissionais e cronógrafos desenhados em casa, com mostradores de trítio, válvula de hélio e até 1.000 metros de resistência à água.",
    None, "audazwatches.com", "@audazwatches",
    "Audaz é \"ousado\" em latim. A marca opera e despacha de Hong Kong e se especializa em relógios de mergulho profissionais e cronógrafos de precisão, com caixas, mostradores, lunetas e pulseiras desenhados internamente.\n\n"
    "Os mergulhadores chegam a 1.000 metros de resistência à água, com válvula de escape de hélio e mostradores iluminados por trítio. Os movimentos vêm de ETA, Ronda, Seiko e Miyota. O site não informa fundador nem ano de criação.",
    "Tri-Hawk Tritium\n\nAbyss Diver\n\nPredator III\n\nSea Ranger GMT\n\nQuantum\n\nDash One",
    "https://www.audazwatches.com/cdn/shop/files/TRANSPARENT_BACKGROUND_410x.png?v=1731403820",
    "E/F vazios: preços não mostrados nas páginas lidas. Fonte: audazwatches.com (home e about-us).")

add("Audoin Watches", "Alemanha", "Berlim",
    "Marca berlinense de Florian Audoin, com um conceito incomum de dois fusos horários e tiragens minúsculas montadas à mão na Alemanha.",
    None, "audoinwatches.com", "@audoinwatches",
    "Florian Audoin fundou a marca que leva seu sobrenome em Berlim, em 2025. A ideia de partida é um conceito pouco convencional de dois fusos: a primeira série usa dois movimentos a quartzo no mesmo relógio e foi limitada a 10 peças.\n\n"
    "O segundo modelo, o Stromlinie Automatic, usa o Miyota 9015, e a primeira série de produção tem 15 peças — a versão prateada já esgotou. As caixas são de aço 316L com desenho próprio, os vidros são de safira e a montagem é feita à mão na Alemanha.",
    "Audoin 1st series — dois fusos com dois movimentos a quartzo, 10 peças\n\nAudoin Stromlinie Automatic — Miyota 9015, primeira série de 15 peças",
    None,
    "E/F vazios: o site não mostra preços. K vazio. Fonte: audoinwatches.com.")

add("AURA", None, None,
    "Relógios de moda de preço baixo com visual de luxo — esqueletizados, cronógrafos e retangulares —, vendidos direto pela internet.",
    897, "aura.watch", "@aura.watch",
    "A AURA promete relógios \"luxuosos, mas acessíveis\": aço inoxidável, vidro de safira e pulseiras de borracha FKM em modelos que custam entre 99 e 268 dólares, vendidos direto pelo site.\n\n"
    "O catálogo aposta em formatos conhecidos — um retangular de estilo tank, um esqueletizado, um cronógrafo — e em temas como o Memento Mori e o Dice. O site não informa país, fundadores nem ano de criação.",
    "Skeleton 002 — US$ 268\n\nChronograph 001 — US$ 238\n\nTank 'Noir' e Tank Élan — US$ 125 a 148\n\nDice — US$ 148\n\nMemento Mori — US$ 130\n\n1023 — US$ 148\n\nPolycarbonate — US$ 99",
    "https://aura.watch/cdn/shop/files/aura-logo-512.png?v=1673473873&width=160",
    "B e C vazios: país e cidade não informados na página lida. Fonte: aura.watch.")

add("Avarth", "Índia", "Mysuru",
    "Marca indiana de Mysuru com modelos de nomes em sânscrito e línguas indianas e preços de entrada.",
    757, "avarth.com", "@avarthwatches",
    "A Avarth vem de Mysuru, no estado de Karnataka, no sul da Índia, e batiza os relógios com palavras do repertório indiano: Eka, Dakshina, Shunya, Chandini, Jugalbandhi, Avanti, Waqt e Ashva.\n\n"
    "O Shunya traz a tecnologia que a marca chama de Lumebloc, pensada para iluminar a leitura no escuro. Os preços vão de cerca de 5.500 a 17.000 rúpias, e na data da pesquisa todos os oito modelos apareciam como esgotados. O site não informa fundadores nem ano de criação.",
    "Jugalbandhi — Rs. 16.975\n\nEka — Rs. 15.275\n\nDakshina — Rs. 14.725\n\nWaqt e Ashva — Rs. 10.990\n\nAvanti — Rs. 9.950\n\nShunya (Lumebloc) — Rs. 8.499\n\nChandini — Rs. 5.475 a 5.950",
    "https://avarth.com/cdn/shop/files/Logo_reversed_1.png?v=1791888905&width=114",
    "Fundadores e ano não informados. Fonte: avarth.com.")

add("Axon Watches", None, None,
    "Calendário completo, fase da lua e indicador de 24 horas sobre um Miyota modificado, com mostrador esmaltado, por 599 euros.",
    3654, "axonwatches.com", "@axon_watches_25",
    "\"Grandes complicações acessíveis a todos\" é a promessa da Axon. O relógio de estreia, o Origo, reúne fase da lua, indicador de 24 horas e calendário completo sobre um movimento Miyota da série 9 modificado, e ainda traz mostrador esmaltado.\n\n"
    "São duas versões, de mostrador preto e cinza, a 599 euros cada. As referências começam com MMXXV — 2025 em algarismos romanos. O site não informa país nem fundadores na página inicial.",
    "Axon Origo mostrador preto — ref. MMXXV.01.DR; 599 €\n\nAxon Origo mostrador cinza — ref. MMXXV.02.DR; 599 €",
    "https://images.squarespace-cdn.com/content/v1/6817342a4d47fc0e126a9602/5626be20-b35e-41aa-b0d6-962b41f59b4c/logos_no_bg.png",
    "H: o site indica @axon_watches_25; a lista do usuário tinha @axon__watches — conferir qual é o oficial. B e C vazios: país e cidade não informados. Fonte: axonwatches.com.")

add("Pierre Lannier", "França", "Ernolsheim-lès-Saverne",
    "Relojoeira familiar da Alsácia, uma das maiores marcas francesas de relógios acessíveis, com cerca de 400 mil peças por ano e boa parte da montagem feita na própria fábrica.",
    915, "pierre-lannier.com", None,
    "Não existe nenhum senhor Pierre Lannier. O nome foi escolhido pela sonoridade bem francesa por Jean-Paul e Béatrice Burgun, que fundaram a empresa em 1977, na Alsácia — segundo a Europa Star, na sala de jantar do casal. Os primeiros relógios eram montados no Haut-Doubs, com componentes franceses e movimentos a quartzo da France Ébauches.\n\n"
    "A empresa continua familiar e é dirigida por Pierre Burgun, filho dos fundadores, em Ernolsheim-lès-Saverne, no Bas-Rhin. Segundo o Journal des Entreprises, vende cerca de 400 mil relógios por ano, em 1.600 pontos de venda na França e em 60 países, com preço médio em torno de 150 euros; cerca de 60% da produção sai da fábrica alsaciana.\n\n"
    "Em 2022, para os 45 anos, a casa lançou um relógio fabricado na França, com movimento France Ébauches — o embrião da marca premium 1977, criada no ano seguinte.",
    "Eolia — coleção emblemática feminina, agora também com movimento automático\n\nPaddock — linha inspirada no automobilismo\n\nWeekend — linha masculina\n\n1977 — relógio dos 45 anos (2022), fabricado na França, 1.977 €; originou a marca 1977",
    None,
    "Marca achada pelo link enviado pelo usuário (é a dona da marca 1977). H vazio: Instagram oficial não confirmado. K vazio: logo não encontrado. Preço médio pela reportagem (≈ 150 €). Fontes: lejournaldesentreprises.com; europastar.com/1004114253.html; commeuncamion.com; pierre-lannier.com.")

# ---------------------------------------------------------------- pendentes (só nome + Instagram)
for nome, ig, extra in [
    ("Agapever Watches", "@agapeverwatches", ""),
    ("Alain Blanco", "@alainblancowatches", ""),
    ("Alanti Watches", "@alantiwatches", "Indício não confirmado: um agregador lista o modelo 'Abalone' a CAD 790 (possível marca canadense)."),
    ("Aleksandr Nesterenko", None, "Relojoeiro independente; conferir o critério (só entra se já fez relógio com o próprio nome)."),
    ("Aloha Timepieces", "@aloha.watch", ""),
    ("Alternative Symmetry", "@altsym", ""),
    ("Altura Watches", "@alturawatches_", "alturawatches.com abre vazio."),
    ("Amir Watch Company", "@amir.watch.co", ""),
    ("Angelo Del Mare", "@angelodelmareofficial", "angelodelmare.com existe, mas veio ilegível na leitura automática; abrir pelo navegador."),
    ("AOS Watches", "@aoswatches", ""),
    ("Aperture", "@aperture.watches", "Marca da Coreia do Sul (segundo a varredura do Instagram de 08/11)."),
    ("Apex Timeworks", "@apextimeworks", ""),
    ("Appella", None, "Marca suíça tradicional (a verificar: fundação em 1943). appella.ch e appella.com NÃO são da marca."),
    ("Arca Opus", "@arca.opus", ""),
    ("Arly Watch", "@arlywatch", ""),
    ("Armonian", "@armonianbrand", ""),
    ("Arthur Charles Watches", "@arthurcharleswatches", "arthurcharles.co.uk NÃO é da marca."),
    ("Artus Watches", "@artus.watches", ""),
    ("Asas Watches", "@asaswatches", ""),
    ("Astiegan Watches", "@astieganwatches", ""),
    ("Astra Watch", "@astra.kwt", "Pelo @, provavelmente do Kuwait (não confirmado)."),
    ("Atelier Esïol", "@atelieresiol", ""),
    ("Atelier Genesis Machine", None, "Estava na lista 'a confirmar' da varredura de 08/11 (perfil não deixa claro se é marca de relógio)."),
    ("Atmoss", "@atmoss.watches", "atmoss.com abre vazio."),
    ("Atomyx C-Watches", "@atomyxcwatches", ""),
    ("Attache Watches", "@attache_watches", "attachewatches.com é um site em russo, sem conteúdo legível; conferir se é a mesma marca."),
    ("Atypik Watches", "@atypikwatches", ""),
    ("AVAIL Watches", "@availwatches", ""),
    ("Avax Watches", "@avax_watches", ""),
    ("Averen", "@averenwatches", "averen.com NÃO é da marca (consultoria farmacêutica)."),
    ("Axiom", "@axiombarleduc", "Pelo @, de Bar-le-Duc, França (não confirmado). Estava na lista 'a confirmar' da varredura de 08/11."),
    ("Thomas Aubert", "@aubert.watch_artisan", "Relojoeiro independente; conferir o critério (só entra se já fez relógio com o próprio nome)."),
]:
    add(nome, ig=ig, obs=extra)


# ---- ajustes depois de abrir o Instagram pelo Chrome e o Microbrand Atlas (10/11/2026, noite)
EXCLUIR={"AOS Watches","Pierre Lannier"}   # AOS = Arthur Oskar Stampfli (já está na planilha); Pierre Lannier veio do link errado
M[:]=[x for x in M if x["A"] not in EXCLUIR]
def upd(nome,**kw):
    x=[m for m in M if m["A"]==nome][0]; x.update(kw)
P2="Incluída a pedido do usuário em 10/11/2026 (lista de marcas novas). DADOS PARCIAIS, tirados só da bio do Instagram e do Microbrand Atlas; história, modelos e preços ainda a pesquisar. Só a aba Marcas."
upd("Agapever Watches",B="Hong Kong",D="Microbrand de Hong Kong em pré-lançamento (início em 2025, \"coming soon\" no Instagram).",M=P2+" Sem site na bio.")
upd("Alain Blanco",D="Marca em pré-lançamento, com o lema \"One Watch, Infinite Emotions\".",M=P2+" Sem site na bio; país não informado.")
upd("Alanti Watches",B="Canadá",G="alantiwatches.com",D="Relógios de luxo moderno com mostradores de pedra natural, a pronta entrega.",M=P2+" País pelo Microbrand Atlas (Canada). O site não abriu na leitura automática. Um agregador lista o modelo Abalone a CAD 790.")
upd("Aloha Timepieces",B="USA",G="linktr.ee/alohawatches",D="\"Espírito aloha + precisão Swiss made\": relógios suíços de inspiração havaiana.",M=P2+" País pelo Microbrand Atlas (United States, listada como 'Aloha'). G é o Linktree da bio; achar o site próprio.")
upd("Alternative Symmetry",G="alt-sym.com",D="Relógio modular de construção dinâmica; a marca abrevia o nome como (A)LT|SYM.",M=P2+" País não informado na bio.")
upd("Altura Watches",D="Marca em pré-lançamento (\"precision in every detail\"), ainda só com lista de espera.",M=P2+" Sem site próprio: a bio leva a uma lista de espera (freewaitlists.com). Perfil com 7 posts.")
upd("Amir Watch Company",G="amirwatchcompany.com",D="Relógios inspirados na natureza, com foco em qualidade e versatilidade.",M=P2+" País não informado na bio.")
upd("Angelo Del Mare",B="Suíça",G="angelodelmare.com",D="Empresa relojoeira suíça desde 2011, com peças de coleção de alto padrão.",M=P2+" O site existe, mas veio ilegível na leitura automática; abrir pelo navegador.")

json.dump(M, open('/home/claude/trabalho/novas/novas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(M), 'marcas;', sum(1 for x in M if x['I']), 'com dados;', sum(1 for x in M if not x['I']), 'pendentes')
