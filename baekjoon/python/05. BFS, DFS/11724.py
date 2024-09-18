import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
v = [0]*(N+1)
def BFS(s) :
    q = []
    v[s] = 1
    q.append(s)
    while q :
        c = q.pop(0)
        for n in arr[c] :
            if v[n] == 0 :
                v[n] = 1
                q.append(n)
    return
ans = 0
for i in range(1,N+1) :
    if v[i] == 0 :
        BFS(i)
        ans += 1
print(ans)