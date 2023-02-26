import sys
from itertools import product

input = sys.stdin.readline


def is_win_first(a, b):
    a_cnt = 0
    b_cnt = 0
    for i in a:
        for j in b:
            if i > j:
                a_cnt += 1
            elif j > i:
                b_cnt += 1

    return a_cnt > b_cnt


for _ in range(int(input())):
    li = list(map(int, input().split(' ')))
    a = li[0:4]
    b = li[4:8]
    flag = False
    for c in product(range(1, 11), repeat=4):
        if (is_win_first(a, b) and is_win_first(b, c) and is_win_first(c, a)) or (is_win_first(b, a) and is_win_first(a, c) and is_win_first(c, b)):
            flag = True
            break
    print('yes' if flag else 'no')
