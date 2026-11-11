# -*- coding: utf-8 -*-
"""Lote 8 (11/11/2026): Microbrand Atlas, letras N, O, P e Q (60 marcas). Sem história.
Ficaram de fora Nadir (Polônia) e Proxima (China): a ficha do Atlas não abre (página vazia ou erro)."""
import sys
import lote_base
from lote_base import add, salvar
lote_base.CAMBIO["F"] = ("CHF", 6.5)
lote_base.CAMBIO["B"] = ("BHD", 14.6)
CHF = "Preço do Atlas em francos suíços (convertido a R$ 6,5)."

# ---------- N ----------
add("Naga Watches", "naga-watches", "Itália", "Roma", None, None, "Relógios neo-vintage com cronógrafos VK64 e automáticos Miyota 9039 de mostrador de pedra.", None, None,
    "Granturismo Chronograph 39 (Dakar, Veloce 1976, Amalfi); E 469; VK64 | Opera 39 (Malachite, Lapis Lazuli); E 890; Miyota 9039 | Spire 39 Cosmic Purple; E 790; Miyota 9039")
add("NAMICA Watches", "namica-watches", "Japão", "Izu", 2020, "Charlie e Aki (sobrenomes não informados)", "Relógios minimalistas de desenho japonês com Miyota 9039 e Seiko NH38A.", "namicawatches.com", None,
    "Shirahama 2 Neo Tokyo Evo; U 675; Miyota 9039 | Okami Neo Tokyo; U 630; Miyota 9039 | Shirahama 1 Neo Tokyo Silver; U 500; Seiko NH38A")
add("Nautage", "nautage", "Dinamarca", "Copenhague", 2019, "Allan Junge-Jensen e Christian Schjøll", "Relógios de mergulho minimalistas com Miyota 9039.", None, None,
    "Diver 1 (Black); U 439; Miyota 9039 | Diver 2 (Black/Black); U 599; Miyota 9039")
add("Nazareno Rossetti", "nazareno-rossetti", "Itália", "Roma", 2020, "Fabio Presicce", "Relógios de desenho autoral com movimentos suíços (P224, Sellita SW100).", "nazarenorossetti.com", None,
    "Fomalhaut Bright Winter (2022); U 1814; P224 Swiss Made | Expeditionary W51 Dual Time (2023); U 11811; Sellita SW100", "Preço a conferir: o Expeditionary W51 aparece a US$ 11.811, muito acima do outro modelo.")
add("Neode", "neode", "Reino Unido", "Londres", None, "Marius-Daniel Dumitrascu", "Relojoaria independente de desenho arquitetônico, com calibre de corda manual derivado do Chronode C101.", "neodewatches.com", "neodewatches",
    "N01 First Edition Pure Silver; F 26400; N01 de corda manual (derivado do Chronode C101)", CHF + " Valor antes de impostos.")
add("Nepto", "nepto", "França", "Le Mesnil-le-Roi", 2018, "Vincent Ifrah", "Relógios a quartzo de desenho autoral.", "nepto.net", None,
    "Vultura Apyrit Rose Gold Mesh Metal; U 284; Miyota GL22 quartzo | Green Spectra Brown Pattern Leather; U 324; Miyota 1L22 quartzo")
add("Neuhaus", "neuhaus", "Alemanha", "Augsburg", 2010, "Manuel Neuhaus", "Relógios minimalistas de corda manual com ETA/Unitas 6498 modificado.", "neuhaus.com", None,
    "JANUS DoubleSpeed; U 3248; ETA 6498 (Unitas) modificado | JANUS minimal; U 1990; ETA 6498 (Unitas)", "Site neuhaus.com como aparece no Atlas: conferir (há uma chocolataria de mesmo nome).")
add("Newmark Watch Co", "newmark-watch-co", "Reino Unido", "Londres", 1875, "Wade Newmark", "Relógios militares e de campo neo-vintage com Seiko VH31/VK64 e Miyota 9039.", "newmarkwatchcompany.com", None,
    "52 Field Ivory; G 199; Seiko VH31A | 52 Field Black; G 199; Seiko VH31A | Waterking Black Dial; G 300; Miyota 9039 | Waterking Blue Dial; G 300; Miyota 9039 | 6BB Hydrographic Service (HS) Chronograph; G 500; Seiko VK64A | 6BB Chronograph; U 672; Seiko VK64 mecaquartzo", "O Atlas dá fundação em 1875 e fundador Wade Newmark na mesma ficha (marca histórica relançada?): conferir.")
add("NFW", "nfw-watches", "USA", "Fairfield (Connecticut)", 2005, "George Fox", "Relógios de campo e relógios-ferramenta americanos com Citizen/Miyota e quartzo suíço.", "nfwonline.com", None,
    "AutoPilot 06908; U 479; Citizen 821A | Vector 00605; U 279; quartzo suíço | Shumate Diver 16120 Black DLC; U 799; Miyota 9015 | Shumate GMT 18023; U 799; Miyota 9075 | Valor 14117 ST; U 599; Miyota 9015")
add("Nicholas Hacko Watchmaker", "nicholas-hacko", "Austrália", "Sydney", 2011, "Nicholas Hacko", "Relojoeiro australiano com relógios de estilo aviador, de base suíça e calibre próprio de corda manual.", "nicholashacko.com.au", None,
    "Mark II \"Curl Curl\"; U 5510; base suíça com fabricação própria | Mark 1; U 2929; Soprod M100 | NH1; -; corda manual de fabricação própria")
add("NIMA Watches", "nima-watches", "Itália", "Lucca", 2022, None, "Relógios de aventura com forte luminescência e GMT Seiko NH34.", "nimawatches.com", None,
    "Gravel Trail Shadow; E 545; NH34 | Stage One Blue Hour; E 585; NH34 | Ice Crusher Classic; E 545; NH34 GMT | Stage One \"Starry Night\"; E 545; NH34")
add("Nine Four Watches", "nine-four-watches", "USA", "Milwaukee (Wisconsin)", 2016, None, "Relógios clássicos de estilo americano com Seiko NH35 e mecaquartzo VK63.", "ninefourwatches.com", None,
    "Successor 2 Midnight Blue; U 400; Seiko NH35 | Culture Chronograph 2 (Constellation); U 250; VK63 mecaquartzo | Successor Automatic Rose Gold/Black; U 200; Seiko NH35 | Culture Chronograph 2 Panda/Red; U 250; cronógrafo a quartzo")
add("Ninov", "ninov", "Bulgária", "Sófia", 2024, "Javor Ninov", "Relógios Art Déco com Miyota 9015.", "ninov.watch", None,
    "NV01 Mother-of-Pearl; U 595; Miyota 9015 | NV02 Red; U 595; Miyota 9015 | NV02 Cosmos #3 (Astronaut); U 715; Miyota 9015 | NV02 Provocateur #4; U 855; Miyota 9015 | NV03 Orange; U 700; Miyota 9015 | Lady NV04 Turquoise; U 700; Miyota 9015")
add("Nixoid", "nixoid", "Ucrânia", "Kiev", 2017, None, "Relógios eletrônicos com mostradores de válvulas Nixie/Numitron e LED.", "nixoid.store", None,
    "TimeRed LED \"Radiation\"; U 342; mostrador LED, sem calibre | Nixie Tube Watch \"Numitron Nuclear\"; U 385; válvula Numitron, sem calibre")
add("No-Watch", "no-watch", "Reino Unido", "Greenwich (Londres)", 2012, None, "Relógios de um ponteiro só e 24 horas, a quartzo suíço Ronda 515.24H.", "no-watch.co.uk", None,
    "24 Hours CL1-1212; U 130; Ronda 515.24H | 24 Hours CM1-2413; U 195; Ronda 515.24H | 24 Hours CL1-1312; U 215; Ronda 515.24H | Traveler CL1-1111; -; Ronda 515.24H | 24 Hours CM2-3611; -; Ronda 515.24H | Zulu CM1-2711; -; Ronda 515.24H", ativa=False)
add("Noble Timepieces", "noble-timepieces", "USA", "Fontana (Califórnia)", 2017, "Westley Noble", "Relógios minimalistas de estilo americano a quartzo suíço Ronda.", "nobletimepieces.com", None,
    "Promise; U 225; Ronda quartzo suíço | Sector (Pursuit); U 275; Ronda 515 | Classic (Estate); U 375; Ronda Z60 cronógrafo | Yale (Offset); U 300; -")
add("Noctua Watch Corp.", "noctua-watch-corp", "Canadá", "Edmonton", 2024, "JP Ribeiro", "Relógios-ferramenta de estilo tático com Seiko NH35A e Miyota 9039.", "noctuawatchcorp.com", None,
    "Sentinel Verdant; E 381.95; Seiko NH35A modificado | The Vigil Collection; E 794.95; Miyota 9039 | PD-1; U 441; Seiko NH35A | P-1; U 374; Seiko NH35A")
add("Nordgreen", "nordgreen", "Dinamarca", "Copenhague", 2017, None, "Relógios minimalistas dinamarqueses a quartzo Miyota.", "nordgreen.com", "nordgreenofficial",
    "Infinity 32mm; U 152; Miyota 5Y20 | Native 28mm; U 154; Miyota 5Y20 | Philosopher 36mm; U 229; Miyota GM12-3H | Pioneer 42mm; U 320; Miyota 6S21-6H | Succession 41mm; U 229; Miyota 2115-3H | Unika 28mm; U 274; Miyota 5R21")
add("Normalzeit", "normalzeit", "Áustria", "Viena", 2015, "Fredi Brodman", "Relógios minimalistas vienenses com automático NH35A.", None, None,
    "Der Adjutant; U 998; NH35A | Der Advokat; U 1077; NH35A | Der Amtsrat; U 970; NH35A | Der General; U 970; NH35A | Der Grenadier; U 970; NH35A | Der Hofmarschall; U 1077; NH35A")
add("Northern Star Watch", "northern-star-watch", "USA", "Orlando (Flórida)", 2021, "Shaheen e Noraida Miller", "Relógios esqueletizados modernos com Miyota 90S5.", "northernstarwatch.com", None,
    "White Sentinel; U 649; Miyota 90S5 | Silver Knight; U 849; Miyota 90S5")
add("Northgate", "northgate", "Holanda", "Voorschoten", 2020, "Willem (sobrenome não informado)", "Relógios esportivos de inspiração clássica a quartzo suíço Ronda.", "northgatewatches.com", None,
    "Club 40 St. Barth Azur; U 399; Ronda quartzo | Club 40 Emerald Green (40 mm); E 349; Ronda Normtech 762 | Club 34 St. Barth Azur Gold (34 mm); E 395; Ronda Normtech 762 | Club Diamond Emerald Green Gold (34 mm); E 1245; Ronda Normtech 762 | Club 40 Yuma Yellow (40 mm); E 349; Ronda Normtech 762")
add("Nuncier", "nuncier", "Bahrein", "Manama", 2020, "Talal Fakhroo", "Relógios de mistura cultural, de esqueletizados a aventureiros, com Miyota, Seiko e Sellita.", "nuncier.com", None,
    "Origen N1837 (2022); U 335; Miyota 1S13 quartzo | N200 Gunmetal V2 (2023); U 750; Seiko NH35A | Space Ranger (2024); U 729; Miyota OS21 cronógrafo a quartzo | The Wrong Wrist Edition (2024); U 599; Sellita SW200 | Xkeleton (2024); U 3189; -")

# ---------- O ----------
add("Oan.Gio", "oan-gio", "Vietnã", "Hanói", None, None, "Relógios de mostrador pintado à mão com ETA Unitas 6498-2 de corda manual.", "oangio.watch", "oan.gio",
    "Doodle Spooky Pumpkin; U 1990; ETA Unitas 6498-2 | Damascene Origins; U 2490; ETA Unitas 6498-2 | Aethusa; U 3990; ETA Unitas 6498-2 | Gotham Black; U 1690; ETA Unitas 6498-2")
add("Obelus", "obelus", "França", "Versalhes", 2020, "Christophe Berthommier", "Relógios neo-vintage com Seiko VK64, NH35/NH38 e quartzo Ronda.", "obelus-watches.com", None,
    "Chronoscope \"The Dirty Panda B\"; U 543; Seiko VK64 | Boussole \"The Seas\"; U 435; Ronda 715 | Flashpoint \"Taylor\"; U 457; Ronda | Hydromatic \"Dark Smoke\" (borracha); U 435; Seiko NH35 | Simplissime \"Turquoise\"; U 240; Ronda 762")
add("Oblvlo", "oblvlo", "Hong Kong", "Hong Kong", 2015, None, "Relógios de visual industrial, com automáticos esqueletizados e turbilhões.", "oblvlowatches.com", None,
    "BR Series Tourbillon White Dial (BR-TB-IWWR); U 1599; Hangzhou 36K0 | FM Series White Dial (FM-DSL-YWBL); U 229; Miyota 8215")
add("Oceanica Watch Co.", "oceanica", "USA", "Long Island (Nova York)", 2017, "Erik Handler", "Relógios de mergulho com Miyota 9015 e Seiko NH35.", "oceanicawatches.com", None,
    "Searaven (2024); U 249; Miyota 9015 | Manta Ray (2021); U 349; Miyota 9015 | Mako (2021); U 299; Miyota 9015", ativa=False)
add("Octanis", "octanis", "USA", "Bellevue (Washington)", 2025, "David Johnson", "Relógios GMT de desenho autoral com Miyota.", "octaniswatches.com", None,
    "Sigma GMT 42 Founders Edition; U 749; Miyota 9075 | Gamma; U 650; Miyota 9120")
add("Olivier Jonquet", "olivier-jonquet", "França", "Tarascon", 2013, None, "Relógios sociais Art Déco de caixa almofada com ETA 6498-1 e Miyota.", "montres-oj.fr", None,
    "Galine 1; U 925; Miyota 9029 | Galinette 1; U 645; Miyota 5R21 quartzo | Marine Capitaine Limited Edition 1; U 2210; ETA 6498-1 de corda manual | Steel Capitaine; U 2560; ETA 6498-1 de corda manual | Carrosse; U 2800; ETA 6498-1 de corda manual")
add("Omnis", "omnis", "França", "Paris", 2023, "Francois Lamberdiere", "Relógios de desenho arquitetônico com mostradores de pedra e meteorito, com Miyota.", "omnis-watches.com", None,
    "Luna; E 249; Miyota série 8 | Origin Céramique Tourbillon Météorite; E 1490; - | Era Meteorite; U 579; Miyota 8215 | Sphere Halloween Edition; U 579; - | Luna Stone Dials; U 350; Miyota série 8 | Origin Carbone; U 1035; Miyota 9015")
add("Omologato", "omologato", "Reino Unido", "Windsor", 2015, "Shami Kalra", "Relógios de inspiração automobilística com Seiko VK64, Ronda e Miyota.", "omologatowatches.com", None,
    "Panamericana Oslo (2026); U 600; Ronda 3540 cronógrafo | Arnage (2025); U 1068; - | Maranello (2017); U 531; Ronda | Heritage Racing Chronograph (2022); U 470; Seiko VK64 mecaquartzo")
add("Ontic Watches", "ontic-watches", "Reino Unido", "Hebden Bridge", 2024, "John Hickling", "Relógios minimalistas solares com Ronda 215 Solartech.", "onticwatches.com", None,
    "Utility 40 (5 cores); U 800; Ronda 215 Solartech")
add("OOSIK Tactical Timepieces", "oosik-tactical-timepieces", "USA", "Rockwall (Texas)", 2025, "Brandon Barbieri", "Relógios militares e de mergulho com Seiko NH35.", "oosiktacticaltimepieces.com", None,
    "Sgt. Rock Dive Watch; U 400; NH35 | The Spectrum; U 400; - | Charlie Don't Surf!; U 400; - | Rebel Frogman; U 350; NH35 | SF HALO Dive Watch; U 400; NH35 | SF Combat Diver Watch; U 400; NH35")
add("OraOrea", "oraorea", "USA", "Nova York", 2026, "Zach Starr Weiss", "Relógios sociais com data por ponteiro e Sellita SW386-1.", "oraorea.com", None,
    "Coriolis Pointer Date Venetus Teal; E 3457; Sellita SW386-1 | Coriolis Pointer Date Skyline Silver; E 3457; Sellita SW386-1 | Coriolis Pointer Date Rhodium Black; E 3457; Sellita SW386-1")
add("Origin Watch Co.", "origin-watch-co", "USA", "Memphis (Tennessee)", 2014, "Dennis Shirokov", "Relógios neo-vintage de corda manual com Sea-Gull e ETA 6498.", "originwatch.com", None,
    "Type 20 Aéronavale chronograph (pré-venda); U 500; Sea-Gull ST1901 | Railway Edition Stainless Red 12; U 389; Sea-Gull TY3620 | Railway Edition Stainless Red 12 (versão suíça); U 999; ETA 6498 | Vintage Field Watch 2nd Edition Black; U 359; Sea-Gull TY3600")
add("Oriorwaith J. Sarnowski", "oriorwaith-j-sarnowski", "Reino Unido", "Mold (País de Gales)", 2024, "Jan Sarnowski", "Relógios sociais galeses de inspiração clássica com Miyota 9039 modificado e Seagull de corda manual.", "sarnowski.cymru", None,
    "Y Sgowt First Edition (Lapis Lazuli); U 873; Miyota 9039 modificado | Y Derwydd; U 402; Seagull ST3621 de corda manual | Y Sgowt Onyx; U 739; Miyota 9039 modificado", ativa=False)
add("Orologi Calamai", "orologi-calamai", "Itália", "Florença", 2012, "Francesco Calamai", "Relógios italianos de engenharia própria com Sellita e Valjoux.", "orologicalamai.com", None,
    "G50 Solotempo (2018); U 1429; Sellita SW200 | GMT Automatico (2025); U 2744; Sellita SW330-2 | CR42 Chronograph (2017); U 4803; Valjoux 7750 | G50 Freccia Black (2020); U 4345; Sellita SW510")
add("Orphic", "orphic", "Hong Kong", "Hong Kong", 2023, None, "Relógios de horas vagantes (wandering hours) de estética espacial com Miyota 9039.", "orphicwatches.com", None,
    "Project 0 Wandering Hour Watch; E 668.95; Miyota 9039")
add("Outline", "outline", "Japão", "Tóquio", 2014, "Yoshimasa Kikuchi", "Relógios neo-vintage japoneses com Miyota, Seiko e Seagull.", "outlinewatches.tokyo", None,
    "1980s Rebuild; U 678; Valjoux 7768 | Military 1940; U 312; Seagull TY2705 | Compre Diver; U 305; Miyota 9015 | Partner; U 678; Miyota 9039 | 2 Register Chrono Series I; U 339; Seiko VK64 | Overtime; U 407; TMI NH34")
add("Ovsky Watches", "ovsky-watches", "Polônia", "Poznań", 2019, "Oskar Janiszyn", "Relógios minimalistas neo-vintage a quartzo Seiko VH31.", "ovskywatches.com", None,
    "Dark Stargazer; U 289; Seiko VH31 quartzo")

# ---------- P ----------
add("Paceracer Watch Company", "paceracer-watch-company", "Nova Zelândia", "Auckland", 2017, "Brett Band", "Ateliê independente de inspiração automobilística com automáticos Sellita.", "paceracer.co", "pace.racer",
    "Sangfroid Quartz Original; U 2035; quartzo | Serendipity Automatic; U 2602; Sellita | Reconnaissance Automatic; U 3963; Sellita | Pianist Automatic; U 4246; Sellita | Rubicon Superacer Automatic; U 9631; Sellita")
add("Pacific Watch Co", "pacific-watch-co", "USA", "Camas (Washington)", None, None, "Relógios de campo de estilo americano com movimento Ameriquartz.", "pacificwatch.co", None,
    "Cascadia Field Watch Slate Blue (4 cores); U 368; Ameriquartz (quartzo)")
add("PALMOS", "palmos", "Reino Unido", "Londres", 2021, "Thanos Repanas", "Relógios minimalistas de desenho autoral com Soprod M100.", "palmos-watches.com", None,
    "PALMOS One Steel Gray (2025); U 1050; Soprod M100")
add("Paradigm Horology", "paradigm-horology", "Canadá", "London (Ontário)", None, "Ryan LeClair", "Relógios minimalistas de uso diário com quartzo Miyota e mecaquartzo Seiko VH31.", "paradigmhorology.com", "paradigmhorology",
    "Skyline; U 275; Miyota JP21 quartzo | Mission Series 01; U 250; Seiko VH31 mecaquartzo")
add("Paradisi Watches", "paradisi-watches", "Itália", "Pineto", 2024, "Roberto Paradisi", "Relógios de mergulho em titânio e bronze com La Joux-Perret G100 e ETA 2824-2.", "paradisiwatches.com", None,
    "RP 02 Titanium Grade 23; U 3888; La Joux-Perret G100 | RP 02 Bronze Ampco 18; U 3774; La Joux-Perret G100 | RP 01; -; ETA 2824-2")
add("Parea", "parea", "Austrália", "Sydney", 2025, "Peter Dess", "Relógios neo-vintage de mostrador setorizado com Miyota 9039.", "pareawatches.com", None,
    "Sector (39 mm, 5 cores); U 554; Miyota 9039", ativa=False)
add("PAROS", "paros", "USA", "Hershey (Pensilvânia)", None, None, "Relógios coloridos e descontraídos com NH35 e GMT NH34.", "paros.us", None,
    "Soloist Salmon Blue Automatic; U 250; NH35 | The Salmon Tail; U 250; NH35 | Honeycomb Automatic (Green Dial); U 250; NH35 | Transatlantic GMT Spirit of St. Louis; U 261; NH34A")
add("Paul Bowman", "paul-bowman", "Reino Unido", "Londres", 2021, None, "Relógios de herança britânica (mergulho e militares) com Miyota 8215 e mecaquartzo Seiko.", "bowmanlondon.com", None,
    "Royal's Reserve Automatic 40mm 18K Gold Infusion Gold Dial; E 512.25; Miyota 8215 | Airbus 1700 Calibre MKI 34/45; E 753.30; - | Royal's Reserve Spectrum 40mm Pistachio Green; E 331.45; Seiko VH60 | DESIGNATION Mk1 Greenwich Diver; E 599.03; Miyota 8215 | Britannic Frostguard Series Arctic Blue 69°N 19°E; E 442.94; - | Britannic Frostguard Series Arctic 69°N 19°E; E 442.94; -", "Ano de fundação (2021) aparece no Atlas como inferido: conferir.")
add("Pedral", "pedral", "Suécia", "Estocolmo", 2020, None, "Relógios de desenho arquitetônico com Sellita SW200-1.", "pedral.eu", None,
    "Maestro; U 1487; Sellita SW200-1 b")
add("Perpetual Watch Company", "perpetual-watch-company", "Hong Kong", "Hong Kong", 2005, "Alex Lee", "Relógios neo-vintage com movimentos Sea-Gull, de reguladores a turbilhões.", "perpetual-watch.com", None,
    "Simple Classic (SC-03); U 240; ST1701 | Pointer Moonphase (PM-01); U 350; ST2108 | Tourbillon (RT-01); U 2500; ST8230 | Regulator; U 250; ST1711")
add("Perun", "perun", "Croácia", "Split", 2024, "Ante Kalajžić", "Relógios de mergulho de inspiração clássica com automático suíço e data por ponteiro.", "perun.watch", None,
    "Veles Pearl White (2 cores); U 1544; automático suíço com data por ponteiro")
add("Phorcydes", "phorcydes", "China", "Pequim", 2020, None, "Relógios de mergulho de estilo homenagem com Seiko NH35A e Seagull.", "phorcydes.net", None,
    "PH-6 (couro); U 179; Seiko NH35A | PH-4C V2.0 (couro); U 149; Seiko NH35A ou Seagull ST2130 | PH-5 (pulseira de aço); U 159; Seiko NH35A | PH-2 (pulseira de aço); U 159; Seiko NH35A | PH-1; U 140; Seiko NH35A | PH-3A (FKM); U 139; Seiko VH31 quartzo")
add("Pitzmann Watches", "pitzmann-watches", "Coreia do Sul", "Seul", 2021, None, "Relógios neo-vintage com Sellita SW300-1, Seiko NE88 e quartzo ETA.", "pitzmann.com", None,
    "Heritage (2022); U 1299; Sellita SW300-1 | Pitzmann II (2023); U 1299; Sellita SW300-1 | Pitzmann III (2024); U 1499; Seiko 8R48 (NE88) | Overture Date (2024); U 349; ETA F07.412 quartzo")
add("POLPORA", "polpora", "Polônia", "Zielona Góra", 2006, "Krzysztof Janczak", "Relógios poloneses com mostradores esmaltados e movimentos Sellita e Dubois Dépraz.", "polpora.com", None,
    "Chrobry (2025); U 2534; Sellita SW270-1 M | Kościuszko II (2020); U 1493; Dubois Dépraz 14400 | Enamels (2024); U 3545; Sellita SW300-1 | Aqua Vigor (2018); U 1333; Sellita SW300-1 | Terra Lux Bianco (2021); U 3202; Sellita SW300-1 | Polon Men (2017); U 1601; Sellita SW300-1 Top")
add("Pook Watches", "pook-watches", "Finlândia", "Joensuu", 2018, None, "Relógios finlandeses de desenho autoral com Miyota 8215 e 9039.", "official.pookwatches.com", None,
    "Torni (2024); U 170; Miyota 8215 | Salpa / Military Heritage (2022); U 326; Miyota 8215 | kom / Kompressor (2021); U 452; Miyota 8215 | TBL Thin Blue Line; U 584; Miyota 8215 | Ahjo; U 584; Miyota 8215 | 1938; U 579; Miyota 9039")
add("pOrtahl", "portahl", "Holanda", "Utrecht", 2020, "Jordi van Staveren e Alain van den Donk", "Relógios automáticos com STP1-11 suíço e Miyota 9015.", None, None,
    "Peacemaker (2022); U 599; STP1-11 suíço | Zenmaster (2025); U 685; Miyota 9015", "D genérico: o Atlas não informa o estilo.")
add("Pragma", "pragma", "Suíça", "Genebra", 2024, "Christopher Wegener e Kai-hsuan Liu", "Ateliê independente de desenho arquitetônico com calibre próprio Pragma 1031-1.", "pragma.watch", "pragma_watches",
    "P1 Perseverance Tantalum Azurite Blue; F 34500; Pragma 1031-1", CHF)
add("Primitive Haus", "primitive-haus", "USA", "Seattle (Washington)", None, "Teslim Alabi e Princewill Esekhile", "Relógios de influência Bauhaus com Miyota 82S5.", "primitivehaus.com", None,
    "Timekeeper Type-A (2023); U 329; Miyota 82S5")

# ---------- Q ----------
add("Qannati Objet d'Art", "qannati-objet-d-art", "Bahrein", "Seef", 2018, "Mahmood Qannati", "Relógios de mistura cultural com movimentos suíços (Sellita SW100).", "qannati.com", "qannati",
    "Quantum II Lily; B 1080; Sellita SW100 b | Quantum I Bahrain; B 1240; Sellita SW100 b | Quantum III Leopard; B 400; quartzo suíço", "Preços do Atlas em dinares do Bahrein (convertidos a R$ 14,6), 'a partir de'.")
add("Quasar", "quasar", "Reino Unido", "Stoke-on-Trent", 2022, None, "Relógios de temática espacial com NH35 e Miyota.", "quasarwatches.com", None,
    "NEBULA Automatic Blue Mother of Pearl; E 119; NH35 | ASTROGRAPH Automatic Venus Edition; E 238; Miyota série 8", "O Atlas informa que a marca fechou (registro de 27/04/2026).", ativa=False)
add("Quiet Club", "quiet-club", "Japão", "Sumida (Tóquio)", 2024, "Norifumi Seki", "Relojoaria independente japonesa com movimento próprio feito à mão e alarme mecânico de gongo.", "quietclub.com", "quietclub_watches",
    "Fading Hours (30 peças); U 85000; movimento próprio com alarme mecânico de gongo e martelo", "Preço de referência do Atlas não verificado.")

salvar(sys.argv[1] if len(sys.argv) > 1 else "lote8.json")
