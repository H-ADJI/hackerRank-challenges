'''
File: compareTriplets.py
-----
Author: KHALIL HADJI 
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
