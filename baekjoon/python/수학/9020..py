import sys
input = sys.stdin.readline

T = int(input())
arr = []
for i in range(0,10001) :
    arr.append(i)
for idx in range(2,101) :
    for j in range(idx*2, 10001, idx) :
        arr[j] = 0
sosu = []
for x in arr :
    if x != 0 :
        sosu.append(x)

for _ in range(T) :
    n = int(input())
    left, right = n//2, n//2
    while True :
        if (left in sosu) and (right in sosu):
            print(left, right)
            break
        else :
            left -= 1
            right += 1