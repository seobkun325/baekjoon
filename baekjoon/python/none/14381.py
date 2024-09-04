import sys
input = sys.stdin.readline

def dream(N) :
    d = [-1]*10
    i = 1
    while True :
        if N == 0 :
            return "INSOMNIA"
        if -1 not in d :
            return max(d)
        lst = list(str(i*N))
        for x in lst :
            if d[int(x)] == -1 :
                d[int(x)] = i*N
        i += 1

T = int(input())
for i in range(T) :
    num = int(input())
    print(f"Case #{i+1}: ", end="")
    print(dream(num))