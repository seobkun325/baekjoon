Tc = int(input())
for _ in range (Tc) :
    n = int(input())
    dp = [list(map(int, input().strip().split(' '))) for _ in range(2)]
    for i in range(0, n) :
        if i == 0 :
            continue
        elif i == 1 :
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
        else :
            dp[0][i] += max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
    print (max(dp[0][n-1], dp[1][n-1]))