# 가위 바위 보

def solution(rsp):
    return rsp.translate(str.maketrans('205', '052'))
# 가위는 2 바위는 0 보는 5