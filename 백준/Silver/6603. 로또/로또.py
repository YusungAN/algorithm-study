import sys

input = sys.stdin.readline

li = []
max_n = 0
while True:
    tmp = list(map(int, input().split(' ')))
    if tmp[0] == 0:
        break
    max_n = max(max_n, tmp[0])
    del tmp[0]
    li.append(tmp)

visited = [False]*max_n
tmp = []
def dfs(depth, arr, idx):
    if depth == 6:
        print(*tmp)
        return
    for i in range(idx, len(arr)):
        if visited[i]:
            continue
        if len(tmp) != 0 and arr[i] <= tmp[-1]:
            continue
        tmp.append(arr[i])
        visited[i] = True
        dfs(depth+1, arr, idx+1)
        tmp.pop()
        visited[i] = False

for i in li:
    dfs(0, i, 0)
    print('')