tot = 0
c2=0
c=0
with open("d8in.txt") as f:
    for x in f:
        b = x.strip()
        tot+=len(b)
        c+=len(eval(b))
        c2+=b.count('"')+b.count("\\")+2
print(tot-c)
print(c2)