n=int(input())
l=list(map(int,input().split()))
p=[]
length=len(l)
for i in range(length//2):
    p.append(l[i])
    p.append(l[length-i-1])
if length%2!=0:
    p.append(l[length//2])
    p.append(0)
for i in p:
    print(i,end=' ')