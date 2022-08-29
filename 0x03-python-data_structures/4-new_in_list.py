#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx in range(0, len(my_list)):
        b = my_list
        b[idx] = element
        return b
    return None
