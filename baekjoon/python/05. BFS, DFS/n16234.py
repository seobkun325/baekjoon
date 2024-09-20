import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]

def BFS(si,sj) :
    global ans
    q = []
    q.append((si,sj))
    lst.append((si,sj))
    v[si][sj] = 1
    sum = A[si][sj]
    while q : 
        ci, cj = q.pop(0)
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)) :
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and (L<=abs(A[ni][nj] - A[ci][cj])<=R) :
                q.append((ni, nj))
                lst.append((ni,nj))
                v[ni][nj] = 1
                sum += A[ni][nj]
    set(lst)
    if len(lst) > 1 :
        daily.append(lst+[sum//len(lst)])
def change() :
    for i in range(len(daily)):
        for j in range(len(daily[i])-1) :
            x,y = daily[i][j]
            t = daily[i][-1]
            A[x][y] = t
ans = 0
while True :
    chk = A
    daily = []
    v = [[0]*(N) for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            lst = []
            if v[i][j] == 0 :
                BFS(i,j)
    if daily :
        change()
        ans+=1
    else :
        break
print(ans)