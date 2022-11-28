import re
states = {}
with open("d25in.txt") as f:
    state = f.readline()[-3]
    step = re.search(r"(\d+)", f.readline()).group(0)
    r = f.read().strip().split("\n\n")
    for x in r:
        mtch = re.match(r"In state (.):\s+If the current value is (1|0):\s+- Write the value (1|0).\s+- Move one slot to the (left|right).\s+- Continue with state (.)\.\s+If the current value is (1|0):\s+- Write the value (1|0).\s+- Move one slot to the (left|right).\s+- Continue with state (.)\.", x)
        s, *dat = mtch.groups()
        states[s] = [dat[:4], dat[4:]]
from collections import defaultdict
d = defaultdict(bool)
cur = 0
for _ in range(int(step)):
    _, new, dr, st = states[state][d[cur]]
    d[cur] = new=="1"
    if dr=="right":
        cur+=1
    else:
        cur-=1
    state = st
print(sum(d.values()))