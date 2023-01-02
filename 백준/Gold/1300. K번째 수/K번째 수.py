import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k

res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += mid // i if mid // i <= n else n
    if cnt < k:
        start = mid+1
    else:
        end = mid-1
        res = mid

print(res)