import sys

x = []
y = []

for i in range(3):
    t1, t2 = map(int, sys.stdin.readline().rstrip().split())
    x.append(t1)
    y.append(t2)

x = sorted(x)
y = sorted(y)
print(x[0] if x[1] == x[2] else x[2], y[0] if y[1] == y[2] else y[2])
