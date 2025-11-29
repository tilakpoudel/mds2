# Write a program to find sum of two matrices.
# Write a program to find product of two matrices.

def input_matrix(rows, cols, matrix_number):
    print(f"Enter elements of Matrix {matrix_number} ({rows}x{cols}):")
    matrix = []

    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError(f"Each row must have exactly {cols} elements.")
        matrix.append(row)

    return matrix

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def multiply_matrices(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in Matrix 1 must be equal to number of rows in Matrix 2 for multiplication.")

    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

rows1 = int(input("Enter number of rows for Matrix 1: "))
cols1 = int(input("Enter number of columns for Matrix 1: "))
matrix1 = input_matrix(rows1, cols1, 1)
rows2 = int(input("Enter number of rows for Matrix 2: "))
cols2 = int(input("Enter number of columns for Matrix 2: "))
matrix2 = input_matrix(rows2, cols2, 2)

if rows1 == rows2 and cols1 == cols2:
    sum_matrix = add_matrices(matrix1, matrix2)
    print("Sum of the two matrices:")

    for row in sum_matrix:
        print(' '.join(map(str, row)))
else:
    print("Matrices cannot be added due to incompatible dimensions.")

if cols1 == rows2:
    product_matrix = multiply_matrices(matrix1, matrix2)
    print("Product of the two matrices:")

    for row in product_matrix:
        print(' '.join(map(str, row)))
else:
    print("Matrices cannot be multiplied due to incompatible dimensions.")

