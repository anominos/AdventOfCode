*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

x = l[0]

for i in range(len(x)):
    if len(set(x[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(x)):
    if len(set(x[i:i+14])) == 14:
        print(i+14)
        break
