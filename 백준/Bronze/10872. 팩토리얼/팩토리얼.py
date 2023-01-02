import sys

n = int(sys.stdin.readline().rstrip())

def factorial(k):
    if k <= 1:
        return 1
    else:
        return factorial(k-1)*k

print(factorial(n))