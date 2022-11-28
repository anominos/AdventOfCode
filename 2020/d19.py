dat = []
with open("d19in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip()))

rules = dat[0]
dat = dat[1]
d = {}
for x in rules.split("\n"):
    a, b = x.split(": ")
    d[a] = b

rules = {}
import re

def get(a):
    if a in rules.keys():
        return rules[a]
    if y:=re.match("\"(.*)\"", d[a]):
        rules[a] = [y.group(1)]
    else:
        rules[a] = []
        if y:=re.match("^(\d+)$", d[a]):
            y = y.group()
            get(y)
            rules[a] = rules[y]
        else:
            rules[a] = []
            for i in d[a].split(" | "):
                for j in i.split():
                    get(j)
                l = [""]
                for x in i.split():
                    new = []
                    for y in l:
                        for z in rules[x]:
                            new.append(y+z)
                    l = new[:]
                rules[a].extend(l)
                    


get("0")
z = set(rules["0"])
c=0
c2=0
a=[]
for x in dat.split("\n"):
    if x in z:
        c+=1
    if y:=re.match(f"((?:{'|'.join(rules['42'])})+)((?:{'|'.join(rules['42'])})+)((?:{'|'.join(rules['31'])})+)$", x):
        l1, l2 = {len(i) for i in rules["42"]}.pop(), {len(i) for i in rules["31"]}.pop()
        a, b, d = map(len, y.groups())
        if a//l1 + b//l1 > d//l2:
            c2+=1
        
print(c) 
print(c2)