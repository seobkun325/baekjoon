import sys
input = sys.stdin.readline

def bfs(si, sj) :
    q = []
    q.append((si, sj))
    v[si][sj] = 0
    while q :
        ci, cj = q.pop(0)
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)) :
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<m and v[ni][nj] == -1 and arr[ni][nj] == 1 :
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


n ,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]
v = [[-1]*m for _ in range (n)]
si= 0
sj = 0
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 2 :
            si = i
            sj = j
        if arr[i][j] == 0 :
            v[i][j] = 0
bfs(si, sj)
for i in range(n) :
    for j in range(m) :
        print(v[i][j],end=" ")
    print()