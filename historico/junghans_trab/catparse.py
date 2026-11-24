import sys,re,json; sys.path.insert(0,'.')
from jh import *
KW=r'(Meister|max bill|Max Bill|MAX BILL|Mega|MEGA|Form|FORM|Milano|Spektrum|Aura|Diplomat|Willy|Voyager|Attach|Ceramic|Tempus|Cuprum|Funk|Solar|Arcus|Avantgarde|Anytime|Lady|Elegance|Chronoscope|Automatic|Pilot|Aviator|Driver|Telemeter|Calendar|Kalender|Agenda|Bogner|Performance|Force|Stratos|1972|Erhard|Aerious|Creator|Kleinuhr|Herren|Damen|Quarz|Titan|Kayla|Kumi|Ellipse|Chronograph|Chronometer|Classic|Trilastic|Astro|Olympia|Astra|Ato|Uhr)'
def parse(md):
    out={}
    for m in re.finditer(r'0?(\d{2,3})\s*/\s*(\d{4})\s*\.\s*\.?\s*(\d{2})',md):
        ref=norm(''.join(m.groups()))
        if ref in out: continue
        pre=md[max(0,m.start()-160):m.start()]
        cands=[c.strip(' |*#-_:') for c in re.split(r'[\n|]',pre)]
        name=''
        for c in reversed(cands):
            c=re.sub(r'0?\d{2,3}\s*/\s*\d{4}\s*\.\s*\d{2}','',c).strip(' |*#-_:,.')
            if c and re.search(KW,c) and len(c)<=45 and not re.search(r'\d{3,}',c): name=c; break
        out[ref]=name
    return out
