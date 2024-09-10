N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse= True)
def gcd(a,b) :
    while b > 0:
        a, b = b, a % b
    return a
arr = []
for i in range(len(lst)-1) :
    arr.append(lst[i] - lst[i+1])
temp = arr[0]
for i in range(len(arr)):
    temp = gcd(temp,arr[i])
ans = []
for i in range(1, int(temp**0.5)+1) :
    if temp % i == 0 :
        if i != 1 :
            ans.append(i)
        if temp//i not in ans :
            ans.append(temp//i)
ans.sort()
print(*ans)