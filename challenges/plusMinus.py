'''
File: plusMinus.py
-----
Author: KHALIL HADJI 
'''


def plusMinus(arr):
    array_size = len(arr)
    positives_count = 0
    negatives_count = 0
    for el in arr:
        if el > 0:
            positives_count += 1
        elif el < 0:
            negatives_count += 1
    print(positives_count/array_size)
    print(negatives_count/array_size)
    print((array_size - negatives_count - positives_count)/array_size)
