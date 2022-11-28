with open("d09in.txt") as f:
    inp = f.read()
inp = inp.replace(" ", "")

i=0
cs=0
while i<len(inp):
    if inp[i]=="(":
        end = inp[i:].index(")")+i
        a, b = map(int,inp[i+1:end].split("x"))
        i=end
        i+=a
        cs+=a*b
    else:
        cs+=1
    i+=1

def rec(s, mul):
    l = 0
    i=0
    while i<len(s):
        if s[i]=="(":
            end = s[i:].index(")")+i
            a, b = map(int,s[i+1:end].split("x"))
            i=end
            i+=a+1
            l+=rec(s[end+1:i], b)
        else:
            i+=1
            l+=1
    return l*mul


gld = rec(inp,1)
print("silver:",cs)
print("gold:",gld)