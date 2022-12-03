*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []


def func(x):
    return x.split(" ")

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!= "":
            l.append(func(x))
#me    rps
wl = [[3,6,0],#r
      [0,3,6],#p
      [6,0,3]]#s


c=0
c2 = 0
for a,x in l:
    a = ord(a) - ord("A")
    x = ord(x) - ord("X")
    c+= wl[a][x]
    c += x + 1
    c2 += [0,3,6][x]
    c2 += 1+wl[a].index([0,3,6][x])
print(c)
print(c2)
