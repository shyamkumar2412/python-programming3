l=list(map(int,input().split()))
n=0
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]<l[j]:
            n=l[i]
for k in range(0,len(l)):
    if l[k]<n:
        n=l[k]
print(n)
