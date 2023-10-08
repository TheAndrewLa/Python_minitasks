# The first realization of function is simpler and shorter
# (and maybe faster, i dont know how list generators actually works on low-level)

# The second realization is easier to read

def custom_zip1(keys: list, values: list)-> list:
    return [(keys[i], values[i]) for i in range(min(len(keys), len(values)))]


def custom_zip2(keys: list, values: list)-> list:
    array = []
    i = 0
    while i < len(keys) and i < len(values):
        array.append((keys[i], values[i]))
        i += 1

    return array


k = ['a', 'b', 'c', 'd', 'e']
v = [1, 2, 3, 4, 5, 6, 7]

# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print(custom_zip1(k, v))

v = [1, 2, 3]

# [('a', 1), ('b', 2), ('c', 3)]
print(custom_zip2(k, v))
