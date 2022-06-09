#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    count_out = 0
    for element in a_dictionary.values():
        if element > count_out:
            count_out = element
    for key in a_dictionary:
        if count_out == a_dictionary[key]:
            return (key)
