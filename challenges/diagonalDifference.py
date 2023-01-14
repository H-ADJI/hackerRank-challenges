'''
File: diagonalDifference.py
File Created: Saturday, 14th January 2023 11:43:33 am
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''


def diagonalDifference(arr):
    n = len(arr)
    l_to_r_sum = 0
    r_to_l_sum = 0
    for i, row in enumerate(arr):
        l_to_r_sum += row[i]
        r_to_l_sum += row[n-i-1]
    return abs(r_to_l_sum-l_to_r_sum)
