*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

nums = "one, two, three, four, five, six, seven, eight, nine".split(", ")
l1 = []
l2 = []
import re
def func1(x):
    return [*map(int, re.findall(r"-?\d",x)),]
    # return str((x))

def func2(x):
    for i, n in enumerate(nums, start=1):
        x = x.replace(n, n+str(i)+n)
    return [*map(int, re.findall(r"-?\d",x)),]
    # return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l1.append(func1(x))
            l2.append(func2(x))



sm = 0
for x in l1:
    sm += x[0]*10 + x[-1]
    # print(x)
print(sm)

sm = 0
for x in l2:
    sm += x[0]*10 + x[-1]
    # print(x)
print(sm)