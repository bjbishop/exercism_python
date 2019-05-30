#!/usr/bin/env python3


class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.splitlines()
        self.matrix = []
        for item in self.matrix_string:
            temp = [int(number) for number in item.split(" ")]
            self.matrix.append(list(temp))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [item[(index - 1)] for item in self.matrix]


if __name__ == '__main__':
    test = Matrix("89 1903 3\n18 3 1\n9 4 800")
    print(f"Matrix: {test.matrix_string}")
    print(f"Row 1: {test.row(1)}")
    print(f"Column 1: {test.column(1)}")
