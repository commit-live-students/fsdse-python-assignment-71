import itertools
import numpy as np

def solution(array):
   result = []
   if (type(array) == 'numpy.ndarray'):
       result = np.flat(array)
       result = np.unique(result)
       return result
   result = np.unique(array)
   print result
   return result
