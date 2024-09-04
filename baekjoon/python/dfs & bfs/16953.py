from collections import deque

def bfs(s,e) :
    q = deque([(s, 0)])
    v = set()
    v.add(s)
    
    while q :
        c, cnt = q.popleft()
        if c == e :
            return cnt +1
        for n in (c*2, c*10+1) :
            if n <= e and n not in v :
                q.append((n, cnt+1))
                v.add(n)
    return -1

A, B = map(int, input().split(" "))
ans = bfs(A,B)
print(ans)
