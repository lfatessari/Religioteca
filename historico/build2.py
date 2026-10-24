import json,re
cn=json.load(open('cn_rows.json')); cw=json.load(open('cw.json'))
PT={'black':'preto','blue':'azul','white':'branco','gray':'cinza','grey':'cinza','green':'verde','orange':'laranja','red':'vermelho','brown':'marrom','coffee':'café','gold':'dourado','golden':'dourado','rose':'rosé','silver':'prateado','tiffany':'azul Tiffany','meteorite':'meteorito','champagne':'champanhe','violet':'violeta','ice':'gelo','light':'claro','full':'todo','all':'todo','grid':'quadriculado','wave':'ondas','leather':'couro','rubber':'borracha','steel':'aço','mesh':'malha','belt':'pulseira','starry':'céu estrelado','surface':'','yelllow':'amarelo','s':'(P)','l':'(G)','with':'com','strap':'','stainless':'','wristwatch':''}
def pt(c):
  c=re.sub(r'\(Miyota 8215\)','',c,flags=re.I)
  strap=''
  for k,v in [('Black Steel Belt','preto, pulseira de aço'),('White Steel Belt','branco, pulseira de aço'),('Black Steel Belt','preto, pulseira de aço'),('Brown Belt','marrom, pulseira de couro'),('Black Belt','preto, pulseira de couro')]:
    if c.strip().lower()==k.lower(): return v
  m=re.match(r'(Rubber|Steel|Leather)\s+(.*)',c.strip(),re.I)
  if m: c=m.group(2); strap={'rubber':', pulseira de borracha','steel':', pulseira de aço','leather':', pulseira de couro'}[m.group(1).lower()]
  w=[PT.get(x.lower(),x.lower()) for x in re.findall(r'[A-Za-z]+',c)]
  w=[x for x in w if x]
  s=' '.join(w); s=s.replace('azul azul Tiffany','azul Tiffany').replace('azul Tiffany azul','azul Tiffany')
  return s+strap
DL={'blue':'U','black':'B','white':'W','gray':'H','grey':'H','green':'L','orange':'O','tiffany':'T','coffee':'F','red':'E','gold':'G','golden':'G','brown':'F'}
def dial_letter(c):
  c=re.sub(r'\(.*?\)','',c); ws=[x.lower() for x in re.findall(r'[A-Za-z]+',c)]
  ws=[x for x in ws if x not in ('steel','rubber','leather','grid','wave','light','ice','champagne','meteorite','full','all','mesh','belt','with','strap','silver','rose')] or ws
  if 'tiffany' in ws: return 'T'
  return DL.get(ws[-1]) if ws else None
LINE={}
for r in cn:
  b=re.sub(r'\D','',r[1])[:4]; nm=re.sub(r'^Titanium ','',r[0])
  nm=re.sub(r'\s+(White|Green|Orange|Blue|Nylon Black)$','',nm)
  if not nm.lower().startswith('ti-7'): LINE.setdefault(b,nm)
def spec(title,desc):
  t=title+' '+desc; f=[]; tt=title
  m=re.search(r'(\d{2}(?:\.\d)?)\s?MM',tt,re.I); 
  if m: f.append(m.group(1)+' mm')
  mv=re.search(r'(MIYOTA\s?\w{4}|Miyota\s?\w{4}|NH\d\dA?|VK\d\d|VD\d\d|OS\d\d|Seagull ST\d+|8N24|82S0|90S5)',t,re.I)
  if mv:
    x=mv.group(1); f.append(('automático '+x) if not re.match(r'(VK|VD|OS)',x,re.I) else 'quartzo '+x)
  elif re.search(r'quartz',t,re.I): f.append('quartzo')
  elif re.search(r'mechanical|automatic',t,re.I): f.append('automático')
  m=re.search(r'(\d{2,3})M Waterproof',t,re.I)
  if m: f.append(m.group(1)+' m')
  if re.search(r'sapph',t,re.I): f.append('vidro de safira')
  if re.search(r'skeleton|hollow',t,re.I): f.append('mostrador vazado (esqueleto)')
  if re.search(r'tourbillon',t,re.I): f.append('abertura tipo "tourbillon" no mostrador (decorativa)')
  if re.search(r'moon phase',t,re.I): f.append('fase da lua')
  if re.search(r'chronograph',tt,re.I) and 'cronógrafo' not in ' '.join(f): f.append('cronógrafo')
  if re.search(r'women|ladies|lady',title,re.I): f.append('feminino')
  if re.search(r'couple',title,re.I): f.append('par de relógios para casal')
  if re.search(r'diamond',title,re.I): f.append('com diamantes')
  nick=re.findall(r'(Datejust|DAY-DATE|Yacht-Master|Submariner|GMT-Master|Nautilus|Palm|Pilot|Moonwatch|Daytona|AP ROYAL OAK|TAG|Conquest)',title,re.I)
  s=', '.join(f)
  if nick: s+=f'. Loja oficial o apresenta como "{nick[0]}"'
  return s
def kind(title,code):
  b=re.sub(r'\D','',code)[:4]
  if b in LINE: return LINE[b]
  t=title.lower()
  if 'couple' in t: return 'Casal'
  if re.search(r'women|ladies|lady',t): return 'Feminino'
  if 'chronograph' in t: return 'Cronógrafo'
  if 'skeleton' in t or 'hollow' in t: return 'Esqueleto'
  if 'diver' in t: return 'Diver'
  if 'quartz' in t: return 'Quartzo'
  return 'Automático'
rows=[]; used=set()
cnby={}
for r in cn: cnby.setdefault(re.sub(r'\D','',r[1])[:4],[]).append(r)
for slug,p in sorted(cw.items()):
  code=slug.replace('cadisen-','').upper()
  if slug=='cadisen-c7065': code='C7067'
  b=re.sub(r'\D','',code)[:4]
  pool=[r for r in cnby.get(b,[]) if r[1] not in used]
  nm=kind(p['title'],code); sp=spec(p['title'],p['desc'][:400])
  for col,img in p['variants']:
    dl=dial_letter(col); gold=bool(re.match(r'(full gold|gold|golden)',col.lower()))
    match=None
    for r in pool:
      sku=r[1]
      if sku in used: continue
      if dl and re.sub(r'-(T|A)$','',sku).endswith(dl) and (sku[6:7]=='G')==gold:
        match=r;break
    cpt=pt(col)
    if match:
      used.add(match[1]); rows.append([f"{nm} – {cpt}",match[1],img or match[2],(sp[0].upper()+sp[1:] if sp else '')+'. Lojas oficiais cadisenwatch.com e cadisen.cn.'])
    else:
      rows.append([f"{nm} – {cpt}",code,img,(sp[0].upper()+sp[1:] if sp else '')+'. Loja oficial cadisenwatch.com (código do modelo; variante de cor sem referência completa publicada).'])
for r in cn:
  if r[1] in used: continue
  nm=r[0]
  if nm.startswith('Titanium '): nm=nm.replace('Titanium TI-7','Ti-7')
  nm=re.sub(r' Titanium Strap$',' – pulseira de titânio',nm)
  nm=re.sub(r'\b([A-Z]{3,})\b',lambda m:m.group(1).title(),nm)
  if not nm.startswith('Ti-7'):
    nm=re.sub(r'\s+(White|Green|Orange|Blue|Nylon Black)$','',nm)
    cor={'U':'azul','H':'cinza','W':'branco','B':'preto','L':'verde','O':'laranja','0':'laranja','T':'azul Tiffany','G':'dourado','F':'café','E':'vermelho'}.get(re.sub(r'-(T|A)$','',r[1])[-1])
    if cor: nm+=' – '+cor
  rows.append([nm,r[1],r[2],r[3]])
# fix names: Title-case english words left
json.dump(rows,open('rows_site.json','w'),ensure_ascii=False,indent=0)
print(len(rows), len(used), len(cn)); print([r[1] for r in cn if r[1] not in used])
import collections
c=collections.Counter((r[0],r[1]) for r in rows); print([k for k,v in c.items() if v>1][:20])
for r in rows[:400:7]: print(r[0],'|',r[1],'|',r[3][:110])
