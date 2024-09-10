import sys
input = sys.stdin.readline
arr = [0]
for i in range(1,2*123456+1):
    arr.append(i)

for idx in range(2, len(arr)) :
    for j in range(idx*2, len(arr), idx) :
        arr[j] = 0
        
while True :
    num = int(input())
    if num == 0:
        break

    ans = 0
    for i in range(num+1, 2*num+1) :
        if arr[i] != 0 :
            ans += 1
    print(ans)