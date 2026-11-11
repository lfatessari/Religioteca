# -*- coding: utf-8 -*-
"""Lote 9 (11/11/2026): Microbrand Atlas, letras R e S (54 marcas). Sem história.
Radcliffe Watches ficou de fora: a ficha do Atlas abre vazia."""
import sys
from lote_base import add, salvar

# ---------- R ----------
add("R. Day Watches", "r-day-watches", "Reino Unido", "Londres", None, "Richard Day", "Relógios minimalistas automáticos com Miyota 8245.", "rdaywatches.co.uk", None,
    "Astro; U 1200; Miyota 8245 | Antares; U 1100; Miyota 8245 | Vega; U 1100; Miyota 8245")
add("Raja Watch Co.", "raja-watch-co", "Filipinas", "Manila", 2020, "Niko de Dios e Raj Khatwani", "Relógios filipinos de desenho autoral e mistura cultural.", "rajawatch.com", "therajawatch",
    "Majesty in Onyx; P 7995; - | The Apprentice Blacksmith in Silver (feminino); P 2995; - | The Apprentice Blacksmith in Silver (masculino); P 2995; - | Warrior 2.0 in Steel; P 9995; - | Warrior 2.0 in Fire; P 9995; - | The Parliament Sapphire Edition; P 24995; -", "Preços do Atlas em pesos filipinos. O Atlas não informa os movimentos.")
add("Ratio", "ratio", "Cingapura", None, 2017, None, "Relógios de mergulho e aviação acessíveis com Seiko e Miyota.", "ratiowatches.com", None,
    "FreeDiver (2018); U 98; Seiko NH35 | FreeDiver X (2024); U 230; Seiko NH35 | FreeDiver 1000M (2019); U 169; Seiko NH35 | Skysurfer (2020); U 145; Seiko NH38A | Quest (2022); U 89; Seiko VX42 | Street Racer Chronograph (2024); U 199; cronógrafo mecaquartzo")
add("Redux", "redux", "USA", "Nova York", 2012, None, "Relógios de estilo militar americano com Miyota 9015 e Seiko NH35.", "reduxwatch.com", None,
    "VALOR (2021); U 1300; Miyota 9015 | Honnr A-13A; U 995; Miyota 9015")
add("Resco", "resco", "USA", "Coronado (Califórnia)", 2009, "Rob Smith", "Relógios-ferramenta de uso militar com Sellita SW200, ETA 2824-2 e Ronda.", "rescoinstruments.com", None,
    "DLC Gold; U 1900; Sellita SW200 | Blasted Grey; U 1150; Sellita SW200 | Brushed Grey; U 1700; Sellita SW200 | Brushed Olive; U 1700; Sellita SW200 | Brushed Red; U 1700; Sellita SW200 | Brushed RWB; U 1700; Sellita SW200")
add("retrovivo", "retrovivo", "Itália", "Sicília", 2024, "Giuseppe Bua", "Relógios neo-vintage de desenho italiano de meados do século, com Seiko VH31.", "retrovivo.store", None,
    "RV01 Green; U 183; Seiko VH31 | RV01 Black; U 183; Seiko VH31 | RV02 Diver; U 228; Seiko VH31", "C: o Atlas diz só 'Sicília'. RV02: a ficha cita também um NH35 automático, em conflito com os dados do modelo.")
add("Reuben Schoots", "reuben-schoots", "Austrália", "Camberra", 2022, "Reuben Schoots", "Relojoeiro independente australiano de relógios sociais de corda manual feitos à mão.", "reubenschoots.com", None,
    "Series Two; U 37500; corda manual de fabricação própria, 18.000 a/h")
add("Revolution Watch Company", "revolution-watch-company", "USA", "Boston (Massachusetts)", 2005, "Wei Koh", "Edições limitadas em colaboração com outras marcas (Tutima, Vulcain, Ralph Lauren e outras).", "shop.revolutionwatch.com", None,
    "Alterum Worldtimer Horizon; U 3650; Sellita SW330-2 GMT | Tutima x Revolution M2 Coastline Chronograph; U 3300; calibre 7750 / Tutima 310 | Ludovic Ballouard et Fils Upside Down \"Series Gaga\"; -; calibre B01 | Vulcain x Seconde/Seconde/ x Revolution Cricket Tradition \"Vulcain Salute\" Green; U 4150; - | Revolution x Maghnam Mohareb \"Ocean Relic\"; U 8350; MCR01 (base Sellita SW210) | Ralph Lauren x Revolution x The Rake Snow Beach Bear; U 1850; RL200 (base Sellita SW200-1)", "Parece ser a loja da revista Revolution (colaborações), não uma marca própria: avaliar se fica. O Ludovic Ballouard (US$ 123.700 no Atlas) ficou fora da média de preço.")
add("Riley Watch Co", "riley-watch-co", "Reino Unido", "Manchester", 2023, None, "Relógios de inspiração aeronáutica, com cronógrafos e fases da lua a quartzo.", "rileywatchco.com", None,
    "Howard Hughes FlyRacer Chronograph; U 249; Seiko VK64 | Almond Rifleman Field Quartz; U 219; Miyota | Lumis Day/Night Dial; U 219; Ronda 515.24H | Howard Hughes Scarface Chronograph HH01 SF; U 349; VK64 mecaquartzo | Deco Moon; U 229; Ronda 708 | Bessie FAI-01; U 229; Miyota JP21")
add("Robotfigs", "robotfigs", "Hong Kong", "Kwun Tong", None, None, "Relógios híbridos de mistura cultural com mecaquartzo Seiko VK64.", "robotfigs.com", "robotfigs",
    "Cubot; U 724; Seiko VK64 mecaquartzo")
add("Rockwell Time", "rockwell-time", "USA", "Woods Cross (Utah)", 2007, "Rich Eggett", "Relógios esportivos americanos com movimentos suíços, japoneses e o automático americano RT1776.", "rockwelltime.com", None,
    "50mm Automatic (2023); U 7500; RT1776 American Automatic | 747 (Silver/Red); U 877; Ronda 763E | 747 (Silver/Black); U 877; Ronda 763E | 747 (Black/Green); U 1052; Ronda 763E | CF Lite (Gold/Black); U 245; - | CF (White); U 300; -")
add("Rolf Cremer", "rolf-cremer", "Alemanha", "Geesthacht", 1989, None, "Relógios alemães de design modernista, a quartzo e automáticos.", "rolf-cremer.de", None,
    "Big Corner; U 200; quartzo | Corner; U 185; quartzo | Mech I; U 350; automático | Pur; U 175; quartzo | Slim 42; U 165; quartzo | Style; U 200; quartzo")
add("Roskopf", "roskopf", "Austrália", "Sydney", 1980, None, "Relógios militares de reprodução, de campo e esqueletizados, a quartzo e automáticos.", "roskopfwatches.com", None,
    "Heritage Trench; U 300; quartzo | Spitfire WW2 Pilots (Aviation Heritage); U 320; quartzo | Racing F1 Automatic Skeleton; U 250; automático")
add("Rotate North", "rotate-north", "Reino Unido", "Belfast (Irlanda do Norte)", 2019, None, "Relógios-ferramenta com NH35A e quartzo Ronda.", "rotatenorth.com", None,
    "Arctic 500m Dive (43 mm); E 203; NH35A | Atlantic Dive (40 mm); E 250; NH35A | Turbulence Cat.1 Aviator (46 mm); E 300; NH35A | Tempest Quartz Navigator (40 mm); E 229; Ronda 715LI")
add("Rotoris", "rotoris", "Índia", "Nova Délhi", 2025, "Aakash Anand", "Relógios indianos de desenho autoral com movimentos suíços e japoneses.", "rotoris.com", "rotoris.world",
    "Manifesta Mother of Pearl; -; Miyota 82S0 | Astonia Dusk Gold; -; Ronda 5030.D | Astonia Sports Circuit Blue; -; Ronda 5030.D | Arvion Espresso Silver; -; Miyota 6L45 | Auriqua Noir Rose; -; Miyota 9039 | Astonia Trophy Gold; -; Ronda 5030.D", "O Atlas só dá a faixa geral da marca (US$ 800 a 2.500), sem preço por modelo.")
add("Royter Watches", "royter-watches", "USA", "Nova York", 2017, "Dan Royter", "Cronógrafos minimalistas de desenho autoral com ETA 7750.", "royterwatches.com", "royterwatches",
    "DR-02 Chronograph Black Dial; U 2950; ETA 7750 | DR-02 Hand-Finished Blue Dial; U 4950; ETA 7750")
add("RVLVR", "rvlvr", "USA", "Honolulu (Havaí)", 2015, "Dan Uchida", "Relógios de desenho autoral com Seiko NH35A/NH70A e quartzo.", "rvlvr.com", None,
    "AD5 Silver (2019); U 349; Seiko NH35A | SD-1 Hawaiian Punch (2021); U 419; Seiko NH70A | Q1 (2015); U 179; quartzo")
add("RVNDSGN", "rvndsgn", "USA", "Grand Rapids (Michigan)", 2011, "Zach Raven", "Relógios modernistas com Sellita SW200-1 modificado.", "rvndsgn.com", None,
    "M1 Nova White (4 cores); U 1999; Sellita SW200-1 modificado")

# ---------- S ----------
add("S.U.F Helsinki", "s-u-f-helsinki", "Finlândia", "Helsinque", 2004, "Stepan Sarpaneva", "Relógios finlandeses neo-vintage com Soprod A10.", "sufhelsinki.com", None,
    "Kaaos Kuura; U 4450; Soprod A10 modificado | Vetehinen Lapis lazuli; U 5500; Soprod A10 | Paroni; U 2500; Soprod A10 | 180 Protox; U 2600; Soprod A10 | Flying Finn FF-S; U 5200; Soprod A10 | Myrsky MY-E; U 2800; Soprod A10")
add("Sangin Instruments", "sangin-instruments", "USA", "El Cajon (Califórnia)", 2016, "Jacob Servantes", "Relógios de campo e militares neo-vintage com Ronda 515.24H, La Joux-Perret G100 e Sellita SW300.", "sangininstruments.com", None,
    "SOCS-C; U 629; - | SERT; U 679; - | Para Overlord; U 489; - | NEPTUNE (FR); U 1599; - | Taclet/Tlei; U 1599; - | ATLAS (FR); U 949; -")
add("Sans Arrêt", "sans-arret", "USA", "Casper (Wyoming)", 2025, None, "Relógios sociais minimalistas de inspiração Art Déco, a quartzo.", "sansarretwatch.com", "sansarretwatch",
    "AMBITIONIST Epic; E 272.95; - | ELEMENT Bois; E 254.95; - | ELEMENT Feu; E 254.95; - | REWIND Gold Hour; E 327.95; - | DOMINATOR Midnight Jade; E 299.95; - | PRISM/SAROS Reflection; E 235.95; -")
add("Santura", "santura", "Indonésia", "Jacarta Ocidental", 2024, "Jason Edward", "Relógios de desenho autoral com Miyota 9039.", "santurawatches.com", None,
    "Santura Novus Blue; U 499; Miyota 9039 | Santura x Bauche Nebula Amethyst; U 499; Miyota 9039", "A ficha do Atlas avisa de possível encerramento da marca.")
add("Santurce", "santurce", "USA", "San Juan (Porto Rico)", 2019, None, "Relógios de mergulho elegantes com Miyota 9075, Sellita SW200 e Ronda.", "santurcecollection.store", None,
    "Guaraguao; U 899; Miyota 9075 | Pitirre True GMT; U 899; Miyota 9075 | Mocho; U 499; Ronda 215 | Picua; U 949; Sellita SW200-B | El Tiburon; U 949; Sellita SW200-B")
add("Satori Watches", "satori-watches", "Reino Unido", "Beckenham", 2020, "Roy Miah", "Relógios minimalistas com Miyota 9015.", "satoriwatches.com", None,
    "Companion Crimson Red; U 500; Miyota 9015 | Companion All-Black Tuxedo (PVD); U 550; Miyota 9015")
add("Saturn Watches", "saturn-watches", "USA", "Antelope (Califórnia)", 2026, "N. Hashimi", "Cronógrafos neo-vintage mecaquartzo Seiko VK63.", "saturn-watches.com", None,
    "New Man; U 380; Seiko VK63 mecaquartzo")
add("Sconvolto", "sconvolto", "Itália", "Castelplanio", 2018, "Luca Ubertini", "Relógios de inspiração automobilística com Miyota 9015 e 82S5.", "sconvolto.com", None,
    "Tipo A; U 1131; Miyota 9015 | Tipo D; U 1028; Miyota 82S5 | Tipo F; U 1131; Miyota 9015 | Tipo L; U 1028; Miyota 82S5")
add("Seaholm", "seaholm", "USA", "Austin (Texas)", 2013, "C. Todd Adams", "Relógios neo-vintage robustos com Sellita SW200-1 e ETA 2894-2.", "seaholmautomatic.com", None,
    "Rover (2016); U 1895; Sellita SW200-1 | Flats Chronograph (2016); U 3495; ETA 2894-2")
add("Seals Watch Company", "seals-watch-company", "USA", "El Dorado Hills (Califórnia)", 2014, "Michael Seals", "Relógios-ferramenta e de mergulho com Miyota 9015/9039 e Sellita.", "seals-watches.com", "sealswatches",
    "Land // Sea Classic; U 695; Miyota 9015 | Sea Storm Fixed Bezel No-Date; U 670; Miyota 9039 | Dark Seal 12-Hour; U 650; Miyota 9039 | Model A; U 800; Miyota 9015 | Dark Seal; U 590; Miyota 9039 | Model C Field Explorer; U 655; Sellita SW200-1")
add("Sequent", "sequent", "Suíça", "Basileia", 2015, "Harry Guhl e Adrian Buchmann", "Relógios de desenho modernista com calibres SC 2.2 e SC 2.3.", "sequentworld.com", None,
    "SolarCharger #tide Azure blue; U 865; SC 2.3 | Elektron; U 1312; SC 2.2 | Smart(ass) Watch (colaboração); U 1349; SC 2.2")
add("Serket Watch Co", "serket-watch-co", "USA", "Denver (Colorado)", 2006, None, "Relógios-ferramenta e GMT de forte luminescência com Seagull, Hangzhou, Miyota e Seiko.", "serketwatch.com", None,
    "ORBITAL Meteor; E 800; Seagull ST1701 | CONTINUUM Verdant; E 475; Hangzhou 5000A | REVENANT Vanguard Blue; E 700; Miyota 8205 | REEF X Mint DLC; E 575; Seiko NH35 | PILOT COMMANDER Green; E 375; Seagull ST3600 | BLACKPOOL GMT Fire Engine; E 450; Seiko NH34 GMT")
add("Sero Watch Company", "sero-watch-company", "Holanda", "Utrecht", 2023, "Sergino Rontgen e Robert van de Stadt", "Relógios minimalistas de corda manual com Sellita SW210-1 b.", "serowatchcompany.com", None,
    "Signature (Silver, Red, Gold, Blue), 37,5 mm; E 1199; Sellita SW210-1 b de corda manual")
add("Sewills", "sewills", "Reino Unido", "Liverpool", 1800, "Joseph Sewill", "Marca histórica de Liverpool com relógios de mergulho e de herança (ETA 2824-2 e Unitas 6498).", None, None,
    "Professional Diver PRS-44; U 700; ETA 2824-2 | Ferreira PRS-39; U 1300; Unitas 6498 modificado de corda manual", "O Atlas lista como ativa, mas os dois modelos estão esgotados e não há lançamento anunciado; tratada como inativa.", ativa=False)
add("Shaw", "shaw", "Índia", "Nova Délhi", 2023, None, "Relógios indianos de uso diário e bom custo com Seiko NH35 e Ronda 713.", "shawwatches.in", None,
    "Spirit-Polar; R 14500; Seiko NH35 | Manta Quartz Atoll Aqua Blue; R 8500; Ronda 713 | Manta Quartz Tropical Reef Green; R 8500; Ronda 713 | Spirit-Anthracite; R 14000; Seiko NH35", "Preços do Atlas em rúpias.")
add("Sheffield Watches", "sheffield-watches", "USA", "Deer Valley (Utah)", 2023, "Jay Turkbas", "Relógios neo-vintage acessíveis com Seiko e Miyota.", "sheffieldwatches.com", None,
    "Allsport Diver 1A 40mm; U 198; Seiko NH35 | QL1 Black; E 59.95; Miyota 2035 quartzo | QL1 Magenta; E 59.95; Miyota 2035 quartzo | Rally 2.0; E 244.95; - | 1A 38 Silver 2.0; E 238.95; - | 1A 38 Black/Blue; E 225.95; NH35")
add("Shelby Watch Company", "shelby-watch-company", "Canadá", "Barrie (Ontário)", 2023, "Matthew McMillan", "Relógios neo-vintage de estilo americano com movimento MD 7081.", "shelbywatchco.ca", None,
    "MEDIC; U 715; MD 7081")
add("Sherpa Watches", "sherpa-watches", "Alemanha", "Meerbusch", 2019, "Martin Klocke", "Relógios neo-vintage de aventura com o calibre Mantramatic MM01 (base Sellita SW200-1).", "sherpawatches.com", None,
    "Ultradive Classic; U 7000; Mantramatic MM01 (base Sellita SW200-1) | OPS; U 6700; Mantramatic MM01 (base Sellita SW200-1)")
add("Shield Watches", "shield-watches", "USA", "Novi (Michigan)", 2008, None, "Relógios de mergulho e relógios-ferramenta com Miyota e Seiko.", "shieldwatches.com", None,
    "Palau Leather-Band Diver; E 390; Miyota 2315 | Condor Bracelet; E 400; - | Atlantis Abalone Bracelet; E 675; Seiko NH35 | Shaw Leather-Band Diver; E 515; Miyota 2415 | Nitrox Bracelet; E 515; Seiko NH35 | Abyss Bracelet; E 300; Miyota 2035")
add("Shiro Kara", "shiro-kara", "USA", "Nova Orleans (Louisiana)", 2023, None, "Relógios de mergulho com NH35/NH36.", "shirokarawatches.com", None,
    "Daibazu 369 SUB; U 800; NH35 | Terebi Modern; U 650; NH35 | SKV Vintage Divers; U 750; NH35 | Grand Line Vintage; U 1200; NH35")
add("Shoreham", "shoreham", "Reino Unido", "Cardiff (País de Gales)", 2020, "dois amigos (nomes não divulgados)", "Relógios de mergulho e de campo elegantes com automáticos Seiko NH.", "shorehamwatches.com", None,
    "Snowdon GMT (2023); U 469; Seiko NH34 GMT | Pembroke Field (2022); U 469; Seiko NH38A | Monmouth Dive (2020); U 456; Seiko NH35A")
add("Sidereus Watches", "sidereus-watches", "Irlanda", "Bagenalstown", 2019, "Bryan Leech e Martin Marley", "Relógios irlandeses de tiragem limitada, com fases da lua e GMT, sobre Sellita modificado.", "sidereus.com", None,
    "Newgrange Moon Phase; U 2687; Sellita SW280-1 modificado | Réalta GMT Special Edition; U 2138; Sellita SW330 modificado | Gordon Bennett Special Edition; U 3202; Sellita SW200-1 modificado")
add("Siduna", "siduna", "Suécia", "Landskrona", 2008, None, "Cronógrafos suecos de estilo militar e aviador com calibre de arquitetura 7750.", "store.siduna.watch", "sidunawatch",
    "Expedition Silver; U 2995; base Sellita/ETA 7750 | Aviation Compax Graphite; U 1995; base Sellita/ETA 7750 | Aviation Compax Tuxedo; U 1995; base Sellita/ETA 7750")
add("Signum", "signum", "Polônia", "Varsóvia", 2018, "Kyle Schut", "Relógios de mergulho de desenho limpo e bom custo com automáticos japoneses.", "signumwatches.com", None,
    "Cuda Titanium GMT Full Lume; U 499; NH34 GMT | Sollus Automatic; U 529; Miyota 9039 | Cuda Orange ou Green Sandstone; U 399; NH35/NH38 | Cuda Steel 39mm; U 499; Miyota 9015 | Cuda Steel Full Lume; U 399; NH35/NH38 | Cuda Bronze Cathedral; U 499; -")
add("SLOMO", "slomo", "Canadá", "Toronto", 2025, "Benjamin Moyle", "Relógios minimalistas com Miyota 9039.", "slomowatches.com", None,
    "GLANCE (verde, marrom, azul); U 685; Miyota 9039")
add("Slow Watches", "slow-watches", "Alemanha", "Hamburgo", 2013, "Corvin Lask e Christopher Noerskau", "Relógios minimalistas a quartzo Ronda e solar.", "slow-watches.com", None,
    "Slow Mo 17; U 250; Ronda 505.24 | Slow O 15; U 300; Ronda 505.24 | Slow Jo 31; U 320; Ronda 505.24 | Slow Round 19; U 340; Ronda 515.24 | Solar 05; U 280; VS42A | Solar 06; U 210; VS42A")
add("Smiths", "smiths", "Reino Unido", "Sheffield", 1996, "Eddie Platts", "Relógios militares neo-vintage com Miyota, Sellita e Seiko.", "timefactors.com", None,
    "Everest PRS-25 Black; U 464; Miyota 9039 | W.W.W. PRS-59; G 485; Sellita SW216 Elaboré | PRS-40 Chronograph; G 235; Seiko VK61/VK67 | Navigator PRS-48; G 495; Sellita SW210 | Traveller PRS-58; G 395; Miyota 9075 | Trans-Global Aventurine; G 365; Miyota 9039", "1996 é o ano da marca atual (Timefactors), segundo o Atlas. Mesmo site e fundador da Timefactors, que entra como marca à parte no lote 10.")
add("Solios", "solios", "Canadá", "Montreal", 2019, "Samuel Leroux e Alexandre Desabrais", "Relógios sociais minimalistas movidos a energia solar (Seiko Epson Solar).", "solioswatches.com", None,
    "Solar Classic; U 345; Seiko Epson Solar | Solar Mini; U 345; Seiko Epson Solar | Solar Curve Mini; U 425; Seiko Epson Solar | Sunseeker; U 560; Seiko Epson Solar | Rainforest Classic; U 415; Seiko Epson Solar")
add("Sopwith Watch Company", "sopwith-watch-company", "USA", "Houston (Texas)", 2022, "Stephen Cox", "Relógios de herança aeronáutica com ETA 2893-A2 Élaboré.", "sopwithwatch.com", None,
    "Aero Marquis Messerschmitt Bf 109 Pas-de-Calais; U 4600; ETA 2893-A2 | Aero Marquis Nieuport 28; U 8500; ETA 2893-A2 | Aero Marquis Focke-Wulf Fw 190 Tunisian Desert; U 5700; ETA 2893-A2 | Aero Marquis Focke-Wulf Fw 190 Arctic Sea; U 4900; ETA 2893-A2 | Aero Marquis Focke-Wulf Fw 190 Baltic Winter; U 4900; ETA 2893-A2 | Aero Marquis Thomas-Morse Scout; U 10500; ETA 2893-A2")
add("Specht & Sohne", "specht-sohne", "China", "Shenzhen", 2017, None, "Relógios de estilo homenagem com Seiko VK63, NH35 e Miyota 8215.", "spechtandsohne.com", None,
    "Monaco Gulf Edition; U 370; Seiko VK63 | Royal Chronometer Black; U 299; NH35 | Aviator Silver Edition; U 249; Miyota 8215 | Icon Blue; U 299; NH35 | Monaco X Black Edition; U 299; Seiko VK63 | Chrono; U 399; Seiko VK63", "País: a lista inicial dava EUA; a ficha do Atlas diz Shenzhen, China.")
add("Split Watches", "split-watches", "Reino Unido", "Londres", 2025, "Ed Margulies e Dara Amjadi", "Relógios de desenho autoral com movimentos japoneses (GMT Miyota 9075 e cronógrafos automáticos).", "splitwatches.com", "splitwatches",
    "Westbourne; U 1054; Miyota 9075 GMT | MC-3; G 1800; cronógrafo automático bicompax de base Seiko | Sub-7; G 1800; cronógrafo automático bicompax de base Seiko")
add("STAALBLOCK", "staalblock", "Alemanha", "Rostock", 2012, "Hendrik Mahlitz", "Relógios-ferramenta alemães com Miyota 8245 e 8215.", "staalblock.de", None,
    "Super Size Next Gen Black; U 628; Miyota 8245 | Super Size Casual Black; U 662; Miyota 8245 | Lady's Silver; U 502; Miyota 8215 | No.1 Reduced Black; U 491; Miyota 8215")
add("Sundays Watch Club", "sundays-watch-club", "USA", "Los Angeles", 2019, None, "Relógios minimalistas de madeira a quartzo japonês.", "sundayswatchclub.com", None,
    "Clark; U 55; quartzo japonês | Denali; U 55; quartzo japonês | Rocky; U 55; quartzo japonês | Sequoia; U 50; quartzo japonês | Zion; U 50; quartzo japonês | Congaree; U 60; quartzo japonês", ativa=False)
add("Svalbard", "svalbard", "Hong Kong", "Hong Kong", 2013, None, "Relógios de 24 horas e de um ponteiro só, a quartzo Ronda.", "svalbard.watch", None,
    "Time Travel HX18 Jump Hour; U 190; quartzo GearBox de base Miyota | Aurora AA42B; U 240; Ronda 515.24H | Horizon GA46; U 259; Ronda 515.24H | Defender GA47; U 259; Ronda 515.24H | Traser GA55; U 259; Ronda 515.24H | Combat GB16; U 249; Ronda 513")
add("Swiss Watch Company", "swiss-watch-company", "USA", "Las Vegas (Nevada)", 1996, "Stephen Roemer", "Relógios de campo, mergulho e GMT montados na Suíça com Sellita, ETA e Ronda.", "swcusa.com", None,
    "ARK Yellow; U 225; Ronda 6004.D | Hyper-G Blue; U 595; Sellita SW200 | Tumbler Green; U 750; Sellita SW200-1 | ARK GMT Grey Blue; U 250; Ronda 515.24 | Bunker Dusk; U 495; Sellita SW200 | Convertible Silver; U 1195; ETA 6497")
add("SYE", "sye", "França", "Paris", 2017, None, "Relógios de inspiração automobilística com Seiko NH34, VK64 e Miyota 8215.", "syewatches.com", None,
    "Cannonball GMT Tulsa; U 1039; Seiko NH34 GMT | MOT1ON Chronograph CUT 7 Black DLC; U 734; Seiko VK64 mecaquartzo | Automatic 24 CUT 7 Black DLC; U 892; Miyota 8215")

salvar(sys.argv[1] if len(sys.argv) > 1 else "lote9.json")
