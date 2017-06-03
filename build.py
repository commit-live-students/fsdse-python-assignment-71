import numpy as np


def solution(array):
    """
    Enter your code here
    """
    array = np.array(array)
    uniqueArray = np.unique(array)

    return uniqueArray

solution([10,10,20,20,30 ,30])
