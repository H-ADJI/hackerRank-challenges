'''
File: matchingStrings.py
-----
Author: KHALIL HADJI 
'''


def matchingStrings(strings, queries):
    count_dict = {}
    q_count = []
    for s in strings:
        count_dict[s] = 1 + count_dict.get(s, 0)
    for i, q in enumerate(queries):
        q_count.append(count_dict.get(q, 0))
    return q_count
