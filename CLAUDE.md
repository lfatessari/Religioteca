# Relogioteca — instruções para cada execução automática

Este repositório guarda a planilha da Relogioteca e o estado do trabalho. Cada execução agendada começa numa conversa nova e vazia: tudo o que é preciso está aqui.

## Arquivos
- `planilha/Relogios_atualizada_NN.xlsx` — a versão atual (só a de maior número fica no repositório; as anteriores ficam no histórico do git).
- `estado.json` — `proxima_linha_marcas` (próxima linha da aba Marcas), `ultima_versao`, `historico` e `marcas_ja_feitas_fora_da_ordem` (marcas que já têm linhas e devem ser PULADAS quando a sequência chegar nelas).
- `gravar_marca.py` — script padrão de gravação, com a trava de profundidade. Nunca contornar a trava.
- `historico/` — notas, dados e marca.json de cada marca já feita.
- `docs/SKILL_relogioteca-pesquisa-exaustiva.md` — cópia de referência do roteiro. A versão que vale é a skill `relogioteca-pesquisa-exaustiva` da conta.

## Trava contra execuções simultâneas
- No início: `git pull`, ler `estado.json`. Se existir `"em_execucao"` com horário de menos de 5 horas atrás, outra execução está rodando: parar sem fazer nada (só uma linha no relatório). Se for mais antigo, considerar que a execução anterior morreu e seguir.
- Antes de pesquisar: gravar `"em_execucao": "<data e hora ISO>"` no `estado.json`, commit "Início de bateria" e push.
- No fim (com ou sem sucesso): remover `em_execucao` no mesmo commit do resultado.

## Roteiro de cada execução
1. Carregar a skill `relogioteca-pesquisa-exaustiva` (ferramenta Skill) e seguir o SKILL.md inteiro, como se fosse a primeira vez.
2. Ler `estado.json`. Se houver `em_andamento`, retomar essa bateria pelas notas em `historico/` em vez de começar outra.
3. Trabalhar numa cópia: `mkdir -p /home/claude/trabalho && cp planilha/*.xlsx gravar_marca.py estado.json /home/claude/trabalho/`. Arquivos de cada marca (`notas_<marca>.md`, `dados_<marca>.txt`, `marca_<marca>.json`) também nessa pasta.
4. Escolher as marcas pela ordem da aba Marcas a partir de `proxima_linha_marcas`, pulando as de `marcas_ja_feitas_fora_da_ordem`. **Até 3 marcas por execução, se forem pequenas; marca grande sempre sozinha.** Se a próxima for grande, só ela; senão, as próximas não grandes em sequência até completar 3, parando antes da primeira grande. Esta regra vale mesmo se a cópia da skill da conta ainda disser "duas". Com mais de uma marca, rodar o `gravar_marca.py` uma vez por marca, em sequência, e entregar só a versão final.
5. Pesquisar e gravar conforme a skill. Só entregar se o script terminar com `RESULTADO: OK`.
6. Atualizar `estado.json` (próxima linha, versão, histórico).
7. Salvar no repositório:
   - `git rm planilha/Relogios_atualizada_<antiga>.xlsx`, copiar a nova para `planilha/`;
   - copiar `estado.json` e os arquivos da marca para `historico/`;
   - `git add -A && git commit -m "Bateria: <marca(s)> (vNN)"` e `git push origin main`.
   - Se o push falhar: `git fetch origin main && git rebase origin/main` e tentar uma vez mais. Se ainda falhar, avisar no relatório.
8. Relatório em português do Brasil, calmo e para leigo (o usuário lê no celular): o que entrou, linhas por passada (fontes e relógios novos), por que parou, dados errados na aba Marcas (só relatar), e a lista "Fontes:". Enviar o relatório com SendUserMessage e a planilha nova com SendUserFile.

## Se a execução for interrompida
Se o WebFetch atingir o limite da sessão ou o contexto encher antes de gravar: salvar as notas da marca em `historico/`, gravar em `estado.json` um campo `"em_andamento": {"marcas": [...], "notas": "historico/notas_<marca>.md"}`, fazer commit e push, e avisar no relatório. A execução seguinte retoma dali.

## Nunca
- Nunca apagar o histórico do git nem forçar push (`--force`).
- Nunca alterar na aba Marcas nada além de K (logo), L (site bloqueado) e o vermelho da coluna A, salvo pedido do usuário com "corrija".
