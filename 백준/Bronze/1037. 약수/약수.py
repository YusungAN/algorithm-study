import sys

N = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split(' ')))

print(min(li)*max(li))
