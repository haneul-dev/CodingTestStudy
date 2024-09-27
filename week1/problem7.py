# 분수의 덧셈

import math

def solution(numer1, denom1, numer2, denom2):
    result_numer = denom2*numer1 + denom1*numer2
    result_denom = denom1 * denom2
    gcd = math.gcd(result_denum, result_numer)
    return [denum//gcd, num//gcd]

#gcd
#fraction