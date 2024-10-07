# 배열 회전시키기 

def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
# 배열 numbers의 원소를 direction 방향으로 한 칸씩 회전시킨 배열을 리턴