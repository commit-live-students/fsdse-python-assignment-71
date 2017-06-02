import numpy as np


def solution(array):
    array1 = np.array(array)
    newshape = 1
    for i in array1.shape:
        newshape *= i
    array1 = np.reshape(array1, newshape)
    return np.array(list(set(array1)))
