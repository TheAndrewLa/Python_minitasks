import functools as funcs


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return funcs.partial(deprecated, since=since, will_be_removed=will_be_removed)

    def inner(*args, **kwargs):
        if since is None:
            print(f"Function {f.__name__} is deprecated")
        else:
            print(f"Function {f.__name__} is deprecated since version {since}")

        if will_be_removed is None:
            print(f"It will be removed in future version")
        else:
            print(f"It will be removed in version {will_be_removed}")

        return f(*args, **kwargs)

    return inner


@deprecated(will_be_removed='1.2')
def add(a, b):
    print(a + b)


add(2, 3)
