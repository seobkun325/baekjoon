n = int(input())
for i in range(n) : 
    string = []
    string = input().split()
    string.reverse()
    str = ' '.join(string)
    print(f"Case #{i+1}: "+str)