#!/bin/env python3

def flatten(array: list[any]) -> list:
    flatten_list = []

    def flat(sub_array: list[any]):
        for i in sub_array:
            if isinstance(i, list):
                flat(i)
            else:
                flatten_list.append(i)

    flat(array)

    return flatten_list


print(flatten([1, 2, '3', [1, [2], 3], -65, False, [True, True, False]]))
# [1, 2, '3', 1, 2, 3, -65, False, True, True, False]
