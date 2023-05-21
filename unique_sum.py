n=int(input())
l=list(map(int,input().split()))
c=0;
m=set(l)
for i in m:
    c+=i
print(c)