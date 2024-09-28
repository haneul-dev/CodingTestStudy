# 최빈값 구하기 

from collections import Counter

def soulution(array):
    counter = Counter(array)

    max_count = max(counter.value) # 빈도수가 가장 큰 값

    most_frequent = [key for key, count in counter.items if count == max_count]

    if len(most_frequent) > 1:
        return -1
    else:
        return most_frequent[0]