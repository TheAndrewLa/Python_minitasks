#!/bin/env python3

def flatten(array: list[any], max_depth=None) -> list:
    flatten_list = []

    def cmp_le(a, b):
        if b is None:
            return True

        return a <= b

    def flat(sub_array: list[any], depth):
        for i in sub_array:
            if isinstance(i, list) and cmp_le(depth, max_depth):
                flat(i, depth + 1)
            else:
                flatten_list.append(i)

    flat(array, 1)
    return flatten_list


print(flatten([1, 2, '3', [1, [[[[[2]]]]], 3], -65, False, [True, True, False]]))
# [1, 2, '3', 1, [[2]], 3, -65, False, True, True, False]
