# 외계 행성의 나이 

def solution(age):
    return str(age).translate(str.maketrans('0123456789', 'abcdefghij'))
# a 0, b 2
# 23살은 cd