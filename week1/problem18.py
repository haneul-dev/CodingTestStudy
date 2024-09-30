# 아이스 아메리카노 

def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money - (5500 * (money // 5500)))
    return answer
# 아메리카노는 5500
# 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈