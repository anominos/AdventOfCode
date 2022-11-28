with open("d01in.txt") as f:
    for x in f:
        r = x.strip()
c=0
for x in range(len(r)):
    if r[x]==r[(x+1)%len(r)]:
        c+=int(r[x])
print("silver:", c)
c=0
l = len(r)//2
for x in range(len(r)):
    if r[x] == r[(x+l)%len(r)]:
        c+=int(r[x])
print("gold:",c)