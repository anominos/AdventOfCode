a = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()
dat = []
def toInt(a):
    try:return int(a)
    except ValueError:return a
from collections import Counter
with open("d16in.txt") as f:
    for x in f:
        d = ":".join(x.strip().split(": ")[1:]).split(", ")
        d = Counter(dict(list(map(toInt, i.split(":"))) for i in d))
        dat.append(d)
targ = Counter()
for x in a:
    c,d = x.split(": ")
    targ[c] = int(d)

for i,x in enumerate(dat,1):
    for a, b in x.items():
        if targ[a]!=b:
            break
    else:
        print(i)

for i,x in enumerate(dat,1):
    for a, b in x.items():
        if a in "cats trees".split():
            if targ[a] >= b:
                break
        elif a in "pomeranians goldfish":
            if targ[a] <= b:
                break
        elif targ[a]!=b:
            break
    else:
        print(i)