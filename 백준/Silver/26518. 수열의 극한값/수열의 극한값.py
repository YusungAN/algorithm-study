import sys

input = sys.stdin.readline

b, c, an_2, an_1 = map(int, input().split(' '))

res = 0
for _ in range(10000):
    an = b*an_1+c*an_2
    res = an/an_1
    an_2 = an_1
    an_1 = an

print(res)