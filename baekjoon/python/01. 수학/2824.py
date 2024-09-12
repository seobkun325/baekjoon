import sys
input = sys.stdin.readline

def gcd(a, b) :
    while b> 0 :
        a, b = b, a%b
    return a
n = int(input())
alst = list(map(int, input().split()))
m = int(input())
blst = list(map(int, input().split()))
A, B = 1, 1
for i in range(n) :
    A*=alst[i]
for i in range(m) :
    B*=blst[i]
G = gcd(A,B)
g = str(G)
glst = list(g)
if len(glst) < 10 :
    print(G)
else :
    for i in range(len(glst)-9,len(glst)) :
        print(glst[i], end="")