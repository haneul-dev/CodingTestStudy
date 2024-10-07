# 개미 군단 

def solution(hp):
    count = 0
    if hp >= 5:
        count += (hp//5) 
        if hp % 5 >= 3:
             count += (hp%5)//3
        else:
             count += (hp % 5)
    elif hp >= 3:
            count += (hp//3) + (hp % 3)
    else:
         count += hp
    return count

# 장군개미 5 병정개미 3 일개미 1
# return hp // 5 + (hp % 5 // 3) + ((hp%5) % 3)