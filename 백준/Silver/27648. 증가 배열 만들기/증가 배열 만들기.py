import sys

input = sys.stdin.readline

n, m, k = map(int, input().split(' '))
li = [[0]*m for _ in range(n)]
idx = 1
if k >= m+n-1:
    for i in range(m+n-1):
        for j in range(n):
            if 0 <= i-j < m and 0 <= j < n:
                li[j][i-j] = idx
        idx += 1

    print('YES')
    for i in li:
        print(*i)
else:
    print('NO')