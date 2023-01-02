import sys

input = sys.stdin.readline

n, x = map(int, input().split(' '))
li = list(map(int, input().split(' ')))
idx = 0
while li[idx] >= x:
    x += 1
    idx = (idx + 1) % n

print(idx+1)