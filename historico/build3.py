import json,re
site=json.load(open('rows_site.json'))
cnc=json.load(open('cncom_rows.json'))
SER={'隽永':'Juanyong','荣耀':'Rongyao','时光永恒':'Shiguang Yongheng','时光见证':'Shiguang Jianzheng','尊尚':'Zunshang','骐致':'Qizhi','天锐':'Tianrui','恒心':'Hengxin','琅玥':'Langyue','朗玥':'Langyue','探索者':'Tansuozhe','至臻':'Zhizhen','极光':'Jiguang','臻金':'Zhenjin','小金表':'Xiaojinbiao','歌雅':'Geya','宇宙':'Yuzhou','黑鲨':'Heisha'}
TR={'荣耀':'Glória','时光永恒':'Tempo Eterno','时光见证':'Testemunho do Tempo','尊尚':'Supremo','恒心':'Perseverança','探索者':'Explorador','极光':'Aurora','臻金':'Ouro Puro','小金表':'Pequeno Relógio Dourado','宇宙':'Universo','黑鲨':'Tubarão Negro'}
rows=[r[:] for r in site]
for s,code,img,url in cnc:
  if code.startswith('C8175'): continue
  nm=f"{SER.get(s,'Série')}"
  e=f"Série {s}"+(f" ('{TR[s]}')" if s in TR else '')+" do site oficial chinês cadisen.com."
  if '/' in code: e+=" Código M/L indica par masculino e feminino."
  if code.endswith('L') and '/' not in code: e+=" Modelo feminino."
  rows.append([nm,code,img,e])
for l in open('extras.txt'):
  n,c,i,e=l.rstrip('\n').split('|'); rows.append([n,c,i,e])
# clean
out=[]
seen=set()
for n,c,i,e in rows:
  n=n.replace('|','/'); e=(e or '').replace('|','/').replace('..','.')
  key=(n,c)
  k=2
  while key in seen: key=(f"{n} ({k})",c); k+=1
  seen.add(key); out.append([key[0],c,i,e])
with open('dados_cadisen.txt','w') as f:
  for r in out: f.write('|'.join(r)+'\n')
print(len(out))
