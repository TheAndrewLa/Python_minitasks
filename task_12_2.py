import typing


def chain(*iterables) -> typing.Iterable:
    for i in iterables:
        yield from i


print(list(chain([1, 2, 3], 'hello', [4, 5, 6])))
