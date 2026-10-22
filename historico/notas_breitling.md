# Breitling (linha 228, grande)

## Seções feitas

## Notas
- 08:40 início. Grande (maison). usa_codigos=true. Dedupe por referência sem o sufixo de pulseira (últimos 2 caracteres, ex. P1/A1/S1/X1) — variações só de pulseira = mesma linha.
- breitling.com: listagens de coleção em JS ("No results found"); fichas /watches/<col>/<modelo>/<REF> abrem (imagem com hash no nome, não dá para montar). L: "Parcial – breitling.com listagens por JS".
- WatchBase: fichas e famílias aparecem em busca, mas WebFetch dá client_error. Títulos das buscas usados como dado (link da página).
- loupe.watch/prices/breitling: página pede que IA não reproduza os dados — não usado, não contado.
- Fontes boas: watchesofswitzerland en-int collections (24/página, fotos), lepage.fr (36/página), handt oembed, 1stdibs, analogshift breitling-sold (vintage).
- Pendentes (achar referência): Aviator 8 Curtiss Warhawk, Chrono-Matic 44, Chronomat 44 Airborne, Cosmonaute, Navitimer 125th Anniversary, Transocean Chronograph 1915 (bernardwatch).
- Wikipedia Breitling SA: Chronomat 1942 (Venus 175), Navitimer 1954, Cosmonaute (Navitimer 24 h, 1962 Scott Carpenter), Chrono-Matic 1969, Emergency/Emergency II (2013)/Orbiter 3 (1.999 peças), Top Time 1965 (Thunderball), Bentley 24 Le Mans, Bentley B04 GMT/B05 Unitime/B06, Aerospace, Chronospace. Buscar refs.
- Fashionphile: grade em JS (0). Bob's Watches: parâmetros de página ignorados (sempre a 1ª página de cada filtro).
- 09:15 1ª passada perto de saturar: CollectorSquare lpi (famílias) e WoS renderam muito; agora 0–5 novos por fonte. Chrono24: buscas site:chrono24.com não retornam resultados (motor de busca não indexa) — usar EveryWatch/1stDibs/CollectorSquare.
- WatchCharts brand_index e várias famílias dão client_error; /watches/brand/breitling/<familia> funciona às vezes (avenger, colt, bentley).
- gressive.jp (notícias de lojas no Japão): robots_disallowed — não abriu.
- rasin.co.jp (Japão, 1.139 anúncios Breitling em ~29 páginas): páginas 6, 14, 15, 16, 19, 23, 24, 26 + Bentley + review abertas (vieram de buscas). Muitas edições limitadas do Japão (Blue Impulse, JSP, Black Eye, Roman, Japan Edition…). Edições com a mesma referência base entram como linhas separadas (prefixo ! no add.py).
## Fim da 1ª passada (~09:20) — 128 fontes, ~1.056 relógios
### 10b auto-auditoria
1. Site oficial: listagens em JS; páginas abertas: ficha Superocean 42, categoria feminina (via api/watches/women → 30 refs), men's watches (20 refs), icons/professional (Emergency, Exospace, Endurance). Blog/imprensa oficial não abre (sem resultados de busca). Páginas 2–7 de mens-watches não apareceram em busca (não alcançadas).
2. §2c: buscas site:breitling.com por linha (Navitimer, Chronomat, Superocean, Heritage 57, Top Time, Premier, Avenger, Aviator 8, Classic AVI, Super AVI, B35, Blackbird) — títulos com refs entraram com link da página.
3. Lojas: WoS (8 páginas Chronomat + Premier + Superocean + men's p12), Lepage, Mayors, Berry's, Market Cross, Knar, Jura, JR Dunn, Wempe, The 1916 Co., Bob's, Exquisite, Wristcheck, Luxury Closet, Watchfinder (UK/HK/US), Rasin (Japão).
4. Primeiro modelo/história: Chronomat 1942 (769), Premier 1940s (777/790/791 Duograph, 760, 782, 754, 778), cronógrafos 171/178/1450/1451, Navitimer 806 (1952/1954), Co-Pilot 765 AVI/7650, Top Time 1964 (2000–2009, 810, 814, 824?), Datora (785, 799, 803, 804, 2030, 2031), Unitime (1260, 2610, 1765), Superocean 807/1004/2005, Long Playing 815/820, Chrono-Matic 1806/2110–2116. Primeiro relógio de Léon Breitling (1884, cronógrafos de bolso) sem modelo nomeado.
5. J (Navitimer, Chronomat, Superocean, Premier, Avenger, Top Time): todos encontrados.
6. Edições limitadas/colaborações na B com nº de peças quando a fonte informa; nenhuma peça única encontrada.
7. Fontes 1ª passada: 128.
- Logo: não encontrado em fonte aberta (cdnlogo deu erro; site oficial sem imagem de logo; Wikipédia sem URL). K fica vazio.
- DECISÃO: VERMELHA. Milhares de referências desde 1884 (vintage 7xx/8xx/2xxx, anos 90 A/B/D/K/L-13xxx, edições do Japão), muitas só com link de página; Chrono24/EveryWatch/WatchBase inacessíveis; listagens oficiais em JS.
## 2ª passada: foco em vintage (Premier/Datora/Top Time/Navitimer anos 50–70, Sprint, Cadette, Bidynator, Unitime), anos 90 (Chronomat 81950/A13047/A13048, Old Navitimer, Aerospace/Jupiter/Pluton), edições limitadas (militares, Japão, aniversários).
- 09:23 fim da 2ª passada: 12 fontes, 31+ relógios novos (vintage Premier/Sprint/outros modelos, edições do Japão) -> 3ª passada obrigatória (foco: famílias CollectorSquare ainda não abertas, leilões Fellows, edições militares).
