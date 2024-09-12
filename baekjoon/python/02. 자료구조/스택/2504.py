arr = list(input().strip())
print(arr)
stack = []
for i in range(len(arr)) : 
    if not stack :
        stack.append(arr[i])
    else :
        if stack[-1] == '(' :
            break # 이거 지우고 시작