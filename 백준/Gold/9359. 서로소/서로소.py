import sys
from itertools import combinations

input = sys.stdin.readline
''''
N까지의 소인수 구하기,
소인수로 포함배제 원리
'''
n = 10**5
arr = [True] * (n + 1)
m = int(n**0.5)

primes = []
primes_insu = []

for i in range(2, m + 1):
    if arr[i]:
        primes.append(i)
        for j in range(i + i, n + 1, i):
            arr[j] = False


def func(b, li):
    cnt = 0
    for size in range(1, len(li) + 1):
        # print(size, list(combinations(li, size)))
        if size % 2 == 1:
            for i in combinations(li, size):
                tmp = 1
                for j in i:
                    tmp *= j
                cnt += b // tmp
        else:
            for i in combinations(li, size):
                tmp = 1
                for j in i:
                    tmp *= j
                cnt -= b // tmp
        # print(cnt)

    return cnt


for k in range(int(input())):
    a, b, n = map(int, input().split(' '))
    if n == 1:
        print('Case #{}:'.format(k+1), b-a+1)
        continue
    ntemp = n
    li = []
    for i in range(2, int(n**(1/2))+1):
        if arr[i] and n % i == 0:
            li.append(i)
            while ntemp % i == 0:
                ntemp //= i
    if ntemp != 1:
        li.append(ntemp)
    print('Case #{}:'.format(k+1), b-a+1-(func(b, li)-func(a-1, li)) if a > 1 else b-func(b, li))
