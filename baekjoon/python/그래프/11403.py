import sys
input = sys.stdin.readline


n = int(input())
v = [[0]*n for _ in range(n)]
graph = [list(map(int, input().split(" "))) for _ in range (n)]



def bfs(s) :
    q = []
    q.append(s)
    ch = [0]*n
    while q :
        c = q.pop(0)
        for next in range(n) :
            if ch[next] == 0 and graph[c][next] == 1 :
                q.append(next)
                ch[next] = 1
                v[s][next] = 1
for i in range(n) :
    bfs(i)
for i in v :
    print(*i)