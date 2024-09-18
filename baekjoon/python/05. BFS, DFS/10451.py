import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이를 늘리기
def DFS(s) :
    if v[s] == 1 :
        return
    v[s] = 1
    DFS(arr[s])
    return
T = int(input())
for _ in range(T) :
    N = int(input())
    cnt = 0
    arr = list(map(int ,input().strip().split()))
    arr = [0] + arr
    v = [0]*(N+1)
    for i in range(1,N+1) :
        if v[i] == 0 :
            DFS(i)
            cnt += 1
    print(cnt)
    