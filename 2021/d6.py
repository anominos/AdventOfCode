dat = [2,1,1,4,4,1,3,4,2,4,2,1,1,4,3,5,1,1,5,1,1,5,4,5,4,1,5,1,3,1,4,2,3,2,1,2,5,5,2,3,1,2,3,3,1,4,3,1,1,1,1,5,2,1,1,1,5,3,3,2,1,4,1,1,1,3,1,1,5,5,1,4,4,4,4,5,1,5,1,1,5,5,2,2,5,4,1,5,4,1,4,1,1,1,1,5,3,2,4,1,1,1,4,4,1,2,1,1,5,2,1,1,1,4,4,4,4,3,3,1,1,5,1,5,2,1,4,1,2,4,4,4,4,2,2,2,4,4,4,2,1,5,5,2,1,1,1,4,4,1,4,2,3,3,3,3,3,5,4,1,5,1,4,5,5,1,1,1,4,1,2,4,4,1,2,3,3,3,3,5,1,4,2,5,5,2,1,1,1,1,3,3,1,1,2,3,2,5,4,2,1,1,2,2,2,1,3,1,5,4,1,1,5,3,3,2,2,3,1,1,1,1,2,4,2,2,5,1,2,4,2,1,1,3,2,5,5,3,1,3,3,1,4,1,1,5,5,1,5,4,1,1,1,1,2,3,3,1,2,3,1,5,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,1,5,2,4,5,5,1,1,5,1,5,5,1,1,3,3,1,1,3,1]
# n = [[i] for i in range(min(dat), max(dat)+1)]
from collections import Counter
d = Counter(dat)
for day in range(256):
    cpy = Counter()
    for x in d.keys():
        if x==0:
            cpy[6] += d[x]
            cpy[8]+= d[x]
        else:
            cpy[x-1]+=d[x]
    d = cpy
    if day==79:
        print(sum(d.values()))
print(sum(d.values()))
# for st in range(len(n)):
#     for day in range(256):
#         for x in range(len(n[st])):
#             if n[st][x] == 0:
#                 n[st][x] = 6
#                 n[st].append(8)
#             else:
#                 n[st][x]-=1
#         input(n[st])
# n = list(map(len, n))

