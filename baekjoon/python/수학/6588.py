import sys
input = sys.stdin.readline
arr = [i for i in range (1000001)]
for idx in range (2, 1001) :
    for j in range (idx*2, 1000001, idx) :
        arr[j] = 0
while True:
    n = int(input())
    if n == 0 :
        break
    for i in range(n -3, 2, -2) :
        if arr[i] != 0 and arr[n-i] != 0 :
            print(f'{n} = {arr[n-i]} + {arr[i]}')
            break
    else :
        print("이럴수가있나")