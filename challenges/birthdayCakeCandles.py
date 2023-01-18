'''
File: birthdayCakeCandles.py
-----
Author: KHALIL HADJI 
'''


def birthdayCakeCandles(candles):
    tallest = 0
    tallest_count = 1
    for c in candles:
        if c > tallest:
            tallest = c
            tallest_count = 1
        elif c == tallest:
            tallest_count += 1
    return tallest_count
