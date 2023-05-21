n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    if l.count(i)==i:
        e.append(i)

if not e:
    print(-1)
else:
    print(min(e),max(e),end=" ")