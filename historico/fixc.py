import sys, re, openpyxl
from urllib.parse import quote
ENT,SAI=sys.argv[1:3]
S='https://cdn.shopify.com/s/files/1/0524/2270/5317/files/'
novo={
 'AD2059':S+'AD2059_dc2ad5f6-dbbf-47f9-b819-f6cd63ebb27b.jpg',
 'AD2504':S+'1_2f677dc1-fbaa-401d-aa90-fc40d9bda189.jpg',
 'AD2036':S+'1_4529778d-b0ec-4f29-8273-10e97596d313.jpg',
 'AD2023-1':S+'2023_03b6696d-ae21-4c7e-9422-8e1a6c907944.jpg',
 'AD2531':S+'2531_d61dd40d-de89-4010-abfc-3ea1ead2b688.jpg',
 'AD2523':S+'3_1c835746-7614-4af6-8ac5-921dd2acfdab.jpg',
 'AD2514':'https://timedreviews.com/wp-content/uploads/2025/10/addiesdive-ad2514-front.jpg',
 'AD2114':'https://m.media-amazon.com/images/I/71EC7rKFfML._AC_.jpg',
 'AD2049':'https://addiesdivewatches.de/cdn/shop/articles/6_314e6245-928c-4485-af2d-efa5f550fdbf.jpg',
 'AD2033':'https://primetimepiece.com/cdn/shop/files/addiesdive-ad2033-dive-black-steel-front.webp',
 'AD2527':'https://m.media-amazon.com/images/I/71z0brs4dzL.jpg',
 'AD2105':'https://dream-watches.com/cdn/shop/files/addiesdive-scuba-vintage-mens-automatic-divers-watch-ad2105-5662444.png',
 'AD2061':'https://watchesgarage.com/wp-content/uploads/2024/07/IMG_3249.jpg',
 'AD2505':'https://img.bestdealplus.com/ae01/kf/Sfde4befdb3be47208687d991de834f9bD.jpg',
 'AD2542':'https://s.alicdn.com/@sc04/kf/Hf6c15758b3084b95a0aff86848df751dt.jpg_960x960q80.jpg',
 'AD2538':'https://img.bestdealplus.com/ae01/kf/S431f0a84f19041cc8554284fb41ba4b1m.jpg',
 'AD2522':'https://www.provence-canoe.com/wp-content/uploads/2026/02/featured-test-de-la-montre-de-plongee-addiesdive-ad2522-etanche-et-performante-1024x1024.jpg',
 'MY-050':'https://img2.elyerromenu.com/images/g-folmes-tiempoesoro/addiesdive-my-050s/img.webp',
}
def enc(u): return quote(u, safe=":/?&=%#+~;,@!$'()*[]-._")
wb=openpyxl.load_workbook(ENT); w=wb['Relógios']
before={(r,c):w.cell(r,c).value for r in range(1,w.max_row+1) for c in range(1,6)}
feitos={}
for r in range(2,w.max_row+1):
    if w.cell(r,1).value!='Addiesdive': continue
    b=w.cell(r,2).value or ''
    for k,u in novo.items():
        if b.endswith(' - '+k):
            assert k not in feitos, k
            u=enc(u); c=w.cell(r,3); c.value=u; c.hyperlink=u
            e=w.cell(r,5)
            if e.value and 'visto só no título do resultado de busca (link da página)' in e.value:
                e.value=e.value.replace('; visto só no título do resultado de busca (link da página)','').replace('visto só no título do resultado de busca (link da página)','').strip('; ')
            feitos[k]=r
assert set(feitos)==set(novo), set(novo)-set(feitos)
wb.save(SAI)
wb2=openpyxl.load_workbook(SAI); w2=wb2['Relógios']
mud=[(r,c) for r in range(1,w2.max_row+1) for c in range(1,6) if w2.cell(r,c).value!=before.get((r,c))]
fora=[x for x in mud if x[0] not in feitos.values() or x[1] not in (3,5)]
ruins=[r for r in feitos.values() if w2.cell(r,3).hyperlink is None or w2.cell(r,3).hyperlink.target!=w2.cell(r,3).value]
print('linhas trocadas:',len(feitos),'| células mudadas:',len(mud),'| fora do permitido:',fora,'| hyperlinks ruins:',ruins, '| max_row', w2.max_row, w.max_row)
for t in ['Marcas','Planilha1','Tabela de faixa de preços']:
    a=wb[t]; b2=wb2[t]
    d=[c.coordinate for c in a._cells.values() if c.value!=b2[c.coordinate].value]
    print(t,'diferenças:',d)
print('RESULTADO:','OK' if not fora and not ruins and len(feitos)==18 else 'FALHOU')
