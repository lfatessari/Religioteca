# Relogioteca — instruções para cada execução automática

Este repositório guarda a planilha da Relogioteca e o estado do trabalho. Cada execução agendada começa numa conversa nova e vazia: tudo o que é preciso está aqui.

## Arquivos
- `planilha/Relogios_atualizada_NN.xlsx` — a versão atual (só a de maior número fica no repositório; as anteriores ficam no histórico do git).
- `estado.json` — `proxima_linha_marcas` (próxima linha da aba Marcas), `ultima_versao`, `historico` e `marcas_ja_feitas_fora_da_ordem` (marcas que já têm linhas e devem ser PULADAS quando a sequência chegar nelas).
- `gravar_marca.py` — script padrão de gravação, com a trava de profundidade. Nunca contornar a trava.
- `historico/` — notas, dados e marca.json de cada marca já feita.
- `docs/SKILL_relogioteca-pesquisa-exaustiva.md` — cópia de referência do roteiro. A versão que vale é a skill `relogioteca-pesquisa-exaustiva` da conta.

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
O WebFetch só abre sem pedir aprovação ao usuário endereços que já apareceram nesta conversa: resultados de WebSearch ou links devolvidos por uma página já aberta. Endereço digitado de memória (ex.: thewatchpages.com, everywatch.com/<marca>, o site da coluna G) trava a execução esperando um clique que ninguém vai dar.
- Antes de abrir qualquer site, fazer uma WebSearch que traga o endereço e abrir exatamente o endereço do resultado.
- **Só abrir endereços que vieram literalmente de um resultado de WebSearch.** Links tirados do resumo de uma página aberta (paginação, fichas de produto, páginas de relógio) também pediram permissão (Armin Strom, out/2026). Exemplos que pediram: páginas `monochrome-watches.com/category/<marca>/page/N/` e fichas `europastar.com/swisstime/...` tiradas de outra página. Para uma página interna, fazer antes uma busca que a traga (ex.: `site:monochrome-watches.com <marca> <modelo>`, `site:europastar.com <marca> <modelo>`) e abrir o link do resultado.
- **Páginas 2, 3, 4… não ficam de fora; só mudam de caminho.** Os buscadores costumam indexar as páginas paginadas. Na Armin Strom, `ablogtowatch.com/watch-brands/armin-strom/page/4/` e `page/2` vieram direto da busca. Para cada lista paginada, fazer buscas como `site:monochrome-watches.com/category/<marca>/page`, `"<marca>" site:<dominio> page 3` ou `<marca> <dominio> page 5`, e abrir as que aparecerem. Para as que não aparecerem, buscar os modelos um a um (`site:<dominio> <marca> <modelo/ano>`) e somar fontes paralelas (outras revistas, lojas e bancos de dados). Registrar no relatório quais páginas não foram alcançadas.
- Esta regra vale acima do que a skill disser: os truques de endereço da skill (paginação `?page=N`, `/page/N/`, `products.json`, `wp-json`, `.oembed`, `sitemap`, páginas de família/ficha do WatchBase e do EveryWatch) só podem ser usados se o endereço exato apareceu num resultado de busca.
- **Nunca montar endereços**, nem no mesmo domínio de uma página já aberta: `/products.json`, `/wp-json/...`, `sitemap.xml`, `.oembed`, `?page=N`, `?limit=…` pedem aprovação mesmo assim (visto na Armin Strom, out/2026). Os truques de endereço da skill (§2, §5, §7) só valem quando o endereço exato apareceu numa busca ou num link devolvido; senão, usar a página normal e buscas `site:`.
- Se o WebFetch responder PROVENANCE_REQUIRED ou pedir permissão: não repetir esse endereço; seguir com outra fonte.
- **Não usar a ferramenta Agent (ajudantes/subagentes)**: criar ajudantes também pede aprovação. Fazer toda a pesquisa na própria execução.
- Site que não aparece em busca nenhuma: pular e registrar no relatório.

## Roteiro de cada execução
1. Carregar a skill `relogioteca-pesquisa-exaustiva` (ferramenta Skill) e seguir o SKILL.md inteiro, como se fosse a primeira vez.
2. Ler `estado.json`. Se houver `em_andamento`, retomar essa bateria pelos arquivos parciais em `historico/` (ver "Retomar") em vez de começar outra.
3. Trabalhar numa cópia: `mkdir -p /home/claude/trabalho && cp planilha/*.xlsx gravar_marca.py estado.json /home/claude/trabalho/`. Arquivos de cada marca (`notas_<marca>.md`, `dados_<marca>.txt`, `marca_<marca>.json`) também nessa pasta.
4. Escolher as marcas pela ordem da aba Marcas a partir de `proxima_linha_marcas`, pulando as de `marcas_ja_feitas_fora_da_ordem`. **Até 3 marcas por execução, se forem pequenas; marca grande sempre sozinha.** Se a próxima for grande, só ela; senão, as próximas não grandes em sequência até completar 3, parando antes da primeira grande. Esta regra vale mesmo se a cópia da skill da conta ainda disser "duas". Com mais de uma marca, rodar o `gravar_marca.py` uma vez por marca, em sequência, e entregar só a versão final.
5. Pesquisar e gravar conforme a skill, fazendo o salvamento parcial a cada 10–15 fontes. Só entregar se o script terminar com `RESULTADO: OK`.
6. Atualizar `estado.json` (próxima linha, versão, histórico).
7. Salvar no repositório:
   - `git rm planilha/Relogios_atualizada_<antiga>.xlsx`, copiar a nova para `planilha/`;
   - copiar `estado.json` e os arquivos da marca para `historico/`;
   - `git add -A && git commit -m "Bateria: <marca(s)> (vNN)"` e `git push origin main`.
   - Se o push falhar: `git fetch origin main && git rebase origin/main` e tentar uma vez mais. Se ainda falhar, avisar no relatório.
8. Relatório em português do Brasil, calmo e para leigo (o usuário lê no celular): o que entrou, linhas por passada (fontes e relógios novos), por que parou, dados errados na aba Marcas (só relatar), e a lista "Fontes:". Enviar o relatório com SendUserMessage e a planilha nova com SendUserFile.

## Se a execução for interrompida
O corte pelo limite de uso é súbito: não dá para contar com um salvamento final. O que protege o trabalho é o salvamento parcial a cada 10–15 fontes (acima). Se a execução perceber que está perto do fim (WebFetch avisando limite, contexto cheio), fazer na hora um salvamento parcial extra e avisar no relatório. A execução seguinte retoma do último salvamento, perdendo no máximo as fontes abertas depois dele.

## Nunca
- Nunca apagar o histórico do git nem forçar push (`--force`).
- Nunca alterar na aba Marcas nada além de K (logo), L (site bloqueado) e o vermelho da coluna A, salvo pedido do usuário com "corrija".
