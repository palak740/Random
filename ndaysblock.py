n=int(input())
l=list(map(int, input().split()))
c=sorted(l)
for i in range(n):
    if(l[i]==max(c)):
        rp=c[n-i-1:n]
        for j in rp[::-1]:
            print(j,end=" ")
        print(sep='\n')
        del c[n-i-1:n]
