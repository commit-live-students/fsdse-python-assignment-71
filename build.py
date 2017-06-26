import itertools
import numpy as np

def solution(array):
    out = []
    if (type(array) == 'numpy.ndarray'):
        out = np.flat(array)
        out = np.unique(out)
        return out
    out = np.unique(array)
    print out
    return out
 
