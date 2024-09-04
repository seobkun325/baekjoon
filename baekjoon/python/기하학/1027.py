n = int(input())

lst = list(map(int, input().strip().split(' ')))

for i in range (len(lst)-1) :
    for j in range (i+1, len(lst)) :
        line = 