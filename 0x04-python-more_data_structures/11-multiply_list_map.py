#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    list_copy = my_list[:]
    return list(map(lambda x: x*number, list_copy))
