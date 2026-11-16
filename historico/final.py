import re,json
exec(open('variantes.py').read())
LIM_SEM={'g400','x100-1'}
CDN='https://benlydesignwatch.com/cdn/shop/files/'
out=[]
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
for l in open('base_benly.tsv'):
    nome,h,img=l.rstrip('\n').split('|')
    lim=LIM.get(h); suf=f' – edição limitada de {lim} peças' if lim else (' – edição limitada' if h in LIM_SEM else '')
    car=C.get(h,'')
    if h=='x100-1': car='Foto da vitrine da loja oficial (a ficha do produto não abriu).'
    if h in V:
        for s,i in V[h]: out.append([f'{nome} {s}{suf}','',CDN+i,car])
    else: out.append([f'{nome}{suf}','',CDN+img,car])
for f in ('extras.txt','extras2.txt'):
    for x in open(f):
        if not x.strip(): continue
        n,c,i,e=x.rstrip('\n').split('|')
        if c and norm(c) in norm(n): c=''
        out.append([n,c,i,e])
nomes=[o[0]+(' - '+o[1] if o[1] else '') for o in out]
import collections; d=[k for k,v in collections.Counter(nomes).items() if v>1]; print('dup',d)
assert all('|' not in x for o in out for x in o)
open('dados_Benlydesign.txt','w').write('\n'.join('|'.join(o) for o in out)+'\n'); print(len(out))
fontes=[]
seen=set()
for l in open('parcial_Benlydesign_fontes.txt'):
    p,u,n=l.strip().split('|'); 
    if u.lower().rstrip('/') in seen: print('rep',u); continue
    seen.add(u.lower().rstrip('/')); fontes.append({'url':u,'passada':int(p),'novos':int(n)})
print('fontes',len(fontes), collections.Counter(f['passada'] for f in fontes))
obs=("Relógios pesquisados em 16/11/2026 (v653): 171 modelos/cores. O site oficial abriu direto. Vermelha: o site tem muitas fichas antigas escondidas (S1000, S3000, X5000, X7000 em várias cores, ex.: S1000S-B, S3000 preto, X7000 SR/SG2/BW citados só em nomes de arquivo ou avaliações) que não deu para listar todas. "
     "Muitas fichas antigas aparecem só com o link da página (fotos não aparecem na leitura automática). "
     "A ficha de fornecedor na HKTDC indica a empresa Shenzhen Benly Watch Co., Ltd (China continental); B/C dizem Hong Kong (o site oficial fala em equipe de Hong Kong) — a verificar. "
     "D corrigido: 'Relógios digitais e a quartzo de desenho futurista e preço baixo.' → inclui automáticos (Steel Tank, Time Gallery, Time Frame, Lighthouse Mechanical, Cylindrex) — fonte: site oficial.")
D_novo='Relógios digitais, a quartzo e automáticos de desenho retrofuturista e preço baixo.'
cfg={"marca":"Benlydesign","usa_codigos":False,"logo":"https://benlydesignwatch.com/cdn/shop/files/logo_new.png?v=1758520853&width=1889",
 "site_bloqueado":"Parcial – benlydesignwatch.com: a ficha x100-1 dá erro e as fotos das fichas antigas (escondidas) não aparecem na leitura automática; revisitar com navegador",
 "vermelho":True,"grande":True,"complemento":False,"observacoes":obs,
 "correcoes":{"D":D_novo},"correcoes_fontes":{"D":["https://benlydesignwatch.com/products/steel-tank","https://benlydesignwatch.com/products/time-gallery"]},
 "fontes":fontes}
json.dump(cfg,open('marca_Benlydesign.json','w'),ensure_ascii=False,indent=1)
