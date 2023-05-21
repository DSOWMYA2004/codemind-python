n=int(input())
l=list(map(int,input().split()))
c=0
p=set(l)
for i in p:
    if(i%2==0):
       c+=i
print(c)