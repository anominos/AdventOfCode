*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

t, d = l
m=1
for i in range(len(t)):
    c=0
    for hold in range(t[i]+1):
        if (t[i] - hold) * hold > d[i]:
            c+=1

    m*=c
print(m)

t = int("".join(map(str, t)))
d = int("".join(map(str, d)))

# low
lb = 0
ub = t//2
mn = 1e12
while lb < ub:
    m = (lb+ub)//2
    if (t - m) * m < d:
        lb = m+1
    else:
        ub = m-1

print(t - 2*lb + 1)
