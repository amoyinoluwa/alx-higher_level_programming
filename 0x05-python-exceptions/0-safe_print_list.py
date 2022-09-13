#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while x:
            print(my_list[0], end = "", flush = True)
            my_list = my_list[1:]
            x -= 1
            i += 1
        print()
        return i
    except:
        print()
        return i
