import numpy as np


def solution(arr):

    return np.unique(arr)


arr1 = np.array([10, 10, 20, 20, 30, 30])
arr2 = np.array([[1, 1], [2, 3]])
print(solution(arr1))
print(solution(arr2))
