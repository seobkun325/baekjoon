N, M = map(int, input().split())
lst = []

def dfs(s) :
    if (len(lst) == M) :
        print(' '.join(map(str, lst)))
        return
    for i in range(s, N+1) :
        lst.append(i)
        dfs(i+1)
        lst.pop()
        
dfs(1)