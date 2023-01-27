import sys

input = sys.stdin.readline

n = int(input())
A = [list(map(int, input().split(' '))) for _ in range(n)]
L = [[0]*n for _ in range(n)]

for i in range(n):
    pivot = A[i][i]
    if pivot == 0:
        print(-1)
        exit(0)
    if i == n-1:
        break
    mul = A[i+1][i] / A[i][i]
    for j in range(n):
        A[i+1][j] -= mul*A[i][j]
    L[i][i] = 1
    L[i+1][i] = mul

L[n-1][n-1] = 1

for i in range(n):
    for j in range(n):
        print('{:.3f}'.format(round(L[i][j], 3)), end=' ')
    print('')
for i in range(n):
    for j in range(n):
        print('{:.3f}'.format(round(A[i][j], 3)), end=' ')
    print('')
