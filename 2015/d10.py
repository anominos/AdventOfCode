pin = "3113322113"

from itertools import groupby
for _ in range(50):
    a = groupby(pin)
    new = ""
    for i, x in a:
        new+=str(sum(1 for _ in x))+i
    pin = new
    if _==39:
        print(len(pin))
print(len(pin))