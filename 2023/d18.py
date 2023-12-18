*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return x.split()

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math

corners1 = []
corners2 = []
cur1 = [0, 0]
cur2 = [0, 0]

d = dict(zip("UDLR", [(-1, 0), (1, 0), (0, -1), (0, 1)]))
for a, b, c in l:
    cur_dir = d[a]
    dist = int(b)
    cur1[0] += cur_dir[0]*dist
    cur1[1] += cur_dir[1]*dist
    corners1.append(tuple(cur1))
    cur_dir = d["RDLU"[int(c[-2])]]
    dist = int(c[2:-2], 16)
    cur2[0] += cur_dir[0]*dist
    cur2[1] += cur_dir[1]*dist
    corners2.append(tuple(cur2))

def shoelace(corners):
    arr = np.vstack(corners)
    i = np.arange(len(arr))

    d = (np.abs(np.sum((arr[i-1,0] * arr[i,1]) - (arr[i-1,1]*arr[i,0])))//2)
    # print(np.append(arr, arr[0], axis=0))
    d+=(np.sum(np.abs(np.diff(np.append(arr, [arr[0]], axis=0), axis=0))))//2
    return d+1


def do_corners(corners):
    mnx, mny = corners[0]
    for x in corners:
        mnx = min(mnx, x[0])
        mny = min(mny, x[1])

    corners = [(i-mnx, j-mny) for (i, j) in corners]
    mxx, mxy = corners[0]
    for x in corners:
        mxx = max(mxx, x[0])
        mxy = max(mxy, x[1])

    # prev = {}
    # nxt = {}
    # for i in range(len(corners)-1):
    #     prev[corners[i+1]] = corners[i]
    #     nxt[corners[i]] = corners[i+1]

    es = defaultdict(list)
    for x, y in corners:
        es[x].append(y)


    fill = set()

    def get_max(a: list[set],b: list[set]):
        combine = sorted(a+b, key=min)
        combine = [[min(i), max(i)] for i in combine]
        res = [combine[0]]
        for i in combine:
            if res[-1][1] >= i[0]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        # print(a, b, res)
        c=0
        for e, f in res:
            # for i in range(a, b+1):
            #     fill.add((x, i))
            c += f-e+1
        return c




    # prev[edges[0]] = edges[-1]
    # nxt[edges[-1]] = edges[0]
    c=0

    cur_intervals = []
    from copy import deepcopy
    prevx = -1
    for x, lx in sorted(es.items()):
        # print(x, sorted(cur_intervals, key=min))
        # for i in range(prevx+1, x):
        #     for j in cur_intervals:
        #         for k in range(min(j), max(j)+1):
        #             fill.add((i, k))
        for g in cur_intervals:
            c += (max(g)-min(g)+1) * (x-prevx-1)
        orig_ints = deepcopy(cur_intervals)
        a = sorted(lx)
        for w, v in zip(a[::2], a[1::2]):
            touched: list[set] = []
            for i in cur_intervals:
                if w in i:
                    touched.append(i)
                elif v in i:
                    touched.append(i)
            if len(touched) == 1:
                i = touched[0]
                if w in i and v in i:
                    i.remove(w)
                    i.remove(v)
                    # print("a")
                    # c+= w-v+1
                elif w in i:
                    i.remove(w)
                    i.add(v)
                    # print("b")
                    # c+= max(*i,w,v) - min(*i,w,v) + 1
                elif v in i:
                    i.remove(v)
                    i.add(w)
                    # print("c")
                    # c+= max(*i,w,v) - min(*i,w,v) + 1
            elif len(touched) == 2:
                s={min(*touched[0], *touched[1]), max(*touched[0], *touched[1])}
                cur_intervals.append(s)
                # c += max(w, v) - min(w, v) - 1
                # for i in range(min(w, v)+1, max(w, v)):
                #     fill.add((x, i))
                # print("d")
                # c += max(s) - min(s) + 1
                touched[0].clear()
                touched[1].clear()
            else:
                for i in cur_intervals:
                    if i != set() and min(i) <= min(w, v) and max(i) >= max(w, v):
                        # c += max(i) - min(i) + 1
                        cur_intervals.append({max(i), max(w, v)})
                        i.remove(max(i))
                        i.add(min(w, v))
                        # print("e")
                        # print(i)
                        break
                else:
                    # print("f")
                    cur_intervals.append({w, v})
                    # c += max(w, v) - min(w, v) + 1

        cur_intervals = [i for i in cur_intervals if len(i) > 0]

        c += get_max(orig_ints, cur_intervals)
        # for a,b in orig_ints + cur_intervals:
        #     for i in range(min(a, b), max(a,b)+1):
        #         fill.add((x, i))

        prevx = x
    print(c)

    # for x in range(mxx+1):
    #     for y in range(mxy+1):
    #         if (x, y) in fill:
    #             print(end="#")
    #         else:
    #             print(end=".")
    #     print()


do_corners(corners1)
do_corners(corners2)