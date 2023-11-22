def coroutine(generator):
    def inner_generator(*args, **kwargs):
        gen = generator(*args, **kwargs)
        next(gen)

        return gen

    return inner_generator


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
# next(st)

print(st.send(42))
print(st.send(42))
