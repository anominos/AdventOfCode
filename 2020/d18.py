dat = []
with open("d18in.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            dat.append((x.strip().replace(" ", "")))
import re
def get(a, i):
    o = i
    while i < len(a) and a[i].isdigit():
        i+=1
    return int(a[o:i])

def calc(a):
    a = a.strip("(").strip(")")
    # while "+" in a:
    #     print(a)
    #     b = re.search(r"(\d+)\+(\d+)", a)
    #     a = a[:b.start()]+str(sum(map(int, b.groups())))+a[b.end():]
    cur = get(a, 0)
    i = len(str(cur))+1
    while i < len(a):
        op = a[i-1]
        if op=="+":
            cur+=get(a, i)
        else:
            cur*=get(a, i)
        n = (len(str(get(a, i))))
        i+= n+1
    return str(cur)
c=0
for x in dat:
    while "(" in x:
        a =re.search(r"\(([^\(\)]+)\)", x)
        x = x[:a.start()]+calc(a.group())+x[a.end():]
    c+=int(calc(x))
print(c)