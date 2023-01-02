import sys

N = int(sys.stdin.readline().rstrip())

li = []
cnt = 0

def hanoi(n, start, via, to):
    global cnt

    if n == 1:
        li.append([start, to])
        cnt += 1
        return
    hanoi(n-1, start, to, via)
    li.append([start, to])
    cnt += 1
    hanoi(n-1, via, start, to)


hanoi(N, 1, 2, 3)

print(cnt)
for i in li:
    print('{} {}'.format(i[0], i[1]))