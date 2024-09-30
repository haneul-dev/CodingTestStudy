# 문자 반복 출력하기

def solution(my_string, n):
    result = ""
    for i in my_string:
        result += i * n
    return result
        
   # ''.join(i*n for i in my_string)