#!/usr/bin/env python3
"""PASSADA ÚNICA (pedido do usuário, 22/11/2026): escolhe o lote da execução, de cima para baixo
da aba Marcas, juntando o que falta em cada marca — dados da aba Marcas (B a K) e modelos da aba Relógios.

Uso:
  python3 proxima_completa.py planilha/Relogios_atualizada_NNN.xlsx [saida=/home/claude/trab]
      -> grava <saida>/plano.json e <saida>/grupo1.json ... (5 marcas "só dados" por grupo) e imprime o lote
  python3 proxima_completa.py --registrar VERSAO [--lote lote_NNN.json] ["Marca A" "Marca B" ...]
      -> anota em passada_unica/feitas.json as marcas já tratadas nesta passada (as do lote e/ou as citadas)

Para cada marca, de cima para baixo:
  - dados e modelos feitos                      -> PULA
  - falta algum dado (B a K vazio), modelos ok  -> "so_dados": preencher os dados (uma tentativa nesta passada)
  - dados ok, sem modelos                       -> "modelos": pesquisar os relógios
  - falta dado e não tem modelos                -> "modelos" com "falta": fazer tudo na mesma pesquisa
"Tem modelos" = o nome aparece na aba Relógios (mesma regra, APELIDOS, PESQUISAR_MESMO_ASSIM e ADIADAS do
proxima_marca.py). Marca em ADIADAS não entra para modelos (só para os dados que faltarem).
Marca já anotada em passada_unica/feitas.json não volta para os dados (evita repetir para sempre a
mesma busca sem resultado); para tentar de novo, tirar o nome desse arquivo.

Tamanho do lote = orçamento de buscas da execução (~200 WebSearch somadas com os ajudantes):
marca "só dados" custa 4, marca com modelos custa 45; o lote é o trecho contínuo, de cima para baixo,
que cabe em 200, com no máximo 3 marcas de modelos (ex.: 50 só dados; ou 3 de modelos + 16 só dados).
"""
import sys, os, json, collections, datetime
import openpyxl
from proxima_marca import APELIDOS, PESQUISAR_MESMO_ASSIM, ADIADAS, chave

AQUI = os.path.dirname(os.path.abspath(__file__))
FEITAS = os.path.join(AQUI, 'passada_unica', 'feitas.json')
L = 'ABCDEFGHIJKLM'
ORCAMENTO, CUSTO_DADOS, CUSTO_MODELOS, MAX_MODELOS = 200, 4, 45, 3
vazio = lambda v: v is None or str(v).strip() in ('', '-', '—', 'n/a')


def ler_feitas():
    return json.load(open(FEITAS, encoding='utf-8')) if os.path.exists(FEITAS) else {}


def pendentes(arq):
    wb = openpyxl.load_workbook(arq, read_only=True)
    rel = collections.Counter(
        chave(r[0]) for r in wb['Relógios'].iter_rows(min_row=2, max_col=1, values_only=True) if r[0])
    feitas = ler_feitas()
    out = []
    for i, r in enumerate(wb['Marcas'].iter_rows(min_row=2, max_col=13, values_only=True), start=2):
        m = r[0]
        if not m:
            continue
        tem = rel[chave(APELIDOS.get(m, m))] > 0
        modelos = m not in ADIADAS and (not tem or (m in PESQUISAR_MESMO_ASSIM and m not in feitas))
        falta = [] if m in feitas else [L[j] for j in range(1, 11) if vazio(r[j])]
        if modelos or falta:
            out.append({'linha': i, 'marca': m, 'modelos': modelos, 'falta': falta,
                        'tem_relogios': tem, 'adiada_para_modelos': m in ADIADAS,
                        'atual': {L[j]: (str(r[j])[:150] if r[j] is not None else '')
                                  for j in range(11) if L[j] != 'I'}})
    wb.close()
    return out


def escolher(pend):
    lote, gasto, nm = [], 0, 0
    for p in pend:
        custo = CUSTO_MODELOS if p['modelos'] else CUSTO_DADOS
        if gasto + custo > ORCAMENTO or (p['modelos'] and nm == MAX_MODELOS):
            break
        lote.append(p); gasto += custo; nm += p['modelos']
    return lote


def registrar(args):
    versao = int(args[0]); nomes = []; k = 1
    while k < len(args):
        if args[k] == '--lote':
            nomes += list((json.load(open(args[k + 1], encoding='utf-8')).get('celulas') or {}).keys()); k += 2
        else:
            nomes.append(args[k]); k += 1
    f = ler_feitas(); hoje = datetime.date.today().isoformat()
    for n in nomes:
        f[n] = {'data': hoje, 'versao': versao}
    os.makedirs(os.path.dirname(FEITAS), exist_ok=True)
    json.dump(f, open(FEITAS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
    print(f'registradas {len(nomes)} marcas (v{versao}); total em feitas.json: {len(f)}')


def main():
    if sys.argv[1] == '--registrar':
        return registrar(sys.argv[2:])
    arq = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/trab'
    pend = pendentes(arq)
    lote = escolher(pend)
    mod = [p for p in lote if p['modelos']]
    dad = [p for p in lote if not p['modelos']]
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.startswith('grupo') and f.endswith('.json'):
            os.remove(os.path.join(out, f))
    for g in range(0, len(dad), 5):
        grp = [{'linha': p['linha'], 'marca': p['marca'], 'falta': p['falta'], 'atual': p['atual']} for p in dad[g:g + 5]]
        json.dump(grp, open(f'{out}/grupo{g // 5 + 1}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    restam = {'marcas_pendentes': len(pend), 'com_modelos_a_fazer': sum(p['modelos'] for p in pend),
              'so_dados': sum(not p['modelos'] for p in pend)}
    json.dump({'planilha': os.path.basename(arq), 'modelos': mod, 'so_dados': dad, 'restam_antes_deste_lote': restam},
              open(f'{out}/plano.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"marcas pendentes: {restam['marcas_pendentes']} (com modelos a fazer: {restam['com_modelos_a_fazer']}; "
          f"só dados: {restam['so_dados']})")
    print(f'lote desta execução: {len(mod)} com modelos + {len(dad)} só dados '
          f'({(len(dad) + 4) // 5} grupos de ajudantes) -> {out}/plano.json')
    for p in lote:
        tipo = 'MODELOS' + (' + dados ' + ''.join(p['falta']) if p['falta'] else '') if p['modelos'] \
            else 'só dados ' + ''.join(p['falta'])
        print(p['linha'], p['marca'], '|', tipo)


if __name__ == '__main__':
    main()
