#!/usr/bin/python3
"""
Python script that prints the pascal triagnle for a give number n
representing the level of the triangle
"""

def pascal_triangle(n):
    """
    In mathematics, Pascal's triangle is a triangular array 
    of the binomial coefficients that arises in probability
    theory, combinatorics, and algebra. This program calculates
    and returns a pascal traingle
    """
    if n <= 0:
        return []
    res = [[1],[1,1]]
    for i in range(n - 2):
            new = [1]
            j = 0
            while j + 1 < len(res[-1]):
                new.append(res[-1][j] + res[-1][j + 1])
                j += 1
            res.append(new)
            res[-1].append(1)
    return res
