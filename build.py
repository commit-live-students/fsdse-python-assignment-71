import numpy as np


def solution(array):

    array = np.array(array)
    uniqueArray = np.unique(array)

    return uniqueArray

print solution([10,10,20,20,30 ,30])
