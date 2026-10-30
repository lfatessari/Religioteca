# Daniel Wellington (linha 361) — GRANDE (loja oficial com centenas de produtos/variações)
- Site: danielwellington.com (Shopify, lojas por país: au., za., my., us., vn.). Usa códigos DW00100xxx (SKU por tamanho; DW006xxxxx = variante "MIC").
- WebFetch não mostra fotos nem SKU das grades da DW; paginação ?page=2 é JS. products.json só pelo Firecrawl (JSON muito grande; extração JSON trunca ~12 itens).
- Firecrawl: créditos "running low".
## Seções feitas
## Fontes
- §2 loja oficial EU (www): products.json p1–7 via Firecrawl (1 crédito cada, saída salva em arquivo e lida com Python): 1521 produtos, 541 relógios, 845 SKUs (685 DW001…, 160 DW006… "MIC"). Decisão: DW006 (MIC) = mesma peça com outra ref. → vai na coluna E da linha DW001; linhas = 688.
- Falta: lojas regionais (us., au., outras) p/ peças fora da EU; modelos antigos (Dapper, Classic Black, Grace?, códigos antigos 0101DW…); blog; imprensa; lojas; usados.
- Lojas regionais AU/US/MY: +13 SKUs (AU tem peças antigas). MY = 0 novos → regionais convergem.
- Justintime (Índia): 64 modelos DW0DG/DW0DL exclusivos da Índia (sem nome de coleção); sufixo K = versão indiana do mesmo DW001.
- ippojapanwatch: 8 códigos novos mas títulos SEO ruins (DW00100840, 841, 793, 676, 108, 090; DW00600270, 041) → buscar nomes.
- Faixas faltando (descontinuados): 59–108 (Classy 26 mm, Dapper 34/38), 112–119, 152–160, 184–200, 287–302, 315–340, 351–357, 371–413, 487–507, 569–589, 600–624, 780–794…
- Jura Watches tem páginas antigas de Dapper (DW00100084–098, 114, 117) mas a coleção está vazia (só via busca).
- Jura (busca site:): Dapper 34/38 DW00100083–098, 114, 117; Classic Petite Durham 222 (sem foto; nomes no endereço). Mastersintime tem páginas historical-dw00100NNN.htm (Firecrawl, includeTags h1+img, 1 crédito) com nome e foto de descontinuados → hist.txt
- Firecrawl SEM CRÉDITOS às ~14:45 (renova em ~23h). Sondagem Mastersintime parou no DW00100118 (próximos: 119, 132, 134, 138, 152–160, 184–200…). Seguir só com WebSearch/WebFetch.
- 1ª passada encerrada: Yahoo TW pg1/2/7, Luxoia, Whamond, imprensa (Moodie, WatchGecko, Teddy B.) sem novidade. Buscas por código exato ("DW00100152") não funcionam no buscador.
- 2ª passada (marca VERMELHA: ~200 números DW001 sem modelo identificado; Firecrawl acabou): 11 fontes novas, 2 relógios novos; parou após 3 fontes seguidas sem novidade.
