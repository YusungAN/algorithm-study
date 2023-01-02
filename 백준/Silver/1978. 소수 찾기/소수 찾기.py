import sys
import math

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

def isPrime(k):
    if k == 1:
        return False
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

cnt = 0
for i in nums:
    if isPrime(i):
        cnt += 1

print(cnt)
