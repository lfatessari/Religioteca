"""Grava uma marca na planilha Relogioteca.
Uso: python3 gravar_marca.py ENTRADA.xlsx SAIDA.xlsx dados.txt marca.json
dados.txt: uma linha por relógio  ->  Nome|CÓDIGO|URL_imagem|Características
marca.json: {"marca": "<igual à coluna A de Marcas>", "usa_codigos": true/false,
             "logo": "url ou vazio", "site_bloqueado": "texto ou vazio", "vermelho": true/false,
             "observacoes": "texto da coluna M (dados errados na aba Marcas) ou vazio",
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
if cfg.get('observacoes'):
    # coluna M: dados da aba Marcas que parecem errados (só registrar, nunca corrigir B–J)
    if m.cell(1, 13).value is None:
        h = m.cell(1, 13); h.value = 'Observações'; h._style = copy.copy(m.cell(1, 12)._style)
    c = m.cell(lm, 13); c.value = cfg['observacoes']; c._style = copy.copy(m.cell(lm, 11)._style)
if cfg.get('vermelho'):
    m.cell(lm, 1).fill = PatternFill(fill_type='solid', start_color='FFFF0000', end_color='FFFF0000')

wb.save(SAI)

# ---------- verificação ----------
wb2 = openpyxl.load_workbook(SAI); after = snap(wb2); w2 = wb2['Relógios']; m2 = wb2['Marcas']
ok = True
for t in before:
    if t == 'Relógios': continue
    mud = sorted(k for k in set(before[t]) | set(after[t]) if before[t].get(k) != after[t].get(k))
    perm = {f'K{lm}', f'L{lm}', f'M{lm}', 'M1'}
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
