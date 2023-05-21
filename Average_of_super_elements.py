n=int(input())
l=list(map(int,input().split()))
e=[]
c=0
for i in l:
    if l.count(i)==i:
        e.append(i)

if not e:
    print(-1)
else:
    m=set(e)
    for i in m:
        c+=i
    a=c/len(m)
    print('%.2f'%a)