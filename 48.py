n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
  c=c+i
avg=c//n
print(avg)
