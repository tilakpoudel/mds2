# Write a program to find sum of each row of a matrix stored in a numpy array.

import numpy as np

def sum_of_rows(matrix):
    row_sums = np.sum(matrix, axis=1)

    return row_sums

# Example usage
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row_sums = sum_of_rows(matrix)

for i, sum_value in enumerate(row_sums):
    print(f"Sum of row {i}: {sum_value}")

# Output the sum of each row
for i, sum_value in enumerate(row_sums):
    print(f"Sum of row {i}: {sum_value}")
