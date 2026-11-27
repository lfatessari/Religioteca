import sys, openpyxl, time, copy
ENT, SAI = sys.argv[1:3]
t0=time.time(); d='26/11/2026'; P=' | Atualizado a partir do post publicado em '+d+': '
AEON_I=("A Aeon Watches nasceu em Seattle, no noroeste dos Estados Unidos, pelas mãos de Azhan Zaheer e Brayden Brackett — dois amigos que se apresentam, antes de tudo, como entusiastas de relógios. Registrada como Aeon Watches LLC, a marca partiu de uma ideia simples: fazer relógios mecânicos automáticos sólidos, bem construídos e a um preço que caiba no bolso de quem está começando a colecionar."
"\n\nO resultado é a linha Pioneer, que tem como assinatura uma pequena janela no mostrador que deixa o balanço à mostra — dá para ver o \"coração\" do relógio batendo enquanto ele marca as horas. Por enquanto são duas versões: a Cascade, de mostrador azul, e a Evergreen, de mostrador verde — ambas com o mesmo DNA que a marca resume como \"nascido no Pacífico Noroeste\".")
M42=("H: @theaeonwatches é de OUTRA marca, a AEON brasileira (theaeonwatches.com, rodapé '© 2026 Aeon Watches · Brasil', Coleção Origin Swiss Made de 150 peças, calibre Sellita SW300-1), não da Aeon Watches LLC de Seattle. A Aeon de Seattle não tem Instagram: o site aeon-watches.com não liga redes sociais e as buscas não acharam perfil. Conferido em 26/11/2026 na conversa do post; o post publicado saiu com '📸 -'. A AEON brasileira ainda não tem linha própria na aba Marcas (decisão do usuário pendente; NÃO criar a linha).")
M43=("I igual à história do post publicado em 26/11/2026 (instagram.com/p/DgOb10LkYPA). Fontes: site oficial aeon-watches.com (home: 'Seattle-designed', 'Born in the Pacific Northwest'; our-world: fundadores Azhan Zaheer e Brayden Brackett; watches: Pioneer - Cascade e Pioneer - Evergreen, US$ 250 cada, no site desde 02/01/2024, editados em 27/08/2026 e à venda em 26/11/2026). Ano de fundação continua a confirmar (rodapé '2023 – Aeon Watches LLC'), por isso fica fora do texto.")
AERA_I=("A ideia da Aera nasceu em Genebra, em janeiro de 2018, quando um pequeno grupo de pessoas de diferentes áreas da relojoaria se reuniu para discutir o que faz um bom relógio; a marca só foi lançada em julho de 2022. À frente estão o britânico Jas Minhas, filho de um imigrante indiano que consertava relógios e teve uma relojoaria em Birmingham, e que antes ajudou a lançar a Jawbone no Vale do Silício, e o sueco Olof Larsson, herdeiro da varejista Nymans Ur, fundada por seu pai, Göran."
"\n\nCom o lema \"Swiss made, British design\", a Aera estreou com o D-1 Diver e o P-1 Pilot, em séries limitadas de 300 peças, com caixa em aço 904L, movimento Sellita SW200-1 e lume Super-LumiNova da RC Tritec. Depois vieram o M-1, de campo, e o C-1, o primeiro cronógrafo da marca. Os fundadores miram a faixa de 1.000 a 3.000 euros, com vendas sobretudo pela internet."
"\n\nNos últimos anos vieram as parcerias: o C-1 Rennsport, em 25 unidades, com a Rennsport, especialista em restaurar o Porsche 911; o D-1 Diver nas versões Blackout e Whiteout, com a Todd Snyder; e o M-1 Krons, de corda manual e 25 peças numeradas, feito com a Krons, relojoaria de Estocolmo que foi a primeira parceira de varejo da Aera.")
M44=("I igual à história do post publicado em 26/11/2026 (instagram.com/p/DgOcjSsEe5L): mesmos fatos dos dois parágrafos antigos (fontes já listadas acima) e um 3º parágrafo novo com as parcerias, pelas páginas de produto e de imprensa do site oficial aera.co vistas em 26/11/2026 (C-1 Rennsport, 25 unidades, com a Rennsport; D-1 Diver Blackout e Whiteout com a Todd Snyder; M-1 Krons, corda manual, 25 peças numeradas, com a Krons de Estocolmo, primeira parceira de varejo). B continua 'Suíça/Reino Unido' e C 'Genebra' (o post saiu assim); a sede registrada no Reino Unido segue anotada acima.")
M45=("Relógios M-1 Krons e C-1 Rennsport incluídos a partir do post publicado em 26/11/2026 (instagram.com/p/DgOcjSsEe5L). Fotos de C-1 Shadow, C-1 Cloud, M-1 Field e M-1 Blackbird trocadas (eram links de página) pelas fotos oficiais de produto usadas no post (cdn.shopify.com da Aera). Nesta execução (v913) não foi possível testar se as 6 fotos abrem: a rede da execução bloqueia cdn.shopify.com, a leitura automática recusou os endereços e o Firecrawl estava sem créditos; gravadas por serem as fotos do post aprovado. C-1 Rennsport conferido na ficha da MR PORTER (42 mm, 15,75 mm, Sellita SW510 BH, 56 h, 10 bar, 904L, 25 peças, US$ 3.400); o site oficial aera.co recusou a leitura (PROVENANCE_REQUIRED). M-1 Krons: dados só do post (página oficial não pôde ser aberta).")
B='https://cdn.shopify.com/s/files/1/0447/4755/4974/files/'
FOTOS={'C-1 Shadow':B+'Catalogue-Primary-Straps_4000px_Shadow_ed0fefca-3cf8-4b8c-bd3d-d4921984ed41.jpg',
'C-1 Cloud':B+'Catalogue-Primary-Straps_4000px_Cloud_bd053064-cb07-412e-b39f-65a5e60ce2bc.jpg',
'M-1 Field':B+'Catalogue-Primary-Straps_4000px_Field.jpg','M-1 Blackbird':B+'Catalogue-Primary-Straps_4000px_Blackbird.jpg'}
NOVOS=[('M-1 Krons - Limited Edition',B+'Catalogue-Front-Primary-4000px-Krons.jpg',"Edição limitada de 25 peças numeradas feita com a Krons (relojoaria de Estocolmo, primeira parceira de varejo da Aera). Corda manual, mostrador cinza com pequenos segundos, pulseira de couro marrom. [⚠️ a confirmar: medidas, calibre e preço — a página oficial não pôde ser aberta na v913]"),
('C-1 Rennsport - Limited Edition',B+'Catalogue-Primary-Straps_4000px_Rennsport.jpg',"Cronógrafo C-1 em edição de 25 unidades com a Rennsport, especialista em restaurar o Porsche 911. Caixa de aço 904L de 42 mm (15,75 mm de espessura, entre-alças 22 mm), safira, fundo transparente; Sellita SW510 BH automático (27 rubis, 28.800 alt/h, 56 h de reserva); mostrador preto com dois subcontadores e Super-LumiNova; pulseira de couro preto; 10 bar; US$ 3.400 (ficha da MR PORTER).")]
def snapro(p):
    wb=openpyxl.load_workbook(p,read_only=True)
    mar=[list(r) for r in wb['Marcas'].iter_rows(min_row=1,max_col=13,values_only=True)]
    rel=[list(r) for r in wb['Relógios'].iter_rows(min_row=1,max_col=5,values_only=True)]
    wb.close(); return mar,rel
mar0,rel0=snapro(ENT)
wb=openpyxl.load_workbook(ENT); m=wb['Marcas']; w=wb['Relógios']; print('load',round(time.time()-t0),flush=True)
def lin(n):
    l=[c.row for c in m._cells.values() if c.column==1 and c.value==n]; assert len(l)==1,n; return l[0]
la=lin('Aeon Watches'); lr=lin('Aera')
m.cell(la,8).value='-'; m.cell(la,9).value=AEON_I
m.cell(la,13).value=(m.cell(la,13).value or '')+P+M42+P+M43
m.cell(lr,9).value=AERA_I
m.cell(lr,13).value=(m.cell(lr,13).value or '')+P+M44+P+M45
rows=sorted(c.row for c in w._cells.values() if c.column==1 and c.value=='Aera')
nomes={w.cell(r,2).value:r for r in rows}
for n,f in FOTOS.items():
    r=nomes[n]; w.cell(r,3).value=f; w.cell(r,3).hyperlink=f
last=rows[-1]; k=len(NOVOS)
for key in sorted((x for x in w._cells if x[0]>last), reverse=True):
    cell=w._cells.pop(key); cell.row=key[0]+k; w._cells[(key[0]+k,key[1])]=cell
for i,(nome,foto,car) in enumerate(NOVOS,1):
    r=last+i
    for col in range(1,6):
        c=w.cell(r,col); c._style=copy.copy(w.cell(last,col)._style)
    w.cell(r,1).value='Aera'; w.cell(r,2).value=nome; w.cell(r,3).value=foto; w.cell(r,3).hyperlink=foto; w.cell(r,5).value=car
for c in w._cells.values():
    if c.hyperlink is not None: c.hyperlink.ref=c.coordinate
wb.save(SAI); print('salvo',round(time.time()-t0),flush=True)
del wb,m,w
mar1,rel1=snapro(SAI); ok=True
dif=[(i,j) for i,(a,b) in enumerate(zip(mar0,mar1)) for j in range(13) if a[j]!=b[j]]
print('Marcas difs',dif); ok&= len(mar0)==len(mar1) and set(dif)<={(la-1,7),(la-1,8),(la-1,12),(lr-1,8),(lr-1,12)}
rel1f=rel1[:last]+rel1[last+k:]
ok&= len(rel0)==len(rel1f)
difr=[(i,j) for i,(a,b) in enumerate(zip(rel0,rel1f)) for j in range(5) if a[j]!=b[j]]
print('difs Relógios',difr); ok&= all(rel0[i][0]=='Aera' and j==2 for i,j in difr) and len(difr)==4
print('novas',rel1[last:last+k])
print('Aera agora:',sum(1 for r in rel1 if r[0]=='Aera'))
print('RESULTADO:','OK' if ok else 'FALHOU',round(time.time()-t0))
