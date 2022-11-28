nums = [2,0,6,12,1,3]
prev = nums[:]
from collections import defaultdict
d = defaultdict(list)
for i,x in enumerate(nums):
    d[x].append(i)
for i in range(len(nums), 30000000):
    if i%1_000_000 == 0:
        print(i)
    # print(prev)
    if len(d[prev[-1]])==1:
        prev.append(0)
    else:
        prev.append(d[prev[-1]][-1] - d[prev[-1]][-2])
    d[prev[-1]].append(i)
print(prev[-1])
