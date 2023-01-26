'''
File: twoArrays.py
-----
Author: KHALIL HADJI 
'''

def twoArrays(k, A, B):
    A.sort(reverse=True)
    B.sort()
    return "YES" if all([t[0] + t[1] >= k for t in zip(A, B)]) else "NO"