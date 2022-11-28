a = 15628416
b = 11161639

# a = 5764801
# b = 17807724

mod = 20201227
'''
7 ** n % mod == a
7 ** m % mod == b
7 ** n == a + x * mod
n = log(a+x*mod, 7)
m = log(b+y*mod, 7)
'''
mm = 1
for g in [a, b]:
    m=1
    c=0
    while m!=g:
        m*=7
        m%=mod
        c+=1

    mm*=c

print(pow(7, mm, mod))

'''
(7 ** nm)% mod = key
'''