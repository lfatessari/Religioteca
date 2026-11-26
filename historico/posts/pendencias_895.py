import sys, json, openpyxl, time
ENT, SAI = sys.argv[1:3]
t0=time.time()
MARCA='Aenigma Watches'
I_NEW = ("A Aenigma nasceu em 2022 no Vale de Aosta, a região alpina do noroeste da Itália, aos pés do Monte Branco. É uma microbrand independente, e o nome, palavra latina para \"enigma\", combina com o jeito da casa: os Codex trazem um código gravado na luneta e no anel interno do mostrador."
"\n\nA coleção tem três famílias. A Codex reúne mergulhadores automáticos de 41 mm, com movimento Seiko NH35 e 200 m de resistência; a SubX sobe para 300 m e movimento suíço; e a DressX, da Collezione Italia, tem caixa de 39 mm e corda manual. No DressX Il Santo, um datário \"criptográfico\" revela, dia após dia, uma citação de São Francisco de Assis. Nomes como Defensor Vitae, Human Rights Defender e Planet Defender falam de causas: a vida, os direitos humanos e o planeta."
"\n\nAs edições especiais contam histórias. O SubX Monte Bianco homenageia o Monte Branco e ganhou uma versão de 20 peças com a veneziana Out Of Order; o Operazione Aenigma acompanhou mergulhadores na recuperação de uma máquina Enigma no fundo do mar da Ligúria; e o Codex Mistery Black, feito com a Orafix, é todo preto e brilha em quatro cores no escuro. Em novembro de 2026, a marca fez sua primeira feira em Roma, a Fix Time.")
M40 = "I igual à história do post publicado em 26/11/2026 (instagram.com/p/DgMuuJmFuA3). 2022 e Vale de Aosta: bio do Instagram oficial @aenigma.watches.official ('independent microbrand established in Aosta Valley in 2022'), lida em 25/11/2026. Coleções, medidas, movimentos e resistências: páginas de produto do site oficial aenigma.world (Codex: NH35, 41 mm, 200 m, código na luneta e no rehaut; SubX: 300 m, Sellita SW200; DressX Collezione Italia: 39 mm, corda manual Landeron L210; DressX Il Santo: 'datario crittografico' que revela uma citação de São Francisco de Assis; Defensor Vitae = defesa da vida). Monte Bianco Extreme com a Out Of Order (Veneza), 20 peças: página outoforderwatches.com/pages/ooo-x-aenigma ('Limited Edition 20 pieces') e post do Instagram oficial ('LIMITED EDITION di soli 20 pezzi al mondo'). Operazione Aenigma e a recuperação de uma máquina Enigma dos fundos lígures com a equipe Libeccio Tek Diving: página do produto no site oficial. Codex Mistery Black Aenigma X Orafix, preto fosco, quatro cores de SuperLuminova: página do produto no site oficial. Primeira feira em Roma, Fix Time, nov/2026: post do Instagram oficial de 23/11/2026 ('la primissima fiera capitolina per Aenigma'). Fundadores (Manuel Ferrante e Nicholas Clapasson) continuam fora do texto: sem fonte oficial."
M41 = ("Aba Relógios e F (v895, item 41 das pendências, pedido do usuário de 25/11/2026; dados vistos no site oficial aenigma.world pela conversa do post em 25/11/2026 — nesta execução o site não pôde ser reaberto: a leitura automática recusou os endereços (PROVENANCE_REQUIRED) e o Firecrawl estava sem créditos): "
"removida a linha duplicada 'SubX Operazione Aenigma Essentia (sem referência publicada)' (o site não tem produto separado; 'Essentia' é o título da descrição do produto 41, o SubX Operazione Aenigma); Operazione Aenigma: 40 → 100 peças ('edizione limitata di 100 esemplari' no site), com Sellita SW200, 42 mm, 300 m, safira, BGW9 e a missão com a Libeccio Tek Diving; Monte Bianco Extreme × Out Of Order: 20 peças confirmadas (página da OOO e Instagram oficial), tirada a dúvida 20/30; referências do site: Codex Human Rights Defender CXBN2309, Codex Planet Defender CXVD2307, Codex Defensor Vitae CXNR2305 (antes CVB2201), Codex Planet Defender Blu Oltremare CXBL2301 (antes CPB2301), Codex Mistery Black CXBLKM, SubX Defensor Vitae SUDV2307, SubX Human Rights Defender SRW2301, SubX Planet Defender SPB2301, SubX Monte Bianco SBMB003, SubX Monte Bianco Extreme SBMB001; o site mostra SBOE0120 tanto no Miage quanto no Operazione Aenigma — mantido só no Miage; o Gaius Julius Caesar aparece como 'subxgc' (código interno, não usado). Fotos: trocadas as versões '-large_default.jpg' (800 px) pelas originais do mesmo caminho (2000 × 2000); no Codex Mistery Black, foto 313 (de frente, com bracelete, a do post) no lugar da 304. "
"F: 6342 → 6426. Preços em euro do site oficial: Codex € 490 (4 modelos), Codex Mistery Black € 589, SubX Defensor Vitae / Human Rights Defender / Planet Defender € 980 cada, SubX Monte Bianco € 1.180, SubX Operazione Aenigma € 1.180, SubX Miage € 1.186, SubX Gaius Julius Caesar € 1.190, SubX Monte Bianco Extreme € 1.298, DressX (3 modelos) € 1.480 cada; soma € 15.963 ÷ 16 = € 997,69 × R$ 6,4413 (PTAX venda do euro de 25/11/2026, a última publicada no início desta execução; numerando.com.br/cambio/euro) = R$ 6.426. E continua 3 (5.001–10.000 na Tabela de faixa de preços).")
IMG='https://www.aenigma.world/img/p/'
def img(n): s=str(n); return IMG+'/'.join(s)+'/'+s+'.jpg'
NDEF=" Mergulhador automático Seiko NH35, caixa de aço 316L de 41 mm, 200 m; código pessoal gravado na luneta e no rehaut."
# nome atual -> (novo nome, nova foto, nova E ou None para manter)
R = {
 'Codex Defensor Vitae - CVB2201': ('Codex Defensor Vitae - CXNR2305', img(227), 'Mostrador preto soleil com data às 3.'+NDEF+' Referência antiga na planilha: CVB2201.'),
 'Codex Human Rights Defender (sem referência publicada)': ('Codex Human Rights Defender - CXBN2309', img(231), None),
 'Codex Planet Defender (sem referência publicada)': ('Codex Planet Defender - CXVD2307', img(230), None),
 'Codex Planet Defender Blu Oltremare - CPB2301': ('Codex Planet Defender Blu Oltremare - CXBL2301', img(225), 'Mostrador azul.'+NDEF+' Referência antiga na planilha: CPB2301.'),
 'Codex Mistery Black (sem referência publicada)': ('Codex Mistery Black - CXBLKM', img(313), 'Edição especial, colaboração Aenigma X Orafix (edição limitada). Mostrador preto fosco sem índices, números nem datário; seta dupla das horas (assinatura da Aenigma) e ponteiro de segundos rosa (assinatura da Orafix); quatro cores de SuperLuminova. Seiko NH35 automático (~41 h). Vendido com bracelete de aço ou pulseira de couro, € 589.'),
 'SubX Defensor Vitae (sem referência publicada)': ('SubX Defensor Vitae - SUDV2307', img(251), None),
 'SubX Human Rights Defender (sem referência publicada)': ('SubX Human Rights Defender - SRW2301', img(241), None),
 'SubX Planet Defender (sem referência publicada)': ('SubX Planet Defender - SPB2301', img(283), None),
 'SubX Gaius Julius Caesar – edição limitada de 30 peças (sem referência publicada)': (None, img(191), None),
 'SubX Miage - SBOE0120': (None, img(266), 'Homenagem à geleira do Miage. Sellita SW200 automático, caixa de 42 mm, 12,5 mm, mostrador branco/prata degradê, 300 m. Também aparece com pulseira de tecido cinza (fotos do produto no site oficial).'),
 'SubX Operazione Aenigma – edição limitada de 40 peças (sem referência publicada)': ('SubX Operazione Aenigma – edição limitada de 100 peças (sem referência publicada)', img(255), "Inspirado na recuperação de uma máquina Enigma do fundo do mar da Ligúria, missão com a equipe Libeccio Tek Diving. Sellita SW200 automático, caixa de 42 mm, 300 m (30 ATM), vidro de safira, SuperLuminova BGW9. Edição limitada de 100 exemplares segundo o site oficial ('edizione limitata di 100 esemplari'). Na descrição do produto aparece como 'SUBX Operazione AENIGMA Essentia 300mt'."),
 'SubX Monte Bianco – edição limitada de 30 peças (sem referência publicada)': ('SubX Monte Bianco – edição limitada de 30 peças - SBMB003', img(284), "Homenagem ao Monte Branco. Edição de 30 exemplares segundo o endereço da página oficial. 'Non disponibile' (esgotado) no site oficial em 25/11/2026."),
 'SubX Monte Bianco Extreme – colaboração Out Of Order × Aenigma, edição limitada de 20 peças (sem referência publicada)': ('SubX Monte Bianco Extreme – colaboração Out Of Order × Aenigma, edição limitada de 20 peças - SBMB001', img(285), "Aço 316L com acabamento 'Damaged in Italy' da Out Of Order; mostrador texturizado com o Monte Branco que aparece à noite. 20 peças, confirmadas pela página da Out Of Order ('Limited Edition 20 pieces') e pelo Instagram oficial ('soli 20 pezzi al mondo')."),
 'DressX Il Santo – Collezione Italia - DR01-25': (None, img(219), None),
 'DressX Il Navigatore – Collezione Italia - DR02-25': (None, img(274), None),
 'DressX Il Poeta – Collezione Italia - DR03-25': (None, img(218), None),
}
REMOVER='SubX Operazione Aenigma Essentia (sem referência publicada)'
def snapro(p):
    wb=openpyxl.load_workbook(p,read_only=True)
    mar=[list(r) for r in wb['Marcas'].iter_rows(min_row=1,max_col=13,values_only=True)]
    rel=[list(r) for r in wb['Relógios'].iter_rows(min_row=1,max_col=5,values_only=True)]
    wb.close(); return mar,rel
mar0,rel0=snapro(ENT); print('snap',round(time.time()-t0),flush=True)
wb=openpyxl.load_workbook(ENT); m=wb['Marcas']; w=wb['Relógios']; print('load',round(time.time()-t0),flush=True)
lm=[c.row for c in m._cells.values() if c.column==1 and c.value==MARCA]; assert len(lm)==1; lm=lm[0]
m.cell(lm,9).value=I_NEW; m.cell(lm,6).value=6426; m.cell(lm,5).value=3
d='26/11/2026'
m.cell(lm,13).value=(m.cell(lm,13).value or '')+' | Atualizado a partir do post publicado em '+d+': '+M40+' | Atualizado a partir do post publicado em '+d+': '+M41
rows=sorted(c.row for c in w._cells.values() if c.column==1 and c.value==MARCA)
nomes={w.cell(r,2).value:r for r in rows}
assert set(R)|{REMOVER}==set(nomes), set(nomes)^(set(R)|{REMOVER})
esperado_rel={}
for nome,(nn,foto,e) in R.items():
    r=nomes[nome]
    if nn: w.cell(r,2).value=nn
    w.cell(r,3).value=foto; w.cell(r,3).hyperlink=foto
    if e is not None: w.cell(r,5).value=e
# remover a linha duplicada
z=nomes[REMOVER]
for k in [k for k in w._cells if k[0]==z]: del w._cells[k]
for k in sorted(k for k in w._cells if k[0]>z):
    cell=w._cells.pop(k); cell.row=k[0]-1; w._cells[(k[0]-1,k[1])]=cell
for c in w._cells.values():
    if c.hyperlink is not None: c.hyperlink.ref=c.coordinate
wb.save(SAI); print('salvo',round(time.time()-t0),flush=True)
del wb,m,w
mar1,rel1=snapro(SAI)
ok=True
# Marcas
dif=[(i,j) for i,(a,b) in enumerate(zip(mar0,mar1)) for j in range(13) if a[j]!=b[j]]
print('Marcas linhas',len(mar0),len(mar1),'difs',dif)
ok&= len(mar0)==len(mar1) and set(dif)<= {(lm-1,8),(lm-1,5),(lm-1,12),(lm-1,4)}
# Relógios
rel0f=[r for i,r in enumerate(rel0) if i!=z-1]
print('Relógios linhas',len(rel0),len(rel1))
ok&= len(rel0f)==len(rel1)
difr=[(i,j) for i,(a,b) in enumerate(zip(rel0f,rel1)) for j in range(5) if a[j]!=b[j]]
fora=[x for x in difr if rel1[x[0]][0]!=MARCA]
print('difs Relógios',len(difr),'fora da marca',fora[:5])
ok&= not fora
print('Aenigma agora:',sum(1 for r in rel1 if r[0]==MARCA))
print('RESULTADO:','OK' if ok else 'FALHOU',round(time.time()-t0))
