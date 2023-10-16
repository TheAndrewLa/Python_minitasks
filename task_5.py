#!/bin/env python3

def div(a, b):
    return a / b


def specialize(f, *args1, **kwargs1):
    def specialized(*args2, **kwargs2):
        kwargs2.update(kwargs1)
        args2 += args1

        return f(*args2, **kwargs2)

    return specialized


mult_reverse = specialize(div, a=1)
print(mult_reverse(a=34, b=34)) # printing 0.0294... (not 1.0 because we set 'a' while specializing)
