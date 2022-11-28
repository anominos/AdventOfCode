from collections import deque
step = 370

cur = 0
ans = -1
for x in range(50_000_000):
    cur+=step
    cur%=x+1
    cur+=1
    if cur==1:
        ans=x+1
print(ans)