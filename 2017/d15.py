afac = 16807
bfac = 48271
mod = 2147483647
aval = 634
bval = 301
from time import time
ttt = time()
c=0
for _ in range(40_000_000):
    aval*=afac
    aval%=mod
    bval*=bfac
    bval%=mod
    if aval%(2**16)==bval%(2**16):
        c+=1

print(c)
print(time()-ttt)
ttt = time()
aval = 634
bval = 301
c=0
for _ in range(5_000_000):
    while True:
        aval*=afac
        aval%=mod
        if aval%4==0:
            break
    while True:
        bval*=bfac
        bval%=mod
        if bval%8==0:
            break
    if aval%(2**16)==bval%(2**16):
        c+=1

print(c)
print(time()-ttt)