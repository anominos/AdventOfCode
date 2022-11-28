# from d16 import *
# ##d16 only contains editedDict = doLine(line, dict)
# dat = []
# with open("d21in.txt") as f:
#     for x in f:
#         dat.append(x.strip().split())
# from collections import Counter
# ip = int(dat[0][1])
# dat = dat[1:]


# d = [0]*6
# d[0] = 12213578
# states = Counter()
# while d[ip] < len(dat):
#     states[d[ip]]+=1
#     # if states[d[ip]] > 50:break
#     line = dat[d[ip]]
#     line = [int(i) if i.isdigit() else i for i in line]
#     d = doLine(line, d)
#     d[ip]+=1
#     print(d[ip], dat[d[ip]], d)


r4 = 0
s = set()
l = []
while not r4 in s:
    s.add(r4)
    l.append(r4)
    r5 = r4 | 65536
    r4 = 1765573
    while True:
        r1 = r5 % 256
        r4 += r1
        r4 = r4 * 65899
        r4 = r4 % 16777216
        if r5 < 256:
            break
        r5 = r5//256
print(l[1])
print(l[-1])
# < 15949699