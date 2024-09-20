import sys
input = sys.stdin.readline
def RGB(si, sj) :
    q = []
    key = arr[si][sj]
    q.append((si,sj))
    v[si][sj] = 1
    while q :
        ci, cj = q.pop(0)
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)) :
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == key :
                q.append((ni,nj))
                v[ni][nj] = 1

N = int(input())
arr = [list(input().strip())for _ in range(N)]
v = [[0]*(N) for _ in range(N)]
ans1 = 0
ans2 = 0
for i in range(N) : 
    for j in range(N) :
        if v[i][j] == 0 :
            RGB(i,j)
            ans1+=1
        if arr[i][j] == 'R' :
            arr[i][j] = 'G'
v = [[0]*(N) for _ in range(N)]
for i in range(N) : 
    for j in range(N) :
        if v[i][j] == 0 :
            RGB(i,j)
            ans2+=1

print(ans1,ans2)
