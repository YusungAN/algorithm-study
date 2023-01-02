import sys

input = sys.stdin.readline

n = int(input())
a = 0
b = 0
print('? 1')
sys.stdout.flush()
a = int(input())
print('? '+str(n))
sys.stdout.flush()
b = int(input())

if b > a:
    print('! 1')
elif a > b:
    print('! -1')
else:
    print('! 0')
