n = int(input())
count = 0
for _ in range(n) :
    stack = []
    arr = list(input())
    for i in arr : 
        stack.append(i)
        if len(stack) > 1 and stack[-1] == stack[-2] : 
            stack.pop()
            stack.pop()
    if not stack : 
        count += 1
print(count)