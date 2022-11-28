import re
slr = 0
def rot(a,s):
    return chr((ord(a)-ord("a")+s)%26+ord("a"))

with open("d04in.txt") as f:
    for x in f:
        a,b,c = re.match(r"(.*)-(\d+)\[(.*)\]",x).groups()
        a = a.split("-")
        a = "".join(a)
        r = "".join(sorted(set(a), key=lambda i:[a.count(i), -ord(i)], reverse=True))[:5]
        if r==c:
            slr+=int(b)
            if "north" in "".join(map(lambda i:rot(i, int(b)),a)):
                gld = b
print("silver:",slr)
print("gold:", gld)