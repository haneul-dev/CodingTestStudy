# 피자 나눠 먹기 (2)
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(n):
    return lcm(6,n) // 6

# return (n * 6) // gcd(n,6) // 6

# 6과 n 의 최소 공배수, 그 다음에 최소 공배수 / 6 