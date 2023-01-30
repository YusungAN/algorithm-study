import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

li = [[0]*m for _ in range(n)]

for i in range(m):
    tmp = list(map(int, input().split(' ')))

    for j in range(n):
        li[j][i] = tmp[j]

res = [0]*n
ans = 0
for i in range(n):
    li[i].sort()
    if m % 2 == 1:
        res[i] = li[i][m//2]
    else:
        res[i] = (li[i][m//2]+li[i][m//2-1])//2

    for j in range(m):
        ans += abs(res[i]-li[i][j])

print(ans)
print(*res)
