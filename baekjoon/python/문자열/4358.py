import sys
from collections import defaultdict
input = sys.stdin.readline
d = defaultdict(int)

while True :
    line = input().strip()
    if not line :
        break
    d[line] += 1
n = sum(d.values())
sd= dict(sorted(d.items()))
for x in sd :
    print(f'{x} {sd[x]/n*100:.4f}')
