t=int(input())
for i in range(t):
    n=input()
    if len(n)>10:
        c=len(n)-2
        print(n[0]+str(c)+n[-1])
    else:
        print(n)
