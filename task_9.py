#!/bin/env python3

def format_table(benchmarks: list, algos: list, results: list):
    """
    This function prints pretty looking table with results of benchmarks
    """

    # Ensurance of correctness of input data
    if len(benchmarks) != len(results):
        print("Bad table data!")
        return

    for i in results:
        if len(algos) != len(i):
            print("Bad table data!")
            return

    # Preparing data
    # Column is a list which looks like [[content1, content2 ... contentN], length]
    # Length is equal to max([len(i) for i in [content1, content2 ... contentN]])

    column0 = [[], 0]
    column0[0].append('Benchmark')

    for i in benchmarks:
        column0[0].append(i)
    column0[1] = max([len(i) for i in column0[0]])

    columns = [column0]

    for i in range(len(algos)):
        tmp_column = [[], 0]
        tmp_column[0].append(algos[i])

        for j in results:
            tmp_column[0].append(str(j[i]))

        tmp_column[1] = max([len(i) for i in tmp_column[0]])
        columns.append(tmp_column)

    total_length = sum([i[1] for i in columns]) + (2 * (len(columns))) + len(columns)

    # Printing table
    def print_row(index: int):
        for i in columns:
            print(f'| {str(i[0][index]).ljust(i[1])} ', end='')
        print(' |')

    print_row(0)

    print(f'|{"".center(total_length, "-")}|')

    for i in range(1, len(benchmarks) + 1):
        print_row(i)


format_table(['best_case', 'worst_case'],
             ['l1', 'l2', 'l3'],
             [[1, 2, 1], [0.5, 1, 1]])
