#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    if type(matrix) is not list or not all(map(lambda x: type(x) == list, matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if all(map(lambda x: len(x) == 0 or x is None, matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    l = len(matrix[0])
    res = []
    if not all(map(lambda x: len(x) == l, matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not (type(matrix[i][j]) is int or type(matrix[i][j]) is float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
