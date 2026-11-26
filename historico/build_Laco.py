# linhas: (nome, codigo, img, carac)
L=[]
def a(n,c,i,e): L.append((n,c,i,e))
M='https://www.laco.de/media/'
# Pilot Watch Original (site oficial, categoria)
orig=[("Replika 55 A","862194","66/2d/c3/1792075629/laco-fliegeruhr-replika-55-laco-fliegeruhr-replika-55-baumuster-A-soldat.webp?ts=1792134062","55 mm, corda manual, mostrador Baumuster A. Réplica do B-Uhr de 55 mm. € 3.950."),
("Replika 55 B","862195","15/ee/56/1792075664/laco-fliegeruhr-replika-55-laco-fliegeruhr-replika-55-baumuster-B-soldat.webp?ts=1792134056","55 mm, corda manual, mostrador Baumuster B. € 3.950."),
("Saarbrücken","861752","89/b1/13/1751014913/laco-fliegeruhr-typ-a-saarbruecken-861752-neu-20201.png?ts=1751014913","45 mm, automático, mostrador tipo A. A partir de € 930."),
("Westerland","861750","b1/01/2f/1751014926/laco-fliegeruhr-typ-a-westerland-861750-neu-20201.png?ts=1751014926","45 mm, corda manual, mostrador tipo A. A partir de € 930."),
("Friedrichshafen","861753","30/7a/74/1751014897/laco-fliegeruhr-typ-b-friedrichshafen-861753-neu-20201.png?ts=1751014897","45 mm, automático, mostrador tipo B. A partir de € 930."),
("Dortmund","861751","e7/e7/e8/1751014901/laco-fliegeruhr-typ-b-dortmund-861751-neu-20201.png?ts=1751014901","45 mm, corda manual, mostrador tipo B. A partir de € 930."),
("Münster","861748","9b/ba/59/1751014918/laco-fliegeruhr-typ-a-muenster-861748-neu-2020_1.png?ts=1751014918","42 mm, automático, mostrador tipo A. A partir de € 930."),
("Memmingen","861746","79/10/b9/1751014922/laco-fliegeruhr-typ-a-memmingen-861746-neu-2020.png?ts=1751014922","42 mm, corda manual, mostrador tipo A. A partir de € 930."),
("Paderborn","861749","e5/67/3a/1751014909/laco-fliegeruhr-typ-b-paderborn-861749-neu-2020.png?ts=1751014909","42 mm, automático, mostrador tipo B. A partir de € 930."),
("Leipzig","861747","0c/a6/ec/1751014905/laco-fliegeruhr-typ-b-leipzig-861747-neu-2020.png?ts=1751014905","42 mm, corda manual, mostrador tipo B. A partir de € 930."),
("Heidelberg","862094","1f/b4/65/1751015460/laco-fliegeruhr-typ-a-heidelberg-862094-neu-2020.png?ts=1751015460","39 mm, automático, mostrador tipo A. € 930."),
("Mülheim an der Ruhr","862092","43/e0/06/1751015448/laco-fliegeruhr-typ-a-muelheim-an-der-ruhr-862092-neu-2020.png?ts=1751015448","39 mm, corda manual, mostrador tipo A. € 930."),
("Speyer","862095","79/12/59/1751015466/laco-fliegeruhr-typ-b-speyer-862095-neu-2020.png?ts=1751015466","39 mm, automático, mostrador tipo B. € 930."),
("Kempten","862093","90/86/13/1751015454/laco-fliegeruhr-typ-b-kempten-862093-neu-20201.png?ts=1751015454","39 mm, corda manual, mostrador tipo B. € 930."),
("Replika 55 A Erbstück","862196","70/f5/d9/1751015951/laco-fliegeruhr-typ-a-replika-erbstueck-861940.png?ts=1751015951","Acabamento envelhecido Erbstück. 55 mm, corda manual, mostrador tipo A. A partir de € 3.950."),
("Replika 55 B Erbstück","862197","3b/c1/03/1751015956/laco-fliegeruhr-typ-b-replika-erbstueck-861941.png?ts=1751015956","Acabamento envelhecido Erbstück. 55 mm, corda manual, mostrador tipo B. A partir de € 3.950."),
("Saarbrücken Erbstück","861933","3c/21/ec/1751015257/laco-fliegeruhr-typ-a-saarbruecken-erbstueck-8619331.png?ts=1751015257","Acabamento envelhecido Erbstück. 45 mm, automático, tipo A. A partir de € 1.890."),
("Westerland Erbstück","861937","87/5e/d8/1751015263/laco-fliegeruhr-typ-a-westerland-erbstueck-8619371.png?ts=1751015263","Acabamento envelhecido Erbstück. 45 mm, corda manual, tipo A. A partir de € 1.890."),
("Friedrichshafen Erbstück","861934","a5/72/55/1751015284/laco-fliegeruhr-typ-b-friedrichshafen-erbstueck-8619341.png?ts=1751015284","Acabamento envelhecido Erbstück. 45 mm, automático, tipo B. A partir de € 1.890."),
("Dortmund Erbstück","861938","1a/8b/3c/1751015290/laco-fliegeruhr-typ-b-dortmund-erbstueck-8619381.png?ts=1751015290","Acabamento envelhecido Erbstück. 45 mm, corda manual, tipo B. A partir de € 1.890."),
("Münster Erbstück","861931","7b/56/c8/1751015245/laco-fliegeruhr-typ-a-muenster-erbstueck-8619311.png?ts=1751015245","Acabamento envelhecido Erbstück. 42 mm, automático, tipo A. A partir de € 1.890."),
("Memmingen Erbstück","861935","29/b4/1f/1751015251/laco-fliegeruhr-typ-a-memmingen-erbstueck-861935.png?ts=1751015251","Acabamento envelhecido Erbstück. 42 mm, corda manual, tipo A. A partir de € 1.890."),
("Paderborn Erbstück","861932","68/8b/e6/1751015269/laco-fliegeruhr-typ-b-paderborn-erbstueck-861932.png?ts=1751015269","Acabamento envelhecido Erbstück. 42 mm, automático, tipo B. A partir de € 1.890."),
("Leipzig Erbstück","861936","e7/87/a9/1751015276/laco-fliegeruhr-typ-b-leipzig-erbstueck-861936.png?ts=1751015276","Acabamento envelhecido Erbstück. 42 mm, corda manual, tipo B. A partir de € 1.890."),
("Heidelberg Erbstück","862098","40/28/93/1751015851/laco-fliegeruhr-typ-a-heidelberg-erbstueck-862098-2022.png?ts=1751015851","Acabamento envelhecido Erbstück. 39 mm, automático, tipo A. € 1.890."),
("Mülheim an der Ruhr Erbstück","862096","40/8e/ca/1751015813/laco-fliegeruhr-typ-a-muelheim-an-der-ruhr-erbstueck-862096-2022.png?ts=1751015813","Acabamento envelhecido Erbstück. 39 mm, corda manual, tipo A. € 1.890."),
("Speyer Erbstück","862099","87/25/f0/1751015857/laco-fliegeruhr-typ-b-speyer-erbstueck-862099-2022.png?ts=1751015857","Acabamento envelhecido Erbstück. 39 mm, automático, tipo B. € 1.890."),
("Kempten Erbstück","862097","b6/18/65/1751015846/laco-fliegeruhr-typ-b-kempten-erbstueck-862097-2022.png?ts=1751015846","Acabamento envelhecido Erbstück. 39 mm, corda manual, tipo B. € 1.890."),
("Venedig 42","861894","f8/c2/cd/1751015086/laco-fliegeruhr-typ-a-venedig-42-861894-2023.png?ts=1751015086","42 mm, automático, tipo A. € 980."),
("Florenz 42","862174","f8/c2/cd/1751015086/laco-fliegeruhr-typ-a-venedig-42-861894-2023.png?ts=1751015086","42 mm, corda manual, tipo A. € 980. Foto do site é a mesma do Venedig 42."),
("Wien 42","861893","cd/e9/d9/1751015082/laco-fliegeruhr-typ-b-wien-42-861893-2023.png?ts=1751015082","42 mm, automático, tipo B. € 980."),
("Graz 42","862175","cd/e9/d9/1751015082/laco-fliegeruhr-typ-b-wien-42-861893-2023.png?ts=1751015082","42 mm, corda manual, tipo B. € 980. Foto do site é a mesma do Wien 42."),
("Venedig 39","862155","39/9f/9b/1751016635/laco-fliegeruhr-typ-a-venedig-39-862155-2023.png?ts=1751016635","39 mm, automático, tipo A. € 980."),
("Florenz 39","862176","39/9f/9b/1751016635/laco-fliegeruhr-typ-a-venedig-39-862155-2023.png?ts=1751016635","39 mm, corda manual, tipo A. € 980. Foto do site é a mesma do Venedig 39."),
("Wien 39","862154","3c/3d/de/1751016631/laco-fliegeruhr-typ-b-wien-39-862154-2023.png?ts=1751016631","39 mm, automático, tipo B. € 980."),
("Graz 39","862177","3c/3d/de/1751016631/laco-fliegeruhr-typ-b-wien-39-862154-2023.png?ts=1751016631","39 mm, corda manual, tipo B. € 980. Foto do site é a mesma do Wien 39."),
("Venedig Erbstück","861943","d8/a3/57/1751015752/laco-fliegeruhr-typ-a-venedig-erbstueck-8619431.png?ts=1751015752","Acabamento envelhecido Erbstück. 42 mm, automático, tipo A. € 1.950."),
("Florenz Erbstück","861945","9b/24/84/1751015758/laco-fliegeruhr-typ-a-florenz-erbstueck-861945.png?ts=1751015758","Acabamento envelhecido Erbstück. 42 mm, corda manual, tipo A. € 1.950."),
("Wien Erbstück","861944","22/ac/6b/1751015764/laco-fliegeruhr-typ-b-wien-erbstueck-861944.png?ts=1751015764","Acabamento envelhecido Erbstück. 42 mm, automático, tipo B. € 1.950."),
("Graz Erbstück","861946","c1/6c/e9/1751015769/laco-fliegeruhr-typ-b-graz-erbstueck-861946.png?ts=1751015769","Acabamento envelhecido Erbstück. 42 mm, corda manual, tipo B. € 1.950."),
]
# fix one path (Westerland)
for n,c,i,e in orig:
    if n=="Westerland": i="b1/01/2f/1751014926/laco-fliegeruhr-typ-a-westerland-861750-neu-20201.png?ts=1751014926"
    a("Pilot Watch Original "+n,c,M+i,"Linha Pilot Watch ORIGINAL. "+e)
def full(prefix, rows):
    for n,c,i,e in rows: a(prefix+n,c,i,e)
B="Linha Pilot Watches BASIC. "
MB="Pulseira de metal (MB). "
full("Pilot Watch Basic ",[
("Augsburg 42","861688.2","https://www.laco.de/media/e1/08/c2/1751015394/laco-fliegeruhr-typ-a-augsburg42-861688_2-neu-2020.png?ts=1751015394",B+"42 mm, automático, mostrador tipo A. € 390."),
("Augsburg 42 MB","861895.2","https://www.laco.de/media/fa/21/60/1751016053/laco-fliegeruhr-typ-a-augsburg-42-mb-8618952mb-neu.png?ts=1751016053",B+MB+"42 mm, automático, tipo A. € 440."),
("Augsburg 39","861988","https://www.laco.de/media/74/e1/21/1751015436/laco-fliegeruhr-typ-a-augsburg-39-861988-neu-2020.png?ts=1751015436",B+"39 mm, automático, tipo A. € 390."),
("Augsburg 39 MB","862140","https://www.laco.de/media/c1/70/50/1751016427/laco-fliegeruhr-typ-a-augsburg-39-mb-8621401.png?ts=1751016427",B+MB+"39 mm, automático, tipo A. € 440."),
("Aachen 42","861690.2","https://www.laco.de/media/d4/a2/59/1751015406/laco-fliegeruhr-typ-b-aachen42-861690_2-neu-2020.png?ts=1751015406",B+"42 mm, automático, mostrador tipo B. € 390."),
("Aachen 42 MB","861891.2","https://www.laco.de/media/1e/4b/0a/1751016048/laco-fliegeruhr-typ-b-aachen-42-mb-8618912mb-neu.png?ts=1751016048",B+MB+"42 mm, automático, tipo B. € 440."),
("Aachen 39","861990","https://www.laco.de/media/47/2d/52/1751015430/laco-fliegeruhr-typ-b-aachen-39-861990-neu-2020.png?ts=1751015430",B+"39 mm, automático, tipo B. € 390."),
("Aachen 39 MB","862139","https://www.laco.de/media/fc/c3/03/1751016423/laco-fliegeruhr-typ-b-aachen-39-mb-862139.png?ts=1751016423",B+MB+"39 mm, automático, tipo B. € 440."),
("Neapel 39","862129","https://www.laco.de/media/b4/d1/d5/1751016332/laco-fliegeruhr-typ-a-neapel-39-862129.png?ts=1751016332",B+"39 mm, automático, tipo A. € 390."),
("Palermo 39","862130","https://www.laco.de/media/bc/4a/5b/1751016327/laco-fliegeruhr-typ-b-palermo-39-862130.png?ts=1751016327",B+"39 mm, automático, tipo B. € 390."),
("Augsburg Blaue Stunde 42","862100.2","https://www.laco.de/media/31/0d/66/1767881094/laco-fliegeruhr-augsburg-blaue-stunde-42mm_862100-2.png?ts=1767881094",B+"Mostrador azul 'Blaue Stunde', tipo A. 42 mm, automático. € 390."),
("Augsburg Blaue Stunde 42 MB","862100.2.MB","https://www.laco.de/media/7e/51/c7/1767881174/laco-fliegeruhr-augsburg-blaue-stunde-42mm_862100-2-mb.png?ts=1767881174",B+MB+"Mostrador azul, tipo A. 42 mm, automático. € 440."),
("Augsburg Blaue Stunde 39","862102.2","https://www.laco.de/media/28/94/d0/1767881112/laco-fliegeruhr-augsburg-blaue-stunde-39mm_862102-2.png?ts=1767881112",B+"Mostrador azul, tipo A. 39 mm, automático. € 390."),
("Augsburg Blaue Stunde 39 MB","862102.2.MB","https://www.laco.de/media/8d/36/b5/1767881191/laco-fliegeruhr-augsburg-blaue-stunde-39mm_862102-2-mb.png?ts=1767881191",B+MB+"Mostrador azul, tipo A. 39 mm, automático. € 440."),
("Aachen Blaue Stunde 42","862101.2","https://www.laco.de/media/f4/00/47/1767881129/laco-fliegeruhr-aachen-blaue-stunde-42mm_862101-2.png?ts=1767881129",B+"Mostrador azul, tipo B. 42 mm, automático. € 390."),
("Aachen Blaue Stunde 42 MB","862101.2.MB","https://www.laco.de/media/5c/d1/8d/1767881208/laco-fliegeruhr-aachen-blaue-stunde-42mm_862101-2-mb.png?ts=1767881208",B+MB+"Mostrador azul, tipo B. 42 mm, automático. € 440."),
("Aachen Blaue Stunde 39","862103.2","https://www.laco.de/media/76/fc/10/1767881151/laco-fliegeruhr-aachen-blaue-stunde-39mm_862103-2.png?ts=1767881151",B+"Mostrador azul, tipo B. 39 mm, automático. € 390."),
("Aachen Blaue Stunde 39 MB","862103.2.MB","https://www.laco.de/media/b3/43/a7/1767881220/laco-fliegeruhr-aachen-blaue-stunde-39mm_862103-2-mb.png?ts=1767881220",B+MB+"Mostrador azul, tipo B. 39 mm, automático. € 440."),
("Augsburg Grau 42","862158","https://www.laco.de/media/7d/7d/07/1751016669/laco-fliegeruhr-typ-a-augsburg-grau-42-862158.png?ts=1751016669",B+"Mostrador cinza, tipo A. 42 mm, automático. € 410."),
("Augsburg Grau 42 MB","862158.MB","https://www.laco.de/media/bb/55/be/1751016683/laco-fliegeruhr-typ-a-augsburg-grau-42-mb-862158mb.png?ts=1751016683",B+MB+"Mostrador cinza, tipo A. 42 mm, automático. € 460."),
("Augsburg Grau 39","862161","https://www.laco.de/media/7d/e5/fc/1751016660/laco-fliegeruhr-typ-a-augsburg-grau-39-862161.png?ts=1751016660",B+"Mostrador cinza, tipo A. 39 mm, automático. € 410."),
("Augsburg Grau 39 MB","862161.MB","https://www.laco.de/media/a7/44/cb/1751016692/laco-fliegeruhr-typ-a-augsburg-grau-39-mb-862161mb.png?ts=1751016692",B+MB+"Mostrador cinza, tipo A. 39 mm, automático. € 460."),
("Aachen Grau 42","862159","https://www.laco.de/media/9a/52/3b/1751016674/laco-fliegeruhr-typ-b-aachen-grau-42-862159.png?ts=1751016674",B+"Mostrador cinza, tipo B. 42 mm, automático. € 410."),
("Aachen Grau 42 MB","862159.MB","https://www.laco.de/media/30/c6/f1/1751016679/laco-fliegeruhr-typ-b-aachen-grau-42-mb-862159mb.png?ts=1751016679",B+MB+"Mostrador cinza, tipo B. 42 mm, automático. € 460."),
("Aachen Grau 39","862162","https://www.laco.de/media/53/49/18/1751016665/laco-fliegeruhr-typ-b-aachen-grau-39-862162.png?ts=1751016665",B+"Mostrador cinza, tipo B. 39 mm, automático. € 410."),
("Aachen Grau 39 MB","862162.MB","https://www.laco.de/media/6b/57/22/1751016688/laco-fliegeruhr-typ-b-aachen-grau-39-mb-862162mb.png?ts=1751016688",B+MB+"Mostrador cinza, tipo B. 39 mm, automático. € 460."),
("Altenburg 42","861759.2","https://www.laco.de/media/39/c6/3f/1751015383/laco-fliegeruhr-typ-a-altenburg42-8617592-neu-2020.png?ts=1751015383",B+"42 mm, automático, tipo A. € 440."),
("Altenburg 39","861991","https://www.laco.de/media/cb/95/78/1751015945/laco-fliegeruhr-typ-a-altenburg39-861991-neu-2020.png?ts=1751015945",B+"39 mm, automático, tipo A. € 440."),
("Bielefeld 42","861760.2","https://www.laco.de/media/22/8c/cc/1751015389/laco-fliegeruhr-typ-b-bielefeld42-861760-neu-20201.png?ts=1751015389",B+"42 mm, automático, tipo B. € 440."),
("Bielefeld 39","861992","https://www.laco.de/media/12/1c/c0/1751015940/laco-fliegeruhr-typ-b-bielefeld39-861992-neu-20201.png?ts=1751015940",B+"39 mm, automático, tipo B. € 440."),
("Genf.2 40","861807.2","https://www.laco.de/media/5f/79/13/1751016368/laco-fliegeruhr-typ-a-genf2-8618072.png?ts=1751016368",B+"40 mm, quartzo, tipo A. € 290."),
("Genf.2 40 MB","861807.2.MB","https://www.laco.de/media/12/50/1f/1751017046/laco-fliegeruhr-genf-2-40mm-861807-2-mb.png?ts=1751017046",B+MB+"40 mm, quartzo, tipo A. € 340."),
("Genf.2.D 40","861807.2.D","https://www.laco.de/media/93/40/c1/1751016372/laco-fliegeruhr-typ-a-genf2d-8618072.png?ts=1751016372",B+"Versão com data. 40 mm, quartzo, tipo A. € 290."),
("Genf.2.D 40 MB","861807.2.D.MB","https://www.laco.de/media/fd/21/4c/1751017052/laco-fliegeruhr-genf-2-40mm-861807-2-d-mb.png?ts=1751017052",B+MB+"Com data. 40 mm, quartzo, tipo A. € 340."),
("Zürich.2 40","861806.2","https://www.laco.de/media/72/8d/ee/1751016360/laco-fliegeruhr-typ-b-zuerich2-8618062.png?ts=1751016360",B+"40 mm, quartzo, tipo B. € 290."),
("Zürich.2 40 MB","861806.2.MB","https://www.laco.de/media/fe/72/95/1751017035/laco-fliegeruhr-zuerich-2-40mm-861806-2-mb.png?ts=1751017035",B+MB+"40 mm, quartzo, tipo B. € 340."),
("Zürich.2.D 40","861806.2.D","https://www.laco.de/media/fc/ec/69/1751016364/laco-fliegeruhr-typ-b-zuerich2d-8618062d.png?ts=1751016364",B+"Com data. 40 mm, quartzo, tipo B. € 290."),
("Zürich.2.D 40 MB","861806.2.D.MB","https://www.laco.de/media/06/c2/62/1751017040/laco-fliegeruhr-zuerich-2-40mm-861806-2-d-mb.png?ts=1751017040",B+MB+"Com data. 40 mm, quartzo, tipo B. € 340."),
])
S="Linha Pilot Watches Special Models (Sellita). "
full("",[
("Köln","862191","https://www.laco.de/media/ee/b7/1a/1766136102/laco-fliegeruhr-koeln-42_5mm_862191.png?ts=1766136102",S+"41 mm, automático. € 1.190."),
("Köln MB","862191.MB","https://www.laco.de/media/41/8f/14/1766136296/laco-fliegeruhr-koeln-42_5mm_862191-mb.png?ts=1766136296",S+MB+"41 mm, automático. € 1.240."),
("Köln Grau","862192","https://www.laco.de/media/6b/55/64/1767881239/laco-fliegeruhr-koeln-42_5mm_862192.png?ts=1767881239",S+"Mostrador cinza. 41 mm, automático. € 1.270."),
("Frankfurt 40 GMT Grau","862188","https://www.laco.de/media/e1/8d/89/1793715606/soldat-grau-laco-fliegeruhr-frankfurt-gmt-40mm-awards.webp?ts=1793715606",S+"GMT, mostrador cinza. 40 mm, automático. € 1.850."),
("Frankfurt 40 GMT Schwarz","862187","https://www.laco.de/media/92/f6/a5/1781610398/soldat-schwarz-laco-fliegeruhr-frankfurt-gmt-40mm_%281%29.webp?ts=1781610398",S+"GMT, mostrador preto. 40 mm, automático. € 1.850."),
("Frankfurt 43 GMT Schwarz","862120.2","https://www.laco.de/media/63/70/b7/1751016032/laco-fliegeruhr-typ-c-frankfurt-gmt-schwarz-862120-2023.png?ts=1751016032",S+"GMT, mostrador tipo C preto. 43 mm, automático. € 1.850."),
("Frankfurt 43 GMT Grau","862121.2","https://www.laco.de/media/db/1f/3a/1751016037/laco-fliegeruhr-typ-c-frankfurt-gmt-grau-862121-2023.png?ts=1751016037",S+"GMT, mostrador tipo C cinza. 43 mm, automático. € 1.850."),
("Kiel.2 Schwarz","862148","https://www.laco.de/media/68/c8/6d/1751016569/laco-chronograph-kiel2-schwarz-862148.png?ts=1751016569",S+"Cronógrafo, mostrador preto. 43 mm, automático. € 2.290."),
("Kiel.2.MB Schwarz","862148.MB","https://www.laco.de/media/e0/60/04/1751016585/laco-chronograph-kiel2-schwarz-mb-862148mb.png?ts=1751016585",S+MB+"Cronógrafo, mostrador preto. 43 mm. € 2.390."),
("Kiel.2 Weiss","862153","https://www.laco.de/media/af/3b/ca/1751016573/laco-chronograph-kiel2-weiss-8621531_2.png?ts=1751016573",S+"Cronógrafo, mostrador branco. 43 mm, automático. € 2.290."),
("Kiel.2.MB Weiss","862153.MB","https://www.laco.de/media/f0/97/97/1751016581/laco-chronograph-kiel2-weiss-mb-862153mb.png?ts=1751016581",S+MB+"Cronógrafo, mostrador branco. 43 mm. € 2.390."),
("Kiel.2 Blau","862186","https://www.laco.de/media/7e/72/d6/1766071904/laco_chronograph_kiel2_43mm_862186.png?ts=1766071904",S+"Cronógrafo, mostrador azul. 43 mm, automático. € 2.290."),
("Kiel.2.MB Blau","862186.MB","https://www.laco.de/media/7b/fe/c2/1767880277/laco_chronograph_kiel2_43mm_862186_mb.png?ts=1767880277",S+MB+"Cronógrafo, mostrador azul. 43 mm. € 2.390."),
("Kiel Sport","862180","https://www.laco.de/media/ae/07/20/1751016917/laco-fliegerchronograph-kiel-sport-862180.png?ts=1751016917",S+"Cronógrafo de piloto. 43 mm, automático. € 2.390."),
("Ulm 42,5","862118.2","https://www.laco.de/media/72/40/3c/1751016886/laco-fliegeruhr-typ-c-ulm-425-8621182.png?ts=1751016886",S+"Mostrador tipo C. 42,5 mm, corda manual. € 1.790."),
("Würzburg 42,5","862119.2","https://www.laco.de/media/2c/af/7e/1751016890/laco-fliegeruhr-typ-c-wuerzburg-425-8621192.png?ts=1751016890",S+"Mostrador tipo C. 42,5 mm, corda manual. € 1.790."),
("Ulm 39","862172","https://www.laco.de/media/9b/2d/ff/1751016894/laco-fliegeruhr-typ-c-ulm-39-862172.png?ts=1751016894",S+"Mostrador tipo C. 39 mm, corda manual. € 1.290."),
("Würzburg 39","862173","https://www.laco.de/media/21/e9/51/1751016899/laco-fliegeruhr-typ-c-wuerzburg-39-862173.png?ts=1751016899",S+"Mostrador tipo C. 39 mm, corda manual. € 1.290."),
])
SQ="Linha Squad (relógios de missão). "
NV="Linha Navy (relógios de marinha). "
SP="Linha Sport (Laco 200, base Sellita SW200), 30 ATM. "
RB="Pulseira de borracha (RB). "
full("",[
("Atacama.3","861632.3","https://www.laco.de/media/1e/c9/78/1767881017/laco-einsatzuhr-atacama-861632-3.png?ts=1767881017",SQ+"46 mm, automático. € 1.130."),
("Atacama.3 MB","861632.3.MB","https://www.laco.de/media/92/51/4f/1766066877/laco-einsatzuhr-atacama-861632-3-mb.png?ts=1766066877",SQ+MB+"46 mm, automático. € 1.230."),
("Atacama Quarz UTC","862163","https://www.laco.de/media/f2/ff/83/1751016754/laco-einsatzuhr-atacama-quarz-utc-862163.png?ts=1751016754",SQ+"UTC, 46 mm, quartzo. € 590."),
("Atacama Quarz UTC MB","862163.MB","https://www.laco.de/media/c3/29/7f/1766138646/laco-einsatzuhr-atacama-quarz-utc-mb-862163.png?ts=1766138646",SQ+MB+"UTC, 46 mm, quartzo. € 690."),
("Seven Seas","861703","https://www.laco.de/media/f5/14/15/1746534139/laco-einsatzuhr-sevenseas-861703-2022.png?ts=1746534139",SQ+"45,8 mm, automático. € 1.940."),
("Cuxhaven 42,5","862104.2","https://www.laco.de/media/13/9c/g0/1751016772/laco-marineuhr-cuxhaven-8621042.png?ts=1751016772",NV+"42,5 mm, corda manual. € 1.790."),
("Bremerhaven 42,5","862105.2","https://www.laco.de/media/ae/37/64/1751015631/laco-marineuhr-bremerhaven-862105.png?ts=1751015631",NV+"42,5 mm, corda manual. € 1.790."),
("Cuxhaven 39","862168","https://www.laco.de/media/22/4a/bb/1751016760/laco-marineuhr-cuxhaven-39-862168.png?ts=1751016760",NV+"39 mm, corda manual. € 1.290."),
("Bremerhaven 39","862169","https://www.laco.de/media/3b/68/6f/1751016764/laco-marineuhr-bremerhaven-39-862169.png?ts=1751016764",NV+"39 mm, corda manual. € 1.290."),
("Valencia 42","861651.2","https://www.laco.de/media/70/3b/68/1751015371/laco-marineuhr-valencia-42-8616512-2022.png?ts=1751015371",NV+"42 mm, automático. € 420."),
("Valencia 39","862090","https://www.laco.de/media/24/77/97/1751015807/laco-marineuhr-valencia-39-862090-2022.png?ts=1751015807",NV+"39 mm, automático. € 420."),
("Casablanca 39","862115","https://www.laco.de/media/c6/aa/7b/1751015961/laco-marineuhr-casablanca39-862115.png?ts=1751015961",NV+"39 mm, automático. € 470."),
("Casablanca 42","861776.2","https://www.laco.de/media/98/0f/cb/1751015377/laco-marineuhr-casablanca42-8617762_1.png?ts=1751015377",NV+"42 mm, automático. € 470."),
])
sport=[("Amazonas 42","862107","c8/e7/e3/1751015648/laco-einsatzuhr-amazonas-862107_1.png?ts=1751015648"),
("Amazonas 42 MB","862107.MB","bd/3d/6e/1751015654/laco-einsatzuhr-amazonasmb-862107mb.png?ts=1751015654"),
("Amazonas 42 RB","862107.RB","g0/1d/7c/1751015781/laco-einsatzuhr-amazonasrb-862107rb.png?ts=1751015781"),
("Amazonas 39","862134","2c/c7/64/1751016546/laco-sportuhr-amazonas-39-862134.png?ts=1751016546"),
("Amazonas 39 MB","862134.MB","69/19/3d/1751016550/laco-sportuhr-amazonas-mb-39-862134mb.png?ts=1751016550"),
("Amazonas 39 RB","862134.RB","96/41/82/1751016554/laco-sportuhr-amazonas-rb-39-862134rb.png?ts=1751016554"),
("Atlantik 42","862108","1f/ff/2e/1751015665/laco-einsatzuhr-atlantik-862108_1.png?ts=1751015665"),
("Atlantik 42 MB","862108.MB","a3/5e/3a/1751015671/laco-einsatzuhr-atlantikmb-862108mb_1.png?ts=1751015671"),
("Atlantik 42 RB","862108.RB","fa/ee/87/1751015786/laco-einsatzuhr-atlantikrb-862108rb_1.png?ts=1751015786"),
("Atlantik 39","862133","bb/86/d2/1751016557/laco-sportuhr-atlantik-39-862133.png?ts=1751016557"),
("Atlantik 39 MB","862133.MB","c6/fc/79/1751016561/laco-sportuhr-atlantik-mb-39-862133mb.png?ts=1751016561"),
("Atlantik 39 RB","862133.RB","d9/a1/7d/1751016565/laco-sportuhr-atlantik-rb-39-862133rb.png?ts=1751016565"),
("Mojave 42","862109","2c/d1/0e/1751015676/laco-einsatzuhr-mojave-862109.png?ts=1751015676"),
("Mojave 42 MB","862109.MB","97/82/05/1751015683/laco-einsatzuhr-mojavemb-862109mb.png?ts=1751015683"),
("Mojave 42 RB","862109.RB","ff/c8/68/1751015793/laco-einsatzuhr-mojaverb-862109rb.png?ts=1751015793"),
("Mojave 39","862132","dd/90/81/1751016534/laco-sportuhr-mojave-39-862132.png?ts=1751016534"),
("Mojave 39 MB","862132.MB","99/69/b6/1751016538/laco-sportuhr-mojave-mb-39-862132mb.png?ts=1751016538"),
("Mojave 39 RB","862132.RB","9d/98/d6/1751016542/laco-sportuhr-mojave-rb-39-862132rb.png?ts=1751016542"),
("Himalaya 42","862106","e8/31/0b/1751015637/laco-einsatzuhr-himalaya-862106.png?ts=1751015637"),
("Himalaya 42 MB","862106.MB","0a/86/7a/1751015642/laco-einsatzuhr-himalayamb-862106mb.png?ts=1751015642"),
("Himalaya 42 RB","862106.RB","eb/64/b3/1751015775/laco-einsatzuhr-himalayarb-862106rb.png?ts=1751015775"),
("Himalaya 39","862131","75/42/d1/1751014263/laco-sportuhr-himalaya-39-862131.png?ts=1751014263"),
("Himalaya 39 MB","862131.MB","12/bf/74/1751016527/laco-sportuhr-himalaya-mb-39-862131mb.png?ts=1751016527"),
("Himalaya 39 RB","862131.RB","8a/e9/8c/1751016531/laco-sportuhr-himalaya-rb-39-862131rb.png?ts=1751016531")]
for n,c,i in sport:
    mm=n.split()[1]
    ex=MB if n.endswith("MB") else (RB if n.endswith("RB") else "")
    a(n,c,M+i,SP+ex+f"{mm} mm, automático. € 990.")
W='https://www.laco-watches.com/media/'
AR="Visto no arquivo de relógios do site oficial (laco-watches.com, 'watch archive'; fora de linha). "
arch=[
("Pilot Watch Original Dortmund Bronze","862088","f0/f2/f3/1751015424/laco-fliegeruhr-typ-b-dortmund-bronze-862088_1.png?ts=1751015424","Caixa de bronze, tipo B. US$ 2.250."),
("Pilot Watch Original Friedrichshafen Bronze","862086","4f/79/e4/1751015411/laco-fliegeruhr-typ-b-friedrichshafen-bronze-8620861_1.png?ts=1751015411","Caixa de bronze, tipo B. US$ 2.250."),
("Edition 97","862160","1c/68/ab/1751016626/laco-edition_97.png?ts=1751016626","Edição de aniversário (97 anos). US$ 1.790."),
("Pilot Watch Original Leipzig Blaue Stunde","862084","54/f4/7e/1751015365/laco-fliegeruhr-typ-b-paderborn-blaue-stunde-862082_1.png?ts=1751015365","Mostrador azul, tipo B. US$ 1.190. A foto do arquivo é do Paderborn Blaue Stunde (mesmo mostrador)."),
("Pilot Watch Original Westerland Bronze","862087","65/a0/2a/1751015418/laco-fliegeruhr-typ-a-westerland-bronze-862087_1.png?ts=1751015418","Caixa de bronze, tipo A. US$ 2.250."),
("Pilot Watch Original Memmingen Blaue Stunde","862083","ed/5c/79/1751015353/laco-fliegeruhr-typ-a-muenster-blaue-stunde-862081_1.png?ts=1751015353","Mostrador azul, tipo A. US$ 1.190. A foto do arquivo é do Münster Blaue Stunde (mesmo mostrador)."),
("Pilot Watch Original Münster Blaue Stunde","862081","0b/4a/0d/1751014067/laco-fliegeruhr-typ-a-muenster-blaue-stunde-862081.png?ts=1751014067","Mostrador azul, tipo A. US$ 1.190."),
("Pilot Watch Original Saarbrücken Bronze","862085","cc/fb/93/1751015400/laco-fliegeruhr-typ-a-saarbruecken-bronze-8620851.png?ts=1751015400","Caixa de bronze, tipo A. US$ 2.250."),
("Pilot Watch Original Paderborn Blaue Stunde","862082","ea/06/ed/1751014072/laco-fliegeruhr-typ-b-paderborn-blaue-stunde-862082.png?ts=1751014072","Mostrador azul, tipo B. US$ 1.190."),
("Pilot Watch Original Replika 45 A","861950","52/2d/b8/1751015065/laco-fliegeruhr-typ-a-replika-45-861950-2022.png?ts=1751015065","45 mm, mostrador tipo A. US$ 1.990."),
("Pilot Watch Original Replika 45 B","861951","4a/9a/15/1751015070/laco-fliegeruhr-typ-b-replika-45-861951-2022.png?ts=1751015070","45 mm, mostrador tipo B. US$ 1.990."),
("Pilot Watch Basic Aachen 42 Taupe California","862171","35/9a/2d/1751016965/laco-fliegeruhr-typ-b-aachen-california-dial-862171.png?ts=1751016965","Mostrador taupe tipo California, 42 mm. US$ 540."),
("Pilot Watch Basic Aachen Blaue Stunde 39 (1ª versão)","862103","7a/9d/26/1751015492/laco-fliegeruhr-typ-b-aachen-blaue-stunde-39-NB-862103.png?ts=1751015492","Mostrador azul, tipo B, 39 mm. Versão anterior à 862103.2. US$ 410."),
("Pilot Watch Basic Aachen Blaue Stunde 42 (1ª versão)","862101","ab/55/a0/1751015480/laco-fliegeruhr-typ-b-aachen-blaue-stunde-42-NB-862101.png?ts=1751015480","Mostrador azul, tipo B, 42 mm. Versão anterior à 862101.2. US$ 410."),
("Pilot Watch Basic Augsburg Blaue Stunde 39 (1ª versão)","862102","0a/63/1b/1751015486/laco-fliegeruhr-typ-a-augsburg-blaue-stunde-39-NB-862102.png?ts=1751015486","Mostrador azul, tipo A, 39 mm. US$ 410."),
("Pilot Watch Basic Augsburg Blaue Stunde 42 (1ª versão)","862100","85/dd/1f/1751015473/laco-fliegeruhr-typ-a-augsburg-blaue-stunde-42-NB-862100.png?ts=1751015473","Mostrador azul, tipo A, 42 mm. US$ 410."),
("Pilot Watch Basic Aachen Grün 39","862190","46/c7/e6/1767881075/laco-flieger-aachen-gruen-39-862190.png?ts=1767881075","Mostrador verde, tipo B, 39 mm. US$ 540."),
("Pilot Watch Basic Aachen Grün 42","862179","c1/1e/4c/1751016933/laco-fliegeruhr-typ-b-aachen-gruen-42-862179.png?ts=1751016933","Mostrador verde, tipo B, 42 mm. US$ 540."),
("Pilot Watch Basic Augsburg Grün 39","862189","e6/c0/59/1767881059/laco-flieger-augsburg-gruen-39-862189.png?ts=1767881059","Mostrador verde, tipo A, 39 mm. US$ 540."),
("Pilot Watch Basic Augsburg Grün 42","862178","dd/07/4d/1751016937/laco-fliegeruhr-typ-a-augsburg-gruen-42-862178.png?ts=1751016937","Mostrador verde, tipo A, 42 mm. US$ 540."),
("Aachen Oliv 39","862136","c7/ea/c7/1751016446/laco-fliegeruhr-typ-b-aachen-39-oliv-862136.png?ts=1751016446","Edição oliva, tipo B, 39 mm. US$ 540."),
("Aachen Oliv 42","862128","37/ab/07/1751016287/laco-fliegeruhr-typ-b-aachen-oliv-42-862128.png?ts=1751016287","Edição oliva, tipo B, 42 mm. US$ 540."),
("Augsburg Oliv 39","862135","96/b2/3c/1751016442/laco-fliegeruhr-typ-a-augsburg-39-oliv-862135.png?ts=1751016442","Edição oliva, tipo A, 39 mm. US$ 540."),
("Augsburg Oliv 42","862127","33/2e/c1/1751016283/laco-fliegeruhr-typ-a-42-augsburg-oliv-862127.png?ts=1751016283","Edição oliva, tipo A, 42 mm. US$ 540."),
("Aachen Polar 39","862184","06/f3/67/1751016998/laco-fliegeruhr-aachen-polar-39mm-862184.png?ts=1751016998","Mostrador branco 'Polar', tipo B, 39 mm. US$ 540."),
("Aachen Polar 42","862157","9d/23/6c/1751016648/laco-fliegeruhr-typ-b-aachen-polar-42-862157.png?ts=1751016648","Mostrador branco 'Polar', tipo B, 42 mm. US$ 540."),
("Augsburg Polar 39","862183","c7/3b/1a/1751016992/laco-fliegeruhr-augsburg-polar-39mm-862183.png?ts=1751016992","Mostrador branco 'Polar', tipo A, 39 mm. US$ 540."),
("Augsburg Polar 42","862156","e9/24/a9/1751016644/laco-fliegeruhr-typ-a-augsburg-polar-42-862156_1.png?ts=1751016644","Mostrador branco 'Polar', tipo A, 42 mm. US$ 540."),
("Aachen Taupe 39","862126","e4/f6/cb/1751016225/laco-fliegeruhr-typ-b-aachen39-taupe-862126.png?ts=1751016225","Mostrador taupe, tipo B, 39 mm. US$ 460."),
("Aachen Taupe 42","862117","86/6a/6a/1751015973/laco-fliegeruhr-aachen-42-taupe-862117.png?ts=1751015973","Mostrador taupe, tipo B, 42 mm. US$ 460."),
("Augsburg Taupe 39","862125","fc/3b/2d/1751016219/laco-fliegeruhr-typ-a-augsburg39-taupe-862125.png?ts=1751016219","Mostrador taupe, tipo A, 39 mm. US$ 460."),
("Augsburg Taupe 42","862116","78/8d/e8/1751015967/laco-fliegeruhr-augsburg-42-taupe-862116_1.png?ts=1751015967","Mostrador taupe, tipo A, 42 mm. US$ 460."),
("Birmingham 36","861801","fc/62/be/1751014580/laco-fliegeruhr-typ-b-birmingham-861801.png?ts=1751014580","Pilot Basic, tipo B, 36 mm. US$ 460."),
("Edition 99","862181","1a/2f/5d/1751016975/Laco-Uhrenmanufaktur-Edition-99-862181.png?ts=1751016975","Edição de aniversário (99 anos). US$ 590."),
("Genf 42","861807","6d/48/6b/1751014982/laco-fliegeruhr-typ-a-genf-861807-neu-2020.png?ts=1751014982","Pilot Basic, quartzo, tipo A, 42 mm. US$ 290."),
("London 36","861800","4e/9f/98/1751014574/laco-fliegeruhr-typ-a-london-861800.png?ts=1751014574","Pilot Basic, tipo A, 36 mm. US$ 470."),
("Neapel","861965","d5/41/d7/1751015112/laco-fliegeruhr-typ-a-neapel-861965.png?ts=1751015112","Pilot Basic, tipo A. US$ 460."),
("Palermo","861966","17/d1/1a/1751015108/laco-fliegeruhr-typ-b-palermo-861966.png?ts=1751015108","Pilot Basic, tipo B. US$ 460."),
("Stockholm 36","861888","a1/78/e9/1751014674/laco-fliegeruhr-typ-a-stockholm-861888.png?ts=1751014674","Pilot Basic, tipo A, 36 mm. US$ 470."),
("Sydney","861890","ed/7f/8e/1751014691/laco-fliegeruhr-typ-b-sydney-861890.png?ts=1751014691","Pilot Basic, tipo B. US$ 460."),
("Visby 36","861900","b2/22/82/1751014680/laco-fliegeruhr-typ-b-visby-861900.png?ts=1751014680","Pilot Basic, tipo B, 36 mm. US$ 460."),
("Zürich 42","861806","5f/a2/b6/1751014977/laco-fliegeruhr-typ-b-zuerich-861806-neu-2020.png?ts=1751014977","Pilot Basic, quartzo, tipo B, 42 mm. US$ 290."),
("Basel","861971","e2/22/16/1751015149/laco-fliegeruhr-typ-a-basel-861971.png?ts=1751015149","Special Models. US$ 350."),
("Bell X-1","861907","0a/ae/b7/1751014779/laco-fliegeruhr-typ-c-bellx-1-861907-neu-2.png?ts=1751014779","Special Models, mostrador tipo C. US$ 650."),
("Bern","861974","49/2d/b5/1751015162/laco-fliegeruhr-typ-c-bern-861974.png?ts=1751015162","Special Models, tipo C. US$ 460."),
("Black Automatic 42","861610.2","01/0b/6f/1751015563/laco-fliegeruhr-typ-c-blackautomatic-42-861610_2.png?ts=1751015563","Special Models, tipo C, 42 mm. US$ 410."),
("DC-3","861901","a0/90/62/1751014737/laco-usedlook-dc-3-861901.png?ts=1751014737","Special Models, acabamento envelhecido (used look). US$ 650."),
("JU","861908","d1/85/df/1751014783/laco-fliegeruhr-typ-c-ju-861908-neu.png?ts=1751014783","Special Models, tipo C. US$ 650."),
("Lausanne","861975","20/46/f3/1751015166/laco-fliegeruhr-typ-c-lausanne-861975.png?ts=1751015166","Special Models, tipo C. US$ 520."),
("Luzern","861972","34/56/7e/1751015153/laco-fliegeruhr-typ-a-luzern-861972.png?ts=1751015153","Special Models, tipo A. US$ 410."),
("Spirit of St. Louis","861909","3b/bf/a7/1751014787/laco-fliegeruhr-typ-c-spiritofstlouis-861909-neu.png?ts=1751014787","Special Models, tipo C. US$ 650."),
("St. Gallen","861973","9d/d1/e8/1751015157/laco-fliegeruhr-typ-a-StGallen-861973.png?ts=1751015157","Special Models, tipo A. US$ 410."),
("Edition 100","861925","64/ff/10/1767881260/laco-editionen-edition-100-38mm-861925.png?ts=1767881260","Edição de aniversário (100 anos, 2025). 38 mm (pelo nome do arquivo). US$ 1.760."),
("Goldstadt-Uhr","862079","c6/37/0a/1751014842/laco-vintage-goldstadtjubilaeumsuhr-862079.png?ts=1751014842","Relógio do jubileu da 'Goldstadt' Pforzheim. US$ 720."),
("Kiel – edição limitada","861716","6f/ff/58/1751015331/861716_Kiel_limited_edition.png?ts=1751015331","Cronógrafo, edição limitada. US$ 2.400."),
("Edition 95","862123","17/8a/a5/1751016271/laco-marineuhr-edition95-862123.png?ts=1751016271","Edição de aniversário (95 anos), estilo relógio de marinha. US$ 1.560."),
("Edition 96","862145","8b/6e/a0/1751016391/laco-edition_961.png?ts=1751016391","Edição de aniversário (96 anos). US$ 1.560."),
("Edition 98","862166","81/37/07/1751016809/laco-edition-98-862160-xs.png?ts=1751016809","Edição de aniversário (98 anos). US$ 3.570."),
("Mission Manx – edição limitada","861878","6e/8c/c7/1751015018/laco-edition-missionmanx-861878.png?ts=1751015018","Edição limitada. US$ 3.900."),
("München","862124","9b/0d/ac/1751016253/862124_Muenchen_Chrono_FS.png?ts=1751016253","Cronógrafo. US$ 2.400."),
("München Erbstück","862144","c6/69/2c/1751016387/862144-muenchen-erbstueck-laco.png?ts=1751016387","Cronógrafo, acabamento envelhecido Erbstück. US$ 3.620."),
("ProLab","862193","f2/6c/74/1767881301/laco-editionen-prolab-862193.png?ts=1767881301","Edição especial. US$ 2.990."),
("Atacama.2","861632.2","aa/b8/2f/1751015660/laco-einsatzuhr-atacama-861632_2.png?ts=1751015660","Squad, versão anterior do Atacama. US$ 1.130."),
("Aleutian","862110","55/40/c9/1751016005/laco-einsatzuhr-aleutian-862110_1_1.png?ts=1751016005","Sport, esgotado. US$ 990."),
("Daintree","862114","86/3a/af/1751016021/laco-einsatzuhr-daintree-862114.png?ts=1751016021","Sport, esgotado. US$ 990."),
("Kilimanjaro","862111","47/80/1d/1751016010/laco-einsatzuhr-kilimanjaro-862111.png?ts=1751016010","Sport, esgotado. US$ 990."),
("Malawi","862112","b9/ab/c5/1751016016/laco-einsatzuhr-malawi-862112.png?ts=1751016016","Sport, esgotado. US$ 990."),
("Mariana","862113","5b/67/c7/1751016027/laco-einsatzuhr-mariana-862113.png?ts=1751016027","Sport, esgotado. US$ 990."),
("Ocean","861704","a0/5a/d4/1784195890/soldat-laco-sportuhr-ocean-neu%20%281%29.png?ts=1784195890","Sport/Squad, esgotado. US$ 2.300."),
("Bremerhaven (1ª versão)","862105","ae/37/64/1751015631/laco-marineuhr-bremerhaven-862105.png?ts=1751015631","Navy, versão anterior à 862105.2. US$ 1.190."),
("Cuxhaven (1ª versão)","862104","82/a6/29/1751015624/Cuxhaven_862104_Soldat_freisteller1.png?ts=1751015624","Navy, versão anterior à 862104.2. US$ 1.190."),
("Monaco","861804","29/12/a8/1751014987/laco-marineuhr-monaco-861804_2.png?ts=1751014987","Navy. US$ 510."),
("Navy 36","861614","96/20/65/1751014856/laco-marineuhr-marine-36-861614.png?ts=1751014856","Navy, 36 mm. US$ 1.190."),
("Navy 36 Black","861615","d3/0c/7c/1751014861/laco-marineuhr-marine-36-black--861615.png?ts=1751014861","Navy, preto, 36 mm. US$ 1.190."),
("Palm Springs","862021","71/c3/44/1751015863/laco-marineuhr-palmsprings-862021.png?ts=1751015863","Navy. US$ 1.190."),
("Philadelphia","861921","a6/92/63/1751015121/laco-marineuhr-philadelphia-861921.png?ts=1751015121","Navy. US$ 1.390."),
("Wilhelmshaven","861205","57/d9/01/1751015698/laco-marineuhr-wilhelmshaven-8612051_1.png?ts=1751015698","Navy. US$ 1.150."),
("Wilhelmshaven","861204","4b/8a/33/1751015705/laco-marineuhr-wilhelmshaven-8612041_1.png?ts=1751015705","Navy. US$ 1.300."),
("Atlanta","861919","88/64/98/1751015139/laco-fliegeruhr-typ-c-atlanta-861919.png?ts=1751015139","Cronógrafo, mostrador tipo C. US$ 350."),
("Chicago","861584","ca/46/c7/1751014852/laco-chronograph-chicago-861584.png?ts=1751014852","Cronógrafo. US$ 2.250."),
("Detroit","861917","b1/03/45/1751015130/laco-fliegeruhr-typ-c-detroit-861917.png?ts=1751015130","Cronógrafo, tipo C. US$ 350."),
("Havanna","861892","ff/fb/05/1751015091/laco-fliegeruhr-typ-c-havanna-861892.png?ts=1751015091","Cronógrafo. US$ 2.250."),
("Helgoland","861989","2a/4e/0e/1751015175/laco-damenuhr-helgoland-861989_1.png?ts=1751015175","Linha de cronógrafos/femininos (arquivo da foto: Damenuhr). US$ 350."),
("Hockenheim","862089","23/91/05/1751015442/laco-chronograph-hockenheim-862089.png?ts=1751015442","Cronógrafo. US$ 2.400."),
("Las Vegas","861587","f3/bd/8d/1751014874/laco-chronograph-lasvegas-861587.png?ts=1751014874","Cronógrafo. US$ 2.250."),
("Monte Carlo","861815","86/b0/5f/1751015117/laco-chronograph-montecarlo-861815.png?ts=1751015117","Cronógrafo. US$ 2.250."),
("Montreal","861920","1d/70/a2/1751015143/laco-damenuhr-montreal-861920.png?ts=1751015143","Arquivo da foto: Damenuhr (feminino). US$ 350."),
]
for n,c,i,e in arch: a(n,c,W+i,AR+e)
arch2=[
("New York","861586","eb/40/97/1751014870/laco-chronograph-newyork-861586.png?ts=1751014870","Cronógrafo. US$ 2.250."),
("Paris","861870","37/a3/fc/1751015013/laco-chronograph-paris-861870.png?ts=1751015013","Cronógrafo. US$ 4.200."),
("Phoenix","861916","ff/be/3a/1751015126/laco-chronograph-phoenix-861916.png?ts=1751015126","Cronógrafo. US$ 2.550."),
("San Francisco","861585","5a/be/75/1751014865/laco-chronograph-sanfrancisco-861585.png?ts=1751014865","Cronógrafo. US$ 2.250."),
("Seattle","861918","6b/25/30/1751015135/laco-fliegeruhr-typ-c-seattle-861918.png?ts=1751015135","Cronógrafo, tipo C. US$ 350."),
("Sylt","861789","40/4e/67/1751015104/laco-damenuhr-sylt-861789_1.png?ts=1751015104","Arquivo da foto: Damenuhr (feminino). US$ 350."),
("Trier","861915","e9/e6/c6/1751015078/laco-fliegeruhr-typ-c-trier-861915.png?ts=1751015078","Cronógrafo, tipo C. US$ 350."),
("Classics Azur 40","862075","0a/28/00/1751015302/laco-classics-azur-40-862075-neu.png?ts=1751015302","Classics, 40 mm. US$ 540."),
("Classics Berlin 40","861861","cc/ff/0e/1751015057/laco-classics-berlin-40-861861.png?ts=1751015057","Classics, 40 mm. US$ 1.450."),
("Classics Brandenburg 40","861859","9c/8c/cc/1751015048/laco-classics-brandenburg-40-861859.png?ts=1751015048","Classics, 40 mm, corda manual. US$ 1.450."),
("Classics Chemnitz 38","862065","be/50/4d/1751015189/laco-damenuhr-chemnitz-38-862065.png?ts=1751015189","Classics, 38 mm. US$ 540."),
("Classics Chemnitz 40","862066","b0/25/4e/1751015194/laco-damenuhr-chemnitz-40-862066.png?ts=1751015194","Classics, 40 mm. US$ 540."),
("Classics Cottbus 38","862063","84/d5/23/1751015179/laco-classics-cottbus-38-862063-neu.png?ts=1751015179","Classics, 38 mm. US$ 540."),
("Classics Cottbus 40","862064","8d/81/c5/1751015184/laco-classics-cottbus-40-862064-neu.png?ts=1751015184","Classics, 40 mm. US$ 540."),
("Classics Dresden 38","862073","53/51/cf/1751015226/laco-classics-dresden-38-862073-neu_1.png?ts=1751015226","Classics, 38 mm. US$ 540."),
("Classics Dresden 40","862074","03/cd/d7/1751015233/laco-classics-dresden-38-862073-neu.png?ts=1751015233","Classics, 40 mm. US$ 540. Foto do arquivo com nome do Dresden 38 (mesmo mostrador)."),
("Classics Gera 40","862062","f7/81/95/1751016488/laco-classics-gera-40-862062.png?ts=1751016488","Classics, 40 mm. US$ 540."),
("Classics Halle 38","862071","b4/29/d5/1751015215/laco-classics-halle-38-862071-neu.png?ts=1751015215","Classics, 38 mm. US$ 540."),
("Classics Halle 40","862072","d2/14/8f/1751015220/laco-classics-halle-40-862072-neu.png?ts=1751015220","Classics, 40 mm. US$ 540."),
("Classics Jena 38","862067","g0/5e/7b/1751015198/laco-classics-jena-40-862068-2020.png?ts=1751015198","Classics, 38 mm. US$ 540. Foto do arquivo é a do Jena 40 (mesmo mostrador)."),
("Classics Jena 40","862068","g0/5e/7b/1751015198/laco-classics-jena-40-862068-2020.png?ts=1751015198","Classics, 40 mm. US$ 540."),
("Classics Mocca 40","862077","b4/f0/4f/1751015314/laco-classics-mocca-40-862077.png?ts=1751015314","Classics, mostrador café, 40 mm. US$ 540."),
("Classics Petrol 40","862076","78/d0/cf/1751015308/laco-classics-petrol-40-862076-neu_1.png?ts=1751015308","Classics, mostrador petróleo, 40 mm. US$ 540."),
("Classics Plauen 40","861860","8e/25/34/1751015053/laco-classics-plauen-40-861860.png?ts=1751015053","Classics, 40 mm, corda manual. US$ 1.450."),
("Classics Stone 40","862078","8c/77/26/1751015320/laco-classics-stone-40-862078-neu.png?ts=1751015320","Classics, 40 mm. US$ 540."),
("Classics Weimar 38","862069","18/cc/83/1751015206/laco-damenuhr-weimar-38-862069.png?ts=1751015206","Classics, 38 mm. US$ 540."),
("Classics Weimar 40","862070","68/d2/6c/1751015210/laco-classics-weimar-40-862070-neu-2022.png?ts=1751015210","Classics, 40 mm. US$ 540."),
("Classics Wismar 40","862061","fa/10/0f/1751016484/laco-classics-wismar-40-862061.png?ts=1751016484","Classics, 40 mm. US$ 540."),
("Classics Wittenberg 40","861862","07/cd/ff/1751015061/laco-classics-wittenberg-40-861862.png?ts=1751015061","Classics, 40 mm. US$ 1.450."),
("Vintage Bordeaux","861876","ce/a0/43/1751015239/laco-damenuhr-bordeaux-861876.png?ts=1751015239","Linha Laco Vintage. US$ 2.150."),
("Laco Absolute","880101","c4/e4/70/1751014931/laco-lacoabsolute-880101.png?ts=1751014931","Linha Laco Vintage (Absolute). US$ 830."),
("Laco Absolute","880102","f0/7b/5b/1751014935/laco-lacoabsolute-880102.png?ts=1751014935","Linha Laco Vintage (Absolute). US$ 830."),
("Laco Absolute","880103","c0/21/bd/1751014939/laco-lacoabsolute-880103.png?ts=1751014939","Linha Laco Vintage (Absolute). US$ 830."),
("Laco Absolute","880104","3e/b7/b7/1751014946/laco-lacoabsolute-880104.png?ts=1751014946","Linha Laco Vintage (Absolute). US$ 900."),
("Laco Absolute","880105","b3/b5/c2/1751014951/laco-lacoabsolute-880105.png?ts=1751014951","Linha Laco Vintage (Absolute). A partir de US$ 300."),
]
AR2="Visto no arquivo de relógios do site oficial (laco-watches.com; fora de linha; trecho lido por resumo da página). "
for n,c,i,e in arch2: a(n,c,W+i,AR2+e)
PRO="Linha Flieger PRO (configurador; peça pronta 'Ready to Wear'). "
pro=[("Karlsruhe PRO 805","862142-FPB-37-U-E-X-A-E-U-X-L-S-R","cb/2c/78/1784801504/862142_805_front.png","Mostrador tipo B. 37 mm, automático."),
("Karlsruhe PRO 806","862142-FPB-40-U-E-G-A-E-U-X-A-M-R","d8/95/4b/1784801661/862142_806_front.png","Mostrador tipo B. 40 mm, automático."),
("Karlsruhe PRO 807","","6e/b6/b8/1784801524/862142_807_front.png","37 mm, automático. Configuração não legível: o site dá 862141/862142 de forma inconsistente para esta peça."),
("Karlsruhe PRO 808","862142-FPB-43-V-E-X-A-E-U-X-L-E-R","9f/53/f0/1784801553/862142_808_front.png","Mostrador tipo B. 43 mm, automático."),
("Karlsruhe PRO 809","862142-FPB-43-U-E-X-H-E-U-H-L-S-R","23/5b/28/1784801570/862142_809_front.png","Mostrador tipo B. 43 mm, corda manual."),
("Stuttgart PRO 1208","862141-FPA-37-U-E-X-A-E-U-D-L-B-R ","fc/92/34/1785163429/862141_1208_front.png","Mostrador tipo A. 37 mm, automático."),
("Stuttgart PRO 1209","862141-FPA-40-U-E-G-A-E-U-B-A-A-R","eb/e8/c1/1784802446/862141_1209_front.png","Mostrador tipo A. 40 mm, automático."),
("Stuttgart PRO 1210","862141-FPA-40-S-E-X-A-E-U-X-L-W-R","ce/bd/07/1784805292/862141_1210_front.png","Mostrador tipo A. 40 mm, automático."),
("Stuttgart PRO 1211","862141-FPA-43-U-E-G-A-E-U-H-L-B-R","14/b0/a6/1784805470/862141_1211_front.png","Mostrador tipo A. 43 mm, automático."),
("Stuttgart PRO 1162","862141-FPA-37-U-E-G-A-E-U-X-A-M-R","b2/08/97/1784805837/862141_1162_front.png","Mostrador tipo A. 37 mm, automático."),
]
for n,c,i,e in pro: a(n,c.strip(),M+i,PRO+e+" De € 950 a € 1.700 conforme a configuração.")
a("Hamburg DIN 8330","862164",M+"a4/0d/62/1750754800/fliegeruhr-hamburg-din-8330-862164-laco-uhrenmanufaktur.png","Relógio de piloto certificado pela norma DIN 8330. 43,5 mm, Sellita SW200 (TOP).")
a("Hamburg GMT DIN 8330","862165",M+"0f/7c/59/1750754868/fliegeruhr-hamburg-gmt-din-8330-862164-laco-uhrenmanufaktur.png","GMT certificado DIN 8330. Sellita SW330 (TOP).")
a("Stuttgart PRO – WatchTime Edition","852141",M+"b3/c3/26/1766056299/kombi-watchtime-edition-v2.png","Edição especial com a revista WatchTime (Flieger PRO, tipo A). € 1.480.")
# edições limitadas: acrescentar tiragem na B
LE={"Aachen Oliv 39":250,"Aachen Oliv 42":250,"Augsburg Oliv 39":250,"Augsburg Oliv 42":250,"Aachen Polar 42":250,"Augsburg Polar 42":250,
"Pilot Watch Basic Aachen Grün 42":250,"Pilot Watch Basic Augsburg Grün 42":250,"Pilot Watch Basic Aachen 42 Taupe California":200,
"München":200,"ProLab":170,"Edition 100":100,"Edition 97":97}
L=[((n+f" – edição limitada de {LE[n]} peças") if n in LE else n,c,i,e) for n,c,i,e in L]
RT="https://www.righttime.com/laco/"
RTx="Visto na lista de modelos descontinuados da loja Right Time (EUA). "
a("California Napa – edição limitada de 100 peças","853073",RT+"editions/853073s.jpg",RTx+"Laco 21 automático, aço, pulseira de couro conhaque. US$ 540.")
a("California Santa Ynez – edição limitada de 100 peças","853074",RT+"editions/853074s.jpg",RTx+"Mostrador branco tipo B. US$ 540.")
a("Vintage Worn Look 42 mm","861783",RT+"classic_watches/861783s.jpg",RTx+"Aço envelhecido, mostrador preto, Miyota 821A. US$ 480.")
a("Vintage Worn Look 36 mm","861784",RT+"classic_watches/861784s.jpg",RTx+"Aço envelhecido, mostrador preto, Miyota 821A. US$ 480.")
a("Pilot Watch Original Replika 55 (1ª versão)","861930",RT+"vintage_flieger/861930s.jpg",RTx+"55 mm, corda manual (ETA 6497.1 modificado). US$ 4.190.")
a("Engadin","861976",RT+"classic_watches/861976s.jpg",RTx+"Special Models; caixa com IP preto, cronógrafo a quartzo. US$ 520. Também no arquivo do site oficial (sem foto).")
a("Pilot Watch Original Paderborn Bronze","862150",RT+"pilot/862150s.jpg",RTx+"Caixa de bronze, 42 mm, automático, 100 m. US$ 1.990.")
a("Pilot Watch Basic Augsburg 42 Taupe California – edição limitada de 200 peças","862170",RT+"editions/862170s.jpg",RTx+"Laco 2S, mostrador cinza tipo A estilo California. US$ 540.")
a("RAD-AUX – edição limitada de 143 peças","862143","https://www.laco.de/media/9c/dc/9d/1751015923/862143-Laco-RAD-AUX-Observer-Erbstuck-Front-Face_1.png?ts=1751015923","Página oficial (descontinuado). Acabamento envelhecido Erbstück, 42 mm × 12,8 mm, Laco 24 automático (base ETA 2824-2), 5 ATM. € 3.130. A Right Time fala em 150 peças.")
a("Pilot Watch Original Replika 55 Erbstück (1ª versão)","861941","https://www.laco.de/media/3b/c1/03/1751015956/laco-fliegeruhr-typ-b-replika-erbstueck-861941.png?ts=1751015956","Visto no WatchBase (Replika 55 Erbstück, aço, mostrador preto); foto do site oficial com o mesmo código no nome do arquivo.")
WB="Visto no WatchBase (família Vintage; só o título, sem foto: link do site da marca). "
for c,d in (("880202","mostrador branco"),("880203","mostrador branco"),("880205","mostrador preto")):
    a("Laco Absolute",c,"https://watchbase.com/laco",WB+"Aço, "+d+".")
a("Beobachtungsuhr (B-Uhr) Baumuster B – Luftwaffe, anos 1940","","https://a.1stdibscdn.com/archivesE/jewelry/upload/15/584/15_1296347760_1.jpg","Relógio de observação da Luftwaffe da Segunda Guerra (Laco era um dos cinco fabricantes). Aço, 55 mm, mostrador tipo II (B) preto fosco, ponteiros luminosos. Anúncio da 1stDibs.")
a("Fliegeruhr 55 mm Laco-Durowe","23883","https://a.1stdibscdn.com/archivesE/jewelry/upload/525/26/XXX_525_1382982829_1-01.jpg","Anos 1940. 'Big Fliegeruhr' de aço, 55 mm, calibre Durowe D5 de 22 rubis, corda manual, segundos centrais com parada. Visto na 1stDibs (código do anúncio, a confirmar).")
a("Relógio de ouro amarelo 25,5 mm (c. 1948)","","https://a.1stdibscdn.com/laco-vintage-in-yellow-gold-with-a-black-dial-255mm-manual-watch-for-sale/22569652/j_212530121701937107583/j_21253012_1701937108064_bg_processed.jpg","Vintage, ouro amarelo, mostrador preto, 25,5 mm, corda manual. Visto na 1stDibs.")
a("Relógio feminino de ouro 14 K (1940)","","https://a.1stdibscdn.com/laco-14-karat-gold-ladies-german-watch-1940-for-sale/1121189/j_93824521588206146666/9382452_master.jpg","Feminino, ouro 14 quilates, 1940. Visto na 1stDibs.")
L=[((n+" – edição limitada de 96 peças") if n=="Edition 96" else n,c,i,e) for n,c,i,e in L]
a("Laco-Sport Duromat (anos 1950)","","https://images.antiquesatlas.com/dealer-stock-images/thevintagewristwatch/Gents_1950s_LacoSport_wrist_wa_as170a4484b.jpg","Vintage dos anos 1950. Caixa banhada a ouro, 33,5 mm, automático Laco-Duromat calibre 552 de 25 rubis. Visto na Antiques Atlas (vendido).")
a("Laco Sport feminino (anos 1960)","53036","https://vintageradar.com/cdn/shop/products/IMG_1321_1200x1200.jpg?v=1673612320","Vintage dos anos 1960. Laminado a ouro, fundo de aço, 25 mm, mecânico de 17 rubis. 'Series 53036' no anúncio da Vintage Radar (código a confirmar).")
a("Laco Durowe automático 34 mm","","https://thewatchpreserve.com/cdn/shop/files/sellbrite_00_88c8b13288e1.jpg?v=1790451719","Vintage. Aço, 34 mm, automático calibre 1172. Visto na The Watch Preserve (vendido).")
a("Relógio Art Déco (anos 1930)","","https://images.antiquesatlas.com/dealer-stock-images/thevintagewristwatch/Unusual_1930s_Art_Deco_Laco_wr_as170a12005b-3.jpg","Vintage dos anos 1930, estilo Art Déco. Aço, 25 × 33 mm, corda manual, calibre Laco 526 de 16 rubis. Visto na Antiques Atlas (vendido).")
