import sys
input = sys.stdin.readline

N = int(input())

arr = [[] for i in range(N)]
arr[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1,N):
    for j in range(10) :
        if j == 0 :
            arr[i].append(1)
        else :
            arr[i].append((arr[i-1][j]+ arr[i][-1])%10007)
print(sum(arr[N-1])%10007)