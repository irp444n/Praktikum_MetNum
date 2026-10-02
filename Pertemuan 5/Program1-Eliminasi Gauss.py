A = [
    [2.0, 1.0, -1.0],
    [4.0, 3.0, 1.0],
    [-2.0, 1.0, 2.0]
]

b = [3.0, 9.0, 4.0]
n = 3

# Forward Elimination
for i in range(n):
    for j in range(i + 1, n):
        m = A[j][i] / A[i][i]

        for k in range(i, n):
            A[j][k] = A[j][k] - m * A[i][k]

        b[j] = b[j] - m * b[i]

# Backward Substitution
x = [0.0, 0.0, 0.0]

for i in range(n - 1, -1, -1):
    jumlah = 0

    for j in range(i + 1, n):
        jumlah = jumlah + A[i][j] * x[j]

    x[i] = (b[i] - jumlah) / A[i][i]

print("Hasil Eliminasi Gauss:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])
