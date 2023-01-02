import sys

input = sys.stdin.readline

n, b = map(int, input().split(' '))
mat = []
for j in range(n):
    mat.append(list(map(int, input().split(' '))))


def dot(mat1, mat2, n):
    res = []
    for i in range(n):
        tmp = []
        for j in range(n):
            _sum = 0
            for k in range(n):
                _sum += (mat1[i][k] * mat2[k][j]) % 1000
            tmp.append(_sum % 1000)
        res.append(tmp)
    return res


def powmat(mat, n, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat
    newmat = powmat(mat, n, b//2)
    if b % 2 == 1:
        return dot(mat, dot(newmat, newmat, n), n)
    else:
        return dot(newmat, newmat, n)


wow = powmat(mat, n, b)
for i in range(n):
    print(*wow[i])
