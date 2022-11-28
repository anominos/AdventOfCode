dat = []
with open("d7in.txt") as f:
    for x in f:
        dat.append(x.strip())
import re
from collections import defaultdict
d = {}
backwards = defaultdict(list)
for x in dat:
    m = x.split()
    frm = " ".join(m[:m.index("bags")])
    tos = x[x.index("contain ")+len("contain "):-1].split(", ")
    d[frm] = []
    for x in tos:
        backwards[" ".join(x.split()[1:-1])].append((1,frm))
        ad = (x.split()[0], " ".join(x.split()[1:-1]))
        if ad != ("no", "other"):
            d[frm].append(ad)

def rec(cur, di, prev):
    n,c = di[cur],1
    for i, x in n:
        if prev==None or not(x in prev):
            (prev if prev!=None else set()).add(x)
            c+=int(i)*rec(x,di, prev)
    return c

print(rec("shiny gold", backwards, set())-1)
print(rec("shiny gold", d, None)-1)