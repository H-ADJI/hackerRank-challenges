'''
File: birthday.py
-----
Author: KHALIL HADJI 
'''


def birthday(s, d, m):
    sliding_window = sum(s[:m])
    counter = 0 if sliding_window != d else 1
    for i in range(len(s)-m):
        sliding_window = sliding_window - s[i] + s[m+i]
        if sliding_window == d:
            counter += 1
    return counter
