*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n\n"):
        if x!="":
            l.append(func(x))

seeds = [*map(int, re.findall(r"-?\d+", l[0]))]
cur = seeds[:]
cur2 = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

def process(i, b):
    # print(i)
    start, end = i
    l = []
    for dest, source, length in b:
        if source < end and source+length > start:
            ## is in range, split cur_range
            pre = (start, max(source, start))
            inn = (max(source, start), min(end, source+length))
            post = (min(end, source+length), end)
            # print(dest, source, length)
            # print(i, pre, inn, post)
            inn = (inn[0]+dest-source, inn[1]+dest-source)

            if pre[0] != pre[1]:
                l.append(pre)

            if inn[1] != inn[0]:
                l.append(inn)

            if post[1] != post[0]:
                l.extend(process(post, b))

            break
    else:
        l.append((start, end))
    return l


for x in l[1:]:
    a, *b = x.strip().split("\n")
    c, d = re.match("([a-z]+)-to-([a-z]+) map:", a).groups()
    b = [[*map(int, re.findall(r"-?\d+", i))] for i in b]
    b.sort(key=lambda a:a[1])
    l = []
    for i in cur:
        for j in b:
            if j[1]<=i<j[1]+j[2]:
                l.append(j[0]+(i-j[1]))
                break
        else:
            l.append(i)
    cur = l

    i = 0
    nw = []
    for i in cur2:
        nw.extend(process(i, b))
    cur2 = nw[:]


print(min(cur))
print(min(cur2)[0])