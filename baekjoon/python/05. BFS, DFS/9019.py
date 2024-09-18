import sys
input = sys.stdin.readline
from collections import deque
def bfs(s,e) :
    q = deque()
    q.append(s)
    v[s] = 1
    command = []
    while q :
        c = q.popleft()
        if c == e :
            return command
        for i in (0, 1, 2, 3) :
            if i == 0 :
                n = c * 2
                if n >9999 :
                    n = n% 10000
                if v[n] == 0 :
                    q.append(n)
                    command.append('D')
            elif i == 1 :
                n = c - 1
                if n < 0 :
                    n = 9999
                if v[n] == 0 :
                    q.append(n)
                    command.append('S')
                
T = int(input())
for _ in range (T) :
    s, e = map(int, input().split())
    v = [0]*10000
    ans = bfs(s, e)
    print (ans)