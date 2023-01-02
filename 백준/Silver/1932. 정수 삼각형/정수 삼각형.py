import sys

input = sys.stdin.readline

n = int(input())
v = []
for i in range(n):
    v.append(list(map(int, input().split(' '))))

for i in range(1, n):
    for j in range(i+1):
        v[i][j] = max(v[i][j]+v[i-1][j-1 if j-1 >= 0 else 0], v[i][j]+v[i - 1][j if j < i else i-1])

print(max(v[n-1]))