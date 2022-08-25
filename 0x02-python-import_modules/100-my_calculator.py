#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    hash_map = {"+": add, "-": sub, "*": mul, "/": div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    function = hash_map.get(argv[2])
    if function:
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], function(int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
