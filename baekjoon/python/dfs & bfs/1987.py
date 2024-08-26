import sys
input = sys.stdin.readline
def dfs(ci, cj, cnt) :
    global ans
    ans = max(ans, cnt)
    for di, dj in ((-1,0), (1,0), (0,1), (0,-1)) :
        ni, nj = ci + di, cj + dj
        if 0<=ni<R and 0<=nj<C and not v[ord(arr[ni][nj])]:
            v[ord(arr[ni][nj])] = 1
            dfs(ni, nj, cnt+1)
            v[ord(arr[ni][nj])] = 0
R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]
ans = 1
v = [0]*128
v[ord(arr[0][0])] = 1
dfs(0,0,1)
print(ans)