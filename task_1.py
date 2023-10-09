def positive_number(n: int) -> int:
    counter = 0

    while n > 0:
        counter += n % 2
        n = (n - (n % 2)) // 2

    return counter


def negative_number(n: int) -> int:
    abs_n = abs(n)
    power = 1

    while abs_n > ((2 ** power) - 1):
        power += 1

    mask = (2 ** power) - 1

    return positive_number((abs_n ^ mask) + 1) + 1


number = int(input('Enter a number: '))

if number >= 0:
    print(positive_number(number))
else:
    print(negative_number(number))
