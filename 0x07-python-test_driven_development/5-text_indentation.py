#!/usr/bin/python3
def text_indentation(text):
    if type(text) is str:
        symbols = {'.','?',':'}
        res = ""
        i = 0
        while i < len(text):
            if text[i] in symbols:
                res += text[i]
                res += '\n\n'
                i += 1
            else:
                res += text[i]
            i += 1
        print(res, end='')

    else:
        raise TypeError("text must be a string")
