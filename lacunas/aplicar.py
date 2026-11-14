"""Uso: python3 aplicar.py ENTRADA.xlsx SAIDA.xlsx acumulado.json [lote_NOVO.json ...]
(cada arquivo pode ser um passo avulso ou um acumulado {"passos": [...]})
Cada passo: {"remover": [...]} (opcional), "celulas": {marca: {col: valor}}.
Passo com "versao" (lotes de lacunas): M é ACRESCENTADA com 'Lacunas revisadas em DD/MM/AAAA: '.
Passo sem "versao" (pacote v569/570): valores finais (M substitui).
"""
import sys, json, copy, gc, time
import openpyxl
from openpyxl.worksheet.formula import ArrayFormula
from openpyxl.utils import column_index_from_string as ci

ENT, SAI = sys.argv[1:3]
PASSOS = []
for _p in sys.argv[3:]:
    _d = json.load(open(_p))
    PASSOS.extend(_d['passos'] if 'passos' in _d else [_d])  # acumulado.json ou passo avulso
vs = [P['versao'] for P in PASSOS if 'versao' in P]
assert vs == sorted(vs) and len(vs) == len(set(vs)), ('versões fora de ordem ou repetidas', vs)
print('passos', len(PASSOS), 'versões', vs[:1], '...', vs[-1:], flush=True)
t0 = time.time()

def snap_ro(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    mar = [list(r) for r in wb['Marcas'].iter_rows(min_row=1, max_col=13, values_only=True)]
    rel = [list(r) for r in wb['Relógios'].iter_rows(min_row=1, max_col=5, values_only=True)]
    wb.close()
    return mar, rel

mar0, rel0 = snap_ro(ENT)
print('snapshot antes', round(time.time()-t0), 's', flush=True)

wb = openpyxl.load_workbook(ENT)
print('carregado', round(time.time()-t0), 's', flush=True)
m = wb['Marcas']; w = wb['Relógios']
print('merged Rel', len(w.merged_cells.ranges), 'merged Mar', len(m.merged_cells.ranges),
      'CF Rel', len(w.conditional_formatting), 'DV Rel', len(w.data_validations.dataValidation),
      'tables', list(w.tables.keys()), list(m.tables.keys()), 'af', w.auto_filter.ref, m.auto_filter.ref)
arr = [(c.coordinate) for c in m._cells.values() if isinstance(c.value, ArrayFormula)]
print('ArrayFormula Marcas', arr[:10], len(arr))

def remover(ws, nome, ncols_max=None):
    rows = sorted({c.row for c in ws._cells.values() if c.column == 1 and c.value == nome})
    if not rows: return 0
    a, z = rows[0], rows[-1]; n = z-a+1
    assert rows == list(range(a, z+1)), rows
    # NÃO usar ws.delete_rows: ele chama iter_rows até max_column (XFD) e estoura a memória
    for k in [k for k in ws._cells if a <= k[0] <= z]:
        del ws._cells[k]
    for k in sorted(k for k in ws._cells if k[0] > z):
        cell = ws._cells.pop(k)
        cell.row = k[0] - n
        ws._cells[(k[0] - n, k[1])] = cell
    return n

removidas = {}
esperado = {}  # (marca, col) -> valor final
mudancas_m = {}
for P in PASSOS:
    for nome in P.get('remover', []):
        nm = remover(m, nome); nr = remover(w, nome)
        removidas[nome] = (nm, nr)
        print('removida', nome, 'Marcas', nm, 'Relógios', nr, flush=True)
# hyperlinks: ref = coordenada atual
for ws in (m, w):
    for c in ws._cells.values():
        if c.hyperlink is not None:
            c.hyperlink.ref = c.coordinate
idx = {}
for c in m._cells.values():
    if c.column == 1 and c.value is not None and c.row > 1:
        idx.setdefault(c.value, c.row)
for P in PASSOS:
    lote = 'versao' in P
    data = P.get('data', '')
    if lote:
        d, mo, y = data[8:10], data[5:7], data[0:4]
        pref = f'Lacunas revisadas em {d}/{mo}/{y}: '
    for marca, cols in P['celulas'].items():
        r = idx[marca]
        for col, val in cols.items():
            cell = m.cell(r, ci(col))
            if col == 'M' and lote:
                old = cell.value
                old = '' if old is None else str(old).strip()
                val = (old + ' | ' + pref + val) if old else (pref + val)
            cell.value = val
            esperado[(marca, col)] = val
wb.save(SAI)
print('salvo', round(time.time()-t0), 's', flush=True)
del wb, m, w; gc.collect()

# conferência
mar1, rel1 = snap_ro(SAI)
rem = set(removidas)
mar0f = [r for r in mar0 if r[0] not in rem]
rel0f = [r for r in rel0 if r[0] not in rem]
ok = True
print('Marcas linhas', len(mar0), '->', len(mar1), '| Relógios', len(rel0), '->', len(rel1))
if len(mar0f) != len(mar1): ok = False; print('ERRO nº linhas Marcas')
if rel0f != rel1: ok = False; print('ERRO Relógios diferente')
cols = 'ABCDEFGHIJKLM'
inesperadas = []
for r0, r1 in zip(mar0f, mar1):
    for j in range(13):
        a = r0[j]; b = r1[j]
        if a != b:
            key = (r1[0], cols[j])
            if key not in esperado or esperado[key] != b:
                inesperadas.append((r1[0], cols[j], a, b))
faltou = [k for k, v in esperado.items() if not any(r[0] == k[0] and r[cols.index(k[1])] == v for r in mar1)]
print('mudanças inesperadas', len(inesperadas), inesperadas[:5])
print('células previstas não encontradas', faltou[:5])
if any(r[0] in rem for r in mar1) or any(r[0] in rem for r in rel1): ok = False; print('ERRO removida ainda presente')
if inesperadas or faltou: ok = False
print('RESULTADO:', 'OK' if ok else 'FALHOU', round(time.time()-t0), 's')
