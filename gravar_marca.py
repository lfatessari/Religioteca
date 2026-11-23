"""Grava uma ou mais marcas na planilha Relogioteca, abrindo e salvando a planilha UMA vez só.
Uso: python3 gravar_marca.py ENTRADA.xlsx SAIDA.xlsx dados1.txt marca1.json [dados2.txt marca2.json ...]
dados.txt: uma linha por relógio  ->  Nome|CÓDIGO|URL_imagem|Características
marca.json: {"marca": "<igual à coluna A de Marcas>", "usa_codigos": true/false,
             "logo": "url ou vazio", "site_bloqueado": "texto ou vazio", "vermelho": true/false,
             "observacoes": "texto NOVO para a coluna M (é ACRESCENTADO ao que já existe) ou vazio",
             "grande": true/false, "complemento": false,
             "catalogo_fechado": {"oficial": "<url do site oficial com a lista completa>",
                                  "confirmacoes": ["<url de fora 1>", "<url de fora 2>", ...]}  (opcional),
             "so_site_oficial": {"dominio": "<domínio da coluna G>", "motivo": "<por que não há fontes de fora>"}  (opcional; exceção do usuário, 23/11/2026),
             "fontes": [{"url": "...", "passada": 1, "novos": 0}, ...]}
Trava de profundidade (conferida para TODAS as marcas antes de gravar qualquer uma):
  - mínimo de fontes diferentes: 15; 25 se grande;
  - catálogo fechado (marca não grande e não vermelha, com o site oficial listando tudo e 2+ fontes
    de fora, de domínios diferentes entre si e do oficial, confirmando a mesma lista): mínimo 8, e as
    3 últimas fontes da lista têm de ter "novos": 0 (critério de parada);
  - vermelho: 2ª passada com 10+ fontes novas (que não estejam na 1ª).
Correções em B, C, D, G, H, I, J da aba Marcas (campo "correcoes") precisam de
"correcoes_fontes": {"<col>": ["<url>", ...]} com fontes já abertas na pesquisa dos relógios (que estejam
em "fontes"): corrige-se só com o que a pesquisa de relógios já mostrou, sem buscas extras.
"complemento": true só vale para marca que já tem linhas na aba Relógios.

LACUNAS DA ABA MARCAS NA MESMA GRAVAÇÃO (passada única, pedido do usuário em 22/11/2026):
um par "lacunas LOTE.json" em qualquer posição depois de SAIDA.xlsx, por exemplo
  python3 gravar_marca.py ENTRADA.xlsx SAIDA.xlsx dados_A.txt marca_A.json lacunas lote_NNN.json
  python3 gravar_marca.py ENTRADA.xlsx SAIDA.xlsx lacunas lote_NNN.json        (só lacunas, sem relógios)
LOTE.json: {"data": "AAAA-MM-DD", "prefixo": "Passada única", "celulas": {"<marca>": {"B": "...", "K": "...", "M": "fontes e explicações"}}}
  - só entram colunas de B a K que estejam VAZIAS na planilha (célula já preenchida é ignorada, com aviso);
  - E e F têm de ser inteiros; M é obrigatória e é ACRESCENTADA como "<prefixo> em DD/MM/AAAA: <texto>";
  - a marca do lote pode ser também uma das marcas com relógios do mesmo comando.
"""
import sys, json, copy, re
from urllib.parse import quote, urlparse
from collections import Counter
import openpyxl
from openpyxl.worksheet.formula import ArrayFormula
from openpyxl.styles import PatternFill

args = sys.argv[1:]
assert len(args) >= 4 and len(args) % 2 == 0, __doc__
import time; _t0 = time.time()
ENT, SAI = args[0], args[1]
pares = [(args[k], args[k + 1]) for k in range(2, len(args), 2)]
LOTES_LAC = [json.load(open(b, encoding='utf-8')) for a, b in pares if a == 'lacunas']
pares = [(a, b) for a, b in pares if a != 'lacunas']
COLS_LAC = {c: i for i, c in enumerate('ABCDEFGHIJKLM', 1) if c in 'BCDEFGHIJK'}
def vazio(v): return v is None or str(v).strip() in ('', '-', '—', 'n/a')
S = ' (sem referência publicada)'
def enc(u): return quote(u, safe=":/?&=%#+~;,@!$'()*[]-._")
def snap(wb):
    return {ws.title: {c.coordinate: (('ARR', c.value.ref, c.value.text) if isinstance(c.value, ArrayFormula) else c.value)
                       for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
def _u(x): return (x['url'] if isinstance(x, dict) else x).strip().lower().rstrip('/')
def dom(u):
    d = urlparse(u if '://' in u else 'https://' + u).netloc.lower()
    return d[4:] if d.startswith('www.') else d

wb = openpyxl.load_workbook(ENT); before = snap(wb)
w = wb['Relógios']; m = wb['Marcas']
st = [copy.copy(w.cell(1190, c)._style) for c in (1, 2, 3)]
COLS_CORR = {'B': 2, 'C': 3, 'D': 4, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
marcas_rel = [w.cell(r, 1).value for r in range(1, w.max_row + 1)]

# ---------- 1) trava de profundidade de TODAS as marcas, antes de gravar ----------
lotes, problemas = [], []
for DADOS, CFG in pares:
    cfg = json.load(open(CFG, encoding='utf-8'))
    marca = cfg['marca']
    lms = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == marca]
    if len(lms) != 1:
        problemas.append(f'{marca}: não encontrada (ou repetida) na aba Marcas: {lms}'); continue
    fontes = cfg.get('fontes') or []
    urls = {_u(f) for f in fontes}
    por_passada = {}
    for f in fontes: por_passada.setdefault(int(f.get('passada', 1)), []).append(f)
    print(f'== {marca} (linha {lms[0]} da aba Marcas)')
    for n_p in sorted(por_passada):
        fs = por_passada[n_p]
        print(f'Passada {n_p}: {len({_u(f) for f in fs})} fontes, {sum(int(f.get("novos", 0)) for f in fs)} relógios novos')
    ja_tem = marca in marcas_rel
    if cfg.get('complemento'):
        if not ja_tem: problemas.append(f'{marca}: "complemento" só vale para marca que já tem linhas')
    else:
        minimo = 25 if cfg.get('grande') else 15
        so = cfg.get('so_site_oficial')
        if so:
            # exceção aprovada pelo usuário (23/11/2026): marca nova e pequena cujo único lugar com os modelos
            # é o site oficial. Vale só para marca não grande e não vermelha, com TODAS as fontes no domínio
            # oficial (mínimo 3 páginas) e o motivo escrito (vai para a coluna M).
            erros = []
            if cfg.get('grande') or cfg.get('vermelho'): erros.append('não vale para marca grande ou vermelha')
            d_of = (so.get('dominio') or '').lower().removeprefix('www.')
            if not d_of: erros.append('falta "dominio"')
            fora = [f['url'] for f in fontes if dom(f['url']) != d_of]
            if fora: erros.append(f'fontes fora do domínio oficial: {fora[:3]}')
            if not (so.get('motivo') or '').strip(): erros.append('falta "motivo"')
            if erros: problemas += [f'{marca}: exceção "só site oficial" recusada — {e}' for e in erros]
            else:
                minimo = 3
                print(f'Exceção só site oficial ({d_of}): mínimo {minimo} páginas oficiais')
        cf = cfg.get('catalogo_fechado')
        if cf:
            erros = []
            if cfg.get('grande') or cfg.get('vermelho'): erros.append('não vale para marca grande ou vermelha')
            of = cf.get('oficial', ''); conf = cf.get('confirmacoes') or []
            if _u(of) not in urls: erros.append('a página oficial não está em "fontes"')
            faltam = [c for c in conf if _u(c) not in urls]
            if faltam: erros.append(f'confirmações fora de "fontes": {faltam}')
            doms = {dom(c) for c in conf} - {dom(of)}
            if len(doms) < 2: erros.append('precisa de 2+ confirmações de domínios diferentes entre si e do site oficial')
            p1 = por_passada.get(1, [])
            if len(p1) < 3 or any(int(f.get('novos', 0)) for f in p1[-3:]):
                erros.append('as 3 últimas fontes da 1ª passada precisam ter "novos": 0')
            if erros: problemas += [f'{marca}: catálogo fechado recusado — {e}' for e in erros]
            else:
                minimo = 8
                print(f'Catálogo fechado: oficial {dom(of)} + confirmações {sorted(doms)} → mínimo {minimo}')
        if len(urls) < minimo: problemas.append(f'{marca}: só {len(urls)} fontes diferentes; o mínimo é {minimo}')
        if cfg.get('vermelho'):
            p1 = {_u(f) for f in por_passada.get(1, [])}
            p2 = {_u(f) for f in por_passada.get(2, [])} - p1
            if len(p2) < 10: problemas.append(f'{marca}: marca vermelha, a 2ª passada tem {len(p2)} fontes novas; o mínimo é 10')
    corr = cfg.get('correcoes') or {}
    fontes_corr = cfg.get('correcoes_fontes') or {}
    for col in corr:
        fc = fontes_corr.get(col) or []
        fora = [u for u in fc if _u(u) not in urls]
        if not fc or fora:
            problemas.append(f'{marca}: correção em {col} precisa de "correcoes_fontes": {{"{col}": [urls]}} '
                             f'com fontes que estejam em "fontes" (fora: {fora})')
    for col in corr:
        if col not in COLS_CORR: problemas.append(f'{marca}: coluna {col} não pode ser corrigida (só B, C, D, G, H, I, J)')
    novas = []
    for l in open(DADOS, encoding='utf-8'):
        if not l.strip(): continue
        partes = l.rstrip('\n').split('|')
        if len(partes) != 4: problemas.append(f'{marca}: linha com {len(partes)} campos em {DADOS}: {l[:60]!r}'); continue
        n, c, i, e = partes
        nome = f'{n} - {c}' if c else (n + S if cfg['usa_codigos'] else n)
        novas.append([marca, nome, enc(i), None, e or None])
    nomes_exist = {w.cell(r, 2).value for r in range(2, w.max_row + 1) if marcas_rel[r - 1] == marca}
    dup = [k for k, v in Counter(x[1] for x in novas).items() if v > 1] + [x[1] for x in novas if x[1] in nomes_exist]
    if dup: problemas.append(f'{marca}: nomes repetidos: {dup}')
    lotes.append((cfg, lms[0] if lms else None, novas, corr))
# lacunas da aba Marcas (lote): só células vazias de B a K, mais M
lac = []  # (marca, linha, {col: valor}, texto_M)
for P in LOTES_LAC:
    data = P.get('data', '')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', data): problemas.append('lote de lacunas sem "data": "AAAA-MM-DD"'); continue
    pref = f"{P.get('prefixo', 'Passada única')} em {data[8:10]}/{data[5:7]}/{data[0:4]}: "
    for marca, cols in (P.get('celulas') or {}).items():
        lms = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == marca]
        if len(lms) != 1: problemas.append(f'{marca} (lacunas): não encontrada (ou repetida) na aba Marcas: {lms}'); continue
        txt = str(cols.get('M') or '').strip()
        if not txt: problemas.append(f'{marca} (lacunas): falta o texto de "M" (fontes e explicações)'); continue
        vals = {}
        for col, val in cols.items():
            if col == 'M': continue
            if col not in COLS_LAC: problemas.append(f'{marca} (lacunas): coluna {col} não é permitida (só B a K, e M)'); continue
            if vazio(val): continue
            if col in ('E', 'F'):
                try: val = str(int(str(val).strip()))
                except ValueError: problemas.append(f'{marca} (lacunas): {col} tem de ser inteiro, veio {val!r}'); continue
            if not vazio(m.cell(lms[0], COLS_LAC[col]).value):
                print(f'  (lacunas) {marca} {col}: célula já preenchida, ignorado'); continue
            vals[col] = val
        lac.append((marca, lms[0], vals, pref + txt))
for cfg, lm, novas, corr in lotes:
    if cfg.get('logo') and any(l[0] == cfg['marca'] and 'K' in l[2] for l in lac):
        problemas.append(f"{cfg['marca']}: logo no marca.json e K no lote de lacunas ao mesmo tempo; use só um")
if len({l[0] for l in lac}) != len(lac): problemas.append('a mesma marca aparece duas vezes nos lotes de lacunas')
nomes_lote = [c['marca'] for c, *_ in lotes]
if len(set(nomes_lote)) != len(nomes_lote): problemas.append('a mesma marca aparece duas vezes no comando')
if problemas:
    for p in problemas: print('  !! TRAVA:', p)
    print('RESULTADO: FALHOU — pesquisa incompleta, nada foi gravado'); sys.exit(1)

# ---------- 2) gravação ----------
permitidas, inicio_geral, todas_novas = {'M1'}, None, []
for cfg, lm, novas, corr in lotes:
    marca = cfg['marca']
    existentes_r = [r for r in range(2, w.max_row + 1) if w.cell(r, 1).value == marca]
    if existentes_r:
        # reescreve do início do bloco até o fim, para manter a marca contígua
        inicio = existentes_r[0]
        cauda = [[w.cell(r, k).value for k in (1, 2, 3, 4, 5)] for r in range(inicio, w.max_row + 1)]
        linhas = [x for x in cauda if x[0] == marca] + novas + [x for x in cauda if x[0] != marca]
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
    inicio_geral = inicio if inicio_geral is None else min(inicio_geral, inicio)
    todas_novas += novas
    # aba Marcas: K (logo), L (site bloqueado), M (observações, acrescentadas), vermelho de A, correções pedidas
    if cfg.get('logo'): m.cell(lm, 11).value = cfg['logo']
    if cfg.get('site_bloqueado'):
        c = m.cell(lm, 12); c.value = cfg['site_bloqueado']; c._style = copy.copy(m.cell(lm, 11)._style)
    obs = (cfg.get('observacoes') or '').strip()
    if obs:
        if m.cell(1, 13).value is None:
            h = m.cell(1, 13); h.value = 'Observações'; h._style = copy.copy(m.cell(1, 12)._style)
        antigo = (m.cell(lm, 13).value or '').strip()
        novo = obs if (not antigo or obs.startswith(antigo)) else f'{antigo} | {obs}'
        c = m.cell(lm, 13); c.value = novo; c._style = copy.copy(m.cell(lm, 11)._style)
    for col, val in corr.items():
        print(f'  correção {col}{lm}: {str(m.cell(lm, COLS_CORR[col]).value)[:80]!r} -> {str(val)[:80]!r}')
        m.cell(lm, COLS_CORR[col]).value = val
    if cfg.get('vermelho'):
        m.cell(lm, 1).fill = PatternFill(fill_type='solid', start_color='FFFF0000', end_color='FFFF0000')
    permitidas |= {f'K{lm}', f'L{lm}', f'M{lm}'} | {f'{c}{lm}' for c in corr}

for marca, lm, vals, txt in lac:
    for col, val in vals.items():
        m.cell(lm, COLS_LAC[col]).value = val
    antigo = str(m.cell(lm, 13).value or '').strip()
    c = m.cell(lm, 13); c.value = f'{antigo} | {txt}' if antigo else txt
    if not c.has_style: c._style = copy.copy(m.cell(lm, 11)._style)
    permitidas |= {f'M{lm}'} | {f'{col}{lm}' for col in vals}
    print(f'  lacunas {marca} (linha {lm}): {"".join(sorted(vals)) or "nada novo"} + M')
if inicio_geral is None: inicio_geral = w.max_row + 1  # só lacunas: nenhuma linha nova na aba Relógios

wb.save(SAI)

# ---------- 3) verificação (uma vez, para todas) ----------
wb2 = openpyxl.load_workbook(SAI); after = snap(wb2); w2 = wb2['Relógios']; m2 = wb2['Marcas']
ok = True
for t in before:
    if t == 'Relógios': continue
    mud = sorted(k for k in set(before[t]) | set(after[t]) if before[t].get(k) != after[t].get(k))
    extra = [k for k in mud if k not in permitidas]
    print(t, 'mudanças:', mud)
    if extra: ok = False; print('  !! mudança fora do permitido:', extra)
arr = sum(1 for c in m2._cells.values() if isinstance(c.value, ArrayFormula))
arr_in = sum(1 for v in before['Marcas'].values() if isinstance(v, tuple) and v and v[0] == 'ARR')
print('ArrayFormula em Marcas:', arr, '(entrada:', arr_in, ')'); ok &= arr == arr_in
antes_ok = all(before['Relógios'].get(k) == after['Relógios'].get(k)
               for k in before['Relógios'] if int(re.sub(r'\D', '', k)) < inicio_geral)
print('linhas anteriores intactas:', antes_ok); ok &= antes_ok
ruins = [r for r in range(inicio_geral, w2.max_row + 1)
         if w2.cell(r, 3).value and (not w2.cell(r, 3).hyperlink or w2.cell(r, 3).hyperlink.target != w2.cell(r, 3).value)]
print('hyperlinks ruins:', ruins); ok &= not ruins
seq = [w2.cell(r, 1).value for r in range(inicio_geral, w2.max_row + 1)]
blocos = ([seq[0]] if seq else []) + [seq[k] for k in range(1, len(seq)) if seq[k] != seq[k - 1]]
contig = len(blocos) == len(set(blocos))
print('blocos contíguos a partir de', inicio_geral, ':', contig); ok &= contig
for cfg, lm, novas, corr in lotes:
    mc = cfg['marca']
    print(f'{mc}: linhas agora {sum(1 for r in range(2, w2.max_row + 1) if w2.cell(r, 1).value == mc)} | novas: {len(novas)}')
print('max_row:', w2.max_row)
ph = any('7WgAAOSwQ7haxTU1' in (x[2] or '') for x in todas_novas)
print('placeholder eBay presente:', ph); ok &= not ph
print('tempo:', round(time.time() - _t0), 's')
print('RESULTADO:', 'OK' if ok else 'FALHOU — não entregar')
