for _ in range(int(input())):
    n, k = map(int, input().split())
    girls_per_km = list(map(int, input().split()))[:n]
    
    max_impressed = -float('inf')
    
    for i in range(n-(k-1)):
        total = 0
        for j in range(i, i+k):
            total += girls_per_km[j]
        max_impressed = max(max_impressed, total)

    print(max_impressed)