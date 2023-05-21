n=int(input())
l=list(map(int,input().split()))
if len(l)%2!=0:
    l.append(0)
for i in l:
    print(i,end=" ")