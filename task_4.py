import typing


def revert_dictionary(dictionary: dict) -> dict:
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    new_keys = []
    new_values = []

    for i in range(len(keys)):
        if not isinstance(values[i], typing.Hashable):
            raise TypeError
        
        if values[i] in new_keys:
            new_values[new_keys.index(values[i])].append(keys[i])
        
        else:
            new_values.append([keys[i]])
            new_keys.append(values[i])

    for i in range(len(new_values)):
        if len(new_values[i]) == 1:
            new_values[i] = new_values[i][0]
        else:
            new_values[i] = tuple(new_values[i])

    return dict(zip(new_keys, new_values))


print(revert_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 4, 'f': 3}))
# {1: ('a', 'd'), 2: 'b', 3: ('c', 'f'), 4: 'e'}
