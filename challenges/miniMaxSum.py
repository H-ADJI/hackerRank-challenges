'''
File: miniMaxSum.py
-----
Author: KHALIL HADJI 
'''


def miniMaxSum(arr):
    min_arr = min(arr)
    max_arr = max(arr)
    min_sum = sum(arr) - max_arr
    max_sum = min_sum - min_arr + max_arr
    print(f"{min_sum} {max_sum}") 
