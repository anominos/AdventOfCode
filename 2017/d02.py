s = []
with open("d02in.txt") as f:
    for x in f:
        s.append(list(map(int, x.strip().split())))
c=0
for x in s:
    c+=max(x)-min(x)
print("silver:",c)
def div(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            c, d= sorted([a[i], a[j]])
            if d%c==0:
                return d//c

c=0
for x in s:
    c+=div(x)
print("gold:", c)