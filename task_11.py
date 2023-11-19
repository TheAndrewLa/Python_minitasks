import functools


def singleton(something):
    func = something.__new__

    @functools.wraps(func)
    def new_init(cls, *args, **kwargs):
        if something.__instance:
            return something.__instance
        else:
            return cls.__new__(*args, **kwargs)

    something.__new__ = new_init
    return something


@singleton
class Printer:
    def __init__(self, prefix):
        self.__prefix = prefix

    def do(self):
        print(f'Hello {self.__prefix}')


a = Printer('World')
b = Printer('Andrew')

b.do()
