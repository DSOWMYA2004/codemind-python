n=int(input())
l=list(map(int,input().split()))
k=int(input())
e=[]
for i in l:
    if l.count(i)==k:
        e.append(i)

if not e:
    print(-1)
else:
    m=set(e)
    for i in m:
        print(i,end=" ")