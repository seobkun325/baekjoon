import sys
input = sys.stdin.readline

def move(start, end, N) :
    if N == 1 :
        print(start, end)
        return
    else :
        move(start, 6-start-end, N-1)
        print(start, end)
        move(6-start-end, end, N-1)

N = int(input())

print(2**N-1)
move(1,3,N)