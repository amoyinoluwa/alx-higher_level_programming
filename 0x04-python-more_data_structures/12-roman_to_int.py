#!/usr/bin/python3
def roman_to_int(roman_string):
    romanDict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    res = i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and (romanDict.get(roman_string[i + 1]) > romanDict.get(roman_string[i])):
            res += (romanDict.get(roman_string[i + 1]) - romanDict.get(roman_string[i]))
            i += 2
        else:
            res += romanDict.get(roman_string[i])
            i += 1
    return res
