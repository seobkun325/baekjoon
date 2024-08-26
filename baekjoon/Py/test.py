# print('Hello World!')
# print('It\'s mine')
# print('그가 소리쳤다, "배고파"')
# print('안녕하세요. \\n만나서\\t\\t반갑습니다.')
# 삼성전자 = 50000
# 주 = 10
# 총평가금액 = 삼성전자*주
# print(총평가금액)
# s = "hello"
# t = "python"
# print(s + "! " + t)

# movie_rank = ["닥터스트레인지", "아이언맨", "스파이더맨"]
# movie_rank.insert(3,"배트맨")
# print(movie_rank)
# price = ['20220928', 100, 130, 140, 150, 160, 170]
# print(price[1:7])
# def print_ai() :
#     print("인공지능")
# for i in range(0, 100) : 
#     print_ai()

# def add_function(a,b) : 
#     return a+b
# print(add_function(3,5))

# score = input("score : ")
# score = int(score)
# if (score > 80 and score <= 100) : 
#     print("A")
# elif (score > 60 and score <= 80) :
#     print("B")
# elif (score > 40 and score <= 60) :
#     print("C")
# elif (score > 20 and score <= 40) : 
#     print("D")
# elif (score >= 0 and score <= 20) :
#     print("F")
# else : print("Wrong score")

# a  = 1
# b = 2
# print (a , b)
# a, b = b, a
# print (a,b)
# a = 10
# b = 3
# print (a / b)


# numbers = [1,2,3,4,5,6,7,8]
# print(numbers.length)

def solution(n):
    answer = []
    t = n
    answer.append(t)
    while(t != 1) : 
        if t % 2 == 0 : 
            t /= 2
        else : 
            t = t*3 + 1
        answer.append(t)
    return answer

print(solution(30))

a = 4
b = 2
kk = a/b
pp = int(a/b)
if kk == pp : 
    print('true')