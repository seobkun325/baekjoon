N, K = map(int, input().split())
result = 0
while True :
    target = (N//K) *K
    result += (N-target)
    N = target

    if N < K :
        break
    result += 1
    N //= K

print(result+N-1)