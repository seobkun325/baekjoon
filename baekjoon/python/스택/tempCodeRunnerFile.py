for i in range(len-2) : 
    if numbers[i] < numbers[i+1] :
        del(numbers[i])
        cnt -= 1
    if cnt == 0 : break
    else :
        for j in range(cnt):
            numbers.pop()
print(numbers)