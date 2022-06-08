#!/usr/bin/python3
def search_replace(my_list, search, replace):
    the_list = my_list[:]
    for i in range(len(the_list)):
        if the_list[i] == search:
            the_list[i] = replace
    return the_list
