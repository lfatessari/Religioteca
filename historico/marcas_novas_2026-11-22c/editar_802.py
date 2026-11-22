"""v802 (pedido do usuário, 22/11/2026): remove 'A&S Watch', insere 'Borna' e 'Michel Chirivi'
(só o nome, em ordem alfabética) e grava K/G/M da AOS Watches.
Uso: python3 editar_802.py ENTRADA.xlsx SAIDA.xlsx
Não usa ws.delete_rows/insert_rows (célula solta em XFD)."""
import sys, copy, gc, time, json
import openpyxl

ENT, SAI = sys.argv[1:3]
REMOVER = ['A&S Watch']
INSERIR = [('Borna', 'Boschett Timepieces'), ('Michel Chirivi', 'Michel Jordi')]  # (nova, antes_de)
MODELO = 'Astrabyss'  # linha inserida na v800: copia o estilo dela
CEL = {'AOS Watches': {
    'K': 'https://aos-watches.com/wp-content/uploads/2025/01/AOS-03.png',
    'G': 'aos-watches.com',
    'M+': " | Atualizado a pedido do usuário em 22/11/2026: K = logo do site oficial aos-watches.com "
          "(imagem AOS-03.png, que o site usa como ícone e mostra na página inicial; o site abriu em 22/11/2026, "
          "mas a imagem em si não abriu para conferência visual). G corrigido: arthuroskarstampfli.com → aos-watches.com "
          "(site oficial ativo, indicado pelo usuário; rodapé 'AOS WATCHES, 2088 Cressier (NE), © 2026').",
}}
t0 = time.time()

def snap_ro(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    mar = [list(r) for r in wb['Marcas'].iter_rows(min_row=1, max_col=13, values_only=True)]
    rel = [list(r) for r in wb['Relógios'].iter_rows(min_row=1, max_col=5, values_only=True)]
    wb.close()
    return mar, rel

mar0, rel0 = snap_ro(ENT)
wb = openpyxl.load_workbook(ENT)
m = wb['Marcas']; w = wb['Relógios']
print('carregado', round(time.time() - t0), 's', flush=True)
assert len(m._hyperlinks) == 0 and len(m.merged_cells.ranges) == 0 and len(m.conditional_formatting) == 0

def linha(nome):
    rows = [c.row for c in m._cells.values() if c.column == 1 and c.value == nome]
    assert len(rows) == 1, (nome, rows)
    return rows[0]

def desloca(de, delta):
    """move todas as células com linha >= de em delta linhas (e as alturas de linha)"""
    keys = sorted((k for k in m._cells if k[0] >= de), reverse=(delta > 0))
    for k in keys:
        cell = m._cells.pop(k)
        cell.row = k[0] + delta
        m._cells[(k[0] + delta, k[1])] = cell
    rd = m.row_dimensions
    ks = sorted((k for k in list(rd.keys()) if k >= de), reverse=(delta > 0))
    for k in ks:
        d = rd.pop(k)
        d.index = k + delta
        rd[k + delta] = d

for nome in INSERIR:
    assert not [c for c in m._cells.values() if c.column == 1 and c.value == nome[0]], nome
for nome in REMOVER:
    assert not any(r[0] == nome for r in rel0), 'tem relógios: ' + nome

rm = linha(MODELO)
estilo = {c: copy.copy(m._cells[(rm, c)]._style) for c in range(1, 14) if (rm, c) in m._cells}
print('modelo', MODELO, 'cols', sorted(estilo), 'fill A', m.cell(rm, 1).fill.fill_type, m.cell(rm, 1).fill.fgColor.rgb,
      'altura', m.row_dimensions[rm].height if rm in m.row_dimensions else None)
print('alturas definidas em', sorted(k for k, v in m.row_dimensions.items() if v.height is not None)[:30])

for nome in REMOVER:
    r = linha(nome)
    for k in [k for k in m._cells if k[0] == r]:
        del m._cells[k]
    if r in m.row_dimensions:
        del m.row_dimensions[r]
    desloca(r + 1, -1)
    print('removida', nome, 'linha', r, flush=True)

for nova, antes in INSERIR:
    r = linha(antes)
    desloca(r, +1)
    for c, st in estilo.items():
        cell = m.cell(r, c)
        cell._style = copy.copy(st)
    m.cell(r, 1).value = nova
    print('inserida', nova, 'linha', r, 'antes de', antes, '| acima:', m.cell(r - 1, 1).value, flush=True)

esper = {}
for marca, cols in CEL.items():
    r = linha(marca)
    for col, val in cols.items():
        if col == 'M+':
            cell = m.cell(r, 13); val = (str(cell.value or '').strip() + val); col = 'M'
        else:
            cell = m.cell(r, openpyxl.utils.column_index_from_string(col))
        print(marca, col, 'antes:', repr(cell.value)[:70])
        cell.value = val
        esper[(marca, col)] = val

wb.save(SAI)
print('salvo', round(time.time() - t0), 's', flush=True)
del wb, m, w; gc.collect()

# conferência
mar1, rel1 = snap_ro(SAI)
exp = [list(r) for r in mar0 if r[0] not in REMOVER]
for nova, antes in INSERIR:
    i = [k for k, r in enumerate(exp) if r[0] == antes]
    assert len(i) == 1
    exp.insert(i[0], [nova] + [None] * 12)
for (marca, col), val in esper.items():
    i = [k for k, r in enumerate(exp) if r[0] == marca][0]
    exp[i]['ABCDEFGHIJKLM'.index(col)] = val
ok = True
if rel0 != rel1: ok = False; print('ERRO Relógios diferente')
if len(exp) != len(mar1): ok = False; print('ERRO nº de linhas', len(exp), len(mar1))
dif = [(i + 1, a[0], b[0]) for i, (a, b) in enumerate(zip(exp, mar1)) if a != b]
if dif: ok = False; print('ERRO linhas diferentes', dif[:10])
print('Marcas linhas', len(mar0), '->', len(mar1), '| Relógios', len(rel0), '->', len(rel1))
mapa = {}
pos1 = {r[0]: i + 1 for i, r in enumerate(mar1) if r[0]}
for i, r in enumerate(mar0):
    if r[0] and r[0] in pos1: mapa[i + 1] = pos1[r[0]]
json.dump(mapa, open(SAI + '.mapa_linhas.json', 'w'))
print('RESULTADO:', 'OK' if ok else 'FALHOU', round(time.time() - t0), 's')
