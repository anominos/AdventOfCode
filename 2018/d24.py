from dataclasses import dataclass
class group:pass
@dataclass
class group:
    n:int
    hp:int
    ad:int
    at:str
    ini:int
    weak:list
    imm:list
    targ:group
    @property
    def ep(s):
        return s.n*s.ad
    
    def setTarg(s,l):
        m = max(l, key=lambda a:((a.weak==s.at)+(a.imm!=s.at), a.ep, a.ini))
        s.targ=m
        return m




import re
a = []
with open("d24in.txt") as f:
    for x in f.read().split("\n\n"):
        a.append([])
        r = True
        for y in x.splitlines():
            if r:
                r=False
                continue
            n,hp,ad,ini = map(int, re.findall("\d+", y))
            w = re.search(r"\((.+)\)", y)
            weak, imm = [], []
            if w:
                w = w.group(1)
                for x in w.split("; "):
                    if x.split()[0] == "weak":
                        weak.extend([x.split()[2:]])
                    else:
                        imm.extend([x.split()[2:]])
            at = re.search("(\S*) damage", y).group(1)
            a[-1].append(group(n,hp,ad,at,ini,weak,imm))


def getOrder(a):
    return sorted(a, key=lambda a:(a[0].ep, a[0].ini), reverse=True)

while True:
    for x in getOrder


# for x in 