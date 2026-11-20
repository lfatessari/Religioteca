import sys, openpyxl
ENT, SAI = sys.argv[1:3]
P = "https://cdn.shopify.com/s/files/1/2321/3069/products/"
A = "https://www.abartwatches.com/"
J = "https://justwatchme.net/"
T = [("Série O - O110","O110.jpg?v=1571699465"),("Série O - O111","O111.jpg?v=1571699465"),
("Série G - G105","G105.jpg?v=1571699693"),("Série G - G121","G121.jpg?v=1571699693"),
("Série GQC - GQC104","GQC104.png?v=1571699463"),("Série KLD - KLD104","KLD104.jpg?v=1571699691"),
("Série KLD - KLD111","KLD111.jpg?v=1571699691"),("Série KLD - KLD112","KLD112.jpg?v=1571699691"),
("Série KLD - KLD123","KLD123.jpg?v=1571699691"),("Série KLD - KLD122","KLD122.jpg?v=1571699691"),
("Série KSD - KSD101","KSD101.png?v=1571699466"),("Série KSD - KSD102","KSD102.png?v=1571699466"),
("Série KSD - KSD103","KSD103.png?v=1571699466"),("Série KSD - KSD104","KSD104.png?v=1571699466"),
("Série KSD - KSD105","KSD105.png?v=1571699466"),("Série KSD - KSD106","KSD106.png?v=1571699466"),
("Série MA - MA101","MA101.png?v=1571699466"),("Série MA - MA102","MA102.png?v=1571699791"),
("Série MA - MA103","MA103.png?v=1571699790"),("Série MA - MA104","MA104.png?v=1571699466"),
("Série DP - DP101","DP101.jpg?v=1571699694"),("Série DP - DP102","DP102.jpg?v=1571699694"),
("Série W - W102","W102.jpg?v=1571699464"),("Série W - W130","W130.jpg?v=1571699464"),
("Série W - W201","W201.jpg?v=1571699464"),("Série W - W202","W202.jpg?v=1571699464"),
("Série W - W230","W230.jpg?v=1571699464"),("Série ES - ES550","ES550.jpg?v=1674899474")]
ITENS = [(m, A, P + f) for m, f in T] + [
("Série OC Chronograph - OC101", J, "https://justwatchme.net/cdn/shop/products/47709f341f672bd97d7241c952d1996b.jpg?v=1508284113"),
("Série OC Chronograph - OC103B", J, "https://justwatchme.net/cdn/shop/products/7af8c8ef51efb2a069dfe96d15f7f17e.jpg?v=1508284678"),
("Série OC Chronograph - OC105", J, "https://justwatchme.net/cdn/shop/files/a.b.artOC105Front.png?v=1732925907"),
("Série I - I301", J, "https://justwatchme.net/cdn/shop/products/433927f31e84bcf1a9b1e45d18dd983e.jpg?v=1508284331")]
def snap(wb):
    return {ws.title: {c.coordinate: c.value for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb = openpyxl.load_workbook(ENT); antes = snap(wb)
r_ = wb['Relógios']; m = wb['Marcas']
idx = {}
for r in range(1, r_.max_row + 1):
    if r_.cell(r, 1).value == 'a.b.art':
        idx.setdefault(r_.cell(r, 2).value, []).append(r)
esperadas = []; avisos = []; n = 0
for mod, pref, novo in ITENS:
    ls = idx.get(mod, [])
    if len(ls) != 1: avisos.append(f'{mod}: {len(ls)} linhas'); continue
    r = ls[0]; c = r_.cell(r, 3).value or ''
    if c == novo: avisos.append(f'{mod}: já estava'); continue
    if not c.startswith(pref): avisos.append(f'{mod}: C atual não começa com {pref}: {c}'); continue
    r_.cell(r, 3).value = novo; esperadas.append(f'C{r}'); n += 1
lm = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == 'a.b.art']
assert len(lm) == 1, lm; lm = lm[0]
if n:
    m.cell(lm, 13).value = (m.cell(lm, 13).value or '') + (f' | Fotos (pedido do usuário, 20/11/2026): {n} linhas da aba Relógios tiveram o link da página trocado pelo endereço direto da foto (loja oficial abartwatches.com, via products.json, e justwatchme.net).')
wb.save(SAI)
depois = snap(openpyxl.load_workbook(SAI))
mud = {t: sorted(k for k in set(antes[t]) | set(depois[t]) if antes[t].get(k) != depois[t].get(k)) for t in antes}
print('trocadas:', n, '| avisos:', avisos)
ok = sorted(mud['Relógios']) == sorted(esperadas) and mud['Marcas'] == ([f'M{lm}'] if n else []) and all(not v for t, v in mud.items() if t not in ('Relógios', 'Marcas'))
print('RESULTADO:', 'OK' if ok else 'FALHOU', {t: len(v) for t, v in mud.items()})
