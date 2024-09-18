import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag= [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]
for _ in range(N) :
    w, v = map(int, input().split())
    bag.append([w,v])
for i in range(N) :
    for j in range(1, K+1) :
        w,v = bag[i]
        if j >= w :
            dp[i][k]
