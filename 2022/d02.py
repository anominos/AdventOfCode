*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []


def func(x):
    return str(x)

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        l.append(func(x))
