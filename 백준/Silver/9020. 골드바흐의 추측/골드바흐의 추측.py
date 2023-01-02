import sys

arr = []
sieve = [0 for i in range(10000)]
sieve[0] = 1
sieve[1] = 1

for i in range(2, 10000):
    if sieve[i] == 0:
        for j in range(i*2, 10000, i):
            sieve[j] = 1

t = int(sys.stdin.readline().rstrip())
arr = []

for i in range(t):
    arr.append(int(sys.stdin.readline().rstrip()))

for i in arr:
    n1 = 0
    n2 = 0
    for j in range(2, i-1):
        if j <= i-j and sieve[j] == 0 and sieve[i-j] == 0:
            n1 = j
            n2 = i-j
    print(n1, n2)
