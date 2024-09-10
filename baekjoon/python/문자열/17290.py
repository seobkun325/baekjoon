import sys
input = sys.stdin.readline
x, y = map(int, input().split())
x, y = x-1, y-1
def bombzone(x,y) :
    for dy in range(0, 10) :
        if arr[x][dy] != 'o' :
            arr[x][dy] = '#'
    for dx in range(0, 10) :
        if arr[dx][y] != 'o' :
            arr[dx][y] = '#'


arr = [list(input().strip()) for _ in range(10)]
for i in range(10) :
    for j in range(10) :
        if arr[i][j] == 'o' :
            bombzone(i, j)
minlen = sys.maxsize
for i in range(10) :
    for j in range(10) :
        if arr[i][j] == 'x' :
            minlen = min(minlen, abs(i-x)+abs(j-y))

print(minlen)
