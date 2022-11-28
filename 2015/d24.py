dat = []
with open("d24in.txt") as f:
    for x in f:
        dat.append(int(x.strip()))

from functools import lru_cache

@lru_cache(maxsize=None)
def knapsack(sm, n):
    if sm == 0:
        return (1,1)
    if n==0:
        return (float("inf"), float("inf"))
    if dat[n-1] > sm:
        return knapsack(sm, n-1)
    else:
        a = knapsack(sm-dat[n-1], n-1)
        a = (a[0]+1, a[1]*dat[n-1])
        return min(a, knapsack(sm,n-1))


sm = sum(dat)
dp = [[(float("inf"), float("inf"))]*(sm+1) for _ in range(len(dat)+1)]
for x in range(len(dat)):
    dp[x][0] = (1,1)

for n in range(1,len(dat)+1):
    for s in range(1,sm+1):
        if dat[n-1] > s:
            dp[n][s] = dp[n-1][s]
        else:
            a = dp[n-1][s-dat[n-1]]
            a = (a[0]+1, a[1]*dat[n-1])
            dp[n][s] = min(a, dp[n-1][s])

print(dp[len(dat)][sm//3][-1])
print(dp[len(dat)][sm//4][-1])