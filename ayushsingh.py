a=[1,3,49,100,2,77,61,63]
d=[0]*len(a)
d[0]=a[0]
for i in range(1,len(a)):
    d[i]=a[i]-a[i-1]
l=1
r=5
x=3
d[l]+=x
if r+1<len(d):
    d[r+1]-=x
arr=[0]*len(d)
arr[0]=d[0]
for i in range(1,len(d)):
    arr[i]=arr[i-1]+d[i]
print(arr)