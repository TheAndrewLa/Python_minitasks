#!/bin/env python3

def add(a, b):
    return a + b


def specialize(f, *args1, **kwargs1):
    def specialized(*args2):
        return f(*(args1 + args2), **kwargs1)

    return specialized


inc = specialize(add, 1)
print(inc(34))
