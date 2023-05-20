l=int(input())
n=list(map(int,input().split()))
o=[]
for i in n:
    if(i%2!=0):
        o.append(i)
print(o[-1])