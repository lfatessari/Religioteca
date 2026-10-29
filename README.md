# Relogioteca

Base de dados de marcas de relógios do @relogioteca: aba **Marcas** (uma linha por marca) e aba **Relógios** (todos os modelos de cada marca, com código, foto e características).

A pesquisa da aba Relógios roda sozinha, algumas vezes por dia, seguindo o roteiro da skill `relogioteca-pesquisa-exaustiva`. As regras de cada execução estão em `CLAUDE.md`.

A planilha mais recente fica em `planilha/`.

## Site público

O site (Atlas Horológico) é gerado a partir da planilha pelo GitHub Actions (`.github/workflows/site.yml`) e publicado no GitHub Pages:

- `site/baixar_fotos.py` baixa as fotos da aba Relógios, reduz para 400 px (WebP) e guarda no ramo `fotos` (só as novas a cada vez).
- `site/gerar_site.py` monta a página e os arquivos de dados com as marcas, histórias e galerias.
- Roda a cada planilha nova e uma vez por dia (para tentar de novo as fotos que falharam). Também dá para rodar à mão na aba Actions → "Site público" → "Run workflow".
