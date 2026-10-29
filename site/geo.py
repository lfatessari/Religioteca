"""Coordenadas das cidades de origem (para os pins do globo da Home).

Usa a base GeoNames (pacote geonamescache, cidades com 500+ habitantes, com os
nomes alternativos em português). Quando a cidade não é achada, usa a capital
do país e marca o ponto como aproximado.
"""
import re
import unicodedata

PAISES = {
    "suica": "CH", "usa": "US", "eua": "US", "estadosunidos": "US", "alemanha": "DE", "franca": "FR",
    "italia": "IT", "reinounido": "GB", "inglaterra": "GB", "escocia": "GB", "irlandadonorte": "GB",
    "pais de gales": "GB", "china": "CN", "japao": "JP", "suecia": "SE", "hongkong": "HK",
    "dinamarca": "DK", "holanda": "NL", "paisesbaixos": "NL", "cingapura": "SG", "singapura": "SG",
    "espanha": "ES", "canada": "CA", "belgica": "BE", "australia": "AU", "russia": "RU",
    "austria": "AT", "india": "IN", "novazelandia": "NZ", "brasil": "BR", "malasia": "MY",
    "republicatcheca": "CZ", "tchequia": "CZ", "portugal": "PT", "coreiadosul": "KR", "noruega": "NO",
    "finlandia": "FI", "eslovaquia": "SK", "polonia": "PL", "taiwan": "TW", "romenia": "RO",
    "qatar": "QA", "catar": "QA", "hungria": "HU", "emiradosarabesunidos": "AE", "albania": "AL",
    "irlanda": "IE", "africadosul": "ZA", "grecia": "GR", "israel": "IL", "islandia": "IS",
    "indonesia": "ID", "filipinas": "PH", "eslovenia": "SI", "lituania": "LT", "ucrania": "UA",
    "arabiasaudita": "SA", "mexico": "MX", "argentina": "AR", "chile": "CL", "colombia": "CO",
    "turquia": "TR", "tailandia": "TH", "vietna": "VN", "luxemburgo": "LU", "monaco": "MC",
    "liechtenstein": "LI", "croacia": "HR", "bulgaria": "BG", "estonia": "EE", "letonia": "LV",
    "servia": "RS", "egito": "EG", "libano": "LB", "kosovo": "XK", "bosnia": "BA", "cuba": "CU",
}

# nomes que a base não resolve sozinha (regiões, vales, grafias da planilha)
MANUAIS = {
    "valedejoux": (46.61, 6.23), "valleedejoux": (46.61, 6.23), "valledejoux": (46.61, 6.23),
    "jura": (47.10, 6.85), "jurasuico": (47.10, 6.85), "jurabernes": (47.20, 7.10),
    "planlesouates": (46.17, 6.12), "lebrassus": (46.58, 6.21), "lesentier": (46.61, 6.23),
    "leslocle": (47.06, 6.75), "biel": (47.14, 7.25), "bienne": (47.14, 7.25),
    "saxonia": (50.93, 13.46), "floresta negra": (48.3, 8.2), "florestanegra": (48.30, 8.20),
    "vallededejoux": (46.61, 6.23), "lachauxdefonds": (47.10, 6.83),
    "cingapura": (1.29, 103.85), "singapura": (1.29, 103.85), "helsinque": (60.17, 24.94),
    "roterda": (51.92, 4.48), "havai": (21.31, -157.86), "kauai": (22.08, -159.50),
}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s).lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s)


def pais_iso(pais):
    p = re.sub(r"\[.*?\]", "", str(pais or ""))
    p = re.split(r"[(/]", p)[0].strip()
    return PAISES.get(norm(p), "")


class Geo:
    def __init__(self):
        import geonamescache
        gc = geonamescache.GeonamesCache(min_city_population=500)
        self.paises = gc.get_countries()
        self.idx = {}      # (iso, nome) -> (pop, lat, lon)
        self.idx_mundo = {}
        for c in gc.get_cities().values():
            nomes = {c["name"], *c.get("alternatenames", [])}
            for n in nomes:
                k = norm(n)
                if len(k) < 3:
                    continue
                v = (c["population"], c["latitude"], c["longitude"])
                ch = (c["countrycode"], k)
                if ch not in self.idx or self.idx[ch][0] < v[0]:
                    self.idx[ch] = v
                if k not in self.idx_mundo or self.idx_mundo[k][0] < v[0]:
                    self.idx_mundo[k] = v
        self.capitais = {}
        for iso, p in self.paises.items():
            cap = self.idx.get((iso, norm(p.get("capital", ""))))
            if cap:
                self.capitais[iso] = cap[1:]
        self.capitais.setdefault("HK", (22.32, 114.17))
        self.capitais.setdefault("SG", (1.29, 103.85))
        self.capitais["CH"] = (46.95, 7.45)

    def candidatos(self, cidade):
        c = re.sub(r"\[.*?\]", "", str(cidade or ""))
        partes = [c.split("(")[0]] + re.findall(r"\(([^)]*)\)", c)
        saida = []
        for p in partes:
            for q in re.split(r"/|,| e | – | - |;", p):
                q = q.strip()
                if q:
                    saida.append(q)
        return saida

    def local(self, pais, cidade):
        """(lat, lon, exato) ou None."""
        iso = pais_iso(pais)
        for cand in self.candidatos(cidade):
            k = norm(cand)
            if k in MANUAIS:
                return (*MANUAIS[k], True)
            if iso and (iso, k) in self.idx:
                v = self.idx[(iso, k)]
                return (v[1], v[2], True)
            if not iso and k in self.idx_mundo and self.idx_mundo[k][0] > 50000:
                v = self.idx_mundo[k]
                return (v[1], v[2], True)
        if iso and iso in self.capitais:
            lat, lon = self.capitais[iso]
            return (lat, lon, False)
        return None
