# 순서쌍의 개수

def solution(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count
# (a, b)
# n 을 나눴을 때 자연수인 경우에만 카운트 .. 