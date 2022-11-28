with open("d09in.txt") as f:
    s = f.read().strip()


score = 0
add = 0
score2 = 0
i=0
while i < len(s):
    if s[i]=="<":
        while s[i]!=">":
            if (s[i]=="!"):
                i+=1
            else:
                score2+=1
            i+=1
        score2-=1
    elif s[i] == "{":
        add+=1
    elif s[i]=="}":
        score+=add
        add-=1
    i+=1

print(score)
print(score2)