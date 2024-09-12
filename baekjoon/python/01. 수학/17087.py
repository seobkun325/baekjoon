import sys
input = sys.stdin.readline

def gcd(a,b) :
    while b> 0 :
        a, b = b, a%b
    return a

N, S = map(int, input().split(" "))
bros = list(map(int, input().split(" ")))
distance = []
for x in bros :
    distance.append(abs(x-S))
ans = distance[0]
for i in range(len(distance)):
    ans = gcd(ans, distance[i])
print(ans)
