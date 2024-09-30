# 짝수 홀수 개수

def solution(num_list):
    even = []
    odd = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
        else:
            odd.append(num_list[i])
    return [len(even), len(odd)]

# 짝수와 홀수의 개수 배열 리턴
# even 짝수 odd 홀수 
