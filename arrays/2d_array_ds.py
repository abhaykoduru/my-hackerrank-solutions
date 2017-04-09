#!/bin/python

import sys

matrix = []
for times in range(6):
    matrix.append(map(int, raw_input().strip().split()))
max = matrix[0][0] + matrix[0][1] + matrix[0][2] + matrix[1][1] + matrix[2][0] + matrix[2][1] + matrix[2][2]
for row in range(4):
    for col in range(4):
        sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col + 1] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if sum > max:
            max = sum

print max
