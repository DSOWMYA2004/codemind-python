n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    m=min(a)
    print(m,end=" ")
    a.remove(m)