import sys

input = sys.stdin.readline

mat1 = []
mat2 = []
n1, m1 = map(int, input().split(' '))
for j in range(n1):
    mat1.append(list(map(int, input().split(' '))))
n2, m2 = map(int, input().split(' '))
for j in range(n2):
    mat2.append(list(map(int, input().split(' '))))

res = []
for i in range(n1):
    tmp = []
    for j in range(m2):
        _sum = 0
        for k in range(m1):
            _sum += mat1[i][k]*mat2[k][j]
        tmp.append(_sum)
    res.append(tmp)

for i in range(n1):
    print(*res[i])