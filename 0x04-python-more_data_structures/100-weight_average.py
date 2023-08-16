#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    val = 0
    for i in my_list:
        num += i[0] * i[1]
        val += i[1]

    return (num / val)
