import sys

n = sys.stdin.readline().rstrip()

if '0' not in n:
    print("-1")
    sys.exit(0)

_sum = 0
arr = []

for i in n:
    arr.append(i)
    _sum += int(i)

if _sum % 3 == 0:
    arr = sorted(arr, reverse=True)
    for i in arr:
        print(i, end='')
else:
    print("-1")
