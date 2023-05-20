n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
for i in range(len(b)):
    print(b[i],end=" ")
    