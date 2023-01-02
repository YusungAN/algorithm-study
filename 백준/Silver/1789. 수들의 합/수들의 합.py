import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(1, n):
    n -= i
    if n > i:
        cnt += 1
    else:
        break

print(cnt+1)
