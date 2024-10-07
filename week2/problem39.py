# 공 던지기 

def solution(numbers, k):
   return numbers[2 * (k-1) % len(numbers)]

# 공은 1번부터 던지며 오른쪽 한 명을 건너뛰고 그다음 사람에게만 던질 수 있음

