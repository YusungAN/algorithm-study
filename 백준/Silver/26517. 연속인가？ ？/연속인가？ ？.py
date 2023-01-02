import sys

input = sys.stdin.readline

k = int(input())
a, b, c, d = map(int, input().split(' '))

print('Yes '+str(a*k+b) if a*k+b == c*k+d else 'No')