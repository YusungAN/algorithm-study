import sys

n = int(sys.stdin.readline().rstrip())

def fibonacci(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k-1)+fibonacci(k-2)

print(fibonacci(n))