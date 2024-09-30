# 배열의 평균값

def solution(numbers):
    avg = sum(numbers)
    return round(avg / len(numbers), 1)

# 원소의 평균값구하기
# return sum(numbers) / len(numbers)