#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) is None :
        return 0
    else:
        w_avg = 0
        b_avg = 0
        for st in my_list:
            w_avg += (st[0] * st[1])
            b_avg += (st[1])
        return w_avg / b_avg
