import numpy as np


def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]

    result = np.zeros((n, p))

    for i in range(n):
        for k in range(m):
            for j in range(p):
                result[i][j] += A[i][k] * B[k][j]

    return result


def split(matrix):
    rows, columns = matrix.shape
    rows = rows // 2
    columns = columns // 2

    return (
        matrix[:rows, :columns],
        matrix[:rows, columns:],
        matrix[rows:, :columns],
        matrix[rows:, columns:],
    )


def strassen(A, B):
    if len(A) <= 2:
        return brute_force(A, B)

    a, b, c, d = split(A)
    e, f, g, h = split(B)

    p1 = strassen(a + d, e + h)
    p2 = strassen(d, g - e)
    p3 = strassen(a + b, h)
    p4 = strassen(b - d, g + h)
    p5 = strassen(a, f - h)
    p6 = strassen(c + d, e)
    p7 = strassen(a - c, e + f)

    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7

    return np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
