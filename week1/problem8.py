# 배열 두 배 만들기

def solution(members):
    answer = []

    for i in members:
        answer = i*2 # 각 원소에 두배한 원소를 가진 배열
    
    return answer

# return [num*2 for num in numbers]

# answer = np.array(numbers)*2
# answer = answer.tolist() # 각각의 요소에 연산이 될 수 있음 