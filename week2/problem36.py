# 구슬을 나누는 경우의 수

def solution(balls, share):
    n = 1
    m = 1
    s = 1
    for i in range(1, balls+1):
        n *= i
    for j in range(1, share+1):
        m *= j
    for k in range(1, balls-share+1):
        s *= k
    return n/(m*s)
# 머쓱이가 갖고 있는 구슬의 개수, 친구들에게 나누어 줄 구슬 개수
# 서로 다른 n 개 중 m 개를 뽑는 경우의 수 공식은 n! / (n-m)! * m!