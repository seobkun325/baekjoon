T = int(input())
for _ in range(T) :
    ans = 0
    bonus = 1
    test = list(input())
    for i, c in enumerate(test) :
        if c == 'O' :
            ans += bonus
            bonus += 1
        else :
            bonus = 1
    print(ans)
