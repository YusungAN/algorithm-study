import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

s1 = set(map(int, sys.stdin.readline().rstrip().split(' ')))
s2 = set(map(int, sys.stdin.readline().rstrip().split(' ')))
print(len(s1-s2)+len(s2-s1))