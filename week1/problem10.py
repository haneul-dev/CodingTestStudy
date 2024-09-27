def solution(array):
    answer = 0
    num = 0

    for i in array:
        num += 1
    main = num// 2
    array.sort()
    answer = array[main]
    return answer

# len(array)
# return sorted(array[len(array)//2])