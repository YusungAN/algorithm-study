import sys

input = sys.stdin.readline

N = int(input())
lenli = [int(input()) for _ in range(N)]
Q = int(input())
qli = [int(input()) for _ in range(Q)]

idx = 0
len_idx = 0
qidx = 0

while qidx < Q:
    q = qli[qidx]
    cnt = 1
    if lenli[len_idx] % 2 == 0:
        while lenli[len_idx] % 2 == 0:
            lenli[len_idx] //= 2
            cnt *= 2
    idx += cnt
    while q <= idx:
        print(lenli[len_idx])
        qidx += 1
        if qidx < Q:
            q = qli[qidx]
        else:
            break
    len_idx += 1