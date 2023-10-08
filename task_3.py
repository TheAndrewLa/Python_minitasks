# Two different variations again. The first one - is easier to read, the second - is shorter

def create_matrix(exp: str) -> list:
    matrix = []
    lines = [i.strip() for i in exp.split('|')]

    for i in lines:
        matrix.append([float(j) for j in i.split(' ')])

    return matrix


def create_matrix2(exp: str) -> list:
    return [[float(j) for j in i.split(' ')] for i in [i.strip() for i in exp.split('|')]]


print(create_matrix("1 2 3 | 4 5 6 | 7 8 9"))
# [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

print(create_matrix2("1 2 | 3 4 | 5 6 | 7 8 | 9 10"))
# [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0], [9.0, 10.0]]
