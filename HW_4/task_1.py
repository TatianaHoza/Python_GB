matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(matrix):
    zipped_rows = zip(*matrix)
    return [list(row) for row in zipped_rows]


print(transpose(matrix))
