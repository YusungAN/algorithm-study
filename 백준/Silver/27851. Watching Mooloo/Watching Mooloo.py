import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
li = list(map(int, input().split(' ')))

prev = 0
ans = 0
for i in range(n-1):
    if li[i+1]-li[i] > k:
        ans += li[i]-li[prev]+1+k
        prev = i+1

ans += li[n-1]-li[prev]+1+k

print(ans)
