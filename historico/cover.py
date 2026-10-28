import json,re,unicodedata
def n(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'– edicao limitada.*','',s); s=re.sub(r'[^a-z0-9 ]',' ',s); s=re.sub(r'\b(mm|the)\b',' ',s)
    return ' '.join(s.split())
db=json.load(open('cw_db.json'))
names=[n(v['nome']) for v in db.values()]
unc=[];cov=[]
for l in open('handbooks.txt'):
    m,p=l.rstrip('\n').split('|')
    nm=n(m)
    if any(x==nm or x.startswith(nm+' ') for x in names): cov.append(m)
    else: unc.append(m)
print(len(cov),'cobertos;',len(unc),'sem linha')
open('handbooks_sem_linha.txt','w').write('\n'.join(unc))
