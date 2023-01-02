import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    s = input().rstrip()
    n = int(input())
    exp = input().rstrip()
    li = []
    if len(exp)<=2:
        pass
    else:
        li = deque(list(map(int, exp.strip(']').strip('[').split(','))))
    dir = True # True -> 앞에서 빼기 False-> 뒤에서 빼기
    err = False
    for j in s:
        if j == 'R':
            dir = not dir
        elif j == 'D':
            if len(li) == 0:
                print('error')
                err = True
                break
            if dir:
                li.popleft()
            else:
                li.pop()

    if err:
        continue
    if not dir:
        li.reverse()
    if len(li) == 0:
        print('[]')
        continue
    print('[{}'.format(li[0]), end='')
    for j in range(1, len(li)):
        print(',{}'.format(li[j]), end='')
    print(']')