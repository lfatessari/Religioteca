import pickle,re
rows=pickle.load(open('rows.pkl','rb'))
merge=[('Complexity','Complexity'),('Shams Crystal Multicolored','Multicolored Shams Saphir'),('Purity Curvy Tourbillon','Curvy Purity Tourbillon'),
('Purity Wavy Central Tourbillon Iridescent','Purity Wavy Central Tourbillon Iridescent'),('Tiny Purity Tourbillon Iridescent','Tiny Purity Tourbillon Iridescent'),
('Purity Wavy HMS Mirror','Purity Wavy HMS Mirror'),('Purity Stairway To Heaven HMS Wavy','Purity Stairway To Heaven Wavy HMS'),
('Russian Roulette Crystal','Russian Roulette Sapphire'),('Purity Wavy Central Tourbillon Purple','Purity Wavy Central Tourbillon Purple'),
('Tiny Purity Tourbillon NanoSaphir Chameleon','Tiny Purity Tourbillon NanoSaphir Chameleon')]
drop=set()
for pn,on in merge:
    p=[i for i,r in enumerate(rows) if r[0]==pn and r[4]=='p'][0]
    o=[i for i,r in enumerate(rows) if r[0]==on and r[4]=='o'][0]
    if 'masterhorologer.com/20' in rows[p][2]:
        rows[p][2]=rows[o][2]; rows[p][3]=rows[p][3].replace('Sem foto direta: link do artigo do Master Horologer.','Foto na página oficial do produto (link da página).')
    drop.add(o)
rows=[r for i,r in enumerate(rows) if i not in drop]
rows.append(['Blue Enamel','','https://everywatch.com/artya/watch-32635855','Caixa de 44 mm em aço, mostrador azul de esmalte. Visto só em anúncio do EveryWatch (link do anúncio).','x'])
for r in rows:
    if r[0].startswith('Purity Stairway To Heaven Steel Black Mirror'): r[3]+=' Código S2HSB na loja The Limited Edition.'
    if r[0]=='Purity Stairway To Heaven Steel': r[3]+=' Código S2HS na The Limited Edition e PUR-HM1 no Hourstriker.'
    r[3]=r[3].replace('|','/').strip()
names=[r[0] for r in rows]; assert len(names)==len(set(names)), [n for n in names if names.count(n)>1]
with open('dados_artya.txt','w') as f:
    for r in rows: f.write('|'.join(r[:4])+'\n')
print(len(rows), sum(1 for r in rows if r[3].startswith('Peça única')))
