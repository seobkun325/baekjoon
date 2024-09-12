import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())) :
    command = list(input().strip())
    n = int(input())
    line = input().strip()
    if line == "[]":
        s = deque()
    else:
        s = deque(map(int, line[1:-1].split(',')))
    flow = 1
    error = 0
    for x in command :
        if x == 'R' :
            flow *= -1
        elif x == 'D':
            if not s :
                error = 1
                break
            elif flow == 1 :
                s.popleft()
            elif flow == -1 :
                s.pop()
    if error > 0 :
        print('error')
    else:
        if flow == 1 :
            print(f"[{','.join(map(str, s))}]")
        else :
            print(f"[{','.join(map(str, reversed(s)))}]")
