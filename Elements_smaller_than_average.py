l=int(input())
n=list(map(int,input().split()))
s=sum(n)
a=s//l
c=0
for i in n:
    if(i<=a):
       c+=1
print(c)