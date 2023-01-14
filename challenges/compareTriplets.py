'''
File: compareTriplets.py
File Created: Saturday, 14th January 2023 11:30:54 am
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''


def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for e_a, e_b in zip(a, b):
        if e_a > e_b:
            a_score += 1
        elif e_a < e_b:
            b_score += 1
        else:
            continue
    return [a_score, b_score]
