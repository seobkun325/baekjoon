import sys
input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))
bank = []
c = sys.maxsize
for idx in range(len(oil)-1) :
    if oil[idx] <= c :
        bank.append(idx)
        c = oil[idx]
ans = 0
for i in range(len(bank)-1) :
    for j in range(bank[i],bank[i+1]) :
        ans += oil[bank[i]]*distance[j]
spot = bank[-1]
ans += sum(distance[spot:])*oil[spot]
print(ans)