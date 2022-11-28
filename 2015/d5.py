a = []
with open("d5in.txt") as f:
    for x in f:
        a.append(x)

import re
pat = re.compile(r"(.)\1")
cc=0
for x in a:
    if any([i in x for i in "ab cd pq xy".split()]):
        continue
    if re.search(pat, x):
        c=0
        for y in "aeiou":
            c+=x.count(y)
        if c >=3:
            cc+=1
print(cc)

pat1 = re.compile(r"(..).*\1")
pat2 = re.compile(r"(.).\1")
cc=0
for x in a:
    if re.search(pat1, x) and re.search(pat2, x):
        cc+=1
print(cc)