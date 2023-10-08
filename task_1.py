def positive_number(n : int) -> int:
    counter = 0
    while n > 0:
        counter += n % 2
        n = (n - (n % 2)) // 2

    return counter

def negative_number(n : int) -> int:
    absolute_n = abs(n)
    power = 8

    while absolute_n >= (2 ** (power - 1)):
        power *= 2

    absolute_n = (2 ** (power - 1)) - absolute_n

    return positive_number(absolute_n) + 1


number = int(input('Enter a number: '))

if number >= 0:
    print(positive_number(number))
else:
    print(negative_number(number))