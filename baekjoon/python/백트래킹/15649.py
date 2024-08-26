import sys
input = sys.stdin.readline

def back(n,lst) :
    if n == M :
        ans.append(lst)
        return
    for j in range(1, N+1) :
        if v[j] == 0 :
            v[j] = 1
            back(n+1,lst+[j])
            v[j] = 0
N, M = map(int, input().split())
v = [0] *(N+1)
ans =[]
back(0,[])
for lst in ans :
    print(*lst)