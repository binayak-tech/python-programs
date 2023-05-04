tc=int(input())
for _ in range(tc):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    
    i=0
    mx=-float('INF');
    while i<=n-k:
        sum=0
        j=i
        while j<=i+k-1:
            sum+=arr[j]
            j+=1
        if sum>mx:
            mx=max(mx,sum)
        i+=1
    print(mx)