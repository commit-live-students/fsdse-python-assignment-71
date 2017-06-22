import numpy as np
def solution(array):
    x = np.array(array)
    print(x)
    print(np.unique(x))
    return(np.unique(x))
solution(([10, 10, 20, 20, 30, 30]))
