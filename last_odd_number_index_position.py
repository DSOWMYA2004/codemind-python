l=int(input())
n=list(map(int,input().split()))
for i in range(len(n)-1,-1,-1):
    if(n[i]%2!=0):
        print(i)
        break