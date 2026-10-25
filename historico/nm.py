import re,sys
def linha(c):
    c=c.upper()
    if c.startswith('MTG'): return 'G-SHOCK MT-G'
    if c.startswith('MRG'): return 'G-SHOCK MR-G'
    if re.match(r'^(G[A-Z]*-|DW|GW|GXW|DWE|AW|AWG|AWM|GAW|GLS|GLX|GWX|GST|GBD|GBA|GPR|GDG|GPW|GWF|GWG|GG-|GN-|GWN|GR-|GWR|GMW|GMA|GMD|GM-|GB-|GD-|GBX|GBM|GSW|DWN|G-\d|GL-|GX-|MRG|ST-B)',c): return 'G-SHOCK'
    if re.match(r'^(BG|BA-|BA1|MSG|BSA|BGD|BGA|BGS|BGR|BLX|MSA)',c): return 'BABY-G'
    if re.match(r'^(OCW|OSW)',c): return 'OCEANUS'
    if re.match(r'^(EF|EQ|EC|ERA)',c): return 'EDIFICE'
    if re.match(r'^(PR[WGJT]|PRX|PRG)',c): return 'PRO TREK'
    if re.match(r'^(LWA|WVA|LWQ|WVQ|LWQ)',c): return 'Casio Wave Ceptor'
    if re.match(r'^(SHE|SHB|SHS)',c): return 'SHEEN'
    return 'Casio'
def serie(c):
    m=re.match(r'^([A-Z]+-?[A-Z]*\d+)',c.upper())
    return m.group(1) if m else c
def strip(c): return re.sub(r'(U?DF|U?EF|JF|JR|IR|JH|ER|PR|CR)$','',c.strip())
if __name__=='__main__':
    # stdin: COD|nota  -> Nome|COD|P|nota V ; nota começando com C: vira parte do nome
    P,V=sys.argv[1],sys.argv[2]
    for l in sys.stdin:
        l=l.strip()
        if not l: continue
        c,n=(l.split('|')+[''])[:2]
        c=strip(c); nm=linha(c)+' '+serie(c); e=''
        if n.startswith('C:'): nm+=' – '+n[2:]
        elif n: e=n.rstrip('.')+'. '
        print(f'{nm}|{c}|{P}|{e}{V}')
