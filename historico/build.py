import re,json,os
os.chdir('/home/claude/trabalho')
B='https://www.relogioscondor.com.br/api/dataentities/FU/documents/'
P={'ago26':('agosto de 2026',B+'7e721a7a-9eec-49a5-b69e-9809884eed64/file/attachments/Condor_Agosto_2026.pdf'),
'jul26':('julho de 2026',B+'12f25f0a-0b4f-4644-8723-26eda5a2c4a4/file/attachments/Condor_Julho_2026.pdf'),
'jun26':('junho de 2026',B+'4f165907-9332-4f4c-b1d8-a1a01bf252c7/file/attachments/Condor_Junho_2026.pdf'),
'mai26':('maio de 2026',B+'9336a8a9-a865-459a-bfe9-cdf2ce1b524b/file/attachments/Condor_Maio_2026.pdf'),
'abr26':('abril de 2026',B+'1834bd94-4e25-438a-a69f-8d56ce458d2c/file/attachments/Condor_Abril_2026.pdf'),
'mar26':('março de 2026',B+'2bcd2614-e6b3-4865-8c04-f62892b05ee5/file/attachments/Condor_Marco_2026.pdf'),
'out25':('outubro de 2025',B+'fa6cfb55-2525-4630-8d80-babed37dbe16/file/attachments/LancamentosCondorOutubro2025.pdf'),
'set25':('setembro de 2025',B+'990fc2aa-0348-484b-96a7-d9700d0dac0b/file/attachments/LancamentosSet25Condor.pdf'),
'ago25':('agosto de 2025',B+'3bdccfe1-0ff4-4761-9d87-977ef53f03a2/file/attachments/CondorLancaAgosto25.pdf')}
def norm(c): return re.sub(r'[^A-Z0-9]','',c.upper())
R={}; order=[]
def rec(code,title=''):
    k=norm(code) or 'T:'+title
    if k not in R: R[k]={'code':code,'line':'','desc':'','img':'','page':'','pdf':'','title':'','note':''}; order.append(k)
    return R[k]
def pdffile(f,blocks):
    for i,l in enumerate(open(f),1):
        p=l.rstrip('\n').split('|')
        code=p[0]; line=p[1] if len(p)==3 else p[1].split(',')[0]; desc=p[-1] if len(p)==3 else ', '.join(p[1].split(', ')[1:])
        cat=[b for s,b in blocks if i>=s][-1]
        r=rec(code)
        if '/' in code and '/' not in r['code']: r['code']=code
        if not r['line']: r['line']=line
        if len(desc)>len(r['desc']): r['desc']=desc
        if not r['pdf']: r['pdf']=cat
pdffile('pdf_2026_08.txt',[(1,'ago26')])
pdffile('pdf_b.txt',[(1,'jul26'),(28,'jun26'),(66,'mai26')])
pdffile('pdf_c.txt',[(1,'abr26'),(87,'mar26')])
pdffile('pdf_d.txt',[(1,'out25'),(79,'set25'),(117,'ago25')])
for f in ['raw_site.txt','raw_site2.txt','raw_site3.txt','raw_site4.txt']:
    for l in open(f):
        c,t,u=l.rstrip('\n').split('|')[:3]; r=rec(c,t)
        if not r['title']: r['title']=t
        if not r['page']: r['page']=u
for f in ['raw_other.txt','raw_search.txt']:
    for l in open(f):
        p=l.rstrip('\n').split('|'); c,t,u,e=(p+['','','',''])[:4]
        r=rec(c,t)
        if not r['title']: r['title']=t
        if re.search(r'\.(jpg|jpeg|png|webp)',u,re.I) or 'imgs.' in u: r['img']=r['img'] or u
        elif not r['page']: r['page']=u
        if e and len(e)>len(r['note']): r['note']=e
for l in open('img.txt'):
    p=l.rstrip('\n').split('|'); r=rec(p[0],p[2]); r['img']=p[1]
    if not r['title']: r['title']=p[2]
LINES=['Mini Joia','Mimos E Sutilezas','Jardim Secreto','Puro Amor','Fé e Proteção','Constelação','Speed Racer','Dia A Dia','Bracelete','Elegante','Elegance','Brilho','Drive','Speed','Militar','Civic','Digital','Elos','Mini','Casual','Mesh']
def linefrom(t):
    for L in LINES:
        if re.search(r'\b'+L+r'\b',t,re.I): return 'Dia a Dia' if L=='Dia A Dia' else ('Elegante' if L=='Elegance' else L)
    return ''
CHAR=['Minnie','Mickey','Stitch','Pato Donald','101 Dálmatas','Toy Story','Carros','Homem-Aranha','Homem Aranha','Hulk','Moana','Frozen','Capitão América','Vingadores']
out=[]; names=set()
for k in order:
    r=R[k]; code=r['code']; t=r['title']; d=r['desc']; n=r['note']
    line=r['line'] or linefrom(t)
    txt=' '.join([t,d,n,line])
    if code.upper().startswith('COSMARTRA'): name='Smartwatch Reebok by Condor – colaboração Reebok'
    elif code.upper().startswith(('COSMART','C0SMART')): name='Condor Smart (smartwatch)'
    elif code.upper().startswith(('CODISNEY','COMARVEL')) or 'Kids' in txt and 'nterativo' in txt:
        ch=[c for c in CHAR if c.lower() in txt.lower()]
        name='Condor Kids '+('Marvel' if code.upper().startswith('COMARVEL') else 'Disney')+' (relógio interativo infantil)'+(' – '+ch[0] if ch else '')
    elif code.upper().startswith('COHB21') and 'lástico' in d:
        ch=[c for c in CHAR if c.lower() in txt.lower()]
        name='Digital infantil'+(' – '+ch[0] if ch else '')
    elif 'Marvel' in txt or 'Disney' in txt or line in ('Disney','Condor Kids'):
        ch=[c for c in CHAR if c.lower() in txt.lower()]
        lic='Marvel' if 'Marvel' in txt or (ch and ch[0] in ('Homem-Aranha','Homem Aranha','Hulk','Capitão América','Vingadores')) else 'Disney'
        name=lic+(' '+ch[0].replace('Homem Aranha','Homem-Aranha') if ch else '')
    elif line: name=line
    elif code.upper().startswith('K'):
        gg=re.search(r'(?i)(masculino|feminino|unissex|cron[oó]grafo)',t)
        name='Linha antiga'+(' – '+gg.group(1).lower().replace('cronografo','cronógrafo') if gg else '')
    else:
        tl=t.lower()
        typ='Analógico-digital' if 'analógico-digital' in tl or 'analógico digital' in tl else ('Digital' if 'digital' in tl else 'Analógico')
        gg=re.search(r'(?i)(masculino|feminino|unissex|infantil)',t)
        name=typ+(' '+gg.group(1).lower() if gg else '')
        if 'mostrador azul' in tl: name+=' – mostrador azul'
        if 'cristais' in tl: name+=' com cristais'
        if 'quadrado' in tl: name+=' quadrado'
        if 'colar e brincos' in tl: name+=' (kit com colar e brincos)'
    kit=bool(re.match(r'^CO.*/K',code.upper())) or t.lower().startswith('kit')
    if kit and 'kit' not in name.lower() and not code.upper().startswith('COSMART'): name+=' (kit)'
    # E
    parts=[]
    if d: parts.append(d[0].upper()+d[1:])
    if n and n not in d: parts.append(n[0].upper()+n[1:])
    url=r['img']
    if not url:
        if r['pdf']:
            mes,pu=P[r['pdf']]; url=pu; parts.append(f'Foto no catálogo oficial de lançamentos de {mes} (link do PDF)')
        elif r['page']:
            url=r['page']
            if 'relogioscondor' in url: parts.append('Visto na loja oficial; foto não acessível na leitura automática (link da página do produto)')
            elif not re.search('(?i)visto só|cadastro',' '.join(parts)): parts.append('Link da página do anúncio')
    elif r['pdf']: parts.append(f'Consta no catálogo oficial de lançamentos de {P[r["pdf"]][0]}')
    if kit and 'kit' not in ' '.join(parts).lower(): parts.insert(0,'Kit relógio + acessório')
    e='. '.join(p.rstrip('.') for p in parts if p)
    e=e.replace('|','/')
    if e: e+='.'
    out.append((name,code.upper().replace('C0SMART','COSMART'),url,e))
# dedupe codes after C0SMART fix
seen=set(); fin=[]
for o in out:
    key=norm(o[1]) or o[0]
    if key in seen: continue
    seen.add(key); fin.append(o)
with open('dados_Condor.txt','w') as f:
    for o in fin: f.write('|'.join(o)+'\n')
print(len(fin))
