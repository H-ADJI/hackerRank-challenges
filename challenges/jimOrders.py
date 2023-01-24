'''
File: jimOrders.py
-----
Author: KHALIL HADJI 
'''


def jimOrders(orders):
    serve_times: list = [(i+1, ord[0] + ord[1])
                         for i, ord in enumerate(orders)]
    serve_times_sorted = sorted(serve_times, key=lambda x: x[1])
    result = [el[0] for el in serve_times_sorted]
    return result
