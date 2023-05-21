n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
k=[]
for i in l:
    if i>=a and i<=b:
        k.append(i)
if not k:
    print(-1)
else:
    for i in k:
        print(i,end=" ")