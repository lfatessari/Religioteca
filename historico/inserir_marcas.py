"""Insere marcas novas na aba Marcas em ordem alfabética (antes da linha 'antes_de').
Uso: python3 inserir_marcas.py ENTRADA.xlsx SAIDA.xlsx novas.json estado.json
novas.json: [{"antes_de": "Allemano", "valores": {"A":..., "B":..., ... "M":...}}, ...]"""
import sys, json, copy, openpyxl
ENT, SAI, NOVAS, EST = sys.argv[1:5]
novas = json.load(open(NOVAS, encoding='utf-8'))
wb = openpyxl.load_workbook(ENT); m = wb['Marcas']
COLS = 'ABCDEFGHIJKLM'
def row_snapshot(ws, r):
    return [(ws.cell(r, k).value, ws.cell(r, k).hyperlink.target if ws.cell(r, k).hyperlink else None) for k in range(1, 14)]
antes = {r: row_snapshot(m, r) for r in range(1, m.max_row + 1)}
nome_linha = {m.cell(r, 1).value: r for r in range(2, m.max_row + 1)}
pos = []
for n in novas:
    assert n['valores']['A'] not in nome_linha, 'já existe: ' + n['valores']['A']
    pos.append(nome_linha[n['antes_de']])
assert pos == sorted(pos)
modelo = 20  # linha de estilo de referência (Addiesdive)
estilo = [copy.copy(m.cell(modelo, k)._style) for k in range(1, 14)]
alturas = {r: m.row_dimensions[r].height for r in list(m.row_dimensions) if m.row_dimensions[r].height}
# inserir de baixo para cima
for n, p in sorted(zip(novas, pos), key=lambda x: -x[1]):
    for (rr_, cc_) in sorted([k for k in m._cells if k[0] >= p], reverse=True):
        m._move_cell(rr_, cc_, 1, 0)
    for k, col in enumerate(COLS, start=1):
        c = m.cell(p, k); c._style = copy.copy(estilo[k - 1]); c.value = n['valores'].get(col)
        if col == 'K' and c.value: c.hyperlink = c.value
# hyperlinks: atualizar a referência depois de mover as células
for c in m._cells.values():
    if c.hyperlink: c.hyperlink.ref = c.coordinate
# alturas das linhas
for r in list(m.row_dimensions): m.row_dimensions[r].height = None
def novo_idx(r):
    return r + sum(1 for p in pos if r >= p)
for r, h in alturas.items(): m.row_dimensions[novo_idx(r)].height = h
wb.save(SAI)
outras = {t: {c.coordinate: c.value for c in wb[t]._cells.values()} for t in ('Planilha1', 'Tabela de faixa de preços')}
nrel = wb['Relógios'].max_row
import gc; del wb, m; gc.collect()
# verificação
wb2 = openpyxl.load_workbook(SAI); m2 = wb2['Marcas']
ok = True
for r, snap in antes.items():
    if row_snapshot(m2, novo_idx(r)) != snap: ok = False; print('!! linha', r, 'mudou'); break
for n, p in zip(novas, pos):
    rr = novo_idx(p) - 1
    print('nova', m2.cell(rr, 1).value, 'na linha', rr, '| entre', m2.cell(rr - 1, 1).value, 'e', m2.cell(rr + 1, 1).value)
    ok &= m2.cell(rr, 1).value == n['valores']['A']
for t, a in outras.items():
    b = {c.coordinate: c.value for c in wb2[t]._cells.values()}
    if a != b: ok = False; print('!!', t, 'mudou')
if wb2['Relógios'].max_row != nrel: ok = False; print('!! Relógios mudou de tamanho')
print('max_row Marcas', m2.max_row)
# estado.json: deslocar referências de linhas da aba Marcas
e = json.load(open(EST, encoding='utf-8'))
e['proxima_linha_marcas'] = novo_idx(e['proxima_linha_marcas'])
for k, v in e.get('marcas_ja_feitas_fora_da_ordem', {}).items(): v['linha_marcas'] = novo_idx(v['linha_marcas'])
for p_ in e.get('marcas_pendentes', []):
    if 'linha_marcas' in p_: p_['linha_marcas'] = novo_idx(p_['linha_marcas'])
if e.get('em_andamento') and e['em_andamento'].get('linha_marcas'): e['em_andamento']['linha_marcas'] = novo_idx(e['em_andamento']['linha_marcas'])
import re
av = {}
for k, v in e.get('avisos', {}).items():
    f = lambda mm: f'(linha {novo_idx(int(mm.group(1)))})'
    av[re.sub(r'\(linha (\d+)\)', f, k)] = re.sub(r'\(linha (\d+)\)', f, v) if isinstance(v, str) else v
e['avisos'] = av
json.dump(e, open(EST, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('proxima_linha_marcas', e['proxima_linha_marcas'])
print('RESULTADO:', 'OK' if ok else 'FALHOU')
sys.exit(0 if ok else 1)
