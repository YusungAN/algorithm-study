import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))
plus, minus, mul, div = map(int, input().split(' '))

_max = None
_min = None
res = li[0]


def func(idx, plus, minus, mul, div):
    global _max
    global _min
    global res
    if idx == n-1:
        if _max is None:
            _max = res
            _min = res
        if _max is not None and _max < res:
            _max = res

        if _min is not None and _min > res:
            _min = res
        return
    for i in range(4):
        if i == 0 and plus > 0:
            res += li[idx + 1]
            func(idx+1, plus-1, minus, mul, div)
            res -= li[idx + 1]
        elif i == 1 and minus > 0:
            res -= li[idx + 1]
            func(idx+1, plus, minus-1, mul, div)
            res += li[idx + 1]
        elif i == 2 and mul > 0:
            res *= li[idx + 1]
            func(idx+1, plus, minus, mul-1, div)
            res //= li[idx+1]
        elif i == 3 and div > 0:
            tmp = res
            if res >= 0:
                res = res // li[idx + 1]
            else:
                res = (-1*res // li[idx+1])*(-1)
            func(idx+1, plus, minus, mul, div-1)
            res = tmp


func(0, plus, minus, mul, div)
print(_max)
print(_min)
