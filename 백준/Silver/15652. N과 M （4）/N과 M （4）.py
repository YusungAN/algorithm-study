import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = []

def func():
    if len(li) == m:
        print(*li)
        return
    for i in range(n):
        if len(li) > 0 and li[-1] > i+1:
            continue
        li.append(i+1)
        func()
        li.pop()

func()
