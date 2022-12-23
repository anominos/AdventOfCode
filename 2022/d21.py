*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

d = {}
for x in l:
    a, b = x.split(": ")
    try:
        d[a] = int(b)
    except ValueError:
        d[a] = b.split()

def get(x, r = False):
    if r:
        if x == "humn":
            return "notvar"
        if x == "root":
            return get(d[x][0], r), get(d[x][2], r)

    if isinstance(d[x], int):
        return str(d[x])

    op = d[x][1]

    a = get(d[x][0], r)
    b = get(d[x][2], r)
    try:
        a = eval(a)
    except NameError:
        pass
    try:
        b = eval(b)
    except NameError:
        pass

    c = f"({a} {op} {b})"
    return c


print(int(eval(get("root"))))
expr = (get("root", True))
import sympy as sp
notvar = sp.symbols("notvar")
eq = sp.Eq(eval(expr[0]), eval(expr[1]))
sol = sp.solve(eq)
print(int(sol[0]))
