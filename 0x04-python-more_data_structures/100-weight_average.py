#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    y = 0
    for x in my_list:
        num += x[0] * x[1]
        y += x[1]
    return (num / y)
