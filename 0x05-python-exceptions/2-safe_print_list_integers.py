#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = i = 0
    while x:
        try:
            print("{:d}".format(my_list[i]), end="", flush = True)
            count += 1
        except (TypeError, ValueError):
            x -= 1
            i += 1
            continue
        x -= 1
        i += 1
    print()
    return count
