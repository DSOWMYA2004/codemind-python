n=int(input())
l=list(map(int,input().split()))

e=[]
for i in l:
    if l.count(i)==i:
        e.append(i)
m=set(e)
print(len(m));