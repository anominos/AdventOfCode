l=[]
with open("d20in.txt") as f:
    for x in f:
        l.append(list(map(int,x.strip().split("-"))))
maxx = 4294967295
'''
maxx = 9
l = [[5, 8], [0, 2], [4,7]]
'''
l.sort()
low=0
i=0
pr = True
c=0
while i < len(l):
    if low<l[i][0]:
        if pr:
            print("silver:",low)
            pr = False
        c+= (l[i][0] if i < len(l)-1 else maxx)-low
    low = max(low, l[i][1]+1)
    i+=1
if low <= maxx:
    c+=maxx-low+1
print("gold:",c)