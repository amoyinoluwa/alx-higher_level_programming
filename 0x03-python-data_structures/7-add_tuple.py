#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def check(tup):
        if len(tup) == 0:
            ret = (0, 0)
        elif len(tup) == 1:
            ret = (tup[0], 0)
        else:
            ret = (tup[0], tup[1])
        return ret
    tup_1 = tuple(map(check, (tuple_a, tuple_b)))
    return tuple(map(sum, zip(tup_1[0], tup_1[1])))
