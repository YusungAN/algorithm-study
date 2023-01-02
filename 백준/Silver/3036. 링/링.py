import sys
from math import gcd

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(1, n):
    gcd_n = gcd(li[0], li[i])
    print('{}/{}'.format(li[0]//gcd_n, li[i]//gcd_n))