import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
s = []
ans = [0]*N
for i in range(N) :
    while s :
        if s[-1][1] > top[i] :
            ans[i] = s[-1][0] + 1
            break
        else :
            s.pop()
    s.append([i, top[i]])
print(*ans)