*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

works = {}
parts = []
import re
def func(x):
    d = {}
    for i in x[1:-1].split(","):
        a, b = i.split("=")
        d[a] = int(b)
    return d

with open(f"{a}/input/{b}.txt") as f:
    a, b = f.read().split("\n\n")
    for x in a.strip().split("\n"):
        c, d = (re.match(r"([a-z]+)\{(.+)\}", x).groups())
        works[c] = d.split(",")

    for x in b.strip().split("\n"):
        parts.append(func(x))


from collections import *
import numpy as np
import math

def check(part):
    cur = "in"
    while True:
        for rule in works[cur]:
            if ":" not in rule:
                if rule in "RA":
                    return rule
                else:
                    cur = rule
                    break
            check, res = rule.split(":")
            for a in "xmas":
                check = check.replace(a, str(part[a]))
            if eval(check):
                if res in "RA":
                    return res
                else:
                    cur = res
                    break
c=0
for x in parts:
    if check(x) == "A":
        c += sum(x.values())
print(c)

ranges = []

def inverse(s):
    return s.replace(">", "..").replace("<", ">=").replace("..", "<=")

def simplify(l: list[str]):
    l = sorted(l)
    rs = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    for x in l:
        if ">=" in x:
            a, b = x.split(">=")
            rs[a][0] = max(rs[a][0], int(b))
        elif "<=" in x:
            a, b = x.split("<=")
            rs[a][1] = min(rs[a][1], int(b))
        elif ">" in x:
            a, b = x.split(">")
            rs[a][0] = max(rs[a][0], int(b)+1)
        elif "<" in x:
            a, b = x.split("<")
            rs[a][1] = min(rs[a][1], int(b)-1)
    for x in rs.values():
        if x[0] > x[1]:
            return None
    return rs


def dfs(cur, cur_range: list[list[int]]):
    if cur=="A":
        if (y:=simplify(cur_range.copy())) is not None:
            ranges.append(y)
        return
    if cur=="R":
        return
    for x in works[cur]:
        if ":" in x:
            a, b = x.split(":")
            r = cur_range.copy()
            r.append(a)
            dfs(b, r)
            cur_range.append(inverse(a))
        else:
            dfs(x, cur_range)

dfs("in", [])
c2=0
for x in ranges:
    m=1
    for a, b in x.values():
        m*= b-a+1
    c2+=m
print(c2)