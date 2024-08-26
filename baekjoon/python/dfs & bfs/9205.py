from collections import deque

def bfs(sj, si, ej, ei):
    q = deque()
    v = [0]*n
    q.append((sj,si))

    while q:
        cj, ci = q.popleft()
        if abs(cj-ej) + abs(ci-ei) <= 1000 :
            return 'happy'

        for i in range(n) :
            if v[i] == 0:
                nj, ni = cvs[i]
                if abs(cj-nj) + abs(ci-ni) <=1000 :
                    q.append((nj,ni))
                    v[i] = 1
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    sj, si = map(int, input().split())
    cvs = []
    for _ in range(n) :
        j,i = map(int, input().split())
        cvs.append((j,i))
    ej, ei = map(int, input().split())
    ans = bfs(sj, si, ej, ei)
    print(ans)
