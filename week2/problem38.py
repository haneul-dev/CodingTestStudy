# 2차원으로 만들기

import numpy as np

def solution(num_list, n):
    data = np.array(num_list).reshape(len(num_list)//n, n)
    return data.tolist()
    