def strassen(A, B):

    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    new_size = n // 2
    A11 = [row[:new_size] for row in A[:new_size]]
    A12 = [row[new_size:] for row in A[:new_size]]
    A21 = [row[:new_size] for row in A[new_size:]]
    A22 = [row[new_size:] for row in A[new_size:]]

    B11 = [row[:new_size] for row in B[:new_size]]
    B12 = [row[new_size:] for row in B[:new_size]]
    B21 = [row[:new_size] for row in B[new_size:]]
    B22 = [row[new_size:] for row in B[new_size:]]


    S1 = matrix_sub(B12, B22)
    S2 = matrix_add(A11, A12)
    S3 = matrix_add(A21, A22)
    S4 = matrix_sub(B21, B11)
    S5 = matrix_add(A11, A22)
    S6 = matrix_add(B11, B22)
    S7 = matrix_sub(A12, A22)
    S8 = matrix_add(B21, B22)
    S9 = matrix_sub(A11, A21)
    S10 = matrix_add(B11, B12)


    P1 = strassen(A11, S1)
    P2 = strassen(S2, B22)
    P3 = strassen(S3, B11)
    P4 = strassen(A22, S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)


    C11 = matrix_add(matrix_sub(matrix_add(P5, P4), P2), P6)
    C12 = matrix_add(P1, P2)
    C21 = matrix_add(P3, P4)
    C22 = matrix_sub(matrix_sub(matrix_add(P5, P1), P3), P7)

    result = []
    for i in range(new_size):
        result.append(C11[i] + C12[i])
    for i in range(new_size):
        result.append(C21[i] + C22[i])
    return result


def matrix_add(A, B):

    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def matrix_sub(A, B):

    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def main():

    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

    B = [[17, 18, 19, 20],
         [21, 22, 23, 24],
         [25, 26, 27, 28],
         [29, 30, 31, 32]]

    assert len(A) == len(A[0]) == len(B) == len(B[0])
    assert (len(A) & (len(A) - 1)) == 0

    result = strassen(A, B)

    for row in result:
        print(row)


if __name__ == "__main__":
    main()
