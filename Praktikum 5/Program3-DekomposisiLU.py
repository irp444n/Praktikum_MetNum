matrix_a = [
    [2.0, 1.0, -1.0],
    [4.0, 3.0, 1.0],
    [-2.0, 1.0, 2.0]
]

vector_b = [3.0, 9.0, 4.0]

dimension = len(vector_b)
lower = [[0.0] * dimension for _ in range(dimension)]
upper = [row[:] for row in matrix_a]

for diagonal_index in range(dimension):
    lower[diagonal_index][diagonal_index] = 1.0

print("Pengali eliminasi:")
for pivot_index in range(dimension - 1):
    if upper[pivot_index][pivot_index] == 0:
        raise ValueError("Pivot bernilai nol; diperlukan pertukaran baris.")

    for row_index in range(pivot_index + 1, dimension):
        multiplier = upper[row_index][pivot_index] / upper[pivot_index][pivot_index]
        lower[row_index][pivot_index] = multiplier
        print(f"m{row_index + 1}{pivot_index + 1} = {multiplier:.6g}")

        for column_index in range(pivot_index, dimension):
            upper[row_index][column_index] -= multiplier * upper[pivot_index][column_index]

if upper[-1][-1] == 0:
    raise ValueError("Pivot terakhir bernilai nol; sistem tidak dapat diselesaikan tanpa pivoting.")

print("\nMatriks L:")
for row in lower:
    print([round(value, 6) for value in row])

print("\nMatriks U:")
for row in upper:
    print([round(value, 6) for value in row])

reconstructed_a = [
    [sum(lower[row_index][inner_index] * upper[inner_index][column_index]
         for inner_index in range(dimension))
     for column_index in range(dimension)]
    for row_index in range(dimension)
]
print("\nHasil perkalian L x U (seharusnya sama dengan A):")
for row in reconstructed_a:
    print([round(value, 6) for value in row])

# Substitusi maju: Ly = b
vector_y = [0.0] * dimension
for row_index in range(dimension):
    known_sum = sum(lower[row_index][column_index] * vector_y[column_index]
                    for column_index in range(row_index))
    vector_y[row_index] = vector_b[row_index] - known_sum

print("\nHasil substitusi maju (y):", [round(value, 6) for value in vector_y])

# Substitusi mundur: Ux = y
solution_x = [0.0] * dimension
for row_index in range(dimension - 1, -1, -1):
    known_sum = sum(upper[row_index][column_index] * solution_x[column_index]
                    for column_index in range(row_index + 1, dimension))
    solution_x[row_index] = (vector_y[row_index] - known_sum) / upper[row_index][row_index]

print("\nHasil dekomposisi LU:")
for index, value in enumerate(solution_x, start=1):
    print(f"x{index} = {value:.6g}")