import unicodedata,re,difflib,json
STOP={'watches','watch','co','company','timepieces','timepiece','the','of','and','instruments','design','studio','studios','corp','corporation','horology','labs','lab','supply','geneve','watchmaker','works','zurich','london','amsterdam','tokyo','berlin','milano','hamburg','stockholm','glashutte','glashuette','swiss','dive','hybrid','timekeepers','projects','engineering','collection','technical'}
def norm(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn').lower().replace('ø','o').replace('ł','l').replace('&',' and ').replace('+',' and ')
    return re.sub(r'[^a-z0-9 ]',' ',s)
def key(s):
    w=[x for x in norm(s).split() if x not in STOP]
    return ''.join(w) or ''.join(norm(s).split())
sheet=[l.rstrip('\n') for l in open('/home/claude/trabalho/nomes.txt') if l.strip() and l.strip()!='None']
sk={key(n):n for n in sheet}
skeys=list(sk)
atlas=[l.rstrip('\n').split('|') for l in open('atlas.txt')]
have=[];miss=[];maybe=[]
for a in atlas:
    n=a[0]; k=key(n)
    if k in sk: have.append((n,sk[k])); continue
    # prefix containment (>=5 chars) or close match
    c=[s for s in skeys if len(k)>=5 and len(s)>=5 and (s.startswith(k) or k.startswith(s))]
    d=difflib.get_close_matches(k,skeys,n=1,cutoff=0.86)
    if c or d: maybe.append((n,a[1] if len(a)>1 else '',sk[(c or d)[0]]))
    else: miss.append(a)
print(len(atlas),'atlas |',len(have),'já temos |',len(maybe),'talvez |',len(miss),'faltam')
print('TALVEZ:'); print('; '.join(f'{n} ~ {s}' for n,c,s in maybe))
json.dump({'miss':miss,'maybe':maybe},open('cruza.json','w'),ensure_ascii=False)
