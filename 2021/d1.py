dat = []
with open("d1in.txt") as f:
    for x in f:
        dat.append(int(x.strip()))
c=0
for x in range(1, len(dat)):
    if dat[x] > dat[x-1]:
        c+=1
print(c)
l =[]
for x in range(3, len(dat)+1):
    l.append(sum(dat[x-3:x]))
c=0
for x in range(1, len(l)):
    if l[x] > l[x-1]:
        c+=1
print(c)