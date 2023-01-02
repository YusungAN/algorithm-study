import sys
import math

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

def isPrime(k):
    if k == 1:
        return False
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

_sum = 0
min = 0
for i in range(n, m+1):
    if isPrime(i):
        if min == 0:
            min = i
        _sum += i
if _sum == 0:
    print("-1")
else:
    print(_sum)
    print(min)
