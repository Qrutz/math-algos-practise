# def printDivisors(n):
#     x = []
#     i = 1
#     while i <= n:
#         if (n % i == 0):
#             x.append(i)
#         i = i + 1
#     return x


# x = printDivisors(12)

# largest = [0]
# # for i in x:
# #     if [i] > largest:
# #         largest = [i]


# # print(largest)
# xd = ["Digg", "Nig", "Zigg"]

# for i in xd:
#     for j in i:
#         for z in j:
#             print(z)

import numpy as np


def solveMatrix(A, b):
    solved = np.linalg.solve(A, b)
    return solved


A = np.array([[1, -2, -1], [2, 2, -1], [-1, -1, 2]])
b = np.array([1, 2, 1])
print(solveMatrix(A, b))
