"""Agrupa os relógios de uma marca por linha (modelo), como nos sites das marcas.

Ex.: Akrone -> "C-02 Nérée", "C-02 Héritage", "C-03 Horizon", "S-05"...

Como funciona, sem depender de lista de linhas:
1. Do nome de cada relógio (coluna B) tira a referência ("... - AKR-C02-NER-ATL"),
   o complemento depois de travessão ("... – edição limitada"), parênteses e medidas ("41 mm").
2. Agrupa pela primeira palavra; o título do grupo é o maior começo comum de todos
   os nomes do grupo (assim "1942 Moon phase" fica inteiro).
3. Grupo grande (10+ relógios) se divide pela palavra seguinte, quando dessa divisão
   saem sublinhas com pelo menos 3 relógios ("C-02" -> "C-02 Nérée"). O que sobra
   fica na linha de cima.
4. Linhas com 1 relógio só vão para "Outros modelos" (quando a marca tem outras linhas).
"""
import re
import unicodedata
from collections import Counter, defaultdict

DIVIDIR_A_PARTIR = 10   # relógios num grupo para tentar dividir em sublinhas
SUBLINHA_MIN = 3        # relógios para uma sublinha existir
LINHA_MIN = 2           # relógios para uma linha ter título próprio
PROFUNDIDADE_MAX = 4    # palavras no título da linha
OUTROS = "Outros modelos"

# palavras que indicam variação (tamanho, mecanismo, público, complicação, cor), não uma linha
VARIANTES = set("""
automatic automatique automatico automatica auto quartz quartzo lady ladies dame dames femme gent gents men mens
women womens homme masculino feminino unissex unisex chrono chronograph chronographe cronografo small medium large
mini midsize petite grande model modelo size gmt moon moonphase phase lune phases regulator regulateur tourbillon
skeleton squelette calendar calendrier calendario perpetual perpetuel date day dual time worldtimer repeater
repetition minute minutes seconds second seconde gold steel titanium titanio ceramic ceramica diamond diamonds
diamants diamantes edition edicao limited limitada special especial black white blue green red silver rose pink
grey gray brown yellow orange purple bicolor new hand handwound manual bracelet strap
selfwinding openworked flying frosted splitseconds full
""".split())
# primeiras palavras genéricas (nomes descritivos, sem linha)
GENERICOS = set("relogio relogios watch watches automatico cronografo calendario modelo modelos pocket bolso".split())


def _norm(w):
    w = unicodedata.normalize("NFKD", w.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", w)


def nome_base(modelo):
    s = str(modelo)
    s = s.split(" - ")[0]
    s = re.split(r"\s[–—]\s", s)[0]
    s = re.sub(r"\([^)]*\)", " ", s)
    s = re.sub(r"\b\d+([.,]\d+)?\s?mm\b", " ", s, flags=re.I)
    s = re.sub(r"\s+", " ", s).strip(" ,;:-–")
    return s or str(modelo).strip()


def _palavras(s):
    return [w for w in s.split() if _norm(w)]


def _variante(w):
    n = _norm(w)
    if n.isdigit():
        v = int(n)
        if len(n) == 4 and 1800 <= v <= 2099:   # ano faz parte do nome ("Family 1881")
            return False
        return len(n) >= 3 or 20 <= v <= 60    # referência ou diâmetro ("Royal Oak 41")
    return n in VARIANTES or w[:1].islower() or bool(re.fullmatch(r"\d+mm", n))


def agrupar(modelos, marca=""):
    """modelos: lista de nomes (coluna B). Devolve lista paralela de títulos de linha."""
    toks = [_palavras(nome_base(m)) for m in modelos]
    mk = [_norm(w) for w in str(marca).split()]
    if mk:   # "Casio Vintage A158" -> agrupa por "Vintage"
        toks = [t[len(mk):] if [_norm(w) for w in t[:len(mk)]] == mk and len(t) > len(mk) else t for t in toks]
    chaves = [[_norm(w) for w in t] for t in toks]
    titulo = [None] * len(modelos)

    def prefixo_comum(idx, d):
        n = d
        while n < PROFUNDIDADE_MAX:
            ws = {tuple(chaves[i][:n + 1]) for i in idx if len(chaves[i]) > n}
            if len(ws) != 1 or any(len(chaves[i]) <= n for i in idx):
                break
            if _variante(toks[idx[0]][n]):
                break
            n += 1
        return n

    def rotulo(idx, n):
        # grafia mais comum entre os relógios do grupo
        c = Counter(" ".join(toks[i][:n]) for i in idx)
        return c.most_common(1)[0][0]

    def resolver(idx, d):
        """idx: relógios que compartilham as d primeiras palavras."""
        n = prefixo_comum(idx, d)
        nome = rotulo(idx, n)
        sub = defaultdict(list)
        resto = []
        for i in idx:
            if len(chaves[i]) > n and not _variante(toks[i][n]):
                sub[chaves[i][n]].append(i)
            else:
                resto.append(i)
        if len(idx) >= DIVIDIR_A_PARTIR and n < PROFUNDIDADE_MAX:
            grandes = [v for v in sub.values() if len(v) >= SUBLINHA_MIN]
            if grandes:
                for v in sub.values():
                    if len(v) >= SUBLINHA_MIN:
                        resolver(v, n + 1)
                    else:
                        resto.extend(v)
                for i in resto:
                    titulo[i] = nome
                return
        for i in idx:
            titulo[i] = nome

    primeiros = defaultdict(list)
    vazios = []
    for i, c in enumerate(chaves):
        (primeiros[c[0]] if c and c[0] not in GENERICOS else vazios).append(i)
    for v in primeiros.values():
        resolver(v, 1)
    for i in vazios:
        titulo[i] = OUTROS

    cont = Counter(titulo)
    if len(cont) > 1:
        titulo = [t if cont[t] >= LINHA_MIN else OUTROS for t in titulo]
    if len(set(titulo)) == 1:   # marca com uma linha só: sem título
        titulo = [""] * len(titulo)
    return titulo


def resto_do_nome(modelo, linha):
    """O que vem depois do nome da linha ("C-02 Nérée Atlantique - AKR..." -> "Atlantique - AKR...")."""
    if not linha or linha == OUTROS:
        return modelo
    ws, lt = str(modelo).split(), [_norm(w) for w in linha.split()]
    j = k = 0
    while j < len(ws) and k < len(lt):
        if not _norm(ws[j]):
            j += 1
            continue
        if _norm(ws[j]) != lt[k]:
            return modelo
        j += 1
        k += 1
    resto = " ".join(ws[j:]).strip()
    resto = re.sub(r"^[-–—:,]\s*", "", resto)
    return resto or modelo


def chave_ordem(t):
    if t == OUTROS:
        return (2, "")
    return (0 if t else 1, [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", _norm(t))])
