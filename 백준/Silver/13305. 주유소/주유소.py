import sys

n = int(sys.stdin.readline().rstrip())
edges = list(map(int, sys.stdin.readline().rstrip().split()))
nodes = list(map(int, sys.stdin.readline().rstrip().split()))
nodes.pop()
cost_sum = 0
cost_min = nodes[0]

for i in range(n-1):
    if cost_min > nodes[i]:
        cost_min = nodes[i]
    cost_sum += cost_min * edges[i]

print(cost_sum)
