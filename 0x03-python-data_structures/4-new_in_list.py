#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    b = my_list.copy()
    if idx in range(0, len(my_list)):
        b[idx] = element
        return b
    return my_list
