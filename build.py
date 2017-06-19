import numpy as np

def solution(array):
    array=np.array(array)
    if array.ndim==1:
        ans=[]
        for i in array:
            if i not in ans:
                ans.append(i)
        return ans
    if array.ndim==2:
        ans=[]
        for i in array[0]:
            if i not in ans:
                ans.append(i)
        for i in array[1]:
            if i not in ans:
                ans.append(i)
        return ans
