'''
File: lonelyinteger.py
-----
Author: KHALIL HADJI 
'''


def lonelyinteger(a):
    visited = {}
    for i in a:
        visited[i] = 1 + visited.get(i, 0)
    for i in a:
        if visited[i] == 1:
            return i
