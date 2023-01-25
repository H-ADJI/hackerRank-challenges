'''
File: countingSort.py
-----
Author: KHALIL HADJI 
'''


def countingSort(arr):
    f_arr = [0]*len(arr)
    for e in arr:
        f_arr[e] += 1
    return f_arr
