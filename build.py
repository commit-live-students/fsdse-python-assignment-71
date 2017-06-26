import numpy as np
def solution(arr):
    array = np.array(arr)
    l = []
    for x in np.nditer(array):
        if x not in l:
            l.append(x)
        else:
            pass
    unique_array = np.array(l)
    return unique_array
