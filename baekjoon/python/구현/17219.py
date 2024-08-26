import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 해시맵(딕셔너리) 생성
domain_pw_dict = {}

# 도메인과 비밀번호를 딕셔너리에 저장
for _ in range(N):
    a, b = input().split()
    domain_pw_dict[a] = b

# 비밀번호 찾기
for _ in range(M):
    a = input().strip()
    print(domain_pw_dict.get(a))
