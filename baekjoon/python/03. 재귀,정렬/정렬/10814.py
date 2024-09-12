import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())) :
    age, name = input().strip().split(" ")
    arr.append((int(age), name))
arr.sort(key = lambda x: x[0])
for x, y in arr :
    print(x, y)