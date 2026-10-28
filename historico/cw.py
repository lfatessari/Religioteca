# uso: python3 cw.py add "Nome|CODIGO|img|E"  ...  (dedupe por cabeça = código sem sufixo de pulseira)
import sys,json,os,re
F='/home/claude/trabalho/cw_db.json'
db=json.load(open(F)) if os.path.exists(F) else {}
def head(c):
    c=c.upper().strip()
    parts=c.split('-')
    if len(parts)>=4: return '-'.join(parts[:3])  # C60-38ADA2-S0RK0-RK -> C60-38ADA2-S0RK0
    if len(parts)==3 and re.match(r'^[A-Z]\d+$',parts[0]) and len(parts[1])>8: return '-'.join(parts[:2])  # C60-40ADA31S0VV0-TK
    return c
cmd=sys.argv[1]
if cmd=='add':
    n=0
    for a in sys.argv[2:]:
        nm,c,img,e=(a.split('|')+['','',''])[:4]
        k=head(c) if c else 'NOREF:'+nm.lower()
        if k in db:
            def isimg(u): return bool(u) and ('/image' in u or 'images' in u or u.split('?')[0].lower().endswith(('.jpg','.jpeg','.webp','.png')))
            if img and (not db[k]['img'] or (isimg(img) and not isimg(db[k]['img']))):
                db[k]['img']=img
            if e and not db[k]['e']: db[k]['e']=e
            continue
        db[k]={'nome':nm,'cod':c.upper(),'img':img,'e':e}; n+=1
    json.dump(db,open(F,'w'),ensure_ascii=False,indent=0); print('novos',n,'total',len(db))
elif cmd=='img':
    k=head(sys.argv[2]); db[k]['img']=sys.argv[3]; json.dump(db,open(F,'w'),ensure_ascii=False,indent=0); print('ok')
elif cmd=='dump':
    with open('/home/claude/trabalho/parcial_ChristopherWard_relogios.txt','w') as f:
        for k,v in db.items(): f.write(f"{v['nome']}|{v['cod']}|{v['img']}|{v['e']}\n")
    print(len(db))
elif cmd=='list':
    for k,v in sorted(db.items()): print(k,'|',v['nome'],'|',('IMG' if '/image' in v['img'] or v['img'].endswith(('.jpg','.webp','.png')) else 'pg'))
