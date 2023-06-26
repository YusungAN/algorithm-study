import sys

input = sys.stdin.readline
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x:x[0])
ans = lines[0][1]-lines[0][0]
e = lines[0][1]
for i in range(1, n):
    if lines[i][0] >= e:
        ans += lines[i][1]-lines[i][0]
        e = lines[i][1]
    elif lines[i][1] > e:
        ans += lines[i][1]-e
        e = lines[i][1]

print(ans)
