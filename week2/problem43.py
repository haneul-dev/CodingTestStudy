# 최댓값 만들기(1)

def solution(numbers):
    numbers = sorted(numbers)
    return numbers[-1] * numbers[-2]
