with open("d05in.txt") as f:
    data = f.read().strip()
from string import ascii_lowercase as alph
ans = float("inf")
for rem in alph+" ":
    dat = list(data.replace(rem, "").replace(rem.upper(), ""))
    x=0
    while x < len(dat)-1:
        polarity = dat[x].islower()
        if polarity:
            if dat[x+1].isupper() and dat[x+1]==dat[x].upper():
                del dat[x+1]
                del dat[x]
                x-=2
        else:
            if dat[x+1].islower() and dat[x+1]==dat[x].lower():
                del dat[x+1]
                del dat[x]
                x-=2
        x+=1
        x = max(x, 0)
    if rem==" ":print(len(dat))
    ans = min(ans, len(dat))
print(ans)