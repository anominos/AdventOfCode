dat = []
with open("d8in.txt") as f:
    for x in f:
        dat.append(x.strip().split(" | "))

valids = ["abcefg", "cf", "acdeg", "acdfg", "bdcf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
ch = set(valids)
from itertools import combinations, permutations
c=0
a=0
print("abcdef" in ch)
for x in dat:
    c+=len([i for i in x[1].split() if len(i) in [2,3,4,7]])
    for y in permutations("abcdefg"):
        d = dict(zip(y,"abcdefg"))
        ch = ["".join(sorted((map(d.get, i)))) for i in valids]
        r = set(ch)

        # if "".join(y) == "cfgabde":
        #     print(d)
        #     print(ch)
        #     print(x[0].split())
        if all("".join(sorted(z)) in r for z in x[0].split()):
            break
    # print(x[0].split(), ch)
    # print(ch)
    n = "".join([str(ch.index("".join(sorted(i)))) for i in x[1].split()])
    a+=int(n)
    # print(a)

print(c)
print(a)