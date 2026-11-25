import sys, openpyxl
ENT, SAI = sys.argv[1:3]
I_AEG = ("A Aegaon nasceu em 2012, na Estônia, criada por Janno Roodi, Kristjan Rabi e Veljo Viikant. Roodi é quem desenha os relógios, e foi ele quem chamou o amigo Rabi para cuidar do negócio. O primeiro modelo foi o Peacemaker 65, com caixa de 65 mm, e a empresa AegaOn OÜ foi registrada em Tallinn em 2015."
"\n\nA proposta nunca foi vender tradição relojoeira: a marca faz relógios grandes e chamativos, de desenho \"forte, simples e marcante\", e leva essa mesma linguagem aos modelos femininos, só mudando o tamanho. Há relógios a quartzo, como o Tabula Rasa, com movimento suíço Ronda; mecânicos de corda manual, como o Peacemaker; e automáticos, como o Tenet 48 e o Temptation III GMT."
"\n\nNos últimos anos vieram as edições especiais: o Tabula Rasa feito em parceria com o time de basquete BC Kalev/Cramo, em dezembro de 2025; a série Ilmarine, limitada a 300 peças e dedicada aos 108 anos da Estônia, em fevereiro de 2026; e o Tabula Rasa 44 Anniversary, de agosto de 2026, que celebra os 12 anos do desenho. A marca tem loja própria em Tallinn, na borda da Cidade Velha.")
M_AEG = "I igual à história do post publicado em 25/11/2026 (instagram.com/p/DgLfoMJFsyy). Os dois primeiros parágrafos reescrevem a I anterior com os mesmos fatos e fontes já listados nesta M (site oficial, página About; Kaminsky; New Labels Only; registro comercial ariregister.rik.ee; revista Time Flies, 2018). O terceiro parágrafo é novo e vem do blog oficial (aegaon.com/blogs/news): parceria com o BC Kalev/Cramo em dezembro de 2025; 'new-aegaon-watch-design-dedicated-to-estonia-s-108th-anniversary', publicado em 04/02/2026 (série Ilmarine, 300 peças); Tabula Rasa 44 Anniversary lançado em agosto de 2026 pelos 12 anos do desenho (linhas da Aegaon na aba Relógios). Loja na borda da Cidade Velha: Time Flies (2018); endereço Rotermanni 7 no FAQ oficial."
K_ADV = "https://iqqobdhdaiavmynhkwop.supabase.co/storage/v1/object/public/brand-logos/8399cb05-6158-4752-beb8-a11a7036b429-atlas-approved-20261005-ce5e3489b364.png"
M_ADV = ("K trocado em 25/11/2026 a pedido do usuário: o valor anterior (Screenshot_36.png) era um print do mostrador do Protégé, não o logo. O site advisorwatches.com não publica arquivo de logo (o cabeçalho mostra o nome em texto); o logo novo é o símbolo oficial da marca publicado na ficha do Microbrand Atlas (microbrandatlas.com/brand/advisor-watch-company). O post de 25/11/2026 usou na capa o logo completo (símbolo + ADVISOR) tirado da foto de perfil do Instagram @advisorwatches, que não tem endereço fixo."
 " | Aba Relógios (v883, pedido do usuário de 25/11/2026): a linha \"SUPA Diver Commando\" passou a se chamar \"SUPA Diver Bronze \"Commando\" – edição limitada\" (mesmo padrão das outras versões da campanha Makuake); as outras colunas não mudaram. Ainda a verificar: a foto dessa linha (img4.gemlis.com/…1755204842117347.jpg) não pôde ser conferida nesta execução (a leitura automática recusou o endereço e o Firecrawl estava sem créditos), por isso foi mantida; e não se confirmou se o \"Ascent Classic SteelWhite Automatic\" é o Ascent de mostrador prata e couro marrom do post (a página da Touch of Modern não abriu e as buscas não trouxeram nada), por isso nada mudou nessa linha.")
NOVO_NOME = 'SUPA Diver Bronze "Commando" – edição limitada'
def snap(wb):
    return {ws.title: {c.coordinate: c.value for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb = openpyxl.load_workbook(ENT); antes = snap(wb)
m = wb['Marcas']; r_ = wb['Relógios']
def linha(nome):
    l = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == nome]; assert len(l) == 1, (nome, l); return l[0]
esp = []
la = linha('Aegaon'); lv = linha('Advisor Watch Company')
if m.cell(la, 9).value != I_AEG:
    m.cell(la, 9).value = I_AEG; m.cell(la, 13).value = (m.cell(la, 13).value or '') + ' | Atualizado a partir do post publicado em 25/11/2026: ' + M_AEG; esp += [f'I{la}', f'M{la}']
if m.cell(lv, 11).value != K_ADV:
    m.cell(lv, 11).value = K_ADV; esp.append(f'K{lv}')
rs = [r for r in range(1, r_.max_row + 1) if r_.cell(r, 1).value == 'Advisor Watch Company' and r_.cell(r, 2).value == 'SUPA Diver Commando']
if rs:
    assert len(rs) == 1; r_.cell(rs[0], 2).value = NOVO_NOME; esp.append(f'B{rs[0]}')
if esp:
    m.cell(lv, 13).value = (m.cell(lv, 13).value or '') + ' | Atualizado a partir do post publicado em 25/11/2026: ' + M_ADV; esp.append(f'M{lv}')
wb.save(SAI)
dep = snap(openpyxl.load_workbook(SAI))
mud = sorted(k for t in antes for k in (set(antes[t]) | set(dep[t])) if antes[t].get(k) != dep[t].get(k))
print('mudadas:', mud, 'esperadas:', sorted(set(esp)))
print('RESULTADO:', 'OK' if mud == sorted(set(esp)) else 'FALHOU')
