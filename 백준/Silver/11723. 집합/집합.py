import sys

input = sys.stdin.readline

s = 0b0

for _ in range(int(input())):
    op = input().rstrip()

    if op[0] == 'a' and op[1] == 'd':
        n = int(op[4:])
        mask = 1 << (n-1)
        s = s | mask
    elif op[0] == 'r':
        n = int(op[7:])
        mask = 1 << (n-1)
        s = s & ~mask
    elif op[0] == 'c':
        n = int(op[6:])
        mask = 1 << (n-1)
        print(0 if s & mask == 0 else 1)
    elif op[0] == 't':
        n = int(op[7:])
        mask = 1 << (n - 1)
        if s & mask == 0:
            s = s | mask
        else:
            s = s & ~mask
    elif op[0] == 'a':
        s = 0b11111111111111111111
    else:
        s = 0
