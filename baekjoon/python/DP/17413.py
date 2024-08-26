arr = list((input().strip()))
stack = []
count = len(arr)
for i in range(count) : 
    stack.append(arr[i])
    if arr[0] == '<' and arr[-1] == '>' :
        while stack :
            print(stack[0],end="")
            del(stack[0])
    else :
        while stack and stack[-1] != '<' :
            print(stack.pop(),end="")
    print(stack)
        # del(stack[-1])



        
