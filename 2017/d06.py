with open("d06in.txt") as f:
    for x in f:
        l = x.strip().split()

l = list(map(int,l))
prev = {}
c=0
while not tuple(l) in prev:
    prev[tuple(l)]=c
    i = l.index(max(l))
    j = l[i]
    l[i] = 0
    for _ in range(j):
        i+=1
        i%=len(l)
        l[i]+=1
    c+=1
print(len(prev))
print(c-prev[tuple(l)])