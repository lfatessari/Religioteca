import json,re,sys
r=json.load(open('armand_nicolet/rows.json'))
codes={x[1].upper() for x in r}
for l in open('armand_nicolet/img_hidden.txt'): codes.add(l.split('|')[0].upper())
names=set()
for l in open('extra.txt'):
  p=l.rstrip('\n').split('|')
  if len(p)==4:
    if p[1]: codes.add(p[1].upper())
    else: names.add(p[0])
def n(c): return re.sub(r'[^A-Z0-9]','',c.upper()).replace('O','0')
N={n(c) for c in codes}
added=0
f=open('extra.txt','a')
for l in open(sys.argv[1]):
  p=l.rstrip('\n').split('|')
  if len(p)!=4: continue
  if p[1] and n(p[1]) in N: print('dup',p[1]); continue
  if not p[1] and p[0] in names: print('dupname',p[0]); continue
  f.write('|'.join(p)+'\n'); added+=1
  if p[1]: N.add(n(p[1]))
  else: names.add(p[0])
print('added',added)
