# 피자 나눠 먹기(1)

def solution(n):
    if ( n > 7 ):
        if ( n % 7 > 0):
            return n//7 +1
        else:
            return n//7
    else:
        return 1
   
   # return (n + 6) // 7
   # return (n - 1) // 7 + 1