import numpy as np


def solution(array):
    npArray = np.array(array)

    return np.unique(npArray)

print solution([10, 10, 20, 20, 30, 30])
