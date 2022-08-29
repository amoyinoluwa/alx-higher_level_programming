#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxNum = float('-inf')
        for i in my_list:
            if i > maxNum:
                maxNum = i
        return maxNum
