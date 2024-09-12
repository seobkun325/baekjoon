import sys
input = sys.stdin.readline
S = list(input().strip())
T = list(input().strip())
def tracer(T) :
    global S
    if len(T) == len(S) :
        if T == S :
            print(1)
            quit()
        return
    
    if T[-1] == 'A' :
        tracer(T[:-1])
    if T[0] == 'B' :
        tracer(T[:0:-1])

tracer(T)
print(0)