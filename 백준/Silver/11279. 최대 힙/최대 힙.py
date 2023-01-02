import sys
from queue import PriorityQueue

input = sys.stdin.readline
q = PriorityQueue()

n = int(input())

for i in range(n):
    a = int(input())
    if a > 0:
        q.put(((2**31)-a, a))
    else:
        if q.qsize() > 0:
            print(q.get()[1])
        else:
            print(0)