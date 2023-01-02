import sys

arr = []

while True:
    edge = list(map(int, sys.stdin.readline().rstrip().split()))
    edge = sorted(edge)

    if edge[0] == 0:
        break
    if edge[2]*edge[2] == edge[0]*edge[0] + edge[1]*edge[1]:
        arr.append('right')
    else:
        arr.append('wrong')


for i in arr:
    print(i)