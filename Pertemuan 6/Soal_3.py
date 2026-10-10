import time
import numpy as np

# Matriks SPL
A = np.array([
    [5, -1, -1,  0,  0],
    [-1, 5, -1, -1,  0],
    [-1, -1, 4, -1, -1],
    [0,  0,  1,  4, -2],
    [0,  1, -1,  1,  4]
], dtype=float)

b = np.array([-1, 2, 6, 2, -1], dtype=float)
n = 5
max_iter = 2


# 1. METODE GAUSS
def gauss(A, b):
    A = A.copy()
    b = b.copy()

    for k in range(n - 1):
        for i in range(k + 1, n):
            faktor = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - faktor * A[k, k:]
            b[i] = b[i] - faktor * b[k]

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x


# 2. METODE GAUSS-JORDAN
def gauss_jordan(A, b):
    M = np.column_stack((A.copy(), b.copy()))

    for k in range(n):
        M[k] = M[k] / M[k, k]

        for i in range(n):
            if i != k:
                faktor = M[i, k]
                M[i] = M[i] - faktor * M[k]

    return M[:, -1]


# 3. DEKOMPOSISI LU
def lu(A, b):
    L = np.eye(n)
    U = A.copy()

    for k in range(n - 1):
        for i in range(k + 1, n):
            faktor = U[i, k] / U[k, k]
            L[i, k] = faktor
            U[i, k:] = U[i, k:] - faktor * U[k, k:]

    # Substitusi maju: L y = b
    y = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # Substitusi mundur: U x = y
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x


# 4. METODE JACOBI
def jacobi(A, b):
    x = np.zeros(n)

    for _ in range(max_iter):
        x_baru = np.zeros(n)

        for i in range(n):
            jumlah = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_baru[i] = (b[i] - jumlah) / A[i, i]

        x = x_baru

    return x


# 5. METODE GAUSS-SEIDEL
def gauss_seidel(A, b):
    x = np.zeros(n)

    for _ in range(max_iter):
        for i in range(n):
            jumlah = np.dot(A[i, :], x) - A[i, i] * x[i]
            x[i] = (b[i] - jumlah) / A[i, i]

    return x


# PENGUKURAN RUNNING TIME
metode = [
    ("Gauss", gauss),
    ("Gauss-Jordan", gauss_jordan),
    ("LU", lu),
    ("Jacobi", jacobi),
    ("Gauss-Seidel", gauss_seidel)
]

print ("-" * 45)
print("HASIL PENYELESAIAN SPL")
print("-" * 45)

for nama, fungsi in metode:
    mulai = time.perf_counter()
    hasil = fungsi(A, b)
    selesai = time.perf_counter()

    waktu = selesai - mulai

    print(f"\nMetode: {nama}")
    print("Solusi:", np.round(hasil, 6))
    print(f"Running time: {waktu:.9f} detik")