import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이를 늘리기

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = [0] * (N+1)

def DFS(s):
    for n in arr[s]:
        if ans[n] == 0:  # 방문하지 않은 노드
            ans[n] = s   # 부모 노드 기록
            DFS(n)       # 재귀적 호출

ans[1] = 1  # 루트 노드의 부모는 자기 자신
DFS(1)

for i in range(2, N+1):
    print(ans[i])
