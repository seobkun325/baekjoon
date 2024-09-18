import sys
input = sys.stdin.readline
N = int(input())
T = []
P = []
for _ in range(N) :
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0]*(N+1)
for i in range(N) :
    if i > 0 :
        dp[i] = max(dp[i], dp[i-1])
    idx = i+T[i]
    if idx <= N:
        dp[idx] = max(dp[idx],dp[idx-1],dp[i]+P[i])
dp[N] = max(dp[N],dp[N-1])
print(dp[N])