d1,d2,d3=map(int,input().split())
a=d1+d3+d2
b=d1+d1+d2+d2
c=d1+d3+d3+d1
d=d2+d3+d3+d2
if a<=b and a<=c and a<=d:
    print(a)
elif b<=a and b<=c and b<=d:
    print(b)
elif c<=a and c<=b and c<=d:
    print(c)
else:
    print(d)
