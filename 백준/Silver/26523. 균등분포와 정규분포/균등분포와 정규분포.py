import sys

input = sys.stdin.readline

for _ in range(100):
    li = [0]*10
    for i in range(5000):
        li[int((float(input())-0.001)*10)] += 1
    for j in li:
        if j <= 400:
            print('B')
            break
    else:
        print('A')
