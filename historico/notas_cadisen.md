# Cadisen (linha 253) — grande
- Site oficial real: cadisen.cn (Shopify, 99 produtos, SKU = referência completa ex. C8185MWWU). G diz cadisen-watch.com (não aparece em busca). Também existe cadisenwatch.com (Shenzhen) e cadisen.net.
- products.json via Firecrawl (1 crédito): 97 relógios + 2 pulseiras.
- Seções feitas: 1 (grande), 2 (cadisen.cn parcial)
- Falta: cadisenwatch.com, cadisen.net, 2c, 3..10b. Linhas antigas: C1032, C8097, C1052, C8089, C8102, C8143, C8172, C8177, C8181, C8183, C8187, C8190, C8197, C8208, C8212 cronógrafo, C9054 etc (AliExpress/Amazon).
- 17:25 cadisenwatch.com: 125 páginas page-data (367 variantes). Fusão com cadisen.cn por SKU (build2.py → rows_site.json, 398 linhas).
- Achados fora dos sites: C8212M/G (Seagull ST1900), C8221G/M, C8203, C8241M/G, C8240M, C8225, C8234, C8021G, C1032G, C8175 (3 cores, primetimepiece), C8189, C8100, C7063G, C8214 verde (primetimepiece).
- cadisen.com = site oficial CHINÊS (fundada 2011 segundo ele; cadisenwatch.com diz 2013 Shenzhen; Instagram diz 2007). Séries: 隽永, 荣耀, 时光永恒, 时光见证, 尊尚, 骐致, 天锐, 恒心, 琅玥, 探索者, 至臻, 极光, 臻金, 小金表, 歌雅, 宇宙, 黑鲨. Paginação por JS (pageNo não funciona). Parse: parse_cn2.py → cncom.json.
- jwlraddicts, eBay (categoria), cadisen.stores.jp (Japão oficial), AliExpress loja (Firecrawl inventou dados: descartado), cadisen.net fora do ar.
- 17:12 1ª passada encerrada (168 fontes, 546 linhas; 3 últimas fontes sem novidade). VERMELHO: catálogo chinês cadisen.com com ~70 modelos inalcançáveis (paginação por JS), variantes AliExpress, versões G. 2ª passada: en.cadisen.com, categorias 22/23/24, news, history, §2c cadisen.cn, Amazon, AliExpress.
