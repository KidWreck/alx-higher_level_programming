#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    lpool = []
    for i in my_list:
        if (i % 2) == 0:
            lpool.append(True)
        else:
            lpool.append(False)
    return lpool
