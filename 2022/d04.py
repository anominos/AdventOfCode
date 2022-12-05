*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"\d+",x)),]

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

n=0
for x in l:
    a,b,c,d = x
    if a<=c and b >= d:
        n+=1
    elif c<=a and d>=b:
        n+=1
print(n)

n=0
for x in l:
    a,b,c,d = x
    if a<=d and b>=c:
        n+=1
    elif d<=a and c>=b:
        n+=1

print(n)
