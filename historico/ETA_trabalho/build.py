import json,re
D={}  # code -> dict(nome,img,e,src)
order=[]
def slug(c): return re.sub(r'[^a-z0-9]+','-',c.lower()).strip('-')
def add(code,img=None,e=None,nick=None,src=None,force=False):
    k=re.sub(r'[\s.\-]','',code.upper())
    if k not in D:
        D[k]=dict(code=code,img=img,e=e,nick=nick,src=src); order.append(k)
    else:
        d=D[k]
        if img and (force or not d['img'] or 'watchbase.com/eta/caliber' in d['img'] or '.pdf' in d['img'] or 'wiki.grail' in d['img']): d['img']=img
        if e and (force or not d['e']): d['e']=e
        if nick and not d['nick']: d['nick']=nick
WB='https://watchbase.com/eta/caliber/'
for c in open('/home/claude/trabalho/wb_list.txt').read().split('\n'):
    if c.strip(): add(c.strip(),WB+slug(c.strip()),None,src='wb')
exec(open('/home/claude/trabalho/extra.py').read())
out=[]
for k in order:
    d=D[k]; nome='Calibre '+d['code']+(' '+d['nick'] if d['nick'] else '')
    img=d['img']; e=d['e'] or ''
    if 'watchbase.com/eta/caliber' in img:
        e=(e+' ' if e else '')+'Sem foto: link da ficha do calibre no WatchBase.'
    elif '.pdf' in img:
        e=(e+' ' if e else '')+'Sem foto avulsa: link do catálogo oficial da ETA (PDF).'
    elif 'wiki.grail-watch.com' in img:
        e=(e+' ' if e else '')+'Sem foto: link da lista de calibres ETA do Grail Watch Wiki.'
    out.append(f"{nome}||{img}|{e.strip()}")
open('/home/claude/trabalho/dados_ETA.txt','w').write('\n'.join(out)+'\n')
print(len(out))
