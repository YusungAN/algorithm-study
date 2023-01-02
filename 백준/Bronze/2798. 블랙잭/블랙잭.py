import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
arr = list(map(int, sys.stdin.readline().rstrip().split()))
_sum = 0
_max = 0
cnt = 0

# arr = sorted(arr, reverse=True)

for i in range(n):
    _sum = arr[i]
    for j in range(i+1, n):
        _sum = arr[i] + arr[j]
        for k in range(j+1, n):
            _sum = arr[i] + arr[j] + arr[k]
            if m >= _sum > _max:
                _max = _sum

print(_max)
