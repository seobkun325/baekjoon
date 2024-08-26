import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = {} 
    for _ in range(n):
        a, b = input().split()
        if b not in arr:
            arr[b] = []
        arr[b].append(a)
    ans = 1
    for i in arr :
        ans *= (len(arr[i])+1)
    print(ans-1)