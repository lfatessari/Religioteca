import sys, copy, openpyxl
ENT, SAI = sys.argv[1:3]
def snap(wb):
    return {ws.title: {c.coordinate: c.value for c in ws._cells.values() if c.value is not None} for ws in wb.worksheets}
wb = openpyxl.load_workbook(ENT); antes = snap(wb); m = wb['Marcas']; w = wb['Relógios']
lin = [r for r in range(2, m.max_row + 1) if m.cell(r, 1).value == 'ADPT']; assert len(lin) == 1; r = lin[0]
assert m.cell(r, 3).value == '-' and m.cell(r, 7).value == 'ADPTGoods.com'
m.cell(r, 3).value = 'Nova York (Brooklyn)'
m.cell(r, 4).value = ('Marca outdoor criada pela equipe da Worn & Wound: começou com pulseiras de nylon feitas nos EUA e lançou relógios coloridos '
    'de titânio, 38 mm e 200 m, com movimento automático Seiko')
m.cell(r, 6).value = 2600
m.cell(r, 7).value = 'adptgoods.com'
m.cell(r, 9).value = ('ADPT (pronuncia-se "adapt", sigla de All Day, Purpose and Terrain) nasceu em 2017 dentro da Worn & Wound, em Nova York, '
    'como uma pulseira de nylon no estilo militar feita inteiramente nos EUA. A linha cresceu para pulseiras, bolsas e acessórios de EDC e, '
    'em setembro de 2022, estreou nos relógios com o Series 1, desenvolvido com a BOLDR: caixa de titânio de 38 mm, Seiko NH35, safira, '
    '200 m e luneta de 12 horas, em quatro cores (Petrol, Carbon, Harvest e Terra). Em 2023 fez com a VERO o Workhorse Limited Edition, '
    'cronógrafo a quartzo de 100 peças, e em março de 2024 lançou o Series 1 Dual-Time, com Seiko NH34 (ponteiro de 24 horas) e luneta com '
    'pontos cardeais, nas cores Aqua Berry e Mossy Shale. A marca é vendida pela Windup Watch Shop, loja da Worn & Wound com showroom em Brooklyn.')
m.cell(r, 10).value = ('Series 1 (Petrol, Carbon, Harvest, Terra; 2022) — titânio 38 mm, Seiko NH35, 200 m, US$ 449\n\n'
    'Series 1 Dual-Time (Aqua Berry, Mossy Shale; 2024) — Seiko NH34 com 24 h, luneta-bússola, US$ 499\n\n'
    'VERO x ADPT Workhorse Limited Edition (2023) — cronógrafo a quartzo, 100 peças, US$ 499')
c = m.cell(r, 13)
c.value = ('Passada a limpo a pedido do usuário em 07/11/2026: C "-" -> Nova York (Brooklyn) (showroom da Windup/Worn & Wound em 540 President St, '
    'Brooklyn; o logo do Instagram diz New York City); G ADPTGoods.com -> adptgoods.com (hoje redireciona para windupwatchshop.com/collections/adpt; '
    'o link do Instagram também leva à Windup); D, I e J reescritos (I tinha restos de citação copiados da web e "titaniumado"; D dizia NH34 para '
    'toda a linha, mas o Series 1 usa NH35); F preenchido (média US$ 449–499 ≈ R$ 2.600). H @adptgoods confirmado. Sem modelos novos: '
    'os relógios estão esgotados na loja e o último post do Instagram é de jun/2024. Relógios: códigos e fotos oficiais da Windup, E preenchido.')
c._style = copy.copy(m.cell(r, 11)._style)

S1 = ('Caixa de titânio de 38 mm (44 mm de ponta a ponta, 13,5 mm), Seiko NH35A automático, safira, 200 m, coroa de rosca, luneta bidirecional '
      'de 12 horas com atrito, ponteiros e índices com lume; desenvolvido com a BOLDR; US$ 449 (lançado em set/2022); ')
DT = ('Seiko NH34 automático com ponteiro de 24 horas independente (segundo fuso ou bússola), luneta unidirecional de 120 cliques com minutos, '
      'pontos cardeais e dia/noite, titânio de 38 mm (38,5 mm na luneta, 44 mm de ponta a ponta, 13,6 mm), safira, 200 m; US$ 499 (lançado em mar/2024); ')
CDN = 'https://cdn.shopify.com/s/files/1/0014/6158/3938/'
novo = {
 'Series 1 Petrol - ADPT-A': ('Series 1 Petrol - ADPT-A', CDN+'products/Adpt_watch_blue_index_TERRAZ.jpg', S1+'tons de azul com fundo esverdeado, titânio escovado, pulseira Paprika'),
 'Series 1 Carbon - ADPT-C': ('Series 1 Carbon - ADPT-C', CDN+'products/Adpt_watch_grey_index_TERRAZ.jpg', S1+'cinzas, pretos e azul, luneta e coroa com PVD preto, pulseira Navy Blue'),
 'Series 1 Harvest - ADPT-B': ('Series 1 Harvest - ADPT-B', CDN+'products/Adpt_watch_khaki_index_TERRAZ.jpg', S1+'mostrador creme com verdes, cáqui e laranja, caixa com PVD gunmetal, pulseira Coyote'),
 'Series 1 Terra': ('Series 1 Terra - ADPT-D', CDN+'products/Adpt_watch_pink_index_TERRAZ.jpg', S1+'laranja, azul, branco e cinza, titânio escovado sem revestimento, pulseira Rust'),
 'Series 1 Dual-Time Aqua Berry - ADPT-DT-AB': ('Series 1 Dual-Time Aqua Berry - ADPT-DT-AB', CDN+'files/ADPT_S1_DT_AQUABERRY_INDEX1.jpg', DT+'versão Aqua Berry'),
 'Series 1 Dual-Time Mossy Shale - ADPT-DT-MS': ('Series 1 Dual-Time Mossy Shale - ADPT-MS-DT', CDN+'files/ADPT_S1_DT_MOSSYSHALE_INDEX.jpg', DT+'versão Mossy Shale'),
 'VERO x ADPT Workhorse Limited Edition': ('VERO x ADPT Workhorse Limited Edition (100 peças)', CDN+'files/Vero_WW_LE_Index_V3.jpg',
   'Colaboração com a VERO: cronógrafo a quartzo Miyota 6S21 (a loja escreve 62S1), 44,5 mm x 49,5 mm x 15,5 mm, caixa com Cerakote azul-água '
   'com pintas brancas, coroa à esquerda, luneta interna, mostrador azul-água com fúcsia e amarelo, 120 m; 100 peças, US$ 499 (jun/2023)'),
}
feitas = {}
for rr in range(2, w.max_row + 1):
    if w.cell(rr, 1).value != 'ADPT': continue
    b = w.cell(rr, 2).value
    assert b in novo, b
    nb, img, e = novo[b]
    w.cell(rr, 2).value = nb
    cc = w.cell(rr, 3); cc.value = img; cc.hyperlink = img
    ce = w.cell(rr, 5); ce.value = e; ce._style = copy.copy(w.cell(rr, 2)._style)
    feitas[b] = rr
assert set(feitas) == set(novo), set(novo) - set(feitas)
wb.save(SAI)
wb2 = openpyxl.load_workbook(SAI); depois = snap(wb2)
mud = {t: sorted(k for k in set(antes[t]) | set(depois[t]) if antes[t].get(k) != depois[t].get(k)) for t in antes}
perm_m = {f'{L}{r}' for L in 'CDFGIJM'}
perm_r = {f'{L}{x}' for x in feitas.values() for L in 'BCE'}
fora = [k for k in mud['Marcas'] if k not in perm_m] + [k for k in mud['Relógios'] if k not in perm_r] + [k for t in mud if t not in ('Marcas', 'Relógios') for k in mud[t]]
w2 = wb2['Relógios']
ruins = [x for x in feitas.values() if not w2.cell(x, 3).hyperlink or w2.cell(x, 3).hyperlink.target != w2.cell(x, 3).value]
print('Marcas:', mud['Marcas']); print('Relógios:', mud['Relógios'])
print('linhas ADPT:', sorted(feitas.values()), '| fora do permitido:', fora, '| hyperlinks ruins:', ruins)
print('RESULTADO:', 'OK' if not fora and not ruins else 'FALHOU')
