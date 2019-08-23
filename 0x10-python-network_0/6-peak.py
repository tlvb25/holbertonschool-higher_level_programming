#!/usr/bin/python3
"""function peak element in unsorted list"""

def find_peak(list_of_integers):
    """function peak element in unsorted list"""
    l = len(list_of_integers)
    if l == 0:
        return None
    if l == 1:
        return l[0]
    if l == 2:
        return max(list_of_integers)

    mid = l//2

    peak = list_of_integers[mid]
    left = list_of_integers[mid - 1]
    right = list_of_integers[mid + 1]

    if peak > left and peak > right:
        return peak
    elif peak < left:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
