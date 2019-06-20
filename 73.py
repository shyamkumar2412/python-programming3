n=int(input())
l,r=map(int,input().split())
for i in range(l,r):
    if(i==n):
        print("yes")
        break
else:
    print("no")
