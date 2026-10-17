---
name: "relogioteca-pesquisa-exaustiva"
description: "Roteiro completo para pesquisar e gravar todos os modelos (nome, código, foto, características) de uma marca de relógios na planilha Relogioteca (abas Marcas e Relógios). Use em toda nova marca (até três pequenas por execução; marca grande sozinha), inclusive em execuções agendadas sem supervisão."
---

# Pesquisa exaustiva de marca – Relogioteca

Objetivo: na PRIMEIRA rodada, listar todos os modelos e versões (atuais e descontinuados, inclusive antigos/vintage) de cada marca (até três por execução, ver §0b), com código de referência e foto, sem que o usuário precise pedir "procure mais". O que mais importa: nome, código e link da imagem. Esta skill tem de bastar sozinha: ela é usada em conversas novas, sem acesso ao histórico.

**Lição da Arcanaut (out/2026):** a 1ª passada achou 53 relógios; a 2ª, pedida pelo usuário, achou mais 33. Causas: (1) confiar no sitemap/products.json do site, que só mostra produtos publicados — a marca despublica as peças vendidas, mas as páginas continuam no ar e indexadas; (2) não ler todos os artigos do blog nem a área de imprensa; (3) abrir poucas lojas e não fazer busca `site:` dentro de cada loja; (4) não procurar o primeiro modelo da marca (ARC-I de 2018). As seções 2c, 10b e 11 existem para isso não se repetir.

## 0a. Como garantir que o roteiro seja seguido (ler primeiro)
**Lição da Archimede (out/2026):** a marca foi pintada de vermelho, mas a 2ª passada foi feita curta (só ~10 fontes, misturada com o fim da 1ª) e o relatório não separou as passadas. Causas: o roteiro foi seguido de memória em vez de relido; a 2ª passada não era uma etapa separada; nada impedia gravar sem ela. Por isso:
- No início de CADA bateria, ler este SKILL.md inteiro (não confiar na memória da conversa), mesmo que já tenha sido lido antes.
- Criar a lista de tarefas com UMA tarefa por seção obrigatória: 1 Dimensionar, 2 Site oficial, 2c Produtos escondidos, 3 Primeira página + buscas extras, 4 Catálogos, 5 Agregadores, 6 Chrono24, 7 Revendedores, 8 Usados, 9 Imprensa, 10 Buracos, 10b Auto-auditoria, e — se a marca ficar vermelha — **"2ª passada" como tarefa própria**, criada no momento em que se decide pintar de vermelho. Só marcar uma tarefa como concluída quando a seção tiver sido feita de verdade.
- Registrar CADA fonte aberta no `marca_<marca>.json` (campo `fontes`, com a passada e quantos relógios novos trouxe). O script de gravação (§13) tem uma **trava**: recusa gravar se faltar o mínimo de fontes (15, ou 25 se grande) ou, em marca vermelha, se a 2ª passada não tiver pelo menos 10 fontes novas que não estejam na 1ª. Não contornar a trava listando fontes que não foram abertas de verdade: o relatório mostra essa lista ao usuário.

## 0. Contexto da planilha (leia antes de tudo)
- Arquivo: `Relogios_atualizada_NN.xlsx` (NN = versão; sempre trabalhar na de maior número e salvar como NN+1, nunca sobrescrever). Abas: `Marcas`, `Planilha1`, `Relógios`, `Tabela de faixa de preços`.
- Aba **Marcas** (≈1494 linhas, uma por marca): A Marca | B País | C Cidade | D Principal Característica | E Faixa de preço (641 células são ArrayFormula – nunca mexer) | F Preço médio | G Site | H Instagram | I História | J Principais relógios | K Logo | L Site bloqueado. `max_column` informa 16384: nunca percorrer todas as colunas (trava); usar só A–L.
- Aba **Relógios** (uma linha por relógio): A Marca (texto IDÊNTICO ao da coluna A de Marcas, ex.: "anOrdaim") | B "Nome do modelo - CÓDIGO" | C URL da imagem (com hyperlink igual ao valor) | D não usar (tem links antigos em ~74 linhas; preservar) | E Características. Estilo das células novas: copiar da linha 1190.
- Ordem de trabalho: seguir a ordem da aba Marcas. O trabalho atual começou na linha 18 (ADPT) e vai em sequência; as linhas 2–17 (1776 Atelier … Acto) ainda não foram feitas e ficam para depois, salvo pedido. No início da planilha existem blocos antigos de outras marcas (Cuervo y Sobrinos, Rado, Tag Heuer… até Ulysse Nardin) feitos em outra época: não mexer.
- Anomalias conhecidas (só relatar, não corrigir sem pedido): blocos antigos e duplicados de Akrone, Akura, Alain Silberstein, Albert Riele, Albishorn e Alcadus nas linhas ~1191–1201; Angular Momentum dividido em dois blocos (≈4208 e ≈4802).

## 0b. Qual marca fazer (execução agendada)
- No máximo TRÊS marcas por execução, sempre na ordem da aba Marcas. Antes de pesquisar, dimensionar rapidamente a próxima marca e as duas seguintes (ver §1):
  - próxima é grande → fazer só ela;
  - senão, pegar as próximas marcas não grandes em sequência, até completar três, parando antes da primeira grande (a grande fica sozinha na execução seguinte). Ex.: pequena, pequena, pequena → as três; pequena, pequena, grande → só as duas pequenas; pequena, grande → só a pequena.
- Pular as marcas listadas em `marcas_ja_feitas_fora_da_ordem` no `estado.json` (já têm linhas em Relógios).
- Fazer várias marcas NUNCA reduz a profundidade de cada uma: cada marca passa por todas as seções e pelo mínimo de fontes do §11, como se estivesse sozinha.
- Se uma marca que parecia pequena se revelar grande no meio da pesquisa, terminar as já concluídas e ela, com a profundidade completa, e deixar as outras para a execução seguinte (atualizar `estado.json`).
- Se existir um arquivo `estado.json` junto da planilha, usar `proxima_linha_marcas`. Senão: a próxima marca é a primeira linha de Marcas, depois da última marca da sequência já gravada (a última marca no fim da aba Relógios), que ainda não tem nenhuma linha em Relógios.
- Ao terminar, atualizar `estado.json` (`proxima_linha_marcas`, `ultima_versao`, e um registro da marca feita: data, linhas, nº de relógios, vermelho sim/não, site bloqueado sim/não, nº de fontes abertas).
- Execução sem ninguém olhando: não fazer perguntas. Tomar a decisão mais razoável, registrar no relatório e seguir. Só parar (sem gravar) se a planilha não for encontrada ou se a verificação final falhar.

## 0c. Limites do ambiente
- Só WebFetch e WebSearch alcançam a internet; curl/pip a sites quaisquer costumam ser bloqueados. Não tentar contornar.
- Se uma página responder "rate limited / do not fetch again" (HTTP 429 do proxy), avisar o usuário (SendUserMessage) dizendo qual página não abriu e por quê, e seguir sem ela.
- O WebFetch resume a página; para listas longas pedir saída compacta e paginar (ex.: `per_page=10&page=N`). Quando a página tiver uma seção fixa repetida (ex.: "Our watches" no rodapé de todo artigo), pedir no prompt para IGNORAR essa seção e ler só o corpo do artigo, com os links e imagens do corpo.

## 1. Dimensionar
- Checagem rápida (poucas chamadas, antes da pesquisa completa) para decidir se a marca é **grande**. Basta UM destes sinais:
  - EveryWatch: a página da marca (`everywatch.com/<marca>`) mostra mais de 150 anúncios no total (somando à venda e vendidos);
  - site oficial com mais de 80 produtos/variações na loja ou no catálogo;
  - linha antiga extensa (dezenas de referências vintage diferentes à venda) ou maison/grupo conhecido;
  - **marca de peças únicas ou mostradores com nome próprio** (Fordite, meteorito, pedras, "one of one", "pièce unique"), configurador/sob encomenda, ou blog com um artigo por peça — cada peça é uma linha e muitas ficam escondidas (ex.: Arcanaut);
  - pistas da própria aba Marcas (coluna J com muitas linhas/coleções, faixa de preço de luxo).
- Na dúvida, tratar como grande (fazer sozinha).
- Exemplos já vistos: Aquastar (775 anúncios, vintage desde 1957), Aquanautic (447 anúncios, configurações intercambiáveis) e Arcanaut (86+ peças únicas de Fordite) = grandes; Aquadive (27 anúncios; tem vintage, mas poucas referências) e Archetype (49 variações, catálogo fechado) = não grandes.
- Crie uma lista de tarefas: pesquisa, gravação, verificação.
- Mantenha um arquivo de notas da marca (`notas_<marca>.md`) durante a pesquisa e grave os achados nele a cada poucas fontes, para não perder nada se o contexto encher. Nele, manter também a **lista de fontes abertas** (endereço + quantos modelos novos trouxe), que alimenta o §11 e o relatório.

## 2. Site oficial (completo)
- Confira se o site da coluna G é mesmo da marca (ex.: aquastar.com é de frutos do mar; o oficial é aquastar.ch). Se estiver errado, use o certo e aponte no relatório (só corrigir a planilha se o usuário disser "corrija").
- Loja: `products.json?limit=250` ou `?limit=15&page=N` (Shopify), `/collections/<x>/products.json`, `/products/<handle>.oembed` (título, foto, preço, descrição), sitemap_products; `/wp-json/wc/store/products?per_page=10&page=N` (WooCommerce; a resposta vem cortada, então paginar pequeno); `?p=N` (Magento); `/shop/page/N` (Odoo).
- Shopify com muitas variantes: listar os handles pelo sitemap de produtos e abrir `/products/<handle>.oembed` de cada um; procurar coleções de arquivo (`/collections/*archive*/products.json`). Abrir TODAS as coleções do `sitemap_collections` (ex.: archive, darc-room), não só all-watches.
- Ler o `sitemap.xml` inteiro: sitemap_products, sitemap_pages, sitemap_collections, **sitemap_blogs e sitemap_articles** (ler o corpo de TODOS os artigos: lançamentos, nomes de peças únicas, fotos de cada peça no nome do arquivo, ex.: `Fordite_June_2024_Csonka_Csonka.jpg`).
- Páginas "about", "the-story", "history", "our-team": procurar o PRIMEIRO modelo da marca e modelos antigos (ex.: ARC-I de 2018 da Arcanaut), e depois buscá-los fora do site (Pinterest, fóruns, EveryWatch).
- Área de imprensa (`/a/press-area`, `/press`, `/media`, presskitbuilder): lista os lançamentos com kits de imprensa.
- Descrição de cada produto limitado/especial (oembed): ler para achar colaborações, homenagens e tiragem (ex.: Garnet Goblin = colaboração Chronoshop.cz × Granát Turnov; Chronomara = homenagem a Johnny McElherron).
- WordPress: `/wp-json/wp/v2/pages?per_page=100&_fields=slug,link,title`, `/wp-json/wp/v2/media?search=<termo>&_fields=source_url` (bom para achar logo e fotos "knockout"/fundo branco).
- Wix: store-products-sitemap.xml e pages-sitemap.xml.
- Páginas de arquivo, "discontinued", "archive", "heritage", "original models", timeline, release schedule, catálogos e folhetos PDF, manuais (às vezes listam todas as linhas).
- Se a home bloquear (robots), tentar subpáginas diretas (ex.: /all-watches/, /collections/<nome>/, /history/), que às vezes abrem.
- PDF só com imagem: pedir ao usuário que anexe (fora de execução agendada) e ler as páginas como imagem.
- Logo: header/og:image, wp-json media "logo", arquivos `*logo*` no CDN; senão revendedores (brand_logos, imagem da coleção), Piazo (`piazo.jp/assets/base/img/content/top_brand/<marca>.png`), Watchonista (logo do perfil da marca), WatchBase, watchtraderhub. Preferir o logo com o nome escrito ao favicon.

## 2b. Site oficial bloqueado: registrar e CONTINUAR
- Se o site oficial (ou a loja oficial, ou o site de uma sublinha) não abrir para leitura automática (robots, 403, 429, erro), escrever na coluna L de Marcas: "Site bloqueado – <domínio> <motivo>; revisitar com navegador" (ou "Parcial – …" quando só parte não abre). O cabeçalho L1 já existe; o script copia o estilo da célula K.
- O registro NÃO encerra nem encurta a pesquisa: seguir todas as seções seguintes na mesma profundidade, compensando com fontes paralelas.
- Bloqueios de sites que não são da marca vão só no relatório.
- Já registrados: Antoine Preziuso, Anstead, Anpassa, Aquadive (parcial), Aquanautic, Aquatrident, Aramar, Arcaido.

## 2c. Produtos escondidos (OBRIGATÓRIO em toda marca)
O sitemap e o products.json só mostram o que está publicado. Peças vendidas e edições antigas costumam ser despublicadas, mas a página continua no ar e o buscador ainda a mostra.
- Fazer várias buscas `site:<domínio>/products <termo>` (e `site:<domínio> "<Linha> —"`), trocando o termo: nome de cada linha/coleção, materiais, palavras dos títulos já vistos (ex.: Groovy, Linear, Ripple, Ultra), "limited", "edition", "one of". Continuar enquanto aparecerem handles novos.
- Buscar também `"<domínio>/products/<prefixo-comum>"` (ex.: `"arcanaut.watch/products/arc-ii-fordite"`).
- Página oculta que não abre (CLIENT_ERROR/404 no oembed): entra assim mesmo, com o título que a busca mostrou e o link da página na coluna C; se um artigo do blog ou uma loja tiver foto da peça, usar a foto.
- Repetir o mesmo nas lojas que vendem a marca (§7): `site:<loja>/products <marca>`, porque as lojas também escondem peças vendidas ("pre-owned", "sold out").
- Lojas com domínio por país (ex.: shop.timeandtidewatches.com e .co.uk): verificar os dois.

## 3. Primeira página de busca (SEMPRE)
- Buscar "<marca> watches" (e "<marca>" watch com aspas se vier poluído) e abrir TODOS os sites da primeira página (lojas, bancos de dados, feiras, revistas, distribuidores). Para cada um: comparar com o que já foi achado, acrescentar o que faltar e anotar no relatório o que trouxe (ou que não trouxe nada / não abriu).
- Buscas extras obrigatórias: "<marca> for sale used", "<marca> pre-owned", "<marca> \"one of one\" OR \"unique piece\" OR \"pièce unique\"", "<marca> limited edition", "<marca> collaboration", "<marca> first watch" / nome do primeiro modelo. Abrir os resultados novos.
- Se o usuário mandar uma lista de sites, abrir todos.

## 4. Catálogos oficiais
- "<marca> catalogue pdf", "katalog", "catalogo", PDFs de feiras (Inhorgenta, Baselworld, Watches & Wonders, HKTDC), press kits, guias de colecionador, manuais. Ler todos os anos encontrados; se um PDF vier cortado, registrar o ponto de corte e avisar.

## 5. Bancos de referências e agregadores
- **EveryWatch** (principal substituto da Chrono24): página da marca `everywatch.com/<marca>` (mostra contagem total, famílias e ~48 anúncios), `?pageNumber=N` (inconsistente: às vezes repete ou vem vazia), páginas de família `everywatch.com/<marca>/<familia>`, e cada anúncio `/watch-NNNN` traz referência, ano, tamanho e a foto `img.everywatch.com/media/...webp` (usar a versão sem `_320`). A aba "Sold" não abre.
- **WatchPatrol**: `watchpatrol.net/discover/brands/<marca>/` e páginas de modelo (`/ja/discover/brands/<marca>/<modelo>/`), anúncios `/listing/NNNN/` com foto `img.watchpatrol.net`.
- **WatchPolice** (`watchpolice.com/brands/<marca>`: lista a linha completa, inclusive esgotados) e **WatchSpies** (`watchspies.com/brand/<marca>`: anúncios de fóruns/Reddit com foto).
- WatchBase (famílias + página de cada relógio, foto `cdn.watchbase.com/watch/lg/...`), The Watch Pages (`/brands/<marca>`), Hourstriker (`/database/<marca>`), Watchonista, allwatches.org, watch-wiki, grail-watch wiki, GPHG (`gphg.org/en/watches/...`, fotos `cms.gphg.org`), Europa Star (`europastar.com/brand-index/<id>-<marca>.html` + fichas `swisstime`), Worldtempus, Masterhorologer, CollectorSquare (índice de leilões), Coveted, WatchCharts, Microbrand Atlas, DreamChrono, Piazo (Japão), Pinterest (pins de modelos antigos; abrir não funciona, usar o link do pin).

## 6. Chrono24 (SEMPRE)
- Acesso direto bloqueado. Usar `site:chrono24.com <marca>` (e .de) e o EveryWatch. Se a sessão tiver navegador ligado ao computador, abrir pela Chrono24.
- Modelo visto só por título de anúncio pode entrar com o link do anúncio no lugar da foto, avisando no relatório e na coluna E ("visto só em anúncio…").

## 7. Revendedores (mínimo 5, países diferentes)
- Shopify (products.json, oembed; limpar `crop=center&height=1&width=1` → `?v=...&width=1200`). Se o products.json da coleção vier vazio, usar o `sitemap_products_1.xml?from=1&to=99999999999` da loja pedindo só os handles com o nome da marca, e a busca `site:<loja>/products <marca>` (§2c).
- WooCommerce: `/wp-json/wc/store/products?search=<termo>&per_page=30` traz nome, link e foto mesmo quando a vitrine não mostra.
- Descobrir as lojas da marca: página "retailers"/"store-locator" do site oficial e lojas que aparecem nas buscas do §3.
- Exemplos: Analog Shift (coleção `<marca>-sold` lista o arquivo de vendidos), Craft & Tailored (`/search?q=<marca>&type=product` + oembed), Collective Horology, The Limited Edition (UK), Time+Tide Shop (.com e .co.uk), Watches.com, Right Time, Delray Watch, Jura Watches, WatchGecko, First Class Watches, Timeanagram, Grailium, La Casa dell'Orologio, FiveFortyFive, Wristler/Chronext, Exquisite Timepieces, Helveti, Mayors/Watches of Switzerland, Touch of Modern, Serious Watches, Watch Collectors, A Collected Man, The Keystone, Swiss Gallery, Betteridge, Chronoshop.cz, Piazo, lojas do país da marca.
- Japão é forte para algumas marcas: Yahoo! Leilões (`auctions.yahoo.co.jp/brand/<id>/`), Mercari (`jp.mercari.com/s/<id>`), Piazo — os títulos trazem códigos.

## 8. Usados e leilões
- eBay: páginas de busca não abrem pelo WebFetch; usar `site:ebay.com <marca>` e `ebay.de/shop/<marca>` (traz títulos, sem links); páginas `/itm/` às vezes abrem. Nunca usar a imagem placeholder `7WgAAOSwQ7haxTU1`.
- WorthPoint, PicClick, Catawiki, 1stDibs, Heritage, Fellows, Phillips (página do artista + lotes, imagens dist.phillips.com), Antiquorum (lotes individuais abrem; a busca não), Christie's, Sotheby's, Bonhams, Lyon & Turnbull, Drouot/Setdart, leilões beneficentes (Only Watch, Pink Dial Project), WatchUSeek, Reddit r/Watchexchange (via WatchSpies), Relojes Especiales, uhrforum.de.

## 9. Imprensa e lançamentos
- Europa Star, aBlogtoWatch, Monochrome (inclusive a série "Collectors", com peças únicas), Worn & Wound (página `wornandwound.com/brand/<marca>/` lista todos os artigos), Hodinkee, WatchPro, Fratello (colaborações!), WatchTime, WatchesBySJX, Gear Patrol, Professional Watches, Two Broke Watch Snobs, Time and Watches, Time+Tide, Quill & Pad, Revolution, 10to2, FLTR, Fifth Wrist, WatchGecko magazine, Kickstarter/Indiegogo/Kicktraq, fóruns (WatchUSeek).
- Nas matérias, ler legendas e nomes de arquivos de imagem: muitas vezes trazem o nome ou número da peça (ex.: "Arcanaut ARC II Fordite 137, 138 and 142").

## 10. Caça aos buracos (obrigatório)
- Tabela por coleção com todos os códigos vistos; buscar lacunas de sequência (ex.: FD11, FD12 → buscar FD13; peças numeradas Nº 23, 34, 47 → buscar outros números), cores/materiais citados sem código, protótipos, peças únicas, encomendas, colaborações, edições de aniversário, o primeiro modelo da marca e linhas antigas (anos 60–90).

## 10b. Auto-auditoria antes de gravar (obrigatória)
Responder por escrito nas notas, e corrigir o que faltar antes de gravar:
1. Li TODOS os artigos do blog e a área de imprensa? Cada nome de peça citado ali está na lista?
2. Fiz as buscas `site:<domínio>/products` do §2c até pararem de aparecer handles novos?
3. Fiz `site:<loja>/products <marca>` em cada loja que vende a marca?
4. Achei o primeiro modelo da marca e os modelos antigos citados no "about"/história?
5. Cada nome em I/J da aba Marcas foi encontrado? (Se não, buscar de novo; se ainda não, relatar.)
6. As edições limitadas, colaborações e homenagens estão na coluna B com o nº de peças? As peças únicas estão marcadas no começo da coluna E ("Peça única.") e NÃO na B?
7. Quantas fontes diferentes abri (§11)?

## 11. Critério de parada
- Mínimo de fontes diferentes abertas por marca, antes de poder parar: **marca pequena 15; marca grande ou de peças únicas 25**. Contam só fontes realmente abertas (não resultados de busca só olhados), de pelo menos 4 tipos diferentes: site oficial (incl. blog/imprensa), lojas, agregadores/usados, imprensa.
- Depois do mínimo, só encerrar quando 3 fontes novas e independentes seguidas não trouxerem nenhum modelo novo.
- **O mínimo é só um piso.** Atingir 15 ou 25 fontes nunca é motivo para parar: quem decide o fim é o critério das 3 fontes seguidas sem novidade. Se a marca pede 40 fontes, abrir 40.
- **Ordem de busca: as fontes que mais rendem primeiro**, seguindo o roteiro (site oficial completo, produtos escondidos do §2c, bancos de dados como WatchBase e EveryWatch, depois lojas, usados e imprensa). Nunca encher a lista com fontes fracas ou repetitivas só para chegar ao número; a coluna `novos` de cada fonte aparece no relatório e mostra isso.
- Deduplicar por código normalizado (sem pontos/hífens, O→0), mantendo a grafia da fonte. Anúncios repetidos do mesmo relógio não contam. Peças únicas com nomes diferentes são relógios diferentes (ex.: "Tidal Barrier" ≠ "Tidal Apocalypse").
- Catálogo fechado (ex.: Archetype): quando o site oficial, a loja dona da marca e a campanha de lançamento batem no mesmo número, registrar essa conferência no relatório como prova de que a lista está completa.

## 11b. Marca vermelha: passadas extras (automático)
- Pintar a coluna A de Marcas de vermelho quando houver certeza de que existem mais modelos que não deu para listar (peças únicas não publicadas, configurador, centenas de anúncios com referências sem foto, configurações intercambiáveis, linhas antigas sem nome conhecido).
- Toda marca pintada de vermelho recebe, na mesma execução, uma 2ª passada profunda: **no mínimo 10 fontes que ainda não foram usadas na 1ª**, obrigatoriamente incluindo o §2c refeito com termos novos e as buscas extras do §3, e indo atrás especificamente do que deixou a marca vermelha (edições sem nome, catálogos antigos, peças únicas) — não de qualquer fonte nova só para completar as 10. A 2ª passada começa só depois de a 1ª estar encerrada pelo critério do §11; fontes abertas antes disso contam como 1ª passada.
- Se a 2ª passada ainda trouxer bastante (5 ou mais relógios novos), fazer uma 3ª, com o mesmo mínimo de 10 fontes novas.
- As fontes de cada passada vão no campo `fontes` do `marca_<marca>.json` com `"passada": 1, 2 ou 3`; o script recusa gravar marca vermelha sem a 2ª passada.
- No relatório: quantas fontes e quantos relógios novos cada passada trouxe (o script imprime essas linhas) e por que parou.

## 12. Regras de conteúdo das linhas
- **Coluna B**: "Nome do modelo - CÓDIGO".
  - Marca que usa códigos como padrão e modelo sem código → "Nome (sem referência publicada)".
  - Marca que NÃO usa códigos como padrão (o site oficial identifica só por nome/cor, ex.: anOrdain, Anton Suhanov, Anstead, Anura Rafael, Aonic, Aquadive, Aquastar, Arcanaut) → só o nome, sem sufixo; quando um revendedor mostrar o código, ele entra.
  - Enxuta: cor, material, tamanho, calibre, ano NÃO vão na B quando nome + código já diferenciam.
  - SEMPRE manter o que torna o relógio especial: edição limitada (com nº de peças: "– edição limitada de 500 peças"), aniversário, colaboração ("– colaboração Chronoshop.cz × Granát Turnov", "Fratello × …"), homenagem ("– homenagem a …"), ligação histórica famosa (ex.: "o do filme 'Tubarão'").
  - **Peça única NÃO vai na coluna B** (nem "peça única", nem "mostrador único", nem "1/1"): vai no começo da coluna E, como "Peça única." seguido das características. Ex.: B `Arc II Fordite "Cosmic Jazz"` e E `Peça única. Mostrador de Fordite…`. Edição limitada, colaboração, homenagem e aniversário continuam na B.
  - Tipo entra quando faz parte da identificação (ex.: "Histórico – Cronógrafo").
  - Dois modelos sem código com o mesmo nome: acrescentar só a diferença mínima ("– mostrador preto e branco", "– 42 mm", "(1ª série, 2019)", "– Nº 137").
  - Códigos: números só de dígitos que parecem de série (5–6 dígitos, "B010718") não entram; códigos de estoque de lojas (SKU da loja, "AQA-001", "AS04878") e códigos duvidosos vão na coluna E; números de calibre (Valjoux 23, Felsa 4000N) não são referência.
  - Anúncios genéricos sem nome e sem referência distinta (ex.: "Aquastar 42mm black") não viram linha.
  - Objetos que não são relógios de pulso (relógios de mesa, peças, pulseiras, bonés): só se forem parte relevante da marca, e avisar no relatório.
- **Coluna C**: preferir o relógio de frente em fundo liso/branco ("knockout", "hero", "front", "soldier", "bg_processed"); senão qualquer foto do modelo (inclusive foto de artigo do blog ou de loja); senão o link da página/anúncio/PDF (indicar a página do PDF na coluna E).
- **Coluna E**: quando o relógio for peça única, começar com "Peça única." (sempre, mesmo que o resto fique vazio). Depois, características SOMENTE do que já aparece na fonte do modelo (material, tamanho, mostrador, calibre, resistência, tiragem, ano), em texto corrido começando com maiúscula. Não pesquisar só para preencher E. Se a fonte não traz, deixar vazio. Quando C for link de página, dizer isso em E ("visto só no título da página do produto (link da página)").
- **Aba Marcas**: só escrever K (logo), L (site bloqueado) e o vermelho em A. Corrigir outros dados só quando o usuário disser "corrija" (apontar no relatório: descrição errada, site errado etc.). Tirar o vermelho só quando o usuário pedir, restaurando o preenchimento original (copiar o fill da versão anterior).
- **Correções pedidas pelo usuário** (ex.: "corrija o endereço") e melhorias em linhas já gravadas (foto melhor, colaboração que faltou na B): fazer num passo separado ANTES do script — abrir a planilha, mudar só as células necessárias, salvar num arquivo temporário e conferir por comparação (snapshot antes/depois) que só essas células mudaram e que as 641 ArrayFormula continuam; depois rodar o script sobre esse temporário.

## 13. Gravação (script padrão)
1. Escrever os relógios em `dados_<marca>.txt`, uma linha por relógio: `Nome|CÓDIGO|URL_imagem|Características` (código vazio quando não houver; nada de "(sem referência publicada)" no nome — o script acrescenta; não usar o caractere "|" dentro dos campos).
2. Escrever `marca_<marca>.json`: `{"marca": "<igual à coluna A de Marcas>", "usa_codigos": true|false, "logo": "<url ou vazio>", "site_bloqueado": "<texto ou vazio>", "vermelho": true|false, "grande": true|false, "complemento": false, "fontes": [{"url": "<endereço aberto>", "passada": 1, "novos": <nº de relógios novos que ela trouxe>}, …]}`. Toda fonte realmente aberta entra na lista (inclusive as que não trouxeram nada, com `novos: 0`). `complemento: true` só para acrescentar linhas a uma marca já gravada, a pedido do usuário (o script confere que a marca já existe).
3. Salvar o script abaixo como `gravar_marca.py` (substituindo uma versão antiga que não tenha a trava) e rodar: `python3 gravar_marca.py Relogios_atualizada_NN.xlsx Relogios_atualizada_NN+1.xlsx dados_<marca>.txt marca_<marca>.json`.
4. Com duas ou três marcas: rodar o script uma vez por marca, em sequência (a saída de uma é a entrada da seguinte, em arquivos temporários) e entregar só a versão final NN+1.
5. Marca que já tem linhas (2ª passada): o `dados` leva só os relógios novos; o script recusa nomes repetidos e acrescenta os novos no fim do bloco da marca.
6. Se o script parar com `!! TRAVA`, nada foi gravado: voltar à pesquisa, fazer o que falta e rodar de novo. Nunca baixar o mínimo nem marcar `complemento` para escapar da trava.
7. Só entregar se a última linha disser `RESULTADO: OK`. Se a marca já tiver linhas, o script reescreve do início do bloco dela até o fim para manter tudo contíguo; se aparecer falha de contiguidade por causa de anomalias antigas abaixo do bloco, não forçar: relatar.

```python
"""Grava uma marca na planilha Relogioteca.
Uso: python3 gravar_marca.py ENTRADA.xlsx SAIDA.xlsx dados.txt marca.json
dados.txt: uma linha por relógio  ->  Nome|CÓDIGO|URL_imagem|Características
marca.json: {"marca": "<igual à coluna A de Marcas>", "usa_codigos": true/false,
             "logo": "url ou vazio", "site_bloqueado": "texto ou vazio", "vermelho": true/false,
             "grande": true/false, "complemento": false,
             "fontes": [{"url": "...", "passada": 1, "novos": 0}, ...]}
Trava de profundidade: sem o mínimo de fontes (15; 25 se grande) e, se vermelho, sem a
2ª passada com 10+ fontes novas (que não estejam na 1ª), a gravação é RECUSADA.
"complemento": true só vale para marca que já tem linhas na aba Relógios.
"""
import sys, json, copy, re
import openpyxl
from openpyxl.worksheet.formula import ArrayFormula
from openpyxl.styles import PatternFill
from urllib.parse import quote
from collections import Counter

ENT, SAI, DADOS, CFG = sys.argv[1:5]
cfg = json.load(open(CFG, encoding='utf-8'))
S = ' (sem referência publicada)'
def enc(u): return quote(u, safe=":/?&=%#+~;,@!$'()*[]-._")
def snap(wb):
    return {ws.title: {c.coordinate: (('ARR', c.value.ref, c.value.text) if isinstance(c.value, ArrayFormula) else c.value)
                       for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}

wb = openpyxl.load_workbook(ENT); before = snap(wb)
w = wb['Relógios']; m = wb['Marcas']
st = [copy.copy(w.cell(1190, c)._style) for c in (1, 2, 3)]
marca = cfg['marca']
linha_marcas = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == marca]
assert len(linha_marcas) == 1, f'marca não encontrada (ou repetida) na aba Marcas: {linha_marcas}'
lm = linha_marcas[0]

# ---------- trava de profundidade (antes de gravar) ----------
fontes = cfg.get('fontes') or []
def _u(x): return x['url'].strip().lower().rstrip('/')
por_passada = {}
for f in fontes:
    por_passada.setdefault(int(f.get('passada', 1)), []).append(f)
ja_tem = any(w.cell(r, 1).value == marca for r in range(2, w.max_row + 1))
problemas = []
if cfg.get('complemento'):
    if not ja_tem: problemas.append('"complemento" só vale para marca que já tem linhas')
else:
    minimo = 25 if cfg.get('grande') else 15
    total = len({_u(f) for f in fontes})
    if total < minimo: problemas.append(f'só {total} fontes diferentes; o mínimo é {minimo}')
    if cfg.get('vermelho'):
        p1 = {_u(f) for f in por_passada.get(1, [])}
        p2 = {_u(f) for f in por_passada.get(2, [])} - p1
        if len(p2) < 10: problemas.append(f'marca vermelha: a 2ª passada tem {len(p2)} fontes novas; o mínimo é 10')
for n_p in sorted(por_passada):
    fs = por_passada[n_p]
    print(f'Passada {n_p}: {len({_u(f) for f in fs})} fontes, {sum(int(f.get("novos", 0)) for f in fs)} relógios novos')
if problemas:
    for p in problemas: print('  !! TRAVA:', p)
    print('RESULTADO: FALHOU — pesquisa incompleta, nada foi gravado'); sys.exit(1)

novas = []
for l in open(DADOS, encoding='utf-8'):
    if not l.strip(): continue
    n, c, i, e = l.rstrip('\n').split('|')
    nome = f'{n} - {c}' if c else (n + S if cfg['usa_codigos'] else n)
    novas.append([marca, nome, enc(i), None, e or None])

existentes_r = [r for r in range(2, w.max_row + 1) if w.cell(r, 1).value == marca]
nomes_exist = {w.cell(r, 2).value for r in existentes_r}
dup = [k for k, v in Counter(x[1] for x in novas).items() if v > 1] + [x[1] for x in novas if x[1] in nomes_exist]
assert not dup, f'nomes repetidos: {dup}'

if existentes_r:
    # reescreve do início do bloco até o fim, para manter a marca contígua
    inicio = existentes_r[0]
    cauda = []
    for r in range(inicio, w.max_row + 1):
        cauda.append([w.cell(r, k).value for k in (1, 2, 3, 4, 5)])
    bloco = [x for x in cauda if x[0] == marca]
    resto = [x for x in cauda if x[0] != marca]
    linhas = bloco + novas + resto
else:
    inicio = w.max_row + 1
    linhas = novas

for k, (a, b, c, d, e) in enumerate(linhas):
    rr = inicio + k
    for col, v, s in ((1, a, st[0]), (2, b, st[1]), (3, c, st[2])):
        cell = w.cell(rr, col); cell.value = v; cell._style = copy.copy(s)
    w.cell(rr, 3).hyperlink = c if c else None
    w.cell(rr, 4).value = d
    cell = w.cell(rr, 5); cell.value = e; cell._style = copy.copy(st[1])

# aba Marcas: só K (logo), L (site bloqueado) e o preenchimento vermelho de A
if cfg.get('logo'): m.cell(lm, 11).value = cfg['logo']
if cfg.get('site_bloqueado'):
    c = m.cell(lm, 12); c.value = cfg['site_bloqueado']; c._style = copy.copy(m.cell(lm, 11)._style)
if cfg.get('vermelho'):
    m.cell(lm, 1).fill = PatternFill(fill_type='solid', start_color='FFFF0000', end_color='FFFF0000')

wb.save(SAI)

# ---------- verificação ----------
wb2 = openpyxl.load_workbook(SAI); after = snap(wb2); w2 = wb2['Relógios']; m2 = wb2['Marcas']
ok = True
for t in before:
    if t == 'Relógios': continue
    mud = sorted(k for k in set(before[t]) | set(after[t]) if before[t].get(k) != after[t].get(k))
    perm = {f'K{lm}', f'L{lm}'}
    extra = [k for k in mud if k not in perm]
    print(t, 'mudanças:', mud)
    if extra: ok = False; print('  !! mudança fora do permitido:', extra)
arr = sum(1 for c in m2._cells.values() if isinstance(c.value, ArrayFormula))
print('ArrayFormula em Marcas:', arr); ok &= arr == 641
antes_ok = all(before['Relógios'].get(k) == after['Relógios'].get(k)
               for k in before['Relógios'] if int(re.sub(r'\D', '', k)) < inicio)
print('linhas anteriores intactas:', antes_ok); ok &= antes_ok
ruins = [r for r in range(inicio, w2.max_row + 1)
         if w2.cell(r, 3).value and (not w2.cell(r, 3).hyperlink or w2.cell(r, 3).hyperlink.target != w2.cell(r, 3).value)]
print('hyperlinks ruins:', ruins); ok &= not ruins
seq = [w2.cell(r, 1).value for r in range(inicio, w2.max_row + 1)]
blocos = [seq[0]] + [seq[k] for k in range(1, len(seq)) if seq[k] != seq[k - 1]]
contig = len(blocos) == len(set(blocos))
print('blocos contíguos a partir de', inicio, ':', contig); ok &= contig
print('linhas da marca agora:', sum(1 for r in range(2, w2.max_row + 1) if w2.cell(r, 1).value == marca),
      '| novas:', len(novas), '| max_row:', w2.max_row)
ph = any('7WgAAOSwQ7haxTU1' in (x[2] or '') for x in novas)
print('placeholder eBay presente:', ph); ok &= not ph
print('RESULTADO:', 'OK' if ok else 'FALHOU — não entregar')
```

## 14. Entrega e relatório (pt-BR, calmo, para leigo; o usuário lê no celular)
- Enviar a nova planilha com SendUserFile (legenda curta: marca, nº de relógios, linhas). Em execução agendada, mandar o relatório também com SendUserMessage.
- Relatório por marca: nº de relógios e linhas; coleções; se usa códigos; logo; o que veio do site oficial (loja, blog, imprensa, produtos escondidos), da Chrono24/EveryWatch e da primeira página de busca; **quantas fontes foram abertas** e quais trouxeram modelos; as linhas "Passada N: X fontes, Y relógios novos" que o script imprime (obrigatório em marca vermelha); registro na coluna L; o que ficou de fora e por quê; dados da aba Marcas que parecem errados.
- Sinalizar inferências. Terminar com "Fontes:" em links markdown.
- Atualizar `estado.json` e, se a planilha estiver num repositório, fazer commit com a nova versão.