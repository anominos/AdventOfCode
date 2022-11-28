dat = []
with open("d19in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append(x)
react, form = dat
react = react.split("\n")
from collections import defaultdict
d =defaultdict(list)
for x in react:
    a,b = x.split(" => ")
    d[a].append(b)

s = set()
i=0
while i < len(form):
    j=i+1
    while j < len(form) and form[j].islower():
        j+=1
    for n in d[form[i:j]]:
        s.add(form[:i] + n + form[j:])
    i = j


print(len(s))
rev = {}
for i,j in d.items():
    for x in j:
        rev[x] = i
rev = dict(sorted(rev.items(), key=lambda a:len(a[0]), reverse=True))
import random
# form = "HFOMg"
f=True
while f:
    f=False
    fringe = {form}
    gs = defaultdict(lambda : float("inf"))
    fs = defaultdict(lambda : float("inf"))
    gs[form] = 0
    fs[form] = len(form)
    c=0
    while fringe:
        cur = min(fringe, key=lambda a:(fs[a], random.random()))
        c+=1
        fringe.remove(cur)
        if cur=="e":
            break
        for i,j in rev.items():
            for x in range(cur.count(i)):
                nei = cur.replace(i, "__", x+1).replace("__", i,x).replace("__", j)
                tgs = gs[cur] + 1
                if tgs < gs[nei]:
                    gs[nei] = tgs
                    fs[nei] = gs[nei]+ len(nei)
                    if not nei in fringe:
                        fringe.add(nei)
        if c > 500:
            f=True
            break
print(gs["e"])