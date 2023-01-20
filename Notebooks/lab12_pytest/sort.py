#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import List


def bubblesort(input_lst: List[int]) -> List[int]:
    if isinstance(input_lst, dict):
        raise Exception('Data type is dict')
    n = len(input_lst)
    input_lst_copy = input_lst[:]
    number_of_comparisons = 0

    swapped = True

    while n > 1 and swapped is True:
        swapped = False
        for i in range(1, n):
            if input_lst_copy[i - 1] > input_lst_copy[i]:
                input_lst_copy[i - 1], input_lst_copy[i] = input_lst_copy[i], input_lst_copy[i - 1]
                swapped = True
            number_of_comparisons += 1
        n -= 1

    return input_lst_copy
