m = 10**9 + 7

def mat_mul(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % m
    return C

def mat_pow(A, k):
    if k == 0:
        return [[1, 0], [0, 1]]
    else:
        if k % 2 == 0:
            B = mat_pow(A, k / 2)
            return mat_mul(B, B)
        else:
            B = mat_pow(A, k-1)
            return mat_mul(B, A)

n = int(input())


A = [[1, 1], [1, 0]]
An = mat_pow(A, n)

print(An[0][0])
