# 진료 순서 정하기

def solution(emergency):
    answer = [0] * len(emergency)
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] >= emergency[j]:
                answer[i] += 1
    return answer


# 응급도가 높은 순서를 정한 배열 리턴
