lst = list(range(256))

dat = open("d10in.txt").read().strip()
lengths = dat.split(",")
# lst = list(range(5))
# lengths = [3, 4, 1, 5]


def a(lengths, ss, lst, shifted):

    for x in lengths:
        x = int(x)
        lst = lst[:x][::-1]+lst[x:]
        #lst.rotate(-x-ss)
        lst = lst[(x+ss)%len(lst):]+lst[:(x+ss)%len(lst)]
        shifted += x+ss
        ss+=1

    #shifted -= x+ss-1
    shifted%=len(lst)
    return ss, lst, shifted

_, b, s = a(lengths, 0, lst, 0)
s = len(lst)-s

b = b[s:]+b[:s]
print(b[0]*b[1])


lengths = list(map(ord, dat))
lengths+=[17, 31, 73, 47, 23]
s=0
sh=0
l = list(range(256))
for _ in range(64):
    s, l, sh = a(lengths, s, l, sh)
sh = len(l)-sh
l = l[sh:]+l[:sh]
from functools import reduce
s=[]
def pad(s):
    if len(s)==1:
        return "0"+s
    return s
for x in range(0,256,16):
    s.append(reduce(lambda a, b:a^b, l[x:x+16]))
s = map(lambda a:pad(hex(a)[2:]), s)
print("".join(s))
