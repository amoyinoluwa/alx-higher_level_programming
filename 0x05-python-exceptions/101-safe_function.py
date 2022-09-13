#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
        return res
    except Exception as exception:
        print("Exception: {}".format(exception), file=sys.stderr)
