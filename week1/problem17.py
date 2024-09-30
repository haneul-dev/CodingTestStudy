# 옷가게 할인 받기 

def solution(price):
    if (price > 500000):
        result = price - price * 0.2 
    elif (price > 300000):
        result = price - price * 0.1
    elif (price > 100000):
        result = price - price * 0.05
    else:
        result = price
    return int(result)


    # 10만원 이상 사면 5%
    # 30만원 이상 사면 10%
    # 50만원 이상 사면 20%
    # 지불해야 할 금액 리턴