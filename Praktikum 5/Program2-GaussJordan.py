A = [
    [2.0, 1.0, -1.0, 3.0],
    [4.0, 3.0, 1.0, 9.0],
    [-2.0, 1.0, 2.0, 4.0]
]

n = 3

for i in range(n):

    # Membuat pivot menjadi 1
    pivot = A[i][i]

    for j in range(n + 1):
        A[i][j] = A[i][j] / pivot

    # Menghilangkan elemen pada kolom pivot
    for k in range(n):
        if k != i:
            faktor = A[k][i]

            for j in range(n + 1):
                A[k][j] = A[k][j] - faktor * A[i][j]

print("Hasil Gauss-Jordan:")

for i in range(n):
    print(A[i])

print("x1 =", A[0][3])
print("x2 =", A[1][3])
print("x3 =", A[2][3])