import sys
from collections import Counter
dat = []
with open("d2in.txt") as f:
    for x in f:
        dat.append((x.strip()))
'''
cc=0
c2=0
for x in dat:
    a, b, c = x.split()
    low, high = map(int, a.split("-"))
    char = b[0]
    # c =Counter(c)
    # if low<=c[char]<=high:
    #     cc+=1
    # print(char, c[low-1], c[high-1], ((c[low-1]==char) + (c[high-1]==char))==1)
    if (c[low-1]==char or c[high-1]==char) and c[low-1]!=c[high-1]:
        c2+=1
# print(cc)
print(c2)'''

cc=0
c2=0
for x in dat:
    a, b, c = x.split()
    low, high = map(int, a.split("-"))
    char = b[0]
    d=Counter(c)
    if low<=d[char]<=high:
        cc+=1
    if (c[low-1]+c[high-1]).count(char)==1:
        c2+=1
print("silver:", cc)
print("gold:",c2)