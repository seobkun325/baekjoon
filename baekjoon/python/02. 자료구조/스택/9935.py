arr = list(input())
bomb = input()

stack = []
for i in range(len(arr)) : 
    stack.append(arr[i])
    if ''.join(stack[-len(bomb):]) == bomb : 
        for i in range(len(bomb)) : 
            stack.pop()

if stack :
    print(''.join(stack))
else :
    print('FRULA')