pin = "iwrupvqb"
from hashlib import md5
x=0
g=True
while True:
    a = md5((pin+str(x)).encode()).hexdigest()
    if g and a[:5]=="00000":
        print(x)
        g=False
    if a[:6]=="000000":
        break    
    x+=1

print(x)