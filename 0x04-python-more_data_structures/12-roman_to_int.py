#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return None
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = [conv[x] for x in roman_string] + [0]
    loop = 0

    for i in range(len(res) - 1):
        if res[i] >= res[i + 1]:
            loop += res[i]
        else:
            loop -= res[i]
    return loop
