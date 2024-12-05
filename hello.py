l=list(map(int,input().split()))
s={}
for val in l:
    if val not in s:
        s[val]=1
    else:
        s[val]+=1
print("ANSWER",s)
