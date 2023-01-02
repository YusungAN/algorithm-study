import sys

input = sys.stdin.readline
p = 1000000007
k = int(input())
mat = [[0, 1], [1, 1]]
start = [0, 1]

def dot(mat1, mat2, n):
    res = []
    for i in range(n):
        tmp = []
        for j in range(n):
            _sum = 0
            for k in range(n):
                _sum += (mat1[i][k] * mat2[k][j]) % p
            tmp.append(_sum % p)
        res.append(tmp)
    return res


def powmat(mat, n, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= p
        return mat
    newmat = powmat(mat, n, b//2)
    if b % 2 == 1:
        return dot(mat, dot(newmat, newmat, n), n)
    else:
        return dot(newmat, newmat, n)

if k == 1:
    print(1)
else:
    powed = powmat(mat, 2, k-1)
    print(start[0]*powed[0][1]+start[1]*powed[1][1])
