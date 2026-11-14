# Regras para preencher lacunas de marcas de relógio (planilha Relogioteca)

Colunas: B País | C Cidade | D Principal característica (frase curta, factual, em português) | E Faixa de preço (1–10) | F Preço médio em R$ (inteiro) | G Site (domínio sem https://, ex.: "apose.fr") | H Instagram ("@conta") | J Principais relógios (em português; formato "Modelo — descrição curta; preço", modelos separados por linha em branco "\n\n") | K Logo (URL direta da imagem do logo do cabeçalho do site oficial) | M Observação (fontes e explicações, em português do Brasil).

- Pesquise SÓ as colunas listadas em "falta". O que já está preenchido fica (só corrija se tiver CERTEZA de erro, explicando em M).
- NUNCA invente. O que não achar fica fora do JSON e é explicado em M ("X não achado: motivo"). Use "-" só se confirmado que não existe (ex.: marca sem Instagram).
- NUNCA escreva a coluna I (História).
- Países como na planilha: "USA", "Reino Unido", "Holanda", "Singapura", "Suíça", "Alemanha", "França", "Hong Kong", "China", "Japão", "Itália", "Espanha", "Canadá", "Austrália", "Bélgica" etc. Cidades em português quando houver forma usual (Genebra, Filadélfia, Tóquio, Londres, Berlim).
- Ferramentas: WebSearch e WebFetch (carregue com ToolSearch "select:WebSearch,WebFetch"). Firecrawl (ToolSearch "firecrawl"): a execução principal diz no pedido se ele tem créditos; se tiver, firecrawl_scrape no site com formats ["branding","links"] dá logo e redes de uma vez; se responder "Insufficient credits", não insista. Não use curl/python para baixar páginas; se WebFetch for bloqueado, aceite e anote.
- Ordem sugerida: (1) WebFetch em https://microbrandatlas.com/brand/<slug> pedindo "Compact: SITE; CITY, COUNTRY; YEAR; FOUNDER; INSTAGRAM; MODELS with price" (resolve várias colunas); (2) WebFetch no site oficial (coluna G) pedindo URL exata da imagem do logo do cabeçalho, link do Instagram, endereço/cidade e preços; (3) WebSearch ("<marca> watch", "site:instagram.com <marca> watch", imprensa: Worn & Wound, Monochrome, Hodinkee, aBlogtoWatch, Time+Tide).
- Seja econômico: 2 a 4 chamadas por marca, máximo 6. Faça buscas de marcas diferentes em paralelo.
- F: média dos preços dos relógios à venda (loja Shopify: WebFetch em <site>/products.json pedindo a lista de título e preço de cada produto; exclua pulseiras/acessórios). FAÇA A CONTA EM PYTHON (Bash) e mostre-a em M. Câmbio fixo: US$ 5,5146; € 6,2257; £ 7,451; CHF 6,5; CAD 3,9018; SEK 0,5610; JPY 0,0349; HKD 0,7189. Outra moeda: buscar cotação e citar fonte/data em M. Marca extinta: preço de lançamento na imprensa.
- E: se já existe, NÃO mude (se F não couber na faixa, só anote em M). Se E estiver vazio, pela tabela de F: 1 até 1.000; 2 1.001–5.000; 3 5.001–10.000; 4 10.001–20.000; 5 20.001–40.000; 6 40.001–70.000; 7 70.001–100.000; 8 100.001–350.000; 9 350.001–600.000; 10 acima de 600.000.
- K: só URL de arquivo de imagem real do logo (png/svg/webp/jpg). Se o cabeçalho usa só texto, deixe vazio e anote "K não preenchido: cabeçalho usa o nome em texto".
- H: prefira o perfil que o site oficial liga; conta do fundador só se a marca não tiver (anote em M).
- D e J: só se vazios; curtos e factuais.
- Atenção a marcas homônimas (ex.: outra "Apex"): confirme que a fonte é sobre a marca de relógios certa (bate com Instagram/site já na planilha).

SAÍDA: grave o arquivo JSON indicado, no formato
{"<Marca exatamente como dada>": {"C": "...", "K": "...", "M": "C: Genebra (fonte...). K: logo do cabeçalho do site oficial ..."}, ...}
TODA marca do grupo tem de aparecer com "M" (mesmo que seja "Nada novo achado: ..."). E e F como números inteiros (não string). Texto de M no estilo: "H e K: do site oficial x.com (logo do cabeçalho). F: média de N relógios ... = US$ X × 5,5146 = R$ Y → E = 2. C não achado: ...". Não comece M com "Lacunas revisadas" (isso é acrescentado depois).
Valide o JSON com python3 -c "import json;json.load(open('ARQ'))". Ao final, responda só com um resumo de 1 linha por marca (o que foi preenchido).
