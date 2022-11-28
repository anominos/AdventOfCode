import sys
from time import daylight, process_time

ttt = process_time()
dat = []
with open("d1in.txt") as f:
    for x in f:
        dat.append(int(x.strip()))
'''
for x in dat:
    for y in dat:
        for z in dat:
            if int(z)+int(x)+int(y)==2020:
                print(int(z)*int(x)*int(y))
'''
'''
for x in range(len(dat)):
    for y in range(x+1, len(dat)):
        if dat[x]+dat[y]==2020:
            pt1=(dat[x]*dat[y])
        for z in range(y+1, len(dat)):
            if dat[x]+dat[y]+dat[z]==2020:
                pt2 =(dat[x]*dat[y]*dat[z])
'''
dat = set(dat)
for x in dat:
    if 2020-x in dat:
        pt1 = (x*(2020-x))
    for y in dat:
        if 2020-x-y in dat:
            pt2 = (x*y)*(2020-x-y)

print("silver:",pt1)
print("gold:",pt2)

print(process_time()-ttt)