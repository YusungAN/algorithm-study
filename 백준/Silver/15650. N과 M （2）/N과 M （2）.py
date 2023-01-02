import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = []
visited = [False]*n

def func():
    if len(li) == m:
        print(*li)
        return
    for i in range(n):
        if visited[i] or (len(li) > 0 and li[-1] >= i+1):
            continue
        visited[i] = True
        li.append(i+1)
        func()
        li.pop()
        visited[i] = False

func()
