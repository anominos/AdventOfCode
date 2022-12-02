*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []

def func(x):
    if "" in x:
        x.remove("")
    return [*map(int, x)]

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n\n"):
        l.append(func(x.split("\n")))

print(sum(max(l, key=sum)))
print(sum(map(sum, sorted(l, key=sum)[-3:])))
