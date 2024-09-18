def bfs(num) :
    q = []
    cnt = 0
    q.append((num, cnt))
    v[num] = 1
    max_cnt = 0
    while q:
        c, ccnt = q.pop(0)
        for idx, val in enumerate (arr[c]):
            if val == 'Y' and v[idx] == 0 :
                q.append((idx, ccnt+1))
                v[idx] = 1
                max_cnt = max(max_cnt, ccnt+1)
    return max_cnt


n = int(input())

arr = [list(input()) for _ in range (n)]
ans = 0

for i in range (n) : 
    v = [0]  *n
    ans = max(ans, bfs(i))

print (ans)