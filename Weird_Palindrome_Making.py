n=int(input())
for i in range(n):
    c=0
    a=int(input())
    b=list(map(int,input().split()))
    s=len(b)
    for j in range(0,s):
        if b[j]%2!=0:
            c=c+1
    print(c//2)    