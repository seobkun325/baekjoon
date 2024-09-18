import sys
from collections import deque
input = sys.stdin.readline

def bfsmax(s) :
    q = deque()
    v = [[0]*3 for _ in range (n)]
    q.append((0,s))
    v[0][s] = 1
    while q :
        ci, cj = q.popleft()
        for di, dj in (1,0), (1,1), (1,-1) :
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<3 and v[ni][nj] == 0 :
                q.append((ni,nj))
                v[ni][nj] = 1
                max = max(max, arr[ni][nj])
    
n = int(input())
arr = list(map(int, input().split()) for _ in range(n))

max = 0
min = 999999999
answer = []
answer.append(bfsmax)