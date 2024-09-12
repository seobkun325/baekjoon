import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
ans =[-1]*N
for idx, val in enumerate(A) :
    while stack and stack[-1][0] < val:
        ans[stack[-1][1]] = val
        stack.pop()

    stack.append((val, idx))

print(ans)
    