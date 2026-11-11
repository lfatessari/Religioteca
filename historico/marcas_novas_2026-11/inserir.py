"""Insere marcas novas na aba Marcas em ordem alfabética (vários por posição). Uso: inserir.py ENT SAI novas.json estado_in estado_out"""
import sys, json, copy, re, unicodedata, openpyxl
ENT, SAI, NOVAS, EIN, EOUT = sys.argv[1:6]
novas = json.load(open(NOVAS, encoding='utf-8'))
def k(s):
    s = unicodedata.normalize('NFD', str(s)); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'[^a-z0-9]', '', s)
wb = openpyxl.load_workbook(ENT); m = wb['Marcas']
def snap(ws, r): return [(ws.cell(r, c).value, ws.cell(r, c).hyperlink.target if ws.cell(r, c).hyperlink else None) for c in range(1, 14)]
N0 = m.max_row
antes = {r: snap(m, r) for r in range(1, N0 + 1)}
nomes = [m.cell(r, 1).value for r in range(2, N0 + 1)]
exist = {k(n) for n in nomes if n}
novas = [n for n in novas if k(n['A']) not in exist or print('JA EXISTE, pulada:', n['A'])]
novas.sort(key=lambda n: k(n['A']))
# posição: antes da primeira linha existente com chave maior
pos = []
for n in novas:
    kn = k(n['A'])
    ant = [r for r in range(2, N0 + 1) if m.cell(r, 1).value and k(m.cell(r, 1).value)[:1] == kn[:1] and k(m.cell(r, 1).value) < kn]
    p = (max(ant) + 1) if ant else next((r for r in range(2, N0 + 1) if m.cell(r, 1).value and k(m.cell(r, 1).value) > kn), N0 + 1)
    pos.append(p)
assert pos == sorted(pos)
def novo_idx(r): return r + sum(1 for p in pos if p <= r)
estilo = [copy.copy(m.cell(20, c)._style) for c in range(1, 14)]
alturas = {r: m.row_dimensions[r].height for r in list(m.row_dimensions) if m.row_dimensions[r].height}
# mover todas as células existentes de uma vez, de baixo para cima
for (r, c) in sorted([x for x in m._cells if x[0] >= min(pos)], reverse=True):
    d = novo_idx(r) - r
    if d: m._move_cell(r, c, d, 0)
dest = []
for i, (n, p) in enumerate(zip(novas, pos)):
    rr = p + i  # i novas já inseridas antes
    dest.append(rr)
    for c, col in enumerate('ABCDEFGHIJKLM', start=1):
        cell = m.cell(rr, c); cell._style = copy.copy(estilo[c - 1]); cell.value = n.get(col)
        if col == 'K' and cell.value: cell.hyperlink = cell.value
        if col == 'E' and cell.value is not None: cell.value = str(cell.value)
        if col == 'F' and cell.value is not None: cell.value = str(cell.value)
for c in m._cells.values():
    if c.hyperlink: c.hyperlink.ref = c.coordinate
for r in list(m.row_dimensions): m.row_dimensions[r].height = None
for r, h in alturas.items(): m.row_dimensions[novo_idx(r)].height = h
outras = {t: {c.coordinate: c.value for c in wb[t]._cells.values()} for t in ('Planilha1', 'Tabela de faixa de preços')}
nrel = wb['Relógios'].max_row; rel_amostra = [(wb['Relógios'].cell(r, 1).value, wb['Relógios'].cell(r, 2).value) for r in (2, 1190, 40000, nrel)]
wb.save(SAI)
wb2 = openpyxl.load_workbook(SAI); m2 = wb2['Marcas']; ok = True
for r, s in antes.items():
    if snap(m2, novo_idx(r)) != s: ok = False; print('!! linha antiga', r, 'mudou'); break
for n, rr in zip(novas, dest):
    if m2.cell(rr, 1).value != n['A']: ok = False; print('!! nova fora do lugar', n['A'])
ordem = [k(m2.cell(r, 1).value) for r in dest]
viz = [(m2.cell(rr - 1, 1).value, m2.cell(rr, 1).value, m2.cell(rr + 1, 1).value) for rr in dest]
print('vizinhança:', [v for v in viz if v[0] not in [n['A'] for n in novas]][:12], viz[-3:])
for t, a in outras.items():
    if a != {c.coordinate: c.value for c in wb2[t]._cells.values()}: ok = False; print('!!', t, 'mudou')
w2 = wb2['Relógios']
if w2.max_row != nrel or rel_amostra != [(w2.cell(r, 1).value, w2.cell(r, 2).value) for r in (2, 1190, 40000, nrel)]: ok = False; print('!! Relógios mudou')
print('Marcas:', N0, '->', m2.max_row, '| novas:', len(novas))
e = json.load(open(EIN, encoding='utf-8'))
e['proxima_linha_marcas'] = novo_idx(e['proxima_linha_marcas'])
for v in e.get('marcas_ja_feitas_fora_da_ordem', {}).values(): v['linha_marcas'] = novo_idx(v['linha_marcas'])
for lst in ('marcas_pendentes', 'marcas_novas_sem_relogios'):
    for p_ in e.get(lst, []):
        if isinstance(p_, dict) and 'linha_marcas' in p_: p_['linha_marcas'] = novo_idx(p_['linha_marcas'])
if e.get('em_andamento') and e['em_andamento'].get('linha_marcas'): e['em_andamento']['linha_marcas'] = novo_idx(e['em_andamento']['linha_marcas'])
f = lambda mm: f'(linha {novo_idx(int(mm.group(1)))})'
e['avisos'] = {re.sub(r'\(linha (\d+)\)', f, a): (re.sub(r'\(linha (\d+)\)', f, b) if isinstance(b, str) else b) for a, b in e.get('avisos', {}).items()}
json.dump(e, open(EOUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump([{'marca': n['A'], 'linha': rr} for n, rr in zip(novas, dest)], open(SAI + '.linhas.json', 'w'), ensure_ascii=False)
print('proxima_linha_marcas', e['proxima_linha_marcas']); print('RESULTADO:', 'OK' if ok else 'FALHOU'); sys.exit(0 if ok else 1)
