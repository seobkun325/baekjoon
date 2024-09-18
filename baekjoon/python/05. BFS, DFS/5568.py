import sys
input = sys.stdin.readline

def DFS(s,L) :
    global ans
    if L == 2 :
        return
    for n in arr[s] :
        check[n] += 1
        DFS(n,L+1)
    return
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
check = [0]*(n+1)
for _ in range(m) :
    a, b = map(int, input().split())
    arr[b].append(a)
    arr[a].append(b)
DFS(1, 0)
ans = 0
for x in check :
    if x != 0 :
        ans+=1
if ans == 0 :
    print(ans)
else :
    print(ans-1)
