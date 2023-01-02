import sys

input = sys.stdin.readline

n = int(input())
v = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

for i in range(1, n):
    v.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for j in range(0, 10):
        if j == 0:
            v[i][j] = v[i - 1][j + 1]
        else:
            v[i][j] = v[i-1][j-1]+v[i-1][j+1]

print(sum(v[n-1])%10**9)


