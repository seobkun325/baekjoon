n = int(input())

lst = list(map(int, input().split(' ')))
s = [[]for _ in range (1001)]
for idx, val in enumerate(lst) :
    s[val].append(idx)
s.sort()
print (s)