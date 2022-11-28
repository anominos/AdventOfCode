l=[]
with open("d01in.txt") as f:
    for x in f:
        l.append(int(x.strip()))
print(sum(l))
c=0
past = set()
f=True
while f:
    for x in l:
        c+=x
        if c in past:
            print(c)
            f=False
            break
        past.add(c)
