# -*- coding: utf-8 -*-
"""Lote 5 (11/11/2026): Microbrand Atlas, letras F, G e H (55 marcas). Sem história.
Ficaram de fora (ficha do Atlas não abriu): Gotham Watch, Hager Watches, Hult Watch Company."""
import sys
from lote_base import add, salvar

# ---------- F ----------
add("Fam al Hut", "fam-al-hut", "China", "Chongqing", None, "Dai e Lukas", "Alta relojoaria independente chinesa: turbilhão biaxial próprio com hora saltante e dupla retrógrada.", "famalhut.com", None,
    "Mark 1 Mobius; U 42000; turbilhão biaxial próprio, hora saltante e dupla retrógrada")
add("Farasute", "farasute", "China", "Shenzhen", 2020, None, "Relógios sociais e homenagens com movimentos chineses (Seagull, Peacock, Hangzhou) e Seiko.", "farasute.com", None,
    "2324B; U 179; Seiko VK64 (meca-quartz) | 2260; U 188; Seagull ST1721 | 5506B-1; U 316; Farasute Cal. FY001 | 5506B; U 298; Farasute Cal. FY001 | 5331; U 628; Peacock SL4801 | 5336A; U 168; Hangzhou")
add("Fateh Watches", "fateh-watches", "Malásia", "Shah Alam", 2016, "Tuan Haji Zainal Mohd Ali", "Relógios sociais malaios, de homenagem e inspiração cultural.", "fatehwatches.com", "fatehwatches",
    "Batheq Azure Blue; U 1175; - | Peramosa Noir Black; U 869; - | Strata Edition 01 Tarum Blue; U 784; - | The Legacy Series Navy Blue; U 784; - | Automatic Moonphase Skeleton Strata Silver Black; U 367; automático")
add("Felix Toucan", "felix-toucan", "USA", "Portland (Oregon)", 2022, None, "Relógios de moda divertidos com quartzo Ronda 763.", "felixtoucan.com", "felixtoucan",
    "JAWS; U 120; Ronda 763 | Mr Bones; U 110; Ronda 763 | Time for Ramen; U 120; Ronda 763 | ROBOTO; U 120; Ronda 763 | RADAR; U 110; Ronda 763 | A Maze Ing; U 120; Ronda 763", ativa=False)
add("Feynman Timekeepers", "feynman-timekeepers", "Cingapura", None, 2018, None, "Relógios de alto padrão com mostradores de esmalte e pedra.", "feynman.watch", "feynman.watch",
    "Q (Malachite, Tiger's Eye, Malachite Steel); E 524; Ronda 1014 | Coalesce \"The Panda\"; E 6279; - | VI Midnight Blue; E 1172; ETA 7001 | Fjorde \"Magma\"; E 1062; ETA 2895-2", "Preços 'a partir de'.")
add("Fieldstand", "fieldstand", "México", "Chihuahua", 2012, None, "Relógios de campo mexicanos de preço baixo.", "fieldstand.com", "fieldstand_official",
    "Mohinora Marine; U 89; - | Mohinora Original; -; - | Mohinora Aluminium; U 149; - | Mohinora Corima; U 89; - | Mohinora Copper; U 199; - | Mohinora Track; U 89; -")
add("FineWatchesBerlin", "finewatchesberlin", "Alemanha", "Berlim", None, "Wilfried Liefer e Mia-Phyllis Liefer", "Relógios de estilo mid-century com automáticos Miyota, com nomes de lugares de Berlim.", "finewatches.berlin", None,
    "TEUFELSBERG Silber #3; E 698; Miyota automático personalizado | HansaViertel #1; E 749; Miyota 821A", "Preços 'a partir de'.")
add("Firle Watches", "firle-watches", "Reino Unido", "Firle (East Sussex)", 2021, None, "Relógios clássicos de inspiração automobilística com STP1-11.", "firlewatches.com", "firlewatches",
    "No. 001 Sennen Automatic, White & Stainless Steel; U 1176; STP1-11 | Sennen Automatic, Green & Stainless Steel, Cognac; E 417; STP1-11", "Os dois preços do Atlas são muito diferentes; conferir.")
add("Fjordson", "fjordson", "Bélgica", "Antuérpia", 2017, "Jonathan e Charlotte (sobrenomes não informados)", "Relógios sociais minimalistas a quartzo.", "fjordson.com", "fjordson",
    "#SLIM White Dial / Red Rubber (unissex); U 340; - | SLIM White Dial / Vegan Leather Strap; U 342; - | White Dial / Black NATO (feminino); U 282; Ronda 1019 | #SLIM White Dial / Blue Rubber (unissex); U 352; Ronda 1019 | 9142 Black Dial / Brown Rubber (masculino); U 283; -")
add("Forteller", "forteller", "Noruega", "Oslo", 2020, "Sven Even", "Relógios de mergulho de inspiração clássica.", "forteller-watches.com", "fortellerwatches",
    "Engineer Diver; U 269; Miyota 9039", ativa=False)
add("Fortuna Chronometrie", "fortuna-chronometrie", "Alemanha", "Worms", 2015, "Jannes Vollmuth", "Relógios clássicos de estilo mid-century, a quartzo e automáticos.", "fortuna-watch.com", None,
    "Lincoln Small Second (Black); U 250; TMI VH60 (quartzo) | Born to Dive (Blue); U 950; automático suíço | Caspar GMT; U 300; Ronda (quartzo, dois fusos) | Tenera MIA; U 280; quartzo | MIA; U 350; - | Lilli; U 300; -")
add("Forward Watch Co.", "forward-watch-co", "USA", "Houston (Texas)", 2017, "Chase Mardis", "Relógios de uso diário de design autoral com temas do Texas, com Miyota.", "forwardwatchco.com", "forwardwatchco",
    "The Stars at Night (pré-venda); U 550; Miyota 9039 | The Gonzales (pré-venda); U 550; Miyota 9039 | Palo Duro (2026); U 550; Miyota 9039", "D: 'temas do Texas' vem dos nomes dos modelos; conferir.")
add("Fukushima Watch Co.", "fukushima-watch-co", "Japão", "Minamisōma", 2022, None, "Relógios japoneses de Fukushima com movimentos Miyota.", "shop.fukushima-watch.com", "fukushima_watch.co",
    "Odaka; E 344; Miyota 82S5 | SAVE UKRAINE WATCH; E 115; Miyota 2035 | Futaba; E 459; Miyota 82S0 | TYPE-03 Kayairo; E 1146; Miyota 9039")
add("FUTURE FUNK", "future-funk", "Japão", "Tóquio", 2017, None, "Relógios retrô-futuristas a quartzo, com mostrador de rolos e LED.", None, None,
    "KF103-BK-MT; U 100; - | KF103-SV-MT; U 100; - | KF301-YG-BK; U 150; - | KF302-BK-BK; U 50; - | KF302-SV-BK; U 50; - | FF104-SV-RB; U 112; quartzo de rolos")

# ---------- G ----------
add("Galo", "galo", "Austrália", "Sydney", 2020, "Zeca Amendola", "Relógios de mergulho de uso diário com Miyota 9039 e NH35.", "watchesgalo.com", None,
    "Copper; E 249; NH35 | Enamel; E 249; NH35 | Novo Cruisin; E 483.95; - | Super200; E 446.95; Miyota 9039 | Super200 Dark Edition; E 483.95; Miyota 9039")
add("Gambrell Rénard", "gambrell-renard", "USA", "Austin (Texas)", 2014, None, "Relógios de design autoral com mecânicos suíços (FHF 96, ETA 2824).", None, "gambrellrenard",
    "Étincelant; U 25000; FHF 96 | KJM Part 1; U 11089; suíço de corda manual | Chocolate Tiger; U 4989; automático suíço | Time Machine Black; U 3989; FHF 96 de corda manual | Steel-Tec; U 3989; ETA 2824 | Régal de fer; U 3989; automático suíço")
add("GB Watch Co.", "gb-watch-co", "USA", "Carmel-by-the-Sea (Califórnia)", 2019, "Monika Greenaway", "Relógios infantis a quartzo.", "gbwatchco.com", None,
    "Carmel Sand; U 37; quartzo | Sierra White; U 37; quartzo | Active Blue Kids Watch; U 29; quartzo | Lux Rose Gold Kids Watch; U 32; quartzo | Black Lux Kids Watch; U 42; quartzo")
add("Geist", "geist", "Reino Unido", "Birmingham", 2026, None, "Relógios de aventura coloridos com Miyota 9015 (lançamento em breve).", "geistwatches.com", None,
    "Tiki (5 cores, em breve); U 698.75; Miyota 9015")
add("Geltier", "geltier", "Suécia", "Estocolmo", 2020, None, "Relógios de estilo mid-century com Seiko VK64 e VD54.", "geltier.com", None,
    "Crescent C40S Gray; U 250; - | Apex A40G Deep Ocean; U 250; Seiko VK64 | Legacy L40G Ivory; U 250; Seiko VD54 | Legacy L40G Forest; U 250; Seiko VD54 | Apex A40G Polar; U 250; Seiko VK64")
add("Genius Watches", "genius-watches", "Suíça", "Lugano", 2020, "Théodoros Ornithopoulos", "Relógios sociais de design autoral com Sellita automático ou quartzo suíço.", "geniusxgenius.com", None,
    "QATAR (5 cores); U 1150; - | HERACLES (5 cores); U 1750; -", "Preços 'a partir de'.")
add("Geo", "geo", "USA", "San Juan (Porto Rico)", 2023, "Georshua Castro", "Relógios-ferramenta porto-riquenhos de inspiração local, automáticos e a quartzo.", "geoshop.co", "geoshop.co",
    "Cofresi Tool Navigator Black PVD; U 550; Miyota 82S5 | Islandtime Automatic GMT Vol.1; U 500; Seiko NH34 | Turquesa Whitesand; U 350; Seiko NH35 | Campo Día Full-Lumed 39mm Silver; U 250; Miyota 1L45 | Bio Bay Two Tone Gold; U 165; Miyota (quartzo) | Retro Future LED Digital SS; U 99; LED")
add("Geylang Watch Co", "geylang-watch-co", "Cingapura", "Cingapura", 2024, None, "Relógios de design autoral de Singapura, com NH35/NH72 e meca-quartz.", "geylangwatchco.store", None,
    "Geylang Lorong O - Carbon Field Watch; E 570.95; NH35/NH72 ajustado | APEX - Hybrid Chronograph; E 319.95; meca-quartz")
add("GhostTown", "ghosttown", "Cingapura", "Cingapura", 2021, None, "Relógios de desenho artístico e inusitado.", "ghosttownwatches.com", None,
    "Old West Watch; U 250; Ronda 515.24D (quartzo)")
add("Ginault Watches", "ginault-watches", "USA", "Lake Tahoe (Nevada)", 2011, None, "Relógios de mergulho de estilo homenagem com calibre Ginault 7275.", "ginault.com", None,
    "Ocean Rover II (2023); U 1349; Calibre 7275 | Silent Service (2021); U 1499; Calibre 7275 | Expeditioner (2022); U 1325; Calibre 7275 | Trans-Atlantic (2025); U 1698; Calibre 7275", "Ocean Rover II: o Atlas dá US$ 1.199–1.499 (usada a média).")
add("Gloriousdays", "gloriousdays", "Reino Unido", "Londres", 2021, None, "Relógios minimalistas com caixa de bambu.", "enjoygloriousdays.com", None,
    "Clipper; U 90; Miyota 2035 | Bambijou; U 90; Miyota 2035 | Catalina; U 90; Miyota 2035 | Bambu White; U 90; Miyota 2035 | Bambu Blue; U 90; Miyota 2035 | Bambu Black; U 90; Miyota 2035", "Movimento a conferir: os modelos citam Miyota 2035, mas outra parte da ficha cita Seiko NH35 e VK64.")
add("Good + Evil", "good-evil", "USA", "Brooklyn (Nova York)", 2024, None, "Relógios de desenho arquitetônico e marcante.", "goodplusevil.com", "good.plus.evil",
    "Ways Watch; E 306; - | Omen Watch; E 262; Ronda (quartzo)")
add("Grandeur Watches", "grandeur-watches", "USA", "Missouri City (Texas)", None, None, "Relógios sociais e esqueletizados de luxo acessível, com hora saltante e módulos próprios.", "grandeur-usa.com", "grandeur",
    "Viridis Flux; E 2899.95; - | Turquoise Tellus; E 2899.95; - | Noctis Astra; E 2899.95; - | Lapis Regalis; E 2899.95; - | Aureus Strata; E 2899.95; - | Strange Quartz Guilloché Enamel – Indigo Blue; E 897.95; -", "Movimentos citados no Atlas: Miyota 9039, Sellita SW200-1, Hangzhou 37Z0E.")
add("Greg Stevens Design", "greg-stevens-design", "USA", "South Jordan (Utah)", 2005, "Greg Stevens", "Relógios de engenharia própria com Miyota 9015 e Sellita SW200-1.", "gregstevensdesign.com", None,
    "GSD-3A Pilot; U 645; Miyota 9015 | GSD-3A Explorer; U 500; Miyota 9015 | GSD-5A Diver; U 695; Sellita SW200-1")
add("Grimoldi Milano", "grimoldi-milano", "Itália", "Milão", 1964, "Anselmo Grimoldi", "Relógios de inspiração Art Déco com automático suíço (ETA 2824-2).", "grimoldiwatches.com", None,
    "G.T.O. (Cobalt, Gold, Hawthorn, Red Portofino, Space); -; ETA 2824 | Zubenelgenubi (com Ercole Pignatelli); E 7438.52; automático")
add("Gruppo Ardito Watches", "gruppo-ardito-watches", "Itália", "Alessandria", 2013, "Fabio Chiappino", "Relógios-ferramenta e de mergulho italianos com Sellita SW200, GAW001 e Landeron 72.", "gaw-gruppoarditowatches.com", None,
    "Lince (2020); U 1340; Sellita SW200 | NumeroZero New Edition (2023); U 2268; Sellita SW200 | NumeroUno (2017); U 1500; GAW001 modificado | Kraken (2019); U 1588; GAW001 modificado | Dandy (2018); U 1528; GAW001 modificado | Centauro (2024); U 2802; Landeron 72 modificado")
add("Guild Timepieces", "guild-timepieces", "USA", "Macon (Geórgia)", None, None, "Relógios-ferramenta militares americanos com Seiko NH35/NH34.", "guildtimepieces.com", "guildtimepieces",
    "Mark V - Bronze Heritage Diver; U 495; Seiko NH35 | Mekong - Black Ops; U 370; Seiko NH35A | Domitor - Titanium Fixed GMT; U 545; Seiko NH34 | FTD - Titanium Pilot: Interceptor Green; U 395; Seiko NH35A | Mekong - Napalm; U 370; Seiko NH35A")
add("Gurlevik", "gurlevik", "Turquia", "Istambul", 2024, "Yusuf Ozdemir", "Relógios turcos de inspiração arquitetônica e cultural com movimentos Miyota.", "gurlevik.co", "gurlevikwatches",
    "Lale; U 599; Miyota automático | Girih; U 325; Miyota 8215 | Ferseng; U 890; Miyota 9039 | The Dome 02; U 599; Miyota 9039 | Gates; U 600; Miyota automático | Discovery; U 299; Miyota automático")

# ---------- H ----------
add("H2O", "h2o", "Alemanha", "Sottrum", 2010, "Clemens Helberg", "Relógios de mergulho e ferramenta alemães com ETA, Sellita e Miyota.", "h2o-watch.com", None,
    "Green Ocean Timascus; E 2021.81; ETA 2824-2 | Kalmar 2 Carbon; E 1426.81; ETA 2892 ou Sellita SW300 | Kalmar 2 Bronze; E 940.10; Miyota 9015 | Kalmar Chronograph SS + Bronze; E 2023; - | Navale Limited Edition 2020; E 534.31; Miyota 9015 | Orca Dive Polished; E 1178.10; ETA 2824")
add("Hagley West", "hagley-west", "Reino Unido", "Berkhamsted", 2017, "Tim Hayden", "Relógios clássicos de uso diário a quartzo.", "hagleywest.com", "hagleywestwatches",
    "Chrono Navigator; G 159; quartzo japonês | Chrono Pioneer; G 159; quartzo japonês | Sport HWW913; G 159; Miyota OS21 | Classic HWW831; G 139; quartzo japonês | Entrepreneur PATIENCE; G 139; 2115 | Entrepreneur RISK; G 139; 2115")
add("Haigh & Hastings", "haigh-hastings", "Austrália", "Sydney", 2019, None, "Relógios de mergulho de design autoral com Seiko NH38 e NH35A.", "haighandhastings.com", None,
    "M2 Blue Ring; U 300; Seiko NH38 | Classic (branco/preto); U 100; NH35A")
add("Halchimy", "halchimy", "França", "Paris", 2012, "Kevin Oualli e Nicolas Oualli", "Relógios de engenharia própria e desenho único com automático suíço.", "halchimy.com", "halchimy",
    "Intuition (2020); U 6199; automático suíço | Audace Lune Noire (2019); U 4516; automático suíço")
add("HappieWatch", "happiewatch", "Hong Kong", "Hong Kong", 2019, None, "Relógios artísticos e lúdicos com duplo quartzo japonês.", "happiewatch.com", None,
    "Crimson Octopus Art Dial; U 229; duplo quartzo japonês | The Chameleon Watch; U 249; duplo quartzo japonês | Medusa Crimson Edition; U 229; duplo quartzo japonês | The Magician Rabbit Watch; U 249; duplo quartzo japonês | The Tiny Master Watch; U 229; duplo quartzo japonês")
add("Haven Watch Co", "haven-watch-co", "USA", "Fort Wayne (Indiana)", 2018, "Weston Cutter", "Cronógrafos e relógios de uso diário de luxo acessível com Sellita suíço.", "havenwatchco.com", "havenwatchco",
    "Chilton (2019); U 1799; Sellita SW510M | Chilluminati (2022); U 1999; Sellita SW510MBHa modificado | Lomax (2022); U 2050; Sellita SW360 | Trotter (2022); U 1699; GMT | Dato (2024); U 2050; Sellita SW510M | LIVE Series/Metro x Haven (2023); U 1699; Sellita SW360")
add("Havid Nagan", "havid-nagan", "USA", "Los Angeles", 2022, "Aren Bazerkanian", "Alta relojoaria independente com mostradores de esmalte e movimentos desenvolvidos com a Chronode.", "havidnagan.com", None,
    "HN02; -; acabamento manual (colaboração Chronode) | HN01 Lucine; -; fase da lua misteriosa | HN00; -; acabamento manual (colaboração Chronode) | Classic One; -; acabamento manual | Origins; -; - | Millesime; -; -")
add("Heitis Watch Company", "heitis-watch-company", "USA", "Buffalo (Nova York)", 2015, "Donald Heider", "Relógios minimalistas e modernistas com Ronda, ST19 e Miyota 9015.", "heitiswatch.com", None,
    "Classic; U 199; quartzo | Aviator; U 189; Ronda 705 | Chronograph; U 199; 0S20 | ST19 Chronograph; U 479; ST19 | Okeanos; U 499; automático")
add("Helgray", "helgray", "Canadá", "Beaconsfield (Quebec)", 2014, "Nadim Elgarhy", "Cronógrafos neo-vintage de inspiração automobilística com Miyota e Seiko.", "helgray.com", "helgray",
    "Superfast Automatic Silver Panda; U 499; - | Le Mans (Legend Rose Gold); U 149; Miyota 6S21 | Speedster (Racing Light Blue); U 149; Miyota 6S21 | Speedster (Silver Panda); U 149; Miyota 6S21 | Brigadier Automatic; U 129; NH35")
add("HGP Dive Watches", "hgp-dive-watches", "França", "Besançon", 2023, "Charles, Maximilien e Jonathan (sobrenomes não informados)", "Relógios de mergulho neo-vintage com Seiko e Miyota.", "hgp-watches.com", "hgp_hommes_grenouilles_paris",
    "Night Diver 200M Automatic; U 492; Seiko NH35 | Night Diver 200M Automatic Full-Lume; U 450; Seiko NH35 | Diver 200M Chrono-Mecaquartz; U 350; Seiko VK64 | Diver 200M Mecaquartz (azul, amarelo, laranja); U 250; Seiko VH31")
add("Hilts", "hilts", "Canadá", "Stoney Creek (Ontário)", 2019, "Steven Fernandez", "Relógios de inspiração automobilística e clássica com Miyota 6S21 e Sellita SW200-1.", "wearehilts.com", "wearehilts",
    "Monaco '29 Chrono; U 600; Miyota 6S21 | Speedway Chrono; U 600; Miyota 6S21 | Sarthe '70 Chrono; U 600; Miyota 6S21 | Hero Diver Umbra 40mm Auto; U 2000; Sellita SW200-1 | Heritage FL1A 40mm Auto; U 2000; Sellita SW200-1 | Heritage Pointer 40mm Auto; U 2000; Sellita SW200-1")
add("HKED", "hked", "Hong Kong", "Hong Kong", 2017, "Ed (Eddy Tse)", "Cronógrafos de bom custo-benefício com Seagull ST1901.", "hkedwatches.com", None,
    "Acrylic ED63 Classic Cream; U 308; Seagull ST1901 | Acrylic ED63 Sunburst Blue Reverse Panda; U 293; Seagull ST1901 | Sunburst Blue (42 mm); U 399; Seagull ST1901", "Dois preços vêm de dólares de Hong Kong, já convertidos pelo Atlas.")
add("HMNWatch", "hmnwatch", "USA", "Boulder (Colorado)", 2021, None, "Relógios de inspiração automobilística a quartzo Miyota.", "hmnwatch.com", "hmnwatch",
    "HMN V12 Cullinan; U 149; Miyota (quartzo) | BMW Bimmer Series; U 99; Miyota (quartzo) | Speed Star GT; U 99; Miyota (quartzo) | F1 Racing Series (HMN Apex Trackmaster); U 150; Miyota (quartzo)")
add("Hook + Gaff", "hook-gaff", "USA", "West Columbia (Carolina do Sul)", 2014, "Michael Sims", "Relógios americanos de pesca e aventura com quartzo suíço.", "hookandgaff.com", None,
    "Sportfisher White Dial (2015); U 550; quartzo suíço | Field Watch (2018); U 365; quartzo suíço | Diver Black Bezel (2023); U 685; quartzo suíço")
add("HoraPictor", "horapictor", "Hong Kong", "Hong Kong", 2017, None, "Relógios com mostradores de esmalte e cloisonné, com Sellita SW200.", "horapictor.com", "o_horapictor",
    "Volcano Grey (2026), esmalte; U 2592; Sellita SW200 | Totem Cipher (2026), cloisonné; U 4092; Sellita SW200")
add("Horloscaphe", "horloscaphe", "França", "Paris", 2017, "Hacene Mouhoubi", "Relógios de mergulho de estilo militar com Ronda 715 Li e STP1-11.", "horloscaphe-watches-paris.com", "horloscaphe.watches",
    "NC 003 Orange; U 396; Ronda 715 Li | NC 003 Scaphtek; U 396; Ronda 715 Li | NC 003 Fluide; U 515; Ronda 715 Li")
add("Horpa Watches", "horpa-watches", "Índia", "Mumbai", 2017, "Rajeev Asrani", "Relógios indianos de inspiração cultural, com quartzo japonês e NH35.", "horpawatch.com", "horpawatch",
    "One Happy Island; -; SII VD78A | Military; -; - | Monarch; -; - | Navy; -; - | Royal; -; - | Lavender; -; -", "Preços não usados: o Atlas mostra valores de 8.000 a 17.500 marcados como dólares, que parecem ser em rúpias. Conferir no site.")
add("Höglund & Sons", "hoglund-sons", "USA", "Minneapolis", 2019, "Brandon e Zachary Höglund", "Relógios de desenho arquitetônico com Seagull ST1901 e Seiko NH34.", "hoglundandsonswatches.com", None,
    "Mark III GMT; U 250; Seiko NH34 | Mark IV Chronograph Panda Dial; U 199; Seagull ST1901 | Mark IV Chronograph Reverse Panda; U 199; Seagull ST1901 | Mark III GMT Aventurine; U 249; Seiko NH34")
add("Hrotsky", "hrotsky", "Bulgária", "Sófia", 2021, "Alex Hrotsky", "Relojoaria independente búlgara com De Bortoli DB6 suíço modificado e ETA 2824-2.", "hrotsky.com", "hrotsky_watches",
    "Flame Blue; -; De Bortoli DB6 modificado | Via Lactea; -; -")
add("HTD Watches", "htd-watches", "Itália", "Florença", 2020, "Federico Del Guerra e Federico Zulian", "Relógios neo-vintage italianos com Miyota 9039, Sellita SW510M e Seagull ST19.", "htdwatches.com", "htdwatches",
    "Hesagraph RitmoCorsa; U 2100; Sellita SW510M | HTD Phantom L.E.; U 690; Miyota 9039 | Chic Velvet Black; U 800; Miyota 9039 | Chic Forest Green; U 800; Miyota 9039 | Chic Champagne Rose; U 690; Miyota 9039 | Tennis Terra; U 800; Miyota 9039")
add("Huizen Watches", "huizen-watches", "Austrália", "Sydney", 2021, None, "Relógios de mergulho e esqueletizados com automáticos Seiko NH e Miyota.", "huizenwatches.com", "huizenwatches",
    "HUI092; E 264.95; Seiko NH | HUI001-S; U 711; Seiko NH | HUI017 (Seiko Mods); E 363.95; Seiko SRPB99 | HUI007-S Mechanisch; E 529.95; Seiko NH esqueletizado | HUI008-S Mechanisch; E 529.95; Seiko NH esqueletizado | HUI009-S; E 430.95; Seiko NH")
add("Humbert-Droz", "humbert-droz", "França", "Besançon", 2016, "Julien Humbert-Droz", "Relógios de campo e sociais montados na França com calibres La Joux-Perret e ETA.", "humbert-droz.fr", "humbert.droz.watches",
    "HD10 \"Porte Noire\"; U 980; La Joux-Perret G1A0 | HD11 \"Germinal\"; U 950; La Joux-Perret G100 | HD6.1 Solaire; U 2889; La Joux-Perret L100 | HD7 \"Pulsomètre\" Orange; U 1290; ETA 7753 | HD8 Vésuve (couro); U 890; La Joux-Perret G100 | HD1 «Équinoxe»; U 750; ETA 2824 | HD Lou Électrique Rose; U 249; - | HD9 Deep Pro 2; U 980; -")
add("Humism", "humism", "Cingapura", None, 2018, "David Sze", "Relógios de arte cinética, com discos esqueletizados em movimento e Seiko NH35A.", "humism.com", "humism",
    "Kato; U 318; NH35A | Dasein; U 298; NH35A | Rhizome; U 318; NH35A | Eudaimonia; U 298; NH35A | Geist; U 298; NH35A | Eidos; U 348; NH35A", "D: 'arte cinética' é conhecimento geral; o Atlas diz só 'anti-vintage, skeleton'. Conferir.")

salvar(sys.argv[1] if len(sys.argv) > 1 else "lote5.json")
