# -*- coding: utf-8 -*-
"""Lote 3 (11/11/2026): Microbrand Atlas, ARC & Co. e toda a letra B (44 marcas).
A pedido do usuário, SEM história (coluna I vazia): ele vai reescrever depois. Só metadados."""
import json, sys
def faixa(p):
    for n, lim in enumerate((1000, 5000, 10000, 20000, 40000, 70000, 100000, 350000, 600000), start=1):
        if p <= lim: return n
    return 10
CAMBIO = {"US$": 5.5, "€": 6.1, "£": 7.2, "S$": 4.2}
M = []
def add(nome, slug, pais, cidade, ano, fund, carac, site, ig, modelos, obs="", ativa=True):
    """modelos: lista de (nome, moeda, preço ou None, movimento ou None)"""
    brl = [p * CAMBIO[m] for _, m, p, _ in modelos if p]
    f = round(sum(brl) / len(brl)) if brl else None
    def linha(n, m, p, mov):
        partes = [x for x in (mov, (f"cerca de {m} {p:,.0f}".replace(",", ".") if p else None)) if x]
        return n + (" — " + "; ".join(partes) if partes else "")
    ficha = "Fundação: " + (str(ano) if ano else "não informada no Atlas") + ". Fundador(es): " + (fund or "não informado no Atlas") + "."
    faltas = [t for t, v in (("H vazio: Instagram não informado no Atlas", ig), ("G vazio: site não informado no Atlas", site), ("E/F vazios: o Atlas não traz preços", f)) if not v]
    M.append({"A": nome, "B": pais, "C": cidade, "D": carac, "E": faixa(f) if f else None, "F": f, "G": site, "H": ig, "I": None,
              "J": "\n\n".join(linha(*x) for x in modelos), "K": None, "L": None,
              "M": "Incluída a pedido do usuário em 11/11/2026 (marcas do Microbrand Atlas que faltavam). Dados da ficha do Atlas (microbrandatlas.com/brand/" + slug + "). " + ficha
                   + " História (I) em branco a pedido do usuário, que vai escrever depois. Preço médio = média dos preços de referência do Atlas convertidos (US$ 5,5; € 6,1; £ 7,2; S$ 4,2) — conferir no site oficial. Logo ainda a buscar. Só a aba Marcas; relógios não pesquisados."
                   + ("" if ativa else " O Atlas marca a marca como inativa (dormant).")
                   + "".join(" " + t + "." for t in faltas) + ((" " + obs) if obs else "")})
U, E, G, S = "US$", "€", "£", "S$"

add("ARC & Co.", "arc-and-co", "Japão", "Tóquio", 2024, None, "Relógios de inspiração Art Déco e world timers com movimentos Miyota.", "arcandcowatches.com", "@arcandcotokio",
    [("World Time WTS-01 Silver", U, 487, "Miyota 9039"), ("Type Art-Deco ADA-01 Asymmetrical Tricolor", U, 480, "Miyota 90S5")])
add("Bahrami Watches", "bahrami-watches", "Canadá", "Vancouver", 2020, "Esfandiar Bahrami", "Relógios de design autoral com mistura de referências culturais, em movimentos Seiko, Miyota e Sellita.", "bahramiwatches.com", "@bahrami.watches",
    [("Adventurer - 05 [Pomegranate]", U, 670, "Seiko NH38"), ("The Lounge (Velvet Oasis, 2025)", U, 960, "Sellita SW200-1B")])
add("Bajer Watches", "bajer-watches", "USA", "Cambridge (Massachusetts)", 2018, "Mehtap Leyla Turanalp Uysal", "Relógios sociais minimalistas com movimento suíço a quartzo.", "thebajer.com", "@bajerwatches",
    [("Basenia Nero", U, 1460, "calibre BAJ-762 GILT (quartzo suíço)"), ("Artemita Chestnut", U, 995, "calibre BAJ-762 GILT (quartzo suíço)"), ("Sophene Champagne Navy", U, 2050, "Swiss Made 1069"), ("Corduene Choco", U, 3290, "Swiss Made BAJ-3520D")])
add("Balticus Watches", "balticus-watches", "Polônia", "Władysławowo", 2015, "Bartosz Knop", "Relógios de mergulho e aventura com movimentos Miyota, ETA e Sellita.", "balticus-watches.com", "@balticuswatches",
    [("Grey Seal", U, 830, "Miyota 9015"), ("New Sky BLT-BALNSSW", U, 257, None), ("Flying Seal Black BALFSQCHBLA", U, 612, "Miyota 6S20"), ("Moonfish Orange BLT-BTMFOR", U, 1139, "Miyota 9015"), ("Moonfish Green BLT-BTMFGR", U, 1139, "Miyota 9015"), ("Flying Seal Blue BALFSQCHBLU", U, 612, "Miyota 6S20")])
add("Baron Watch Company", "baron-watch-company", "USA", "St. Petersburg", 2022, "Mike Baron e Josh Baron", "Relógios de mergulho de tema espacial e preço acessível, com Seiko NH35A.", "baronwatch.co", None,
    [("Stargazer 1.0", U, 260, "Seiko NH35A")], "C: o Atlas diz só 'St. Petersburg, United States' (provavelmente Flórida; conferir).")
add("Batiscafo by Centvm", "batiscafo-by-centvm", "Hong Kong", "Hong Kong", 2019, "Andrei Troff", "Relógios de mergulho em bronze e titânio.", "batiscafo.store", "@batiscafo_watch",
    [("Zero45 Bronze, Green Dial", U, 449, "Seiko NH35A"), ("Zero45 Bronze, Meteorite Dial", U, 549, "Seiko NH35A"), ("Zero45 Bronze, Military Green", U, 679, "ETA 2824-2"), ("Zero45 Titanium, White Dial", U, 689, "ETA 2824-2")])
add("BegHof", "beghof", "França", "Le Mans", 2021, "Nicolas Beguin (cofundador)", "Relógios de uso diário e de aviador, coloridos, com movimentos Miyota.", "beghof.com", "@beghofwatches",
    [("Urban 39 Ruby", U, 572, "Miyota 8315"), ("Urban 39 Phantom", E, 610, "Miyota 9019"), ("Urban 39 Ruby - 2 bracelets", E, 645, "Miyota 9019"), ("Urban 39 Sky Blue - 2 bracelets", E, 645, "Miyota 9019"), ("Urban 39 Navy - 2 bracelets", E, 645, "Miyota 9019"), ("Skull - pulseira de silicone", E, 370, "Miyota 8N24")])
add("Belhamel Watches", "belhamel-watches", "Reino Unido", "Kington (Herefordshire)", 2021, "Fouad Tolaib", "Relógios minimalistas de design autoral com Miyota 9039.", "belhamel.com", None,
    [("Contra A40 (Raisin Black)", U, 738, "Miyota 9039"), ("Contra A39 (Forest Green)", U, 603, "Miyota 9039")])
add("Bellecour", "bellecour", "França", "Morteau", None, "Daniel Montmasson", "Relógios esqueletizados de tradição francesa, com calibres Unitas 6497/6498, ETA e até turbilhão volante.", "montres-bellecour.fr", None,
    [("DM 1995", U, None, "Unitas 6498"), ("DM 1993 Carbone", U, None, "Unitas 6498"), ("DM 1996 Cadran Ouvert", U, None, "Unitas 6498"), ("DM 1994", U, None, "Unitas 6498"), ("DM 3001 Chrono", U, None, "cronógrafo automático"), ("DM 1991", U, None, "ETA automático esqueletizado")])
add("Belvans", "belvans", "França", "Paris", 2023, None, "Relógios sociais clássicos de luxo acessível, com La Joux-Perret G100 e Miyota 8315.", "belvans.com", "@belvans",
    [("Daylee (mostrador branco)", U, 1081, "La Joux-Perret G100"), ("Heritage (Gold)", U, 795, "Miyota 8315"), ("Prestige (mostrador azul)", U, 1707, None)])
add("Benlydesign", "benlydesign", "Hong Kong", "Hong Kong", 2016, None, "Relógios digitais e a quartzo de desenho futurista e preço baixo.", "benlydesignwatch.com", None,
    [("Stargazer (S1000)", U, 99, "digital"), ("G100", U, 104, "digital"), ("Gladiator (X7000)", U, 129, "digital"), ("Cyber (S3000)", U, 129, "digital"), ("Cube (M3)", U, 139, "quartzo Miyota"), ("Feather (M1)", U, 159, "quartzo Miyota")])
add("Bermuda Watch Company", "bermuda-watch-company", "Reino Unido", "Littleborough", 2015, "Anna Marie Henderson", "Relógios clássicos de uso diário e preço baixo, a quartzo e automáticos.", "bermudawatchcompany.com", None,
    [("Somerset Automatic", G, 209, "automático"), ("Hamilton Chronograph", G, 30, "quartzo"), ("Shelly Bay Smart Light", G, 45, "quartzo com luz"), ("Stovel Bay", G, 60, "quartzo")])
add("BERNY", "berny", "China", "Shenzhen", 1995, "Fred Chu", "Relógios de mergulho, campo, piloto e sociais de preço acessível, com movimentos Miyota, Seiko e Seagull.", "bernywatch.com", "@berny.watch",
    [("AM339M Compressor Diver (2023)", U, 300, "Miyota 8215"), ("AMT143M Titanium Field (2024)", U, 150, "Miyota 8215"), ("AM158M Railroad (2024)", U, 111, "Miyota 8215"), ("AM7110VM Dress (2024)", U, 200, "Seagull ST2130"), ("AM127M Pilot (2024)", U, 300, "TMI NH36")])
add("Berthet", "berthet", "França", "Villers-le-Lac", 1877, "Joseph Berthet", "Relógios sociais e esqueletizados de corda manual, sobre base ETA/Unitas 6498 com módulos próprios.", "berthet.com", "@berthethorlogerie",
    [("Imperium Blanche", U, 2859, "ETA/Unitas 6498, reserva de marcha"), ("Noctem Minuit", U, 3087, "ETA/Unitas 6498, reserva de marcha e fase da lua"), ("Classique Seconde à 9:00 Noire", U, 1023, "ETA/Unitas 6498"), ("Linea Squelette Bicolore", U, 1429, "ETA/Unitas 6498 esqueletizado"), ("Agilis Rétrograde Blanche", U, 2001, "ETA/Unitas 6498 com módulo de minutos retrógrados")])
add("Bespo Watches", "bespo-watches", "USA", "Miami (Flórida)", 2024, None, "Relógios de mergulho em tiragens limitadas, com Seiko NH38.", "bespowatches.com", None,
    [("Horizon Diver, Shadow Moon", U, 250, "NH38"), ("Horizon Diver, Polished White–Forest Green", U, 250, "NH38"), ("Horizon Diver, Polished White–Night Sky", U, 250, "NH38"), ("Horizon Diver, Forest Green–Pearl White", U, 250, "NH38"), ("Horizon Diver, Classic Black–Pearl White", U, 250, "NH38"), ("Horizon Diver, Grey–Aventurine", U, 350, "NH38")])
add("Bespoke Watch Projects", "bespoke-watch-projects", "USA", "Oakland (Califórnia)", 2014, "John Beck McConnico", "Relógios americanos feitos em pequenas séries e sob encomenda, com automáticos suíços (ETA 2824-2) personalizados.", "bespokewatchprojects.com", None,
    [("Tabernacle Bicentennial Edition 36mm", U, 650, None), ("Custom Intaglio 38 Iris Sasu Edition", U, 1335, None), ("Intaglio 38 Tonneau \"Modèle Nu\" Radial", U, 925, "ETA 2824-2 / STP1-11"), ("Intaglio 39 Classic \"Neu Sector\" Copper & Carbon", U, 870, "ETA 2824-2"), ("Intaglio 36 Midsize Pulsometer Brass & Carbon Sunray", U, 845, "ETA 2824-2"), ("Super 60", U, 740, "Unitas 3620 (corda manual)")])
add("Beyond Boring", "beyond-boring", "USA", "Seattle", 2020, None, "Relógios de campo e cronógrafos coloridos e baratos, com movimentos VK64 e NH35.", "beyondboringbrand.com", None,
    [("Blue Retro Chronograph", U, 200, None), ("Yellow Sunburst", U, 170, None), ("White Field Watch", U, 130, None), ("Black and Gold Classic", U, 170, None)])
add("Big Idea Design", "big-idea-design", "USA", "Chattanooga", 2011, "Chadwick Parker e Joe Huang", "Relógios-ferramenta de titânio, com movimentos Miyota, SII/Seiko e Epson (solar).", "bigidesign.com", "@bigidesign",
    [("Ti GMT (2025)", U, 975, "Miyota 9075"), ("Ti Field Watch Automatic Stonewashed", U, 199, "SII NH36A"), ("Ti Field Watch Solar Stonewashed", U, 399, "Epson VS43"), ("Ti Daily Solar 2025", U, 275, "Miyota 2070")], "Os preços dos três últimos modelos são 'a partir de'.")
add("Black Corner", "black-corner", "Reino Unido", "Londres", 2015, None, "Relógios de inspiração Art Déco e neo-vintage, do Miyota 8215 a um turbilhão central montado na Suíça.", "black-corner.com", None,
    [("Sailing Stones", U, 750, "Miyota 8215"), ("The Wormhole", U, 3500, "turbilhão volante central 37Z0, montado na Suíça"), ("Neoma Star Nero (Black Corner x Omnis)", U, 1150, "Omnis F28-12 automático")])
add("BlackCat", "blackcat", "França", "Paris", 2025, "JC e François (sobrenomes não informados)", "Cronógrafos meca-quartz Seiko de preço acessível.", "blackcat-watches.com", None,
    [("Shaka Copper Black", U, 270, "Seiko VK64"), ("Shura Grey", U, 325, "Seiko VK73")])
add("Blacklist", "blacklist", "USA", "Cotati (Califórnia)", 2013, "Justin Eterovich", "Relógios de estética industrial e 'anti-vintage', com Miyota 9039/9015, Seiko NH35, meca-quartz e quartzo suíço.", "blacklistwatches.com", "@blacklistwatches",
    [("Black Sunray, Black", U, 300, None), ("Stinger, Black", U, 350, None), ("Verde Ithaca, Black", U, 400, None), ("Glacier Bay Divematic", U, 750, "Miyota 9039"), ("Stinger, Steel", U, 300, None), ("Laguna Seca, Black", U, 400, None)])
add("BND Watches", "bnd-watches", "França", "Valence", 2021, "Vincent Bonnaud", "Relógios de mergulho neo-vintage com Seiko NH38A.", "bnd-watches.com", "@bndwatches",
    [("MNKHA", U, 566, "Seiko NH38A"), ("MNWHI", U, 566, "Seiko NH38A"), ("MNGRA", U, 566, "Seiko NH38A")])
add("Bobwellson", "bobwellson", "Japão", "Tóquio", 2010, "Seiji Namague e Tatori Auchi", "Relógios de mergulho e cronógrafos neo-vintage, com movimentos VK64 e NH35.", "bobwellson.com", None,
    [("LordAtlantis Glorious ERA", U, 413, None), ("LordKraken Legion 8", U, 147, None), ("Capt. Hawk Hijacker", U, 167, None), ("LordAtlantis Pioneer ERA", U, 216.5, None), ("Bronze Emperor Pirate Edition", U, 950, None), ("Legion 7", U, 220, None)], "LordAtlantis Pioneer ERA: o Atlas dá US$ 173–260 (usada a média).")
add("BOMBFROG", "bombfrog", "Alemanha", "Windeby", 2011, "Dirk Assmann", "Relógios de mergulho de estilo militar, automáticos e a quartzo.", "bombfrog.eu", None,
    [("Minesweeper", U, 525, "Seiko NH35"), ("Minesweeper Black", U, 549, "Seiko NH35"), ("Professional 500", U, 268, "Seiko VX42 (quartzo)"), ("Professional 500 Kampfschwimmer Edition", U, 308, "quartzo"), ("Steel Magna II", U, 442, "Seiko NH35"), ("BT-25 Stainless Steel Edition", U, 770, "Seiko NH35")])
add("Bonest Gatti", "bonest-gatti", "Hong Kong", "Hong Kong", 1999, None, "Relógios chamativos e esqueletizados, em caixas tonneau, automáticos e a quartzo.", "bonestgattiwatches.com", "@bonestgattiofficial.time",
    [("BG3004 Animated Dial Quartz (feminino)", U, 289, "quartzo"), ("BG5502 Tonneau Skeleton Automatic", U, 254, "automático"), ("BG5001 Eiffel Tower Tonneau Automatic", U, 239, "automático"), ("BG5005 Moon Phase Automatic", U, 369, "automático"), ("BG5802 Skeleton Automatic", U, 289, "automático"), ("BG4002 Carbon Fiber Automatic", U, 446, "automático")])
add("Borgward", "borgward", "Alemanha", "Efringen-Kirchen", 2010, None, "Relógios sociais e cronógrafos clássicos com movimentos suíços automáticos e de corda manual.", "borgward.ag", "@borgward.watch",
    [("B2300 Chronograph Black", U, 2836, "Valjoux 7750"), ("P100 Deluxe Chronograph Metal Green Grey", U, 7776, "ETA Valjoux 7751")])
add("Boschett Timepieces", "boschett-timepieces", "USA", "Pearl River (Nova York)", 2007, "Keith Boschetti", "Relógios de mergulho neo-vintage.", "boschett-timepieces.com", "@boschett",
    [("Cave Dweller", U, 750, "Sellita SW200"), ("Legacy", U, 385, "Miyota 9015")], ativa=False)
add("Bōken", "b-ken", "Reino Unido", None, None, "Daniel Banks e Ignacio Fernandez", "Relógios-ferramenta britânicos de mergulho e aventura com movimentos Sellita.", "boken.co.uk", None,
    [("The Odyssey (42 mm)", U, None, "Sellita SW200-1"), ("The Breacher (39 mm)", U, None, "Sellita automático")], "C vazio: cidade não informada no Atlas.")
add("Bragdur", "bragdur", "Noruega", "Tønsberg", 2020, "Lars Erik Hansen", "Relógios minimalistas de design norueguês, com Sellita SW200-1/SW330-2 e Seiko VK64.", "bragdur.no", None,
    [("The Orange", U, 715, None), ("Jernmann Protektor Grønn", U, 715, None), ("Porsche Club Norge x Bragdur — Gulf", U, 715, None), ("Dive", U, None, "Sellita SW200-1"), ("Chronograph", U, None, "Seiko VK64"), ("Explorer", U, None, "Sellita SW200-1")], "Preços 'a partir de'.")
add("Branch Horology", "branch-horology", "Canadá", "Trenton (Ontário)", 2019, None, "Relógios de design autoral com materiais incomuns e Sellita SW210-1.", "branchhorology.com", None,
    [("The Sector", U, 411, "Sellita SW210-1")], "Preço a conferir: o Atlas dá faixa de 700–950 (moeda não indicada) e preço de referência de US$ 411 para o The Sector.")
add("Breda", "breda", "USA", "Dallas", 2006, "Amir Meghani", "Relógios de moda de desenho americano, quase todos a quartzo japonês (Miyota/Seiko).", "breda.com", "@bredastudio",
    [("Virgil (Revival)", U, 185, None), ("Jane (Tethered)", U, 195, None), ("Esther", U, 150, None), ("Groove", U, 195, None), ("Pulse (Tandem)", U, 195, None), ("Coda", U, 215, None)], "Pulse (Tandem): o Atlas mostra US$ 195 e US$ 250 (usado 195).")
add("Brigade Watch Co", "brigade-watch-co", "USA", "Nova York", 2024, "Kevin Ding", "Relógios-ferramenta militares e de mergulho com Sellita SW200 e ETA 2824-2.", "brigadewatches.com", "@brigadewatch",
    [("Subcommander Date", U, 1100, "Sellita SW200-1 Elaboré"), ("Subcommander No-Date", U, 1100, "Sellita SW200-1 Elaboré"), ("Pioneer Legend Edition", U, 1150, "Sellita SW200-1b Top"), ("Hurricane", U, 880, "ETA 2824-2"), ("Subcommander Limited", U, 1450, "Sellita SW200-2 Power Plus Elaboré")])
add("Brillier", "brillier", "USA", "Fountain Hills (Arizona)", 2019, "Kunal Naik", "Relógios de tema americano montados em Mesa, no Arizona, com Ameriquartz, Ronda suíço e automáticos importados.", "brillier.com", None,
    [("Air Wing (Americana Chapter 3), 2024", U, 695, "Ameriquartz 7M21"), ("Mono Mechanical Blue, 2022", U, 795, "automático de 29 rubis"), ("Airborne X1 60, 2025", U, 595, "automático importado"), ("Americana Chapter 2 Western Standard Steel, 2021", U, 395, "Ronda 1069 suíço"), ("Americana Chapter 1, 2021", U, 695, None)])
add("Broad & Swan", "broad-and-swan", "Irlanda", "Dublin", 2021, None, "Relógios minimalistas e clássicos com quartzo suíço.", "broadandswan.com", "@broadandswan",
    [("Jack Red (2021)", U, 257, "quartzo suíço"), ("Libertie (2022)", U, 314, "quartzo suíço"), ("Endurance Racer (2023)", U, 555, "cronógrafo suíço")])
add("Brunmontagne", "brunmontagne", "Holanda", "Gorredijk", 2019, "Pascal Bruinenberg", "Relógios sociais minimalistas com Sellita SW200/SW216/SW280 e Seiko NH35.", "brunmontagne.com", None,
    [("Representor Tigereye LE", U, 642, "Seiko NH35"), ("Representor Skeletonized Steel 40mm", U, 642, None), ("Representor Dutch Waffle", U, 514, "Seiko NH35"), ("Representor Malachiet LE", U, 642, "Seiko NH35"), ("Representor (coleção)", U, 380, "Seiko NH35–NH72"), ("Connector", U, 1400, "Sellita SW200"), ("Connector Zilver", U, 1462, "Sellita SW200"), ("Connector Zwart", U, 1462, "Sellita SW200"), ("Ambassador Zilver Small Second", U, 1462, "Sellita SW216"), ("Ambassador (coleção)", U, 1250, "Sellita SW216"), ("Ambassador Blauw Moonphase", U, 1580, "Sellita SW280")])
add("Bruvik", "bruvik", "Noruega", "Haugesund", 2009, "Rune Bruvik", "Relógios de mergulho neo-vintage noruegueses, com automáticos suíços e quartzo.", "bruviktime.com", None,
    [("Fjord Hydracapsule Bronze Blue (edição limitada de 197)", U, 2165, "Sellita SW300"), ("Lady Fjord Misty Morning", E, 1181.95, None), ("Lady Fjord Evening Rose", E, 1181.95, None), ("Lady Fjord Golden Hour", E, 1181.95, None), ("Ambassadør Travel Blue", E, 1219.95, None), ("Lady Fjord Misty Evening", E, 1181.95, None)])
add("Bryan Laurent", "bryan-laurent", "Cingapura", "Cingapura", 2026, None, "Relógios sociais minimalistas com mostradores guilloché e de pedra, com Seiko NH38.", "bryanlaurent.com", None,
    [("Rose Guilloché", S, 500, "NH38"), ("Ruby Guilloché", S, 500, "NH38"), ("Ocean Blue Iris", S, 500, "NH38"), ("Mystic Lapis Lazuli", S, 550, "NH38"), ("Fuchsia Guilloché", S, 500, "NH38"), ("Azure Guilloché", S, 500, "NH38")], "Preços em dólares de Singapura (S$).")
add("BSHQRF", "bshqrf", "Kuwait", "Cidade do Kuwait", 2020, None, "Relógios minimalistas de design autoral com movimentos Miyota e Epson.", "bshqrf.com", None,
    [("The Signature Collection", U, 850, "Miyota 8N24"), ("Antico", U, 950, "Miyota 8217"), ("Solar Elite Special Edition (2024)", U, 700, "Epson VS75"), ("The Eleganza Collection", U, 900, "Miyota 8217"), ("Lusso Automatic – Gold 34mm", U, 1250, "Miyota 8215")])
add("Burnt Creek Watch Company", "burnt-creek-watch-company", "USA", "Bismarck (Dakota do Norte)", 2024, None, "Relógios de campo e ferramenta, com Seiko NH35, Ronda 515 e automáticos suíços.", "burntcreekwatch.com", None,
    [("Sentinel Black", U, 475, "Seiko NH35"), ("Manitou", U, 370, "Ronda 515 (quartzo)"), ("Plainsman", U, 325, "Ronda 515 (quartzo)"), ("Bullion", U, 695, "Sellita SW200-1"), ("Cutbank", U, 695, "automático suíço")])
add("BUUR+", "buur-plus", "Dinamarca", "Dragør", 2017, "Thomas Buur Bækgaard", "Relógios de design dinamarquês com fase da lua e quartzo suíço Ronda.", "buurwatches.com", "@buur_watches",
    [("Tungl Moonphase Black", U, 680, "Ronda 762"), ("Multiscale White Black Markers", U, 680, "Ronda 715")])
add("Buyalov", "buyalov", "Rússia", "Chistopol", 2018, "Dmitry Buyalov", "Relógios de mergulho em titânio e bronze, com Seiko NH35A/NH36A/NH34A e Miyota 82S5.", "buyalov.com", "@buyalov.watches",
    [("RR02.2 Akula (Radioroom), 2020", U, 518, "Miyota 82S5"), ("A67 Titanium, 2022", U, 388, "NH35A"), ("Sevmorput, 2023", U, 450, "NH34A"), ("Classica, 2022", U, 255, "NH35A"), ("NVCH-20, 2021", U, 350, "NH35A")])
add("Bühlmann Watches", "buhlmann-watches", "Suíça", "Arogno", 2020, "Thomas Buhlmann", "Relógios de mergulho profundo suíços com Sellita SW300.", "buhlmannwatches.com", None,
    [("Decompression 02 First Edition Orange", U, 5000, "Sellita SW300"), ("Decompression 02 First Edition \"Druckkammer\"", U, 5000, "Sellita SW300"), ("Decompression 01 \"Druckkammer\"", U, None, "automático suíço")], "O Atlas indica faixa de US$ 3.500–4.000, mas preço de referência de US$ 5.000; conferir.")
add("BVOR", "bvor", "Reino Unido", "Hertsmere (Hertfordshire)", 2019, None, "Relógios de desenho modernista com Miyota 8205 automático.", "bvorwatches.com", "@bvor_watches",
    [("BVOR Vision (Brushed Silver)", G, 549, "Miyota 8205"), ("Aldenham BVOR Vision (Black)", G, 599, "Miyota 8205")])
add("BYOP Watches", "byop-watches", "USA", "Detroit (Michigan)", 2017, "Brian Auré", "Relógios de piloto, campo e GMT de estilo militar, com automáticos Seiko NH e Miyota.", None, "@byopwatches",
    [("Meridian Ti GMT (Orange)", U, 359, "Miyota 9075"), ("Naviator Titanium Ghost GMT (12 Dial)", U, 649, "Miyota 9075"), ("Maverick", U, 395, "Miyota 0S00 (cronógrafo a quartzo)"), ("Aviator", U, 259, "Seiko NH35"), ("Iceman", U, 359, "Seiko NH34")])

json.dump(M, open(sys.argv[1] if len(sys.argv) > 1 else "lote3.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(M), "marcas;", sum(1 for m in M if not m["H"]), "sem Instagram;", sum(1 for m in M if not m["F"]), "sem preço")
