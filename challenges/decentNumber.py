'''
File: decentNumber.py
-----
Author: KHALIL HADJI 
'''


def enough_5_and_3(number: str):
    return number.count("3") % 5 == 0 and number.count("5") % 3 == 0


def decentNumber(n: int):
    greedy_decent = "5"*n
    count_of_3 = 0
    while not enough_5_and_3(greedy_decent) and n > 0:
        count_of_3 += 1
        n -= 1
        greedy_decent = "5"*n + "3"*count_of_3
    if enough_5_and_3(greedy_decent):
        print(greedy_decent)
    else:
        print(-1)
