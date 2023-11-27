import typing


def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res


def cycle(itr: typing.Iterable) -> typing.Iterable:
    while True:
        yield from itr


print(take(cycle([1, 2, 3]), 10))
