import sys
input = sys.stdin.readline

while True :
    arr = list(map(int, input().split()))
    if arr[0] == 0 :
        break
    arr.pop(0)
    lst = []
    def back(start) :

        if len(lst) == 6 :
            print(' '.join(map(str, lst)))
            return
        for i in range(start, len(arr)) :
            lst.append(arr[i])
            back(i+1)
            lst.pop()
    back(0)
    print()
