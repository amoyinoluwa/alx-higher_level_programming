#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = [row[:] for row in matrix]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = m[i][j] * m[i][j]
    return m
