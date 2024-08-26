arr = list(input().strip())
stack = []
key = ['P','P','A','P']
for i in range(len(arr)) : 
    stack.append(arr[i])
    if len(stack) > 3 and stack[-4:] == key : 
        for _ in range(3) : 
            stack.pop()

if stack :
    if len(stack) == 1 and stack[0] == 'P':
        print('PPAP')
    else :
        print('NP')
else :
    print('PPAP')