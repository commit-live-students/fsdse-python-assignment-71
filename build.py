"""
Write a Python program to get the unique elements of an array using Numpy.
Sample Output:
Scenario 1:

Original array: [10 10 20 20 30 30]
Unique elements of the above array: [10 20 30]
Scenario 2:

Original array: [[1 1] [2 3]]
Unique elements of the above array: [1 2 3]
"""
import numpy as np
def solution(array):
    return np.unique(array)
