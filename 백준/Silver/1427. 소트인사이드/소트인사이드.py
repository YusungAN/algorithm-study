import sys

n = int(sys.stdin.readline().rstrip())
li = []

while n > 0:
    li.append(n % 10)
    n //= 10

li.sort(reverse=True)

for i in li:
    print(i, end='')