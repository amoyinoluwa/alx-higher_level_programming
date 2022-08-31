#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_cpy = my_list.copy()
    l = list(map(lambda x: int(str(x).replace(str(search), str(replace))), list_cpy))
    return l
