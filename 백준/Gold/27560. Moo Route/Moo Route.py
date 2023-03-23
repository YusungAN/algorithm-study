import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))

now = 0
dir = 1
T = []
while True:
    if now == 0 and li[0] == 0:
        break
    if now == n:
        li[now - 1] -= 1
        now -= 1
        dir = -1
        T.append('L')
    elif now == 0:
        li[now] -= 1
        now += 1
        dir = 1
        T.append('R')
    elif dir == 1:
        if li[now] > 0:
            li[now] -= 1
            now += 1
            T.append('R')
        else:
            li[now - 1] -= 1
            now -= 1
            dir = -1
            T.append('L')
    elif dir == -1:
        if li[now-1] > 1 or li[now] == 0:
            li[now-1] -= 1
            now -= 1
            T.append('L')
        else:
            li[now] -= 1
            now += 1
            dir = 1
            T.append('R')
    # print(now)

print(''.join(T))
