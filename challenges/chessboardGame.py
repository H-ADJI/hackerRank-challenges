'''
File: chessboardGame.py
-----
Author: KHALIL HADJI 
'''


def chessboardGame(x,y):
    return 'Second' if 0<x%4<3 and 0<y%4<3 else 'First'
