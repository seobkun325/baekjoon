N = int(input())
dp = [0]*N
if N >= 1:
    dp[0] = 1
if N >= 2 :
    dp[1] = 2
if N >= 3 :
    for i in range(2,N) :
        dp[i] = (dp[i-1] + dp[i-2])%10
print(dp[N-1])