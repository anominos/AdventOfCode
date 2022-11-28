from collections import deque
n = list(map(int, list("739862541")+list(range(10, 1_000_001))))
cur = 0

d = {}
for x in range(len(n)-1):
    d[n[x]] = n[x+1]
d[n[-1]] = n[0]

cur = n[0]
for turn in range(10_000_000):
    # print(d, cur)
    a = d[cur] #n+1
    c = d[d[a]] #n+3
    d[cur] = d[c] #remove n+1:n+3
    dest = (cur)
    while dest in [cur, a, c, d[a]]:
        dest-=1
        if dest < 1:
            dest = 1_000_000
    end = d[dest]
    d[dest] = a
    d[c] = end
    cur = d[cur]
print(d[1]*d[d[1]])
