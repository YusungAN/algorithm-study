import sys

arr = []
sieve = [0 for i in range(2*123456+1)]
sieve[0] = 1
sieve[1] = 1

for i in range(2, 2*123456+1):
    if sieve[i] == 0:
        for j in range(i*2, 2*123456+1, i):
            sieve[j] = 1

while True:
    tmp = int(sys.stdin.readline().rstrip())
    if tmp == 0:
        break
    arr.append(tmp)

for i in arr:
    cnt = 0
    for j in range(i+1, 2*i+1):
        cnt += 1 if sieve[j] == 0 else 0
    print(cnt)
