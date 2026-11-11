# -*- coding: utf-8 -*-
"""Lote 7 (11/11/2026): Microbrand Atlas, letras L e M (61 marcas). Sem história.
M2Z Watch ficou de fora: está na lista de nomes do Atlas, mas a ficha não abre e o índice /brands não a mostra mais."""
import sys
import lote_base
from lote_base import add, salvar
lote_base.CAMBIO["F"] = ("CHF", 6.5)
CHF = "Preço do Atlas em francos suíços (convertido a R$ 6,5)."

# ---------- L ----------
add("La Touraine", "la-touraine", "USA", "Charlotte (Carolina do Norte)", 2019, None, "Relógios neo-vintage de influência francesa com Miyota e Seagull.", None, "latourainewatches",
    "Heritage Racer Noir; E 503.95; Seagull ST1902 | Heritage Racer Phantom; E 503.95; Seagull ST1903 | Rally Chronograph; E 337.95; - | Oltre Field Watch; E 539.95; Miyota 9015 | Maritimer Happy Holidays 2026 Edition; E 128.95; -", "O Atlas dá os preços em euros.")
add("Lacite", "lacite", "Canadá", "Montreal", 2020, "Olivier e Frederic (sobrenomes não informados)", "Relógios GMT urbanos de uso diário com Miyota 9075.", "lacitewatches.com", "lacite.watches",
    "Urbanite GMT Slate Black; U 699; Miyota 9075")
add("Lamberti Orologiai", "lamberti-orologiai", "Itália", "Rovato", 1937, "Carlo Lamberti", "Relojoaria italiana de tradição familiar, com cronógrafos e automáticos Seagull ST19 e Seiko NH35.", None, "lambertiorologiaishop",
    "Ref. 18824V Damatic (feminino automático); E 390; Seiko NH35A | Mod. 26322 Vitruvio; E 480; calibre LO 638 | Mod. 26523G 50 ST (30 peças); E 480; Seiko NH35A | Mod. 50508G Chronodromo Velocimetro; E 590; Sea-Gull ST19 | Mod. 50508V Chronodromo Safari; E 580; Sea-Gull ST19 | Mod. 50508 NZ Chronodromo; E 580; Sea-Gull ST1901")
add("LaMotte Watch Company", "lamotte-watch-company", "USA", "Rancho Santa Margarita (Califórnia)", 2023, "Jonnie LaMotte", "Relógios sociais de inspiração clássica com movimentos americanos Americhron e mecaquartzo VK63.", None, None,
    "Balboa; U 895; Americhron 7000 | Shoreline; U 400; -")
add("LAPS", "laps", "França", "Paris", 2016, None, "Relógios minimalistas parisienses, a quartzo e com Miyota 9015.", "laps.fr", "laps_paris",
    "Prima Peacock Gold; U 234; quartzo | Signature Malick Sidibé; U 234; quartzo | Prima Popova; U 189; quartzo | Arche S02 Black; U 789; Miyota 9015 | Arche S01 Ivoire; U 789; Miyota 9015 | Arche S01 Green; U 789; Miyota 9015")
add("Le Pin Watches", "le-pin-watches", "Croácia", "Samobor", 2025, "Marko Šimonek e Karlo Šimonek", "Relógios clássicos minimalistas com Sellita SW261-1.", "lepinwatches.com", None,
    "Le Pin Automatic; U 1900; Sellita SW261-1")
add("Lebond", "lebond", "Espanha", "Barcelona", None, "Asier Mateo", "Relógios de arquitetos, desenhados em parceria com nomes como Álvaro Siza e Souto de Moura.", "lebondwatches.com", "lebondwatches",
    "Siza Black Edition; E 2700; - | Attraction Dark Edition; E 2400; - | Souto Moura Dark Edition; E 2700; - | Attraction Original Edition; E 2400; - | Siza Original Edition; E 2700; - | Souto Moura Original Edition; E 2700; -")
add("LEFF Amsterdam", "leff-amsterdam", "Holanda", "Almere", 2011, "Arno Ruijzenaars, Dennis Ruijzenaars e Erwin Termaat", "Relógios minimalistas de design holandês (série Tube), a quartzo.", "leffamsterdam.com", "leffamsterdam",
    "Tube Watch S42; U 400; movimento suíço | Tube Watch S38; U 400; movimento suíço | Tube Watch T40; U 229; Miyota quartzo | Tube Watch T32; U 229; Miyota quartzo | D38; U 295; Miyota 2035")
add("Levenaig", "levenaig", "Suécia", "Gråbo", 2013, "Holme Finnilä", "Relógios mecânicos suecos de linhas minimalistas com Sellita SW200.", "levenaig.com", "levenaig_watches",
    "Lost Sea 41 M; U 3200; Sellita SW200")
add("Lèrin", "l-rin", "Dinamarca", "Slagelse", 2023, None, "Cronógrafos mecaquartzo de desenho contemporâneo com Seiko VK64.", "lerinwatches.com", "lerinwatches",
    "Hybrid Chronograph Mistral Black; U 227; Seiko VK64 | Hybrid Chronograph Espresso Brown; U 250; Seiko VK64 | Hybrid Chronograph Pine Green Rose Gold; U 250; Seiko VK64 | Hybrid Chronograph Obsidian Black; U 250; Seiko VK64 | Hybrid Chronograph Salmon; U 250; Seiko VK64 | Hybrid Chronograph Pine Green Steel; U 250; Seiko VK64")
add("Libertas Watch Co.", "libertas-watch-co", "Brasil", "Belo Horizonte (Minas Gerais)", 2024, None, "Microbrand mineira de inspiração histórica com automático NH35.", "libertaswatchco.com", "libertaswatchco",
    "The Conspirator; U 395; NH35")
add("Lilienthal Berlin", "lilienthal-berlin", "Alemanha", "Berlim", 2015, "Jacques Colman e Michael Gilli", "Relógios berlinenses de desenho modernista com Ronda e Sellita.", "lilienthal-berlin.com", "lilienthalberlin",
    "The Classic (2015); U 199; Ronda quartzo | Chronograph (2016); U 299; Ronda 3540.D | Zeitgeist Automatik (2018); U 819; Sellita SW200 | Huxley (2017); U 199; quartzo japonês | Neolux (2020); U 499; automático suíço | Lilienthal 1 (2015); U 249; Ronda quartzo")
add("Lineage Watch Co", "lineage-watch-co", "USA", "San Diego (Califórnia)", 2023, "Brianna Edwards e Evan Edwards", "Relógios de estilo americano com movimentos FTS Ameriquartz e Americhron montados nos EUA.", "lineagewatchco.com", "lineagewatchco",
    "Destiny; U 200; Ameriquartz 7320b | Destiny II; U 220; Ameriquartz 7320b | Limited Edition San Diego Gulls; U 165; Ameriquartz 7320b | Legacy; U 650; Americhron 7A20 | Legacy II; U 636; Americhron 7A20")
add("LOBOR", "lobor", "Hong Kong", "Hong Kong", 1989, "Kam Law Po", "Relógios automáticos neo-vintage acessíveis com Seagull e Miyota.", "lobor.com", "loborwatches",
    "Heritage Canterbury Brown; U 280; Seagull automático | Planetarium; U 240; automático esqueletizado | Cellini; U 230; Seagull automático | Belfry; U 310; Miyota automático | Dynasty; U 300; Miyota automático")
add("Loresum", "loresum", "Hong Kong", "Hong Kong", 2020, "Jason Chan", "Relógios esqueletizados modernos com mostradores de pedra, Miyota 9015 e Sellita SW200-1.", "loresum.watch", "loresumwatches",
    "LS04 Aventurine; E 950.95; Miyota 9015 com módulo de fases da lua | LS04 Black Mother of Pearl; E 950.95; Miyota 9015 | LS04 All Black; E 1354.95; Sellita SW200-1 | LS06 Tiger's Eye; E 592.95; HZ5000a | LS06 Onyx; E 592.95; HZ5000a")
add("LOTH Watches", "loth-watches", "Cingapura", "Cingapura", 2024, "Tristan Ho", "Relógios de corda manual de desenho autoral, com calibre baseado no Unitas 6498.", "loth.sg", "lothwatches",
    "LOTH Watch 1; S 6498; Caliber 1 de corda manual (base Unitas 6498)")
add("Luckyshroom", "luckyshroom", "Suíça", "Zug", 2025, "Jordan Spence", "Relógios retangulares de titânio montados sobre módulos digitais Casio.", "theluckyshroom.com", "luckyshroom",
    "FLATHEAD BR; F 580; módulo Casio 3551 | ANDO x LS Balance in contrast; E 1200; módulo Casio 3572", CHF)
add("Lyrique", "lyrique", None, None, None, None, "Relógios clássicos de corda manual com calibres Agenhor.", "lyrique.ch", None,
    "Étude N°1 (2022); -; Agenhor AGH-6801, corda manual | Étude N°2 Guilloché (2024); U 36250; Agenhor AGH-6802, corda manual", "B vazio: o Atlas não informa o país (o site é .ch, provavelmente Suíça: confirmar).")

# ---------- M ----------
add("M. Laurent", "m-laurent", "Polônia", "Poznań", 2025, "Laurent Vedrenne", "Relógios irreverentes e chamativos a quartzo (Ronda 715).", "mlaurent.com", "m.laurent.watches",
    "Absolute Black + Dark Gold; U 400; Ronda 715")
add("Mad Hudson Watches", "mad-hudson-watches", "USA", "Chicago", 2024, "Mad Hudson, Connor Hudson e Brad Podray", "Relógios divertidos a quartzo, em colaborações com artistas.", "madhudsonwatches.com", "madhudsonwatches",
    "Broken Time; U 195; Miyota quartzo | Pride Watch (Alex Donahue); U 178; - | Marshall Watch; U 183; - | CD Watch (Riki Prosper); U 192; - | Broken Time (Brad Podray); U 215; - | Dogma (Bryce Wong); U 157; -")
add("Maison Boanton", "maison-boanton", "França", "Paris", 2022, "Hassan Sefrioui", "Relógios sociais Art Déco com automático suíço La Joux-Perret G100.", "maisonboanton.com", "maisonboanton",
    "Emblème Ivoire Vintage; U 2224; La Joux-Perret G100 | Emblème Pink Edition (Storm Grey); U 2460; La Joux-Perret G100 | Ellipse B2201-RM Lunar Silver; U 2187; La Joux-Perret G100 | Ellipse B2201-AR Terra Nera; U 2187; La Joux-Perret G100 | Héritage; U 2385; La Joux-Perret G100")
add("Majestic Craftsmen", "majestic-craftsmen", "Índia", "Bangalore", 2020, None, "Relógios sociais vistosos com Miyota 8205.", "majesticcraftsmen.com", "majesticcraftsmen",
    "Monarch Emerald; U 301; Miyota 8205 | Monarch Bronze; U 186; Miyota 8205")
add("Makara Watches", "makara-watches", "Canadá", "Montreal", 2013, "Nadim Elgarhy", "Relógios de mergulho de visual elegante com automáticos e quartzos japoneses.", "makarawatches.com", "makarawatches",
    "M3-CHR Lizard Iridescent; U 100; Seiko VK64 | Hawksbill Sea Turtle; U 395; Seiko NH35A | Hawksbill; U 395; Seiko NH35A")
add("Makydo", "makydo", "Reino Unido", "Londres", None, "Nadeem Fazlani", "Relógios neo-vintage de mostradores brilhantes com Miyota 9015, NH35 e quartzo.", "makydo.com", "makydowatches",
    "Pearl White Mosaic 38; U 485; Miyota 9015 | Velocity White 42 (cronógrafo); U 304; Miyota quartzo | Deep Black 38 (mergulho); U 443; NH35")
add("MALM Watches", "malm-watches", "Suécia", "Linköping", 2019, "Marcus Malm", "Relógios minimalistas suecos inspirados na aviação (Spitfire, Tunnan, J35) com Sellita e Seiko.", "malmwatches.com", "malmwatches",
    "Art S31 Spitfire Silver Swiss; E 904.95; Sellita SW200-1 | Dalton Birdie Chronograph 41; U 600; Seiko VK63 | A-11 Silver 44 Automatic Ltd.; U 750; Seiko NH35 | Art J29 Tunnan Silver Swiss; E 904.95; Sellita SW200-1 | Art Dalton UTC Automatic 38; E 814.95; Seiko NH34 | Art Dalton J35 Chronograph; E 623.95; Seiko VK67 mecaquartzo")
add("MAN of the SEA Watch Co.", "man-of-the-sea", "USA", "Venice (Flórida)", 2022, "Don Weismantel", "Relógios de temática náutica e pirata, de visual exuberante, com Sellita SW200-1.", "manoftheseawatchco.com", "peglegdon",
    "Smooth Seas!; U 2495; Sellita SW200-1 | Wings Unfurled; U 2495; Sellita SW200-1 | Dead Men Tell No Tales; U 2495; Sellita SW200-1 | SkullNBones; U 2495; Sellita SW200-1 | Need A Bigger Boat!; U 2495; Sellita SW200-1 | Poseidon's Rule!; U 2495; Sellita SW200-1", "Instagram do Atlas é @peglegdon (parece conta do fundador): conferir se há conta da marca.")
add("Maranez", "maranez", "Tailândia", "Phuket", 2012, None, "Relógios de mergulho neo-vintage (latão, bronze e titânio) com Seiko NH35 e Miyota 9015.", "maranez.com", None,
    "Rawai 42; U 349; NH35 | Racha (mostrador verde); U 399; NH35 | Kata (mostrador azul); U 329; Seiko NH35 | Samui Army (verde, luneta de mergulho); U 399; Seiko NH35 | Samui vintage titanium red; U 399; Seiko NH35")
add("MARC & SONS", "marc-sons", "Alemanha", "Altdorf", 2006, "Marco Heimrich", "Relógios de mergulho e relógios-ferramenta com automáticos suíços e Seiko.", "marcandsons.de", None,
    "Military Diver (2021); U 961; Sellita SW200-1 | Elegance (2020); U 806; ETA 2824-2 | Navy Pilot Chronograph (2022); U 1874; Sellita SW510b | GMT II-D (2023); U 1336; Sellita SW330-2")
add("March Hare", "march-hare", "USA", "Nova York", None, "Mabel (sobrenome não informado)", "Relógios sociais femininos a quartzo suíço Ronda.", "marchharewatches.com", None,
    "Kimsey; U 389; Ronda quartzo suíço | Kimsey Double Wrap; U 389; Ronda quartzo suíço | Harriet; U 359; Ronda quartzo suíço")
add("Marchand Watch Company", "marchand-watch-company", "Reino Unido", "Cambridge", 2015, "Daniel Brigham", "Relógios de inspiração automobilística a quartzo (Miyota, Seiko VK64).", "marchandwatches.com", None,
    "Driver Chronograph MKII Quartz (Yellow Reverse Panda); U 169; Miyota quartzo | Matt Black GT; U 129; quartzo japonês | Sportline (Silver Dial); U 99; quartzo japonês | Esses GT; U 99; Miyota OS10 | Silver Dial Driver; U 89; quartzo japonês")
add("Marcks & Co.", "marcks-co", "USA", "Raleigh (Carolina do Norte)", 2024, "Bhavish Malkani e Arjun Shankar", "Relógios neo-vintage que misturam referências indianas e ocidentais, com Sellita SW260-1.", "marcksandco.in", None,
    "The Captain; U 1200; Sellita SW260-1 | The Raja; U 1200; Sellita SW260-1 | The Nizam; U 1200; Sellita SW260-1", "O site é .in (Índia), mas o Atlas dá a sede em Raleigh, EUA: conferir o país.")
add("Marcu Genève", "marcu-geneve", "Suíça", "Genebra", 2026, "Jérôme Marcu", "Ateliê independente genebrino de relógios de corda manual.", "marcu-geneve.ch", "marcu_geneve",
    "Initial; -; corda manual, 50 horas de reserva, 18.000 a/h")
add("Mark Time Watches", "mark-time-watches", "USA", "Filadélfia (Pensilvânia)", 2021, None, "Relógios minimalistas de uso diário com Miyota 9039.", "marktimewatches.com", None,
    "M 1.2; U 345; Miyota 9039 | M 6 GMT; U 495; -")
add("Marlin Diving Watches", "marlinwatch", "Reino Unido", "St Neots", 2020, "Paul Harris", "Relógios de mergulho acessíveis com NH35/NH36 e quartzo.", "marlinwatch.co.uk", "marlinwatch",
    "Mk9 Automatic (luneta interna giratória); U 296; automático | Mk8 Chronograph; U 255; cronógrafo a quartzo")
add("Mason Watch Collection", "mason-watch-collection", "USA", "San Diego (Califórnia)", 2019, "Mike Mason", "Relógios de estilo eclético.", "masonwatchcollection.com", None,
    "MAS312; -; - | MAS313; -; - | MAS315; -; - | MAS316; -; - | MAS317; -; - | MAS318; -; -", "D genérico: o Atlas não informa movimentos nem preços.")
add("Mater Made", "mater-made", "USA", "Los Angeles", None, "Hayden Mater", "Relógios de desenho autoral com Miyota 9015.", "matermade.com", None,
    "The Don (Ultramarine e mais 2 cores); U 550; Miyota 9015")
add("Matterhorn Watch Co.", "matterhorn-watch-co", "Reino Unido", "Londres", 2019, "Taahir Abdul", "Relógios de mergulho para aventura com Miyota 9015.", "matterhornwatchco.com", None,
    "DiveMaster 300 (Ocean Blue e mais 2 cores); U 402; Miyota 9015")
add("Matthew Mercury Watches", "matthew-mercury-watches", "USA", "Wilmington", None, None, "Relógios minimalistas a quartzo suíço Ronda.", "matthew-mercury.com", None,
    "Dan; U 395; Ronda 3540.D | Dre Gold; U 250; Ronda 763 | Obsidian 36mm; U 250; Ronda 762 | Dan Red All Stars (conjunto); U 500; Ronda 3540.D | Magnum; U 395; Ronda 3540.D | Wall Street; U 250; Ronda 763", "C: o Atlas diz só Wilmington (sem o estado).")
add("Maughan Jones", "maughan-jones", "Reino Unido", "Londres", 2018, "Ben Maughan e Sam Jones", "Relógios esqueletizados de desenho arquitetônico com Miyota 8215 e quartzo.", "maughanjones.com", None,
    "Spectra Pro (Gold); U 769; Miyota automático | Luna (Blue Steel); U 212; quartzo | Momentum Auto (Green); U 470; Miyota 8215")
add("Max Twelve", "max-twelve", "Suíça", "Uitikon", 2024, "Fabian Lehner", "Relógios esqueletizados de desenho contemporâneo com Sellita.", "max-twelve.com", None,
    "The Skeleton All-Black; U 3965; Sellita esqueletizado | Astronaut; U 4052; Sellita esqueletizado | Hexagon; U 3222; Sellita", "The Skeleton All-Black: o Atlas dá de US$ 3.965 a 5.081; usei o menor.")
add("Mazzucato", "mazzucato", "Itália", "Milão", 2018, "Simone Mazzucato", "Relógios esportivos reversíveis (automático de um lado, cronógrafo do outro) com Miyota 9015 e JS00.", "mazzucatowatches.com", None,
    "RIM Sport; U 1400; Miyota 9015 + JS00 | RIM Scuba; U 2200; Miyota 9015 | RIM GT; U 600; Seiko NH70 | RIM Monza; U 1800; Miyota 9015 + JS00 | RIM Sub; U 600; - | LAX; U 1800; -")
add("McDowell Time", "mcdowell-time", "USA", "Rockville (Maryland)", 2016, "Bill McDowell", "Relógios de inspiração americana clássica com Seiko, Sellita, Miyota e MWW.", "mcdowelltime.com", None,
    "DelRay (2016); U 295; Seiko YT57 | Tidewater (2020); U 549; Sellita SW200 | Maxton V2 (2025); U 349; Miyota 6S20 | Rockville (2021); U 699; MWW 7081")
add("McQuaide Watches", "mc-quaide-watches", "Reino Unido", "Reading", 2023, "Rob McQuaide", "Relógios britânicos de uso diário com automáticos Sellita.", "mcquaide.co.uk", None,
    "Q1-B Crimson; E 904.95; Sellita SW200-1 | C1 Midnight × WatchGecko Strap; E 783.95; - | C1 Sunburst; E 783.95; Sellita SW200-1b")
add("Meia Lua", "meia-lua", "Portugal", "Lisboa", 2018, None, "Relógios de estilo aviador e desenho contemporâneo, alguns com Miyota 9122.", "meialuawatches.com", None,
    "Callisto Blue Moon; E 659; Miyota 9122 | Deepmoon Black Leather; E 429; - | Moonmetal Dust Bright Side Cocoa Leather; E 429; -")
add("Memphis Belle", "memphis-belle", "Itália", "Gênova", 1998, "Alessandro Roman e Giovanni Panucci", "Relógios de inspiração militar e de aviação com ETA, Sellita e Seiko.", "memphisbellewatches.shop", None,
    "Crono Leonardo MB PVD Nero; U 550; OS6S20 | Caimano Meccanico Nero Bracciale; U 1250; MBDB9 | Caimano Meccanico Heritage Br; U 1250; MBDB9 | Caimano Meccanico Mancino Quadrante Bianco; U 1250; MBDB9 | Nuovo Sandy Meccanico Automatico Acciaio; U 295; TMI NH35 | Predator Evolution Militech MB Sale & Pepe Trigalight; U 1290; Sellita SW200-1")
add("Meridiano Watches", "meridiano-watches", "França", "Marselha", 2023, None, "Relógios minimalistas (alguns de um ponteiro só) com Seiko NH38/NH70 e quartzo.", "meridiano.fr", None,
    "Beyond 34mm; U 400; Seiko NH38 | Mono Hand 40mm; E 350; Seiko NH70 | Kilroy Burnt Earth 40mm; E 390; Seiko NH70 | Mono Hand 34mm; U 350; Seiko NH38 | The Lost Astronaut 34mm; U 400; Seiko NH38 | La Playa 38mm; U 300; quartzo")
add("Micserah", "micserah", "Nigéria", "Lagos", 2018, "Adekunle Adeniji", "Relógios nigerianos de luxo acessível a quartzo.", "micserah.com", "micserah",
    "Luna 38 Rose; -; - | Boyfriend Rose Silver; -; Miyota 2025 | 5th Rose Gold; -; - | Seashell rose-silver; -; - | Phantom Silver; -; - | Boyfriend II Gold Silver; -; -", "Sem preço: o Atlas mostra 162.500 a 242.500 marcados como dólares, que parecem ser nairas nigerianas. Conferir.")
add("Minim Watches", "minim-watches", "Reino Unido", "Londres", 2019, "Chloe Chan", "Relógios sociais minimalistas com Sellita SW261-1.", "minim-watches.com", None,
    "MN01 Laan4 蘭; G 1199; Sellita SW261-1 M | MN01 Bik1 碧; G 1199; Sellita SW261-1 M | MINIM x MIC MN01; G 1199; Sellita SW261-1 M | MN01 Zing1 晶; G 1199; Sellita SW261-1 M | MN01 CNY LE 1/50 Giu1 嬌; G 1199; -")
add("Minor Watches", "minor-watches", "Espanha", "Ourense", 2018, "Héctor, Santiago e César Pérez Salgado", "Relógios minimalistas de uso diário com Sellita SW200-1.", "minorwatches.com", None,
    "Heritage Elegance Grey (5 cores); U 926; Sellita SW200-1")
add("Mirco", "mirco", "Japão", "Minamisoma", 2019, "Masayasu Hiraoka", "Relógios de mergulho de engenharia japonesa com Miyota 9039 e Seiko NE86.", "eng.mircowatch.com", None,
    "TYPE-03 Masuhanairo (2022); -; Miyota 9039 | TYPE-02 (2019); -; Seiko NE86", "Sem preço: os valores dos modelos na ficha (US$ 14 e 17) não batem com a faixa da própria página (US$ 1.300 a 1.800). Conferir.")
add("Monarte Watches", "monarte-watches", "Eslovênia", "Liubliana", 2019, "Domen Veleusic", "Relógios de mergulho minimalistas com ETA 2824-2.", "monartewatches.com", None,
    "Squid Blue (3 cores); U 1369; ETA 2824-2")
add("Monchard Watches", "monchard-watches", "Suécia", "Malmö", 2016, "Oskar Gydell e Jonathan Belvér", "Relógios neo-vintage com Seiko VK64, Ronda e Miyota 9015.", "monchardwatches.com", None,
    "Skytrain Telemeter Chronograph; U 432; Seiko VK64 mecaquartzo | Étape Classic; U 299; Ronda 762 ou 1032")
add("MONOGRIIS", "monogriis", "Japão", "Osaka", 2018, "Tsubasa Ohira", "Relógios sociais neo-vintage com Miyota 8N40.", "monogriis.com", "monogriis_jp",
    "RESTA R50-001 Automatic Small Seconds (36 mm); E 290; Miyota 8N40")
add("Monserrate Atelier", "monserrate-atelier", "Portugal", "Palmela", None, None, "Relógios de inspiração manuelina portuguesa com Sellita SW200-1.", None, "monserrate_official",
    "Manueline (Lioz / Valverde); U 1774; Sellita SW200-1 A", "A ficha cita o nome Zac-Manuel, mas não como fundador: conferir.")
add("Montera", "montera", "Reino Unido", None, 2025, "Sachin Velmurugan e Noah Wilson", "Relógios britânicos de tiragem limitada com NH35 e GMT NH34.", "monterawatches.com", None,
    "Coral Montera Watch; E 315.95; - | Cortado Montera Watch; E 315.95; - | Pistachio Montera Watch; E 315.95; - | Bluewater GMT; -; NH34")
add("Monterey Watch Co", "monterey-watch-co", "USA", "Swannanoa (Carolina do Norte)", 2022, "Tim Hermes", "Relógios de mergulho e aventura de estilo americano com Seiko NH35/NH34 e Miyota.", "montereywatches.com", None,
    "Blacktip Standard; U 299; - | EBC GMT Pro; U 529; Peacock SL3032 | CAROVA; U 479; Miyota 8215 | Kitty Hawk EK; U 269; Seagull ST3600 de corda manual | DARKFATHOM DT; U 509; Miyota 9015 | Hatfield; U 209; -")
add("Montjuïc Watches", "montjuic-watches", "Espanha", "Barcelona", 2018, "Rosendo Rabat, Tendu Rabat e Edu Méndez", "Relógios de inspiração automobilística com Miyota e Seiko/TMI.", "montjuicwatches.com", None,
    "Speed Automatic Black Tarmac; U 1346; Miyota automático | Speed Rally Costa Brava; U 374; Seiko VH31A mecaquartzo | GMT Tarmac Black; U 462; quartzo GMT | Black Orange Accents Chrono SS; U 573; Miyota mecaquartzo | Urban Pilot PRO SS (MOMO Design); U 462; Miyota mecaquartzo")
add("Montmartre Watchworks", "montmartre-watchworks", "França", "Paris", 2018, "Robert Morrison", "Relógios minimalistas (redondos e tonneau) com Seiko, Sellita SW200 e Landeron 24.", "montmartre-watchworks.com", None,
    "MW1 (2022); U 526; VK61 mecaquartzo, NH36 ou Landeron 24 | MW3 Tonneau Automatic (2023); U 571; NH35, Sellita SW200 ou Landeron 24 | MW5 Tonneau Chronograph (2023); U 548; VK61 mecaquartzo")
add("Mount West Watch Co.", "mount-west-watch-co", "USA", "Salt Lake City (Utah)", None, "Drew Zayach", "Relógios-ferramenta com Sellita SW200.", "mountwestwatchco.com", "mountwestwatchco",
    "Summit V1 Medic (edição limitada); U 1725; Sellita SW200 | Summit (Abyss, Treeline, Snowfall, Obsidian); U 1450; -")
add("Mr. Eatwell", "mr-eatwell", "USA", "Portland (Oregon)", 2020, "Matt Rebackoff", "Relógios coloridos e bem-humorados com NH35, NH34 e Sellita SW200.", "mreatwell.com", None,
    "SubMeloner; U 370; NH35 | OffShorer; U 370; NH35 | SubLime; U 370; Seiko VD78A | GMT Challenger; U 480; NH34 | Chino; U 355; NH35")
add("MTK Watches", "mtk-watches", "USA", "Montauk (Nova York)", 2021, "Greg Martin", "Cronógrafos mecaquartzo Seiko VK64 de inspiração clássica.", None, None,
    "New York Chronograph (Reverse Panda); U 299; VK64 mecaquartzo | New York Chronograph (Silver Sector); U 299; VK64 mecaquartzo", ativa=False)

salvar(sys.argv[1] if len(sys.argv) > 1 else "lote7.json")
