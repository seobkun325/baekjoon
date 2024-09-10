import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N) :
    arr.append(input().strip())


# 문자열 내에 숫자값만 받아서 합 구하는 함수 생성
def arrNumSum(x) : 
    result = sum(int(s) for s in x if s.isdigit())
    return result

# 3개의 정렬 조건으로 정렬한다. (1)길이, (3) 사전순은 평소 하던 방법. (2) 숫자합은 함수 생성
arr.sort(key = lambda x: (len(x), arrNumSum(x), x)) 
for word in arr :
    print(word)