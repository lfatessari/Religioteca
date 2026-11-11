# -*- coding: utf-8 -*-
"""Lote 12 (11/11/2026): as 8 marcas do Microbrand Atlas cuja ficha não abre. Dados pesquisados FORA do Atlas
(buscas na web, sites oficiais, revendedores e imprensa). Sem história."""
import sys
import lote_base
from lote_base import add, salvar, M

def fora(fontes):
    """Troca na coluna M o texto-padrão 'ficha do Atlas' pelo de pesquisa externa."""
    m = M[-1]["M"]
    ini = m.index("Dados da ficha do Atlas"); fim = m.index(" Fundação:")
    m = m[:ini] + "A ficha do Atlas não abre; dados pesquisados fora do Atlas em 11/11/2026. Fontes: " + fontes + "." + m[fim:]
    for a, b in (("não informada no Atlas", "não encontrada"), ("não informado no Atlas", "não encontrado"),
                 ("média dos preços de referência do Atlas convertidos", "média dos preços encontrados nas fontes, convertidos"),
                 ("o Atlas não traz preços confiáveis", "preço não encontrado")):
        m = m.replace(a, b)
    M[-1]["M"] = m

add("M2Z Watch", "-", "Itália", None, None, None, "Relógios de mergulho de desenho italiano com caixa monobloco de aço 316L (200 m) e automático Seiko NH35.", None, None,
    "Diver 200 Automatic Rose Gold (M2Z-200-008); U 650; Seiko NH35 | Diver 200 Plated Bracelet Grey (200-004X); G 589; Seiko NH35",
    "Preços de revendedores, não do site oficial (não encontrado): US$ 650 na watches.com (a página também mostra US$ 499,99; rótulos ambíguos) e £589 de tabela na Watches & Crystals. Conferir.")
fora("watches.com (coleção M2Z e ficha do Diver 200) e watchesandcrystals.com")

add("Nadir", "-", "Polônia", None, None, "Bart Maniecki", "Relógios de aventura para uso diário em aço 904L com Miyota 9015.", "nadirwatches.com", None,
    "Vespera (azul, preto, cinza); E 490; Miyota 9015 | Vespera GMT; -; -",
    "Site nadirwatches.com veio só de um agregador (MetropolisWatches), que também dá Varsóvia como sede: conferir os dois. Preço = preço de tabela (€ 490) citado pela Serious Watches.")
fora("resenha da WatchBandit, entrevista com o fundador no WatchCrunch, Serious Watches e Trusted Shops")

add("Proxima", "-", "China", None, 2016, None, "Relógios de mergulho chineses de estilo homenagem com NH35, PT5000 e Miyota 9015.", None, None,
    "MM300; U 195; - | MM300 Uni-Dive; U 230; - | Samurai; U 215; - | Bronze 65 PX01 Black Dial; U 279; - | Black 65; U 229; - | PX1697; -; PT5000 | PX1752; -; Miyota 9015 | PX1719 GMT; -; NH34",
    "Ano de fundação (2016) segundo a WatchPatrol: conferir. Preços do revendedor WR Watches. A marca vende por loja própria no AliExpress; site oficial não encontrado.")
fora("WR Watches (revendedor), WatchPatrol, JwlrAddicts e Homage Forum")

add("Radcliffe Watches", "-", "Reino Unido", "Oxford", None, "Tayeb Boussalia", "Relógios de desenho autoral (mostrador em cúpula, turbilhão) com movimentos de base Seiko.", "radcliffewatches.com", None,
    "Signature (2022); G 289; Seiko NH35 | Le Dome Classic; E 620; base Seiko NH38 modificada | REVERSE (edição especial); E 1400; - | REVERSE HARLEQUIN; E 890; - | Le Dome Tourbillon; E 1800; - | MAD WATCH COLLECTOR X RADCLIFFE (relógio de campo); E 299; -",
    "Fundador aparece como Tayeb Boussalia (Trustpilot) e 'Tayeb TBOUSSALIA' (The Watch Gallery): conferir a grafia. Preços em euros do revendedor The Watch Gallery; o Signature é de 2022 (The Time Bum).")
fora("The Time Bum (resenha de 10/02/2022), The Watch Gallery (revendedor) e Trustpilot")

add("Tesse Watches", "-", "Canadá", "Toronto", 2024, "Thomas Brissiaud", "Relógios suíços de desenho autoral em caixa almofada (GMT e três ponteiros).", "tesse-watches.com", "tesse.watches",
    "Michel GMT (5 cores); U 1250; Sellita SW330-2 | The Architect; -; ETA 2892-A2 Elaboré",
    "País: a lista inicial dava Reino Unido, mas as fontes dizem Canadá (Toronto, segundo o Watch Review Blog): conferir. A marca se escreve Tessé. Preço do Michel GMT: 'pouco abaixo de US$ 1.250' no lançamento no Kickstarter.")
fora("entrevista com o fundador no Watch Is This, podcast WatchDNA, Oracle Time, The Calibrated Wrist e Watch Review Blog")

add("The Camden Watch Company", "-", "Reino Unido", "Londres (Camden Town)", 2014, "Anneke Short e Jerome Robert", "Relógios acessíveis desenhados em Camden Town, inspirados no passado industrial e vitoriano de Londres, a quartzo e com um automático suíço.", "camdenwatchcompany.com", None,
    "No.24; G 99; quartzo | No.27 GMT (aço, pulseira preta); G 155; quartzo suíço | No.27 GMT (aço, malha); G 175; quartzo suíço | No.27 GMT (ouro rosa e oxblood); G 165; quartzo suíço | No.274; -; automático suíço | Relógio de bolso (pré-venda, 2026); G 170; -",
    "Outros modelos citados sem preço: No.29, No.88 e No.253. Preços de revendedor (loja do Royal Museums Greenwich) e da imprensa.")
fora("Crave Magazine, Camden Market, The Chap, County Wedding, Shortlist e loja do Royal Museums Greenwich")

add("Wayforth", "-", "Canadá", "Toronto", 2021, "Stephen (sobrenome não informado)", "Relógios de viagem: cronógrafo mecaquartzo com segundo fuso por luneta interna giratória.", "wayforthwatches.com", "wayforthwatches",
    "Voyager Ref. V1.01 a V1.06 (edições limitadas); U 383; Seiko VK64 mecaquartzo",
    "Preço: o site oficial mostra US$ 383 na página da coleção e US$ 373 na inicial. Cidade e ano (Toronto, 2021) segundo The Calibrated Wrist; o site diz só 'Canadá'.")
fora("site oficial wayforthwatches.com, The Calibrated Wrist e Oracle Time")

add("Yelang Watches", "-", "China", None, None, None, "Relógios militares e de mergulho com iluminação por tubos de trítio (T100).", None, None,
    "V1019; U 239; Seiko NH36A | V1029S (cronógrafo); -; quartzo japonês OS00 | V1034; -; automático | V5.1; -; ETA 2836 | V1021 (piloto); -; - | V1215 (solar); -; -",
    "Marca chinesa 野狼 (Yelang). Site oficial não encontrado: vende por lojas próprias no AliExpress, JD.com e Tmall. Único preço confiável é o do V1019 na China Watch Shop.")
fora("China Watch Shop, JwlrAddicts e Desertcart (revendedores)")

salvar(sys.argv[1] if len(sys.argv) > 1 else "lote12.json")
