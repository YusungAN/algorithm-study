import sys

input = sys.stdin.readline

n = int(input())
v = []
for i in range(n):
    v.append(list(map(int, input().split(' '))))

r = []
g = []
b = []

for i in range(1, n):
    v[i][0] = min(v[i][0]+v[i-1][1], v[i][0]+v[i-1][2])
    v[i][1] = min(v[i][1] + v[i - 1][0], v[i][1] + v[i - 1][2])
    v[i][2] = min(v[i][2] + v[i - 1][1], v[i][2] + v[i - 1][0])


print(min(v[n-1]))
