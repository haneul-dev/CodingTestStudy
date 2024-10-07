# 합성수 찾기

def solution(n):
     answer = 0
     for i in range(1, n+1):
        c = 0
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c >= 3:
            answer += 1
     return answer
# 약수의 개수가 세 개 이상인 합성수 개수를 리턴