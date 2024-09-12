T = int(input())

lst = [True] * 1000001
for i in range(2, int(len(lst)**0.5)+1) :
    if lst[i] :
        for j in range(i*2, 1000001, i):
            lst[j] = False

for _ in range(T) :
    n = int(input())
    cnt = 0
    if lst[2] and lst[n - 2]:
        cnt += 1
    for i in range(3, n//2+1, 2) :
        if lst[i] and lst[n-i] :
            cnt+=1
    print(cnt)