import sys
input = sys.stdin.readline
n = int(input())
if n == 0 :
    print(0)
    quit()
elif n == 1 :
    print(1)
    quit()
else :
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1) :
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n])