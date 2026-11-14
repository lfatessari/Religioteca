# Relogioteca — instruções para cada execução automática

Este repositório guarda a planilha da Relogioteca e o estado do trabalho. Cada execução agendada começa numa conversa nova e vazia: tudo o que é preciso está aqui.

## FASE ATUAL (ler antes de tudo) — pedido do usuário, 14/11/2026
O campo `"fase"` do `estado.json` decide o que a execução faz:
- `"marcas"`: NÃO pesquisar relógios. Preencher SÓ as células vazias da aba Marcas (B, C, D, E, F, G, H, I, J, K), de cima para baixo, **40 marcas por execução** (seção "Fase Marcas" no fim deste arquivo). Marca com tudo preenchido é PULADA; História (I) já escrita NÃO é conferida nem reescrita (correção do usuário, 14/11/2026: a v577 conferiu histórias prontas por engano). A skill `relogioteca-pesquisa-exaustiva` não é usada nesta fase.
- `"relogios"` (ou campo ausente): roteiro normal da aba Relógios, descrito abaixo.
Quando a fase Marcas acabar, a própria execução muda para `"relogios"` e as seguintes voltam às baterias a partir de `proxima_linha_marcas`.

## Arquivos
- `planilha/Relogios_atualizada_NN.xlsx` — a versão atual (só a de maior número fica no repositório; as anteriores ficam no histórico do git).
- `estado.json` — `proxima_linha_marcas` (próxima linha da aba Marcas), `ultima_versao`, `historico` e `marcas_ja_feitas_fora_da_ordem` (marcas que já têm linhas e devem ser PULADAS quando a sequência chegar nelas).
- `gravar_marca.py` — script padrão de gravação, com a trava de profundidade. Nunca contornar a trava.
- `historico/` — notas, dados e marca.json de cada marca já feita.
- `docs/SKILL_relogioteca-pesquisa-exaustiva.md` — cópia de referência do roteiro. A versão que vale é a skill `relogioteca-pesquisa-exaustiva` da conta.
- `site/` e `.github/workflows/site.yml` — o site público (GitHub Pages). Ele se atualiza sozinho a cada planilha nova enviada para `planilha/`, e as fotos ficam no ramo `fotos`. As execuções de pesquisa não mexem nesses arquivos nem no ramo `fotos`.

## Trava contra execuções simultâneas (com sinal de vida)
Uma execução pode ser cortada a qualquer momento pelo limite de uso, sem chance de salvar nada no fim. Por isso o progresso é salvo DURANTE o trabalho, e a trava mostra se a execução ainda está viva.
- No início: `git pull`, ler `estado.json`. O horário que vale é `"ultimo_sinal"` (ou, se não existir, `"em_execucao"`).
  - Menos de **40 minutos** atrás: outra execução está viva. Parar sem fazer nada (só uma linha no relatório).
  - Mais de 40 minutos: a anterior morreu (provavelmente pelo limite de uso). Seguir; se houver `em_andamento`, **retomar** (ver "Retomar").
- Antes de pesquisar: gravar `"em_execucao"` e `"ultimo_sinal"` com a data e hora ISO (UTC) no `estado.json`, e já gravar `"em_andamento"` (ver abaixo) para a(s) marca(s) escolhida(s). Commit "Início de bateria" e push.
- A cada salvamento parcial (abaixo), atualizar `"ultimo_sinal"` no mesmo commit.
- No fim (com sucesso): remover `em_execucao`, `ultimo_sinal` e `em_andamento` no mesmo commit do resultado.

## Salvamento parcial obrigatório (a cada 10–15 fontes)
- Durante a pesquisa, manter em `/home/claude/trabalho/` dois arquivos por marca, sempre atualizados:
  - `parcial_<marca>_relogios.txt` — uma linha por relógio já achado, no formato do `dados` (`Nome|CÓDIGO|URL_imagem|Características`);
  - `parcial_<marca>_fontes.txt` — uma linha por fonte já aberta: `passada|url|novos`;
  - e as notas `notas_<marca>.md` (seções já feitas, o que falta, buracos, decisões).
- **A cada 10 a 15 fontes abertas OU a cada 20 minutos, o que vier primeiro** (e sempre ao terminar uma seção da skill): copiar esses arquivos para `historico/`, atualizar `ultimo_sinal` e o `em_andamento` no `estado.json`, commit "Parcial: <marca> (N fontes, M relógios)" e push. Não esperar o fim para salvar. Mesmo sem nenhuma novidade (páginas lentas, buscas sem resultado), fazer o salvamento ao completar 20 minutos, só para atualizar `ultimo_sinal`: uma execução viva nunca pode ficar 40 minutos sem dar sinal, senão a seguinte a considera morta e as duas trabalham ao mesmo tempo. Conferir a hora com `date -u` antes de cada pesquisa nova.
- `em_andamento` fica assim: `{"marcas": ["<marca>"], "linha_marcas": N, "grande": true|false, "relogios": "historico/parcial_<marca>_relogios.txt", "fontes": "historico/parcial_<marca>_fontes.txt", "notas": "historico/notas_<marca>.md", "secoes_feitas": ["1","2","2c",...], "passada": 1}`.

## Retomar
- Se `estado.json` tiver `em_andamento` (e o sinal de vida tiver mais de 40 minutos): NÃO começar a marca do zero nem escolher outra. Copiar os arquivos parciais de `historico/` para `/home/claude/trabalho/`, ler as notas, e continuar das seções que faltam.
- Não reabrir as fontes já listadas em `parcial_<marca>_fontes.txt` (elas já contam para o mínimo e para o critério de parada). Os relógios já anotados entram como estão; só acrescentar novos.
- Se o usuário colar na conversa uma lista de modelos levantados por outra execução, tratá-la como progresso salvo: comparar com o que já há, buscar o que faltar e seguir.

## Abrir sites sem pedir permissão (ninguém está olhando)
(As regras desta seção valem para a WebFetch. Quando um endereço não puder ser aberto por ela, usar o Firecrawl — ver a seção "Firecrawl" abaixo.)
O WebFetch só abre sem pedir aprovação ao usuário endereços que já apareceram nesta conversa: resultados de WebSearch ou links devolvidos por uma página já aberta. Endereço digitado de memória (ex.: thewatchpages.com, everywatch.com/<marca>, o site da coluna G) trava a execução esperando um clique que ninguém vai dar.
- Antes de abrir qualquer site, fazer uma WebSearch que traga o endereço e abrir exatamente o endereço do resultado.
- **Só abrir endereços que vieram literalmente de um resultado de WebSearch.** Links tirados do resumo de uma página aberta (paginação, fichas de produto, páginas de relógio) também pediram permissão (Armin Strom, out/2026). Exemplos que pediram: páginas `monochrome-watches.com/category/<marca>/page/N/` e fichas `europastar.com/swisstime/...` tiradas de outra página. Para uma página interna, fazer antes uma busca que a traga (ex.: `site:monochrome-watches.com <marca> <modelo>`, `site:europastar.com <marca> <modelo>`) e abrir o link do resultado.
- **Páginas 2, 3, 4… não ficam de fora; só mudam de caminho.** Os buscadores costumam indexar as páginas paginadas. Na Armin Strom, `ablogtowatch.com/watch-brands/armin-strom/page/4/` e `page/2` vieram direto da busca. Para cada lista paginada, fazer buscas como `site:monochrome-watches.com/category/<marca>/page`, `"<marca>" site:<dominio> page 3` ou `<marca> <dominio> page 5`, e abrir as que aparecerem. Para as que não aparecerem, buscar os modelos um a um (`site:<dominio> <marca> <modelo/ano>`) e somar fontes paralelas (outras revistas, lojas e bancos de dados). Registrar no relatório quais páginas não foram alcançadas.
- Esta regra vale acima do que a skill disser: os truques de endereço da skill (paginação `?page=N`, `/page/N/`, `products.json`, `wp-json`, `.oembed`, `sitemap`, páginas de família/ficha do WatchBase e do EveryWatch) só podem ser usados se o endereço exato apareceu num resultado de busca.
- **Nunca montar endereços**, nem no mesmo domínio de uma página já aberta: `/products.json`, `/wp-json/...`, `sitemap.xml`, `.oembed`, `?page=N`, `?limit=…` pedem aprovação mesmo assim (visto na Armin Strom, out/2026). Os truques de endereço da skill (§2, §5, §7) só valem quando o endereço exato apareceu numa busca ou num link devolvido; senão, usar a página normal e buscas `site:`.
- Se o WebFetch responder PROVENANCE_REQUIRED ou pedir permissão: não repetir esse endereço; seguir com outra fonte.
- **Não usar a ferramenta Agent (ajudantes/subagentes)**: criar ajudantes também pede aprovação. Fazer toda a pesquisa na própria execução.
- Site que não aparece em busca nenhuma: tentar com o Firecrawl (abaixo); se nem assim abrir, pular e registrar no relatório.

## Firecrawl (conector) — complemento, não substituto (pedido do usuário, out/2026)
Na BWC-Swiss o Firecrawl abriu as páginas 5, 6, 8 e 9 da loja oficial (que a WebFetch não alcançava), trouxe as fotos de uma loja WooCommerce cujas fotos não apareciam na leitura normal e abriu a Chrono24.de com 27 modelos novos. Custa créditos (~5 por página), então:
- **Continuar usando WebSearch + WebFetch como base** (buscas e a maioria das páginas).
- **Usar `mcp__Firecrawl__firecrawl_scrape` (carregar com ToolSearch "firecrawl") nestes casos:**
  1. páginas 2, 3, 4… de lojas, catálogos e listas que não vieram em nenhum resultado de busca (o Firecrawl abre qualquer endereço sem pedir aprovação, inclusive `/shop/page/N/`, `?page=N`, `index-2.htm`);
  2. site que a WebFetch não abre (client_error, 403, robots, PROVENANCE_REQUIRED, redirecionamento em loop) — inclusive o site oficial e a Chrono24.de (`chrono24.de/<marca>/index.htm`, `index-2.htm`…);
  3. lojas cujas fotos não aparecem na leitura normal (carregamento tardio);
  4. quando a WebFetch atingir o limite semanal/diário: seguir a pesquisa só com o Firecrawl (`firecrawl_search` para buscar e `firecrawl_scrape` para abrir) em vez de parar.
- Pedir saída em JSON (`formats: ["json"]` com `jsonOptions.prompt` + `schema`: título, referência, URL, imagem). Para conferir fotos, `formats: ["images"]` ou o `og:image` do anúncio.
- **Fotos devolvidas pelo extrator só valem se seguirem o padrão real do site** (ex.: `bwc-swiss.de/wp-content/uploads/2020/12/<ref sem pontos>.jpg`, confirmado em outra página). Na Chrono24 o extrator inventou endereços (o formato real tem hash: `img.chrono24.com/images/uhren/<id>-<hash>-ExtraLarge.jpg`); nesses casos usar o link do anúncio na coluna C. Na dúvida, abrir um anúncio e conferir o `og:image` antes de usar o padrão.
- **Não usar `proxy: "auto"`, `"stealth"` ou `"enhanced"`**: o controle de segurança da sessão recusou (chrono24.com, out/2026). Usar o padrão; se o site recusar, registrar e seguir.
- Toda página aberta pelo Firecrawl entra no campo `fontes` do `marca_<marca>.json` como qualquer outra fonte, e conta para o mínimo e para o critério de parada.
- No relatório, dizer quais fontes vieram pelo Firecrawl e quantos créditos foram usados (o resultado de cada chamada mostra `creditsUsed`).

## Roteiro de cada execução
1. Carregar a skill `relogioteca-pesquisa-exaustiva` (ferramenta Skill) e seguir o SKILL.md inteiro, como se fosse a primeira vez.
2. Ler `estado.json`. Se houver `em_andamento`, retomar essa bateria pelos arquivos parciais em `historico/` (ver "Retomar") em vez de começar outra.
3. Trabalhar numa cópia: `mkdir -p /home/claude/trabalho && cp planilha/*.xlsx gravar_marca.py estado.json /home/claude/trabalho/`. Arquivos de cada marca (`notas_<marca>.md`, `dados_<marca>.txt`, `marca_<marca>.json`) também nessa pasta.
4. **Primeiro as marcas novas:** se `estado.json` tiver `marcas_novas_sem_relogios` com algum item, escolher a(s) marca(s) DESSA lista, na ordem em que aparecem (ver "Marcas novas fora da sequência" abaixo), em vez de seguir `proxima_linha_marcas` (esta prioridade vale acima do que a skill disser sobre "seguir a ordem da aba Marcas"). Só quando essa lista estiver vazia (ou não existir), escolher as marcas pela ordem da aba Marcas a partir de `proxima_linha_marcas`, pulando as de `marcas_ja_feitas_fora_da_ordem`. **Até 3 marcas por execução, se forem pequenas; marca grande sempre sozinha.** Se a próxima for grande, só ela; senão, as próximas não grandes em sequência até completar 3, parando antes da primeira grande. Esta regra vale mesmo se a cópia da skill da conta ainda disser "duas". Com mais de uma marca, rodar o `gravar_marca.py` uma vez por marca, em sequência, e entregar só a versão final.
5. Pesquisar e gravar conforme a skill, fazendo o salvamento parcial a cada 10–15 fontes. Só entregar se o script terminar com `RESULTADO: OK`.
6. Atualizar `estado.json` (próxima linha, versão, histórico).
7. Salvar no repositório:
   - PRIMEIRO copiar a nova: `mkdir -p planilha && cp /home/claude/trabalho/Relogios_atualizada_<nova>.xlsx planilha/`; SÓ DEPOIS `git rm -q planilha/Relogios_atualizada_<antiga>.xlsx`. (Se o `git rm` vier antes, ele apaga a pasta `planilha/`, a cópia falha e o resto da cadeia `&&` não roda — foi o que derrubou a Artime em out/2026.) Rodar cada passo como comando separado, não numa cadeia `&&` longa;
   - conferir com `ls planilha/` que só a nova está lá;
   - copiar `estado.json` e os arquivos da marca para `historico/`;
   - `git add -A && git commit -m "Bateria: <marca(s)> (vNN)"` e `git push origin main`.
   - Se o push falhar: `git fetch origin main && git rebase origin/main` e tentar uma vez mais. Se ainda falhar, avisar no relatório.
8. Relatório em português do Brasil, calmo e para leigo (o usuário lê no celular): o que entrou, linhas por passada (fontes e relógios novos), por que parou, dados da aba Marcas ("Corrigido na aba Marcas" — o que teve certeza e foi corrigido — separado de "Só anotado em M"; ver "Correções com certeza" abaixo), e a lista "Fontes:". Enviar o relatório com SendUserMessage e a planilha nova com SendUserFile.

## Marcas novas fora da sequência (pedido do usuário, nov/2026)
Em 03/11/2026 (v409) entraram 18 marcas novas na aba Marcas, achadas no Instagram seguido pela @relogioteca (letras A e B). Elas ficaram ANTES de `proxima_linha_marcas`, então a sequência normal nunca chegaria nelas. Por isso:
- Enquanto `marcas_novas_sem_relogios` tiver itens, cada execução pega as marcas dessa lista (mesma regra: até 3 pequenas, ou 1 grande sozinha), na ordem da lista. Achar a linha pelo NOME na coluna A (o número `linha_marcas` da lista é só referência; o `gravar_marca.py` também acha pelo nome).
- Pesquisar e gravar exatamente como qualquer outra marca (skill, mínimo de fontes, salvamento parcial, `em_andamento`).
- Ao gravar com sucesso, TIRAR a marca de `marcas_novas_sem_relogios` e registrá-la no `historico` com `"fora_da_sequencia": true`.
- **NÃO mexer em `proxima_linha_marcas`** por causa dessas marcas: ele continua apontando para onde a sequência normal parou (Esprit). Também não é preciso pôr essas marcas em `marcas_ja_feitas_fora_da_ordem`, porque ficam antes do ponteiro.
- A Baume (linha da sub-marca encerrada da Baume & Mercier) segue a mesma regra; registrar em M o que for encontrado.
- Se aparecerem novas marcas inseridas no meio da aba Marcas no futuro, quem inserir deve somar o deslocamento em `proxima_linha_marcas`, `marcas_pendentes`, `em_andamento`, `marcas_ja_feitas_fora_da_ordem` e nos textos de `avisos`, e pôr as marcas nesta lista.

## Se a execução for interrompida
O corte pelo limite de uso é súbito: não dá para contar com um salvamento final. O que protege o trabalho é o salvamento parcial a cada 10–15 fontes (acima). Se a execução perceber que está perto do fim (WebFetch avisando limite, contexto cheio), fazer na hora um salvamento parcial extra e avisar no relatório. A execução seguinte retoma do último salvamento, perdendo no máximo as fontes abertas depois dele.

## Nunca
- Nunca apagar o histórico do git nem forçar push (`--force`).
- Nunca alterar na aba Marcas a coluna A (nome; liga com a aba Relógios) nem E/F (faixa e preço médio). B, C, D, G, H, I e J só se corrigem quando houver certeza (ver "Correções com certeza" abaixo); K, L, M e o vermelho de A como sempre.

## Coluna M da aba Marcas (Observações) — pedido do usuário, out/2026
- Tudo o que for notado na aba Marcas e não puder ser corrigido por falta de certeza, e também o que foi corrigido (ver seção abaixo), (B/C/G/H vazios ou errados, D/I/J genéricos ou errados, data de fundação divergente, site da coluna G errado, nome em J não encontrado, "[⚠️ verificar]" etc.) vai TAMBÉM na coluna M da linha da marca, em português, curto, com o dado certo quando se souber (ex.: "G vazio: site arlanch.se").
- Como gravar: campo `"observacoes"` no `marca_<marca>.json`; o `gravar_marca.py` escreve em M (cabeçalho M1 "Observações") e a verificação aceita só K, L, M daquela linha (mais as células do campo `correcoes`).
- Se não houver nada a observar, deixar `"observacoes"` vazio. Não apagar o que já estiver em M de outra marca.

## Correções com certeza na aba Marcas — pedido do usuário (07/11/2026)
"Quando você encontrar coisas que tem certeza, pode corrigir, não precisa me perguntar." Esta regra vale acima do que a skill disser ("só relatar, não corrigir").
- **Certeza** = o dado certo aparece no site oficial ou no Instagram oficial da marca, ou em 2 fontes independentes e confiáveis (imprensa relojoeira, Wikipedia com fonte, registro da empresa), e a pesquisa da própria execução abriu essas fontes. Erros evidentes do próprio texto (palavra repetida, nome de modelo com erro de digitação, site que é de outra empresa) também contam.
- **Pode corrigir:** B (país), C (cidade), D (característica), G (site), H (Instagram), I (história), J (principais relógios). **Nunca:** A (nome), E/F (faixa/preço), nem nada fora da linha da marca da bateria.
- **Como:** campo `"correcoes": {"G": "valor novo", "I": "texto inteiro novo", ...}` no `marca_<marca>.json`; o `gravar_marca.py` aplica e a verificação aceita só essas células, mais K, L, M. Para corrigir sem gravar relógios, usar `corrigir_marca.py ENTRADA.xlsx SAIDA.xlsx correcao.json` (mesmo formato, com `"marca"`), que confere que só essas células mudaram.
- Em I, mudar só o trecho errado ou acrescentar o fato confirmado, mantendo o resto do texto. "[⚠️ verificar]" só sai quando tudo o que o texto afirma foi conferido.
- **Sempre registrar em M** o que foi corrigido (valor antigo → novo, curto) e, à parte, o que ficou sem certeza ("Ainda a verificar: …"). No relatório, listar "Corrigido na aba Marcas" separado de "Só anotado".
- Sem certeza: continua só em M, como antes.

## Fase Marcas — preencher SÓ o que está vazio na aba Marcas (pedido do usuário, 14/11/2026; regra corrigida no mesmo dia)
Objetivo: deixar a aba Marcas completa nas colunas B, C, D, E, F, G, H, I, J e K. **Só se pesquisa o que está vazio.** Marca com tudo preenchido é PULADA. A História (coluna I) entra só quando está vazia: história já escrita NÃO é conferida, corrigida nem reescrita (o usuário não pediu isso; a v577 conferiu 40 histórias prontas por engano). **Lote de 40 marcas por execução** (8 ajudantes × 5 marcas). Não mexer na aba Relógios nesta fase. A trava contra execuções simultâneas vale igual (`em_execucao`/`ultimo_sinal`, commit "Início de lacunas" e push antes de pesquisar; atualizar `ultimo_sinal` com commit+push ao receber os resultados dos ajudantes e antes de gravar).
- Arquivos: `lacunas/fila.py` (escolhe o lote), `lacunas/aplicar.py` (grava e confere), `lacunas/regras.md` (regras dos ajudantes), `historico/lacunas_marcas/` (um `lote_NNN.json` por versão).
- **Planilha:** a aba Marcas tem uma célula solta ";" na coluna XFD. Nunca percorrer até `max_column`, nunca usar `ws.delete_rows`; ler com `read_only=True` e `max_col=13`.
- **Escolha do lote:** rodar `python3 lacunas/fila.py planilha/Relogios_atualizada_<atual>.xlsx 40 /home/claude/trab`. Ele grava `grupo1.json` … `grupo8.json` (5 marcas cada: `marca`, `falta` = só as colunas vazias, `atual`) e diz quantas marcas restam. Regra do script: pula marca já tratada nesta fase (M com "istória revisada" ou "istória preenchidas"); nas marcas com "Lacunas revisadas"/"preenchimento a pedido" em M (rodadas antigas) só entra a I, e só se estiver vazia; nas demais entram as colunas vazias entre B e K; marca sem nada vazio fica de fora. Não montar a fila à mão.
- **Pesquisa com ajudantes (nesta fase a ferramenta Agent PODE ser usada; a proibição acima vale só para a fase Relógios):** testar o Firecrawl uma vez; depois lançar, numa só mensagem, um ajudante (`general-purpose`) por grupo: "Você vai pesquisar SÓ as células vazias (campo "falta") de 5 marcas de relógio para uma planilha. Leia primeiro as regras em <repo>/lacunas/regras.md (siga-as à risca) e os dados em /home/claude/trab/grupoN.json. Não pesquise nem altere colunas que não estejam em "falta". Firecrawl: <com | sem créditos>. Grave o resultado em /home/claude/trab/resN.json. Ninguém está olhando: não faça perguntas. Grave o arquivo parcial a cada 2 marcas." Se a ferramenta Agent não existir ou pedir aprovação, pesquisar na própria execução, quantas marcas couberem (mínimo 10), e gravar essas.
- **Abrir sites sem pedir permissão (vale também para os ajudantes):** o WebFetch só abre sem aprovação endereços que vieram literalmente de um resultado de WebSearch; nada de endereço de memória, da coluna G ou montado. Buscar primeiro e abrir o link do resultado; o que não aparecer em busca vai pelo Firecrawl; se pedir permissão, não repetir e seguir com outra fonte. Repetir esta regra no pedido de cada ajudante.
- **Revisão antes de gravar:** todas as marcas presentes e com "M"; só colunas que estavam em `falta` (mais M) — descartar qualquer outra; E e F inteiros; descartar (explicando em M como "a confirmar") o que o ajudante diz não ter confirmado ou que pode ser de marca homônima. Possível erro em célula já preenchida: só anotar em M, não alterar. **História nova (I vazia):** todo fato (ano, fundador, cidade, dono, marcos) tem de ter fonte citada em M; fato sem fonte sai; fato de 1 fonte só → texto termina com "[⚠️ a confirmar: …]"; marca pouco documentada fica com 2 ou 3 frases; conferir que bate com B, C e D. Grupo que falhar: um novo ajudante, uma vez; se falhar de novo, fica para a próxima execução.
- **Gravação:** `lote_NNN.json` = `{"versao": NNN, "data": "AAAA-MM-DD", "tipo": "lacunas_marcas", "prefixo": "Lacunas e história preenchidas", "marcas": [...], "celulas": {marca: {col: valor, "M": "texto"}}, "base": "Relogios_atualizada_<anterior>.xlsx"}` (NNN = ultima_versao + 1; o aplicar.py acrescenta "Lacunas e história preenchidas em DD/MM/AAAA: " ao M — é esse texto que tira a marca da fila, por isso TODA marca do lote recebe M, mesmo sem nada achado). Rodar `python3 lacunas/aplicar.py planilha/Relogios_atualizada_<anterior>.xlsx /home/claude/trab/Relogios_atualizada_NNN.xlsx /home/claude/trab/lote_NNN.json` com tempo limite de 600000 ms; só vale com `RESULTADO: OK`.
- **Salvar:** copiar a planilha nova para `planilha/` e só depois `git rm` da antiga; lote em `historico/lacunas_marcas/`; `estado.json` (ultima_versao, historico, `lacunas_marcas.ultima_marca_revisada`, sem em_execucao/ultimo_sinal); commit "Marcas: <primeira> a <última> (vNNN)" e `git push origin main` (nunca --force). Se o push for recusado (403): entregar a planilha com SendUserFile, avisar no relatório e na notificação que o GitHub não gravou, e não tentar de novo.
- **Relatório curto** (SendUserMessage, pt-BR, para leigo): versão, quantas marcas e intervalo, quantos logos/sites/Instagrams/cidades/países/preços/características/principais relógios entraram, quantas histórias novas (e quantas com "a confirmar"), o que não foi achado, pontos a conferir anotados em M, quantas marcas ainda restam na fila (número dado pelo `fila.py`), se gravou no GitHub, se o Firecrawl tinha créditos. Não listar as 40. Enviar a planilha (SendUserFile) e a notificação "Marcas: <primeira> a <última> (vNNN)".
- **Fim da fase:** quando o `fila.py` disser 0 marcas na fila, gravar `"fase": "relogios"` no `estado.json` no mesmo commit, listar no relatório as lacunas sem solução e avisar que a próxima execução volta à aba Relógios (linha `proxima_linha_marcas`, achando sempre a marca pelo NOME).
- Lições: fazer as contas de preço em Python; câmbio fixo em `lacunas/regras.md`; o Microbrand Atlas deu erro em todas as tentativas em 13/11; muitas marcas antigas têm E=2 e F genérico que não bate com os preços reais (só anotar em M).
