#!/usr/bin/env python3
"""Lista as próximas marcas da aba Marcas, de cima para baixo, que AINDA NÃO têm
nenhum relógio na aba Relógios (pedido do usuário, 14/11/2026).

Uso: python3 proxima_marca.py planilha/Relogios_atualizada_NNN.xlsx [quantas=10]

Uma marca conta como "já feita" se o nome dela (coluna A da aba Marcas) aparece
na coluna A da aba Relógios, comparando sem acentos, maiúsculas, espaços e
pontuação, ou se está em APELIDOS abaixo (nome diferente nas duas abas).
"""
import sys, re, unicodedata, collections, openpyxl

# nome na aba Marcas -> nome usado na aba Relógios
APELIDOS = {
    "Victorinox Swiss Army": "Victorinox",
    "Zeno-Watch Basel": "Zeno Watch-Basel",
    "Cabot Watch Company": "CWC",  # mesma marca da linha CWC (82 relógios, v.  bateria CWC); 16/11/2026
}


# marcas com só uns poucos relógios que entraram de passagem: pesquisar normalmente
# (pedido do usuário, 14/11/2026). Os relógios que já existem ficam; a bateria nova
# não deve duplicá-los.
PESQUISAR_MESMO_ASSIM = {"Tiffany & Co.", "Urban Jürgensen", "Wyler", "ZRC 1904"}


# marcas adiadas: sem fontes suficientes para a trava (pular até o usuário decidir ou a marca lançar).
# Adiadas em 15/11/2026 (v622); notas em historico/notas_<marca>.md. Para voltar a pesquisar, tirar daqui.
ADIADAS = {
    "Eternal Watches": "eternalwatches.com.au não abre pela WebFetch (PROVENANCE) e não aparece em busca; fora dele só o Microbrand Atlas e a matéria do Daily Bhutan (coleções ET 087, ET 097, Royal Green, Royal Silver, Emerald, Thunder Dragon, quartzo, sem fotos por modelo); Firecrawl sem créditos (17/11/2026, v686) — refazer com Firecrawl no oficial",
    "Eulux": "não faz relógios: é a linha de pulseiras de couro da alemã Eulit (ver M da aba Marcas) (17/11/2026, v686) — usuário decide se fica na lista",
    "Ercigoj": "1 modelo só (Cornely: mostrador bordado sob encomenda, 50 peças, 40 mm, Sellita SW200-1b); ercigoj.com não abre pela WebFetch (PROVENANCE), watches.ercigoj.com não aparece em busca e o mundo só tem 3 fontes (WatchProSite, WatchTime promocional, metro-ruddy); Firecrawl sem créditos; notas em historico/notas_Stohlman_Ercigoj_Ergon.md (17/11/2026, v685) — refazer com Firecrawl no oficial (catálogo fechado)",
    "Ergon Watches": "1 modelo (Adventum: Midnight Black, Ocean Teal Fume, Full Lume White, 100 de cada, Miyota 9015) e um 1º modelo de bronze sem nome; ergonwatches.com não abre pela WebFetch (PROVENANCE) e só há 3 fontes (Fratello, WatchReport, Keep the Time); Firecrawl sem créditos; notas em historico/notas_Stohlman_Ercigoj_Ergon.md (17/11/2026, v685) — refazer com Firecrawl",
    "E. Stohlman Watch Co": "1 modelo (The Earl, 6 mostradores de 50 peças: Gray Rose, Star Burst, Chocolate, Black Enamel, Black e White Mother of Pearl); estohlman.com não abre pela WebFetch (PROVENANCE) e site:estohlman.com sem resultado; só ~4 fontes (The Time Bum, The Watch Preserve, WatchCrunch); Firecrawl sem créditos; notas em historico/notas_Stohlman_Ercigoj_Ergon.md (17/11/2026, v685) — refazer com Firecrawl no oficial (catálogo fechado)",
    "ETA": "usuário pediu em 04/11/2026 para tirar a ETA da tabela (não é marca de relógio); as linhas saíram na v434 — não refazer (registrado aqui em 17/11/2026, v685)",
    "eClock": "grande pelo catálogo (89 relógios individuais no site eclockmx.com, que abre); fora do site nada legível (Facebook/TikTok/YouTube bloqueados, nenhuma loja, imprensa ou agregador) e Firecrawl sem créditos — não chega às 25 fontes; lista pronta em historico/eclock_raw.txt e notas em historico/notas_eClock.md (17/11/2026, v682) — usuário decide se grava só com o site oficial",
    "EK Watch Co.": "ekwatchcompany.com não abre pela WebFetch (PROVENANCE), site:ekwatchcompany.com sem resultado e as buscas só trazem outras marcas nepalesas (Samaya, Alma Artes); Firecrawl sem créditos (17/11/2026, v682) — refazer com Firecrawl",
    "Earhart Watches": "earhartwatches.com não abre pela WebFetch (PROVENANCE), Firecrawl sem créditos e 8 buscas não trouxeram nenhuma página sobre a marca; notas em historico/notas_Earhart.md (17/11/2026, v681) — refazer com Firecrawl",
    "Drayton Watches": "draytonwatches.com não abre pela WebFetch (PROVENANCE), site:draytonwatches.com e buscas pela marca não trazem nada (só um espelho kreafolk sem conteúdo); Firecrawl sem créditos; aba Marcas cita DV-01 Anthracite Grey e DV-02 Burnt Orange/Forest Green (Seiko NH38) (17/11/2026, v680) — refazer com Firecrawl no oficial (catálogo fechado)",
    "Döttling": "não faz relógios (cofres de luxo e watch winders, desde 1919); a fase Marcas não achou nenhum relógio de pulso, bolso ou mesa da marca (adiada em 17/11/2026, v679) — usuário decide se fica na lista",
    "DeMarco Watches": "1 linha só (The Chronograph, Seiko VK64, 41 mm, US$ 329–499, ~10 cores: Black, Blue, Ice Blue, White, Salmon, Teal, Purple, Pistachio Green, Green, deconstructed preta); demarcowatches.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; o mundo só tem ~6 fontes (Worn & Wound, Watch Is This, Oracle of Time, WatchPatrol, metro-ruddy); Firecrawl sem créditos; notas em historico/notas_DeMarco.md (17/11/2026, v677) — refazer com Firecrawl no oficial (catálogo fechado)",
    "Cubli": "não é marca de relógios: robô em forma de cubo da ETH Zurique; 16 fontes abertas antes (historico/notas_Cubli.md) e nenhuma marca de relógio com esse nome (17/11/2026, v675)",
    "Crudo Carattere": "crudocarattere.pl não abre e não aparece em busca nenhuma; a busca \"Crudo Carattere\" só traz a marca alemã Crude e lojas italianas; Firecrawl sem créditos (17/11/2026, v675) — refazer com Firecrawl",
    "Coromandel": "coromandelwatchco.com não abre pela WebFetch (pede permissão), site:coromandelwatchco.com sem resultado e Firecrawl sem créditos; fora do site só citações sem modelos (New Indian Express, blog The Wired Mind: Varnam, Tanjore, Blue Mountain); 'Marina Edition' da J pode ser da Madras Watch Works; fontes em historico/parcial_Coromandel_fontes.txt (17/11/2026, v674) — refazer com Firecrawl",
    "Corso": "corsowatches.com.br não aparece em busca nenhuma e nenhuma fonte sobre a marca (só Citizen Corso e lojas de outras marcas) (17/11/2026, v674) — conferir se a marca ainda existe; refazer com Firecrawl",
    'Compass Timepieces': "11 relógios no site oficial (collections/all abre pela busca: Explorer Black/White, Gratitude Black/Gold, innerG, Pathfinder, Titan 2 Black/Navy Blue/White, Voyager Black/Gold e Silver), mas nenhuma fonte de fora cita os modelos (watchDNA, CanvasRebel, ShoppeBlack, VoyageLA só falam do fundador; shop.app client_error; X/Spotify bloqueados); sem 2 fontes externas (17/11/2026, v671; notas em historico/notas_Compass.md) — refazer quando houver imprensa ou lojas",
    'CLE-Time': "marca da joalheria Steven DiFranco (Willoughby, Ohio), vendida só lá; cletime.com: raiz PROVENANCE na 1ª tentativa, a home abriu pela busca mas sem nomes de modelos e a loja (cletime.com/store/) não aparece em busca; nenhuma loja, imprensa ou banco de dados fora do site; Firecrawl sem créditos (17/11/2026, v669) — refazer com Firecrawl na loja oficial (logo: cletime.com/__static/ogimage-.../cle-time-logo-jpg(3).jpg)",
    'Choosz': "choosz.com: raiz PROVENANCE; collections/mens abre pela busca (43 produtos, só 24 na pág. 1; ?page=2 e a coleção feminina não vêm em busca); nenhuma loja, imprensa ou banco de dados fora do próprio site; Firecrawl sem créditos; notas em historico/notas_bateria_v668.md (17/11/2026, v668) — refazer com Firecrawl (collections/all, products.json)",
    'ChronoDivers': "chronodivers.co.uk não abre pela WebFetch (PROVENANCE) e nenhuma busca traz a marca; Firecrawl sem créditos (17/11/2026, v668) — refazer com Firecrawl",
    "CEON Watch Co.": "1 modelo (GR-01: aço-ferramenta VC-150 de 38 mm, Peseux 7001, CHF 15.000, sob encomenda); ceonwatches.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; fora dele só a Monochrome (ago/2026) e cópias em sites-lixo; Firecrawl sem créditos (17/11/2026, v667; notas em historico/notas_bateria_v667.md) — refazer com Firecrawl no oficial (catálogo fechado)",
    "BVOR": "só 1 modelo (Vision: 42 mm, aço escovado/polido/PVD preto ou azul, mostrador ondulado azul ou preto, £599); bvorwatches.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; fora dele só BQ Watches e WatchPro, sem fotos por versão; Firecrawl sem créditos (17/11/2026, v664; notas em historico/notas_bateria_v664.md) — refazer com Firecrawl no oficial (catálogo fechado)",
    "BYOP Watches": "site oficial não achado em busca nenhuma; fora só Fifth Wrist (Avitimer, 2023) e 1 anúncio no eBay; J (Atlas) cita Meridian Ti GMT, Naviator Titanium Ghost GMT, Maverick, Aviator, Iceman (17/11/2026, v664) — refazer com navegador/Firecrawl",
    "Call Sign": "mycallsign.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; diretório metro-ruddy diz 15 modelos; achados 8 na Watch Gang (Discovery Series CSW-DC38-BL/-WH/-GL, CSW-DC42-BK/-WH; Wright Brothers Bishop CSW-WB-BSH 50 pç, Katharine CSW-WB-KAT 100, Brothers CSW-WB-BR 200) + The Gentleman Racer, AOPA, Aircraft Spruce (antigo nome Bravo Golf); só ~6 fontes; notas em historico/notas_bateria_v664.md (17/11/2026, v664) — refazer com Firecrawl",
    "Canister Watches": "1 modelo (Fieldmaster, 41 mm, Miyota 9015, 200 m; 2ª produção e peças sob encomenda sem detalhes); canisterwatches.com não abre pela WebFetch (PROVENANCE); só ~7 fontes (Fifth Wrist, The Calibrated Wrist, Worn & Wound digest fev/2024, SIGforum) (17/11/2026, v664) — refazer com Firecrawl no oficial (catálogo fechado)",
    "Canuck Timepieces": "canucktimepieces.com não abre pela WebFetch (PROVENANCE); fora dele só The Calibrated Wrist (Unity, Wormhole × AndoAndoAndo, The 4th Dimension) e Gear Patrol (17/11/2026, v664) — refazer com Firecrawl no oficial",
    "BSHQRF": "bshqrf.com não abre pela WebFetch (PROVENANCE) e as buscas só trazem outras marcas; Firecrawl sem créditos (16/11/2026, v662) — refazer com Firecrawl",
    "Burnt Creek Watch Company": "7 relógios no site (collections/all abre pela busca), mas fora dele só posts no X da própria marca; sem 2 fontes externas (16/11/2026, v662; notas em historico/notas_bateria_v662.md) — refazer quando houver imprensa ou lojas",
    "BUUR+": "buurwatches.com não abre pela WebFetch (PROVENANCE); só a Oracle of Time (2020) fala da marca (16/11/2026, v662) — refazer com Firecrawl",
    'Bryan Laurent': "marca lançada em abr/2026 por Bryan Ng (Cingapura); só o site oficial existe (bryanlaurent.com abre pela busca), nenhuma loja, imprensa ou fórum; categorias iris/ e guilloche/ dão client_error; ~20 modelos (Iris, Abyss, Metaleton, Silveleton, Guilloché em 8 cores, Stone, Opal, Swisseleton); notas em historico/notas_BryanLaurent.md (16/11/2026, v661) — refazer quando houver fontes de fora",
    'Bonest Gatti': 'grande (Hong Kong/China, dezenas de referências BG####); bonestgattiwatches.com não abre pela WebFetch (PROVENANCE), o domínio não aparece em busca e Firecrawl sem créditos; fontes vistas: jwlraddicts.com (BG9960, BG9902, BG5602), sometimeslab.hk (BG9010-L3), eBay, WatchCharts; notas em historico/notas_bateria_v658.md (16/11/2026, v658) — refazer com Firecrawl',
    'Borgward': 'borgward.ag não abre pela WebFetch (PROVENANCE) e não aparece em busca (só a montadora); fora dele só a WatchTime.net (B511 de 2011, Chronograph P100 de 2012); Firecrawl sem créditos (16/11/2026, v658) — refazer com Firecrawl',
    'Bragdur': 'bragdur.no não abre pela WebFetch (PROVENANCE) e nenhuma busca traz a marca (só 2 anúncios no Finn.no); Firecrawl sem créditos (16/11/2026, v658) — refazer com Firecrawl',
    'Branch Horology': '1 modelo (The Sector, mostrador setorizado prata/cinza, SW210-1, 36,5 mm); branchhorology.com não abre pela WebFetch (PROVENANCE) e o mundo só tem ~9 fontes (Time+Tide, The Calibrated Wrist, Watchclicker, WatchPatrol); sem o site não dá para usar o catálogo fechado (16/11/2026, v658) — refazer com Firecrawl no oficial',
    'Blacklist': 'blacklistwatches.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; Firecrawl sem créditos; fora dele só Watch Report (Streetmatic 2015, Phantom P2.1, Divematic 2020 com 9 variações sem nome), The Time Bum, reach.dog (Graphite Rhino DM4), Watch Gang e Massdrop, quase sem fotos por variante; nomes de J (Black Sunray, Stinger, Verde Ithaca, Laguna Seca, Glacier Bay) não aparecem em busca; notas em historico/notas_bateria_v657.md (16/11/2026, v657) — refazer com Firecrawl',
    'Blanchefontaine': 'não tem relógios com nome próprio publicados (fabricante de marca própria/private label em Bonfol; domínio expirado) (16/11/2026, v657) — usuário decide se fica na lista',
    'Blu': "provável duplicata da 'Bernhard Lederer (BLU)' (linha 184, já com relógios); nenhuma outra marca Blu de relógios identificada (fase Marcas, 14/11/2026; adiada em 16/11/2026, v657) — usuário decide se fica na lista",
    'Bobwellson': 'bobwellson.com não abre pela WebFetch (PROVENANCE) e site:bobwellson.com não traz nada; catálogo provavelmente grande (LordAtlantis, LordKraken, Capt. Hawk, Legion…); Firecrawl sem créditos (16/11/2026, v657) — refazer com Firecrawl',
    'Bōken': "boken.co.uk não abre pela WebFetch (PROVENANCE) e não aparece em busca; o mundo só tem ~5 fontes (Time+Tide, Oracle of Time, Kicktraq): Nomad (Arctic Frost, Ember Blaze, Midnight Sapphire, Solar Flare, Moonlight Onyx), Breacher (Time Only, GMT, Black Ops GMT) e a campanha 'The Odyssey' (quartzo) sem detalhes; notas em historico/notas_bateria_v657.md (16/11/2026, v657) — refazer com Firecrawl",
    "Beyond Boring": "beyondboringbrand.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; fora dele só lojas de terceiros sem fotos (Faire, Triathlete Store, Anglers Pro Tackle, reach.dog): ~8 cronógrafos/relógios de campo; notas em historico/notas_BeyondBoring.md (16/11/2026, v656) — refazer com Firecrawl",
    "Bezel": "nenhuma marca de relógios 'Bezel' identificada (só o marketplace Bezel/getbezel.com e o termo técnico); aba Marcas sem site, país nem Instagram (fase Marcas, 14/11/2026; adiada em 16/11/2026, v656) — usuário decide se fica na lista",
    "BlackCat": "blackcat-watches.com não abre pela WebFetch (PROVENANCE) e o mundo só tem ~13 fontes (The Watch Gallery, O'Clock Store, Dialicious): Shaka (Blue, Copper Black, Silver, Green, Purple) e Shura (Grey, Green, Purple); notas em historico/notas_BlackCat.md (16/11/2026, v656) — refazer com Firecrawl no oficial (catálogo fechado)",
    "Black Corner": "black-corner.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; fora dele só Ocarat e The Watch Gallery (linha Shadows × Anka: Marco Polo's Journey, Black Dynamite, Times Dwellers; Sailing Stones BC.26.0001.ST1); Wormhole e Neoma Star não achados; notas em historico/notas_BlackCorner.md (16/11/2026, v656) — refazer com Firecrawl",
    "BERNY": "grande (Shenzhen, centenas de referências); bernywatch.com não abre pela WebFetch (PROVENANCE), site:bernywatch.com sem resultado e Firecrawl sem créditos; notas em historico/notas_adiadas_BERNY_Berthet_Bespo.md (16/11/2026, v655) — refazer com Firecrawl (collections/all, products.json)",
    "Berthet": "berthet.com não abre pela WebFetch (PROVENANCE) e não aparece em busca; fora dele só a Time Transformed (5 modelos, 2016–2018); notas em historico/notas_adiadas_BERNY_Berthet_Bespo.md (16/11/2026, v655) — refazer com Firecrawl",
    "Bespo Watches": "bespowatches.com não abre pela WebFetch (PROVENANCE) e nenhuma busca traz a marca; notas em historico/notas_adiadas_BERNY_Berthet_Bespo.md (16/11/2026, v655) — refazer com Firecrawl",
    "Bellecour": "montres-bellecour.fr não abre pela WebFetch (PROVENANCE) e o domínio não aparece em nenhuma busca; fora dele só 1 relógio achado (Tête de Mort em aço, ETA 6497, loja 58 Facettes); 11 buscas sem resultado (Ocarat, eBay, Dalla Turca) (16/11/2026, v652) — refazer com Firecrawl (coleção Squelette do site: DM 1991, 1993, 1994, 1995, 1996, 3001)",
    "Baron Watch Company": "1 modelo só (Stargazer 1.0, Seiko NH35, 39 mm, US$ 260) e acessórios; baronwatch.co abre pela busca, mas fora do site só o Microbrand Atlas fala da marca (falta a 2ª confirmação externa para o catálogo fechado); Firecrawl sem créditos; notas em historico/notas_bateria_v651.md (16/11/2026, v651) — refazer quando houver mais fontes",
    "Avian Watches": "avianwatches.com: raiz PROVENANCE e quase todas as fichas client_error (só 2 abriram, sem fotos); Firecrawl sem créditos; ~11 variantes vistas só em títulos de busca (Genesis, Genesis X, Commodore 2020LE/2022OR/2024BR GMT, Solaris); notas em historico/notas_Avian.md (16/11/2026, v649) — refazer com Firecrawl",
    "Bahrami Watches": "bahramiwatches.com não abre pela WebFetch (PROVENANCE), site:bahramiwatches.com sem resultado e Firecrawl sem créditos; fora do site só a resenha do Ω-02 Eucalyptus Sport (Microbrand Watch World) e a ficha do CC - Persian Gulf (2 peças); notas em historico/notas_Bahrami_Bajer_adiadas.md (16/11/2026, v650) — refazer com Firecrawl",
    "Bajer Watches": "thebajer.com não abre pela WebFetch (PROVENANCE) e o domínio não aparece em busca; fora dele só Europa Star (coleções Urfa e Antep), The Cool Hour (Artemita) e Kurdistan Chronicle; notas em historico/notas_Bahrami_Bajer_adiadas.md (16/11/2026, v650) — refazer com Firecrawl",
    "Avax Watches": "aba Marcas vazia (só @avax_watches); a fase Marcas só achou a criptomoeda AVAX e outras marcas (14/11/2026; adiada em 16/11/2026, v648) — refazer com navegador",
    "Avel & Men": "não faz relógios (pulseiras de lona de vela e acessórios, Bretanha) (16/11/2026, v648) — usuário decide se fica na lista",
    "Averen": "aba Marcas vazia (só @averenwatches); nenhuma busca da fase Marcas achou a marca; averen.com é de outra empresa (14/11/2026; adiada em 16/11/2026, v648) — refazer com navegador",
    "Asas Watches": "aba Marcas vazia (só @asaswatches); asaswatches.com não abre e as buscas só trazem homônimos (fase Marcas, 14/11/2026; adiada em 16/11/2026, v645) — refazer com navegador",
    "Ash's Watches": "~6 modelos (VTOL, Living Color, Vanishing Point, Outrider, Gyre, Mirkwood); ashswatches.com não abre pela WebFetch (PROVENANCE) e nenhuma busca traz a marca (16/11/2026, v645) — refazer com Firecrawl (Shopify: products.json)",
    "Astiegan Watches": "é revendedora de relógios vintage suíços de outras marcas (Sierre), sem modelos próprios (16/11/2026, v645) — usuário decide se fica na lista",
    "Astra Watch": "aba Marcas vazia (só @astra.kwt); buscas só trazem homônimos (fase Marcas, 14/11/2026; adiada em 16/11/2026, v645)",
    "Atelier Esïol": "aba Marcas vazia (só @atelieresiol); buscas sem resultado (fase Marcas, 14/11/2026; adiada em 16/11/2026, v645)",
    "Atelier Genesis Machine": "aba Marcas vazia; não confirmado nem que é marca de relógio (fase Marcas, 14/11/2026; adiada em 16/11/2026, v645)",
    "Atmoss": "1 modelo (SR-01 Everyday Pilot: branco, preto, cinza-ardósia); projeto em pausa, sem site; só ~5 fontes no mundo (Time+Tide, Wrist Enthusiast, Worn & Wound) (16/11/2026, v645)",
    "Atomishine": "catálogo Shopify com ~14 coleções (Hydrocore, Eondate, Eondate Maxi, Velocirex, Technautic, Octaforma, Xenoflux, Illusion, Voidframe…); atomishine.com não abre pela WebFetch (PROVENANCE) e as buscas não trazem produtos (16/11/2026, v645) — refazer com Firecrawl (products.json)",
    "Atomyx C-Watches": "aba Marcas vazia (só @atomyxcwatches); fase Marcas não achou a marca (adiada em 16/11/2026, v645)",
    "Attache Watches": "attachewatches.com não abre pela WebFetch (PROVENANCE); só uma resenha russa (ixbt) aparece nas buscas (16/11/2026, v645) — refazer com Firecrawl",
    "Atypik Watches": "1 modelo (AT01, 25 peças); atypik.watch não abre pela WebFetch (PROVENANCE) e as buscas não trazem a marca (16/11/2026, v645) — refazer com Firecrawl",
    "Aubliq": "não faz relógios (só caixas e suportes para relógios) (16/11/2026, v645)",
    "Auctor Horologium": "1 modelo (Auctor Zen: Éclat e Noire); auctorwatches.com não abre pela WebFetch (PROVENANCE) e as buscas não trazem a marca (16/11/2026, v645) — refazer com Firecrawl",
    "Armonian": "aba Marcas quase vazia; armonian.com bloqueia leitura automática (robots) e nenhuma imprensa fala da marca (fase Marcas, 13–14/11/2026; adiada em 16/11/2026, v644) — refazer com navegador",
    "Artus Watches": "aba Marcas vazia; @artus.watches não ligado a site; artuswatch.ru (candidata) em loop de redirecionamento (fase Marcas, 14/11/2026; adiada em 16/11/2026, v644)",
    "Arion": "1 coleção (Delphinus: Ichthyian Silver, Aeolian Blue, Melian Pearl); artofarion.com não abre pela WebFetch (PROVENANCE) e só a Fratello e o Microbrand Atlas falam dela (16/11/2026, v644) — refazer com Firecrawl",
    "Arly Watch": "~13 modelos (Burgos, Leon, Logroño, Pamplona, Valença, Porto, Ponteferrada, Belorado); arlywatch.de não abre pela WebFetch (PROVENANCE) e o mundo só tem 2 fontes (Bruce's World of Watches, WatchTime.net) (16/11/2026, v644) — refazer com Firecrawl no oficial",
    "Arthur Charles Watches": "~8 modelos (Moonphase, Westminster, Chrono Prestige, Chrono Master); arthurcharleswatches.com não abre pela WebFetch (PROVENANCE) e nenhuma busca traz a marca (16/11/2026, v644) — refazer com Firecrawl (Shopify: products.json)",
    "Art Watch Gallery": "artwatchgallery.com não abre pela WebFetch (PROVENANCE) e as buscas só trazem homônimos (Swatch Art) (16/11/2026, v644) — refazer com Firecrawl",
    "Arima Watches": "1 modelo em pré-venda (Ascent, 5 mostradores: Slate, Moss, Fog, Dark Blue, Light Blue; Chronoscout cita também Night Sky e Ice); só ~3 fontes no mundo (arimawatches.com e llms.txt via busca, Chronoscout); blog de fabricação deu erro (16/11/2026, v643; notas em historico/notas_arima.md) — refazer quando lançar (entregas até ago/2027)",
    "ARC & Co.": "4 modelos (World Traveler 1ª versão, Black, Silver; Type Art-Deco ADA-01); arcandcowatches.com não abre pela WebFetch (PROVENANCE) e o mundo só tem ~9 fontes (Makuake, PR Times, Gizmodo/Lifehacker/Roomie) (16/11/2026, v641; notas em historico/notas_arc_co.md) — refazer com Firecrawl",
    "Arca Opus": "aba Marcas sem dados (só @arca.opus); as buscas de 13 e 14/11/2026 (fase Marcas) só trouxeram homônimos; Instagram bloqueado (adiada em 16/11/2026, v641)",
    "Arcus Watches": "6 modelos (Tropos, Mesos, Exos peça única, Exos Traveler roxo/azul, ExoStop); arcuswatch.com não abre pela WebFetch (PROVENANCE) e só há ~9 fontes (Worn & Wound, Watch Clicker, WatchPatrol) (16/11/2026, v641; notas em historico/notas_arcus.md) — refazer com Firecrawl",
    "Ardra Labs": "1 modelo (Delta Type, 2026); ardralabs.com não abre pela WebFetch (PROVENANCE) e só há ~5 fontes (SJX, Fratello, The Hour Markers) (16/11/2026, v641) — refazer com Firecrawl",
    "Arena Timepieces": "1 modelo (Vanitas); arenatimepieces.com não abre pela WebFetch (PROVENANCE) e só há ~3 fontes (Time+Tide, The Calibrated Wrist) (16/11/2026, v641) — refazer com Firecrawl",
    "Aft and Anchor Watch Co": "só o site oficial existe (4 relógios em pré-venda); sem fontes externas para a trava",
    "Agapever Watches": "pré-lançamento, sem site nem relógios publicados",
    "Alain Blanco": "pré-lançamento, só Instagram; nenhuma fonte com relógios (busca de 15/11/2026, v629)",
    "Alkimos Watch Co.": "só o site oficial existe (Ghostship GMT, 2 edições de 50, entrega fim nov/2026); nenhuma fonte externa (busca de 15/11/2026, v633)",
    "Aloha Timepieces": "1 modelo (GMT 40, 3 mostradores); só ~12 fontes no mundo e aloha.watch não abre pela WebFetch — refazer com Firecrawl no site oficial para usar o catálogo fechado (dados em historico/notas_bateria.md, v633)",
    "Alpharo": "só o site oficial (Model 1); alpharo.co.uk não abre pela WebFetch (PROVENANCE) e nenhuma busca trouxe loja ou imprensa (15/11/2026, v634) — refazer com Firecrawl",
    "Alp Watches": "1 modelo (ALP-1 Aurea, por reserva); alpwatches.com não abre pela WebFetch (PROVENANCE); só 2–3 matérias (quotidianomotori, gearpatrol) — refazer com Firecrawl no oficial para usar o catálogo fechado (15/11/2026, v634)",
    "Alpha-Leonis": "só o site oficial (XR-72 em 9 mostradores + XR-71); nenhuma fonte externa com a lista (busca de 15/11/2026, v633)",
    "Alternative Symmetry": "alt-sym.com não abre pela WebFetch (PROVENANCE) e nenhuma busca trouxe a marca (15/11/2026, v635) — refazer com Firecrawl",
    "Altura Watches": "pré-lançamento, sem site (só Instagram e lista de espera); buscas sem resultado (15/11/2026, v635)",
    "ALVION": "2 modelos; alvionwatches.com não abre pela WebFetch (PROVENANCE) e nenhuma busca trouxe a marca (15/11/2026, v635) — refazer com Firecrawl",
    "Amaros": "1–2 modelos; amaros-watches.com não abre pela WebFetch (PROVENANCE); só a The Watch Gallery na busca (15/11/2026, v635) — refazer com Firecrawl",
    "Amaux Boze": "amauxboze.com não abre pela WebFetch (PROVENANCE) e a busca não trouxe a marca (15/11/2026, v635) — refazer com Firecrawl",
    "Amir Watch Company": "pré-lançamento (Dragonfly 'em breve'); amirwatchcompany.com não abre pela WebFetch (PROVENANCE) (15/11/2026, v635)",
    "anemoic.": "pré-lançamento, 1 modelo (Versailles); anemoicwatches.com não abre pela WebFetch (PROVENANCE); só Worn & Wound e Fratello falam dela (15/11/2026, v636) — refazer com Firecrawl ou quando lançar",
    "Angelo Del Mare": "angelodelmare.com não abre pela WebFetch (PROVENANCE) e o mundo só tem ~6 fontes (Oceanic Time, Master Horologer, CronotempVs) — Royal Master e Royal Officer (15/11/2026, v636) — refazer com Firecrawl",
    "Ansley Watches": "ansleywatches.com não abre pela WebFetch (PROVENANCE) e as buscas só trazem diretórios (Design Ireland, DCCI, The Slender Wrist) (15/11/2026, v636) — refazer com Firecrawl",
    "Aperture": "aba Marcas sem dados (sem site/país) e nenhuma busca identificou a marca (15/11/2026, v636)",
    "Apex Timeworks": "aba Marcas sem dados e nenhuma busca identificou a marca (só Apex de outras marcas) (15/11/2026, v636)",
    "Apogee Watches": "apogee-watches.com fora das buscas (só aparece o Apogee da Bangalore Watch Co.) (15/11/2026, v636) — refazer com Firecrawl",
    "AURA": "aura.watch não abre pela WebFetch (PROVENANCE) e Firecrawl sem créditos; fora do site só nomes de ~30 variantes (Loox, EcomScout, Hypebeast) e 4 fotos; 17 fontes abertas, notas em historico/notas_AURA.md (16/11/2026, v647) — refazer com Firecrawl (collections/all, products.json)",
    "Autran & Viala": "autran-viala.com não abre pela WebFetch (PROVENANCE) e o domínio não aparece em nenhuma busca; fora dele só 2 matérias antigas da WatchTime (NightFlight, Aviator B) e a Massdrop (Eremitage); notas em historico/notas_Autran_Viala.md (16/11/2026, v647) — refazer com Firecrawl",
    "Audoin Watches": "2 modelos; audoinwatches.com não abre pela WebFetch (PROVENANCE) e nenhuma busca trouxe a marca (só Charles Oudin) (16/11/2026, v646) — refazer com Firecrawl",
}


def chave(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def main():
    arq = sys.argv[1]
    quantas = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    wb = openpyxl.load_workbook(arq, read_only=True)
    feitas = collections.Counter(
        chave(r[0]) for r in wb["Relógios"].iter_rows(min_row=2, max_col=1, values_only=True) if r[0]
    )
    linhas = [
        (i, r[0]) for i, r in enumerate(wb["Marcas"].iter_rows(min_row=2, max_col=1, values_only=True), 2) if r[0]
    ]
    sem = [(i, m) for i, m in linhas
           if m not in ADIADAS and (m in PESQUISAR_MESMO_ASSIM or feitas[chave(APELIDOS.get(m, m))] == 0)]
    print(f"marcas sem relógios: {len(sem)} de {len(linhas)}")
    for m, motivo in ADIADAS.items():
        print(f"(adiada: {m} — {motivo})")
    for i, m in sem[:quantas]:
        print(i, m)


if __name__ == "__main__":
    main()
