n = 1000 - int(input())
cnt = 0

cnt += n // 500
n -= (n // 500) * 500
cnt += n // 100
n -= (n // 100) * 100
cnt += n // 50
n -= (n // 50) * 50
cnt += n // 10
n -= (n // 10) * 10
cnt += n // 5
n -= (n // 5) * 5
cnt += n

print(cnt)