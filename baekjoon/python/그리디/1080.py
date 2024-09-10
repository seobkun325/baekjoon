import sys
input = sys.stdin.readline

n, m = map(int, input().split())
before = [list(input().strip()) for _ in range(n)]
after = [list(input().strip()) for _ in range(n)]
print(before, after)