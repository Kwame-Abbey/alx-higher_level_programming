#!/usr/bin/python3
"""contains function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    left = 0
    right = len(list_of_integers) - 1
    return peak_find(list_of_integers, left, right)


def peak_find(list, left, right):
    """finds peak recursively using binary search"""
    if left == right:
        return (list[right])
    mid = (left + right) // 2
    if list[mid] > list[mid + 1]:
        return peak_find(list, left, mid)
    return peak_find(list, mid + 1, right)
