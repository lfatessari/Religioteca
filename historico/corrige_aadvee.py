import openpyxl, copy, sys
E, S = 'Relogios_atualizada_506.xlsx', 'Relogios_atualizada_507.xlsx'
wb = openpyxl.load_workbook(E)
m, r = wb['Marcas'], wb['Relógios']
assert m['A13'].value == 'Aadvee'
assert r['B87235'].value == 'Pioneer – Violet - AA-01' and r['B87236'].value == 'Pioneer – Purple - AA-01'
base = 'Mesma base do AA-01 (aço 316L, 45 mm, Miyota 9015, 50 m, safira dos dois lados, rotor personalizado). '
r['B87235'] = 'Pioneer – Purple - AA-01'
r['E87235'] = base + 'Versão roxa (Purple). O site oficial chama esta peça de "violet" na legenda da foto ("The violet AADVEE watch"), mas no Instagram a marca separa o roxo ("A little purple power to every hour!") do Violet Plum, um tom vinho ("Two watches, two moods. Violet or purple"). Lançado em 2023; o site diz "Not available" (esgotado/descontinuado). Preço não publicado.'
r['B87236'] = 'Pioneer – Violet Plum - AA-01'
r['C87236'] = 'https://www.instagram.com/p/DAqq70MoGlq/'
r['C87236'].hyperlink = 'https://www.instagram.com/p/DAqq70MoGlq/'
r['E87236'] = base + 'Versão Violet Plum, mostrador em tom vinho com pulseira de couro marrom, apresentada pela marca no Instagram ("Giving a Violet Plum vibe", "Some Violet Plum content for you all to enjoy"). Foto: link do post da marca no Instagram (página, não imagem). Lançado em 2023; esgotado/descontinuado. Preço não publicado.'
I = m['I13'].value
assert I.startswith('A AADVEE nasceu de uma herança.')
m['I13'] = 'O nome vem do sânscrito: segundo a marca, AADVEE se inspira na palavra Advaiya, que significa "único". ' + I
J = m['J13'].value
m['J13'] = J.replace('violeta, roxo e verde-limão', 'roxo, Violet Plum (vinho) e verde-limão')
m['M13'] = m['M13'].value + ' Correção em 08/11/2026 (v507), ao montar o post: as linhas "Violet" e "Purple" eram a mesma cor (roxo); a segunda virou "Violet Plum" (tom vinho, posts DAqq70MoGlq e DBv-ZqCI02_ do Instagram). I: origem do nome (post de 12/11/2023: "Our name Aadvee is inspired by the Sanskrit word Advaiya which means unique").'
wb.save(S)
del wb
A = openpyxl.load_workbook(E); B = openpyxl.load_workbook(S)
mud = []
for t in A.sheetnames:
    a = {c.coordinate: (c.value, c.hyperlink.target if c.hyperlink else None) for c in A[t]._cells.values()}
    b = {c.coordinate: (c.value, c.hyperlink.target if c.hyperlink else None) for c in B[t]._cells.values()}
    for k in set(a) | set(b):
        if a.get(k, (None, None)) != b.get(k, (None, None)): mud.append((t, k))
print(sorted(mud))
esperado = {('Relógios', x) for x in ['B87235', 'E87235', 'B87236', 'C87236', 'E87236']} | {('Marcas', x) for x in ['I13', 'J13', 'M13']}
ok = set(mud) == esperado
print('J13 mudou:', ('Marcas','J13') in mud)
print('RESULTADO:', 'OK' if ok else 'FALHOU')
sys.exit(0 if ok else 1)
