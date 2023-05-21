n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
k=[]
for i in l:
    if i>=a and i<=b:
        k.append(i)
for i in k:
    c+=i
print(c)