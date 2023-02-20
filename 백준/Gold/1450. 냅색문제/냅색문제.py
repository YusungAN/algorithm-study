import sys

input = sys.stdin.readline

n, c = map(int, input().split(' '))
m_li = list(map(int, input().split(' ')))

p1 = []
p2 = []

def dfs(s, e, p, res):
    if s > e:
        p.append(res)
        return
    dfs(s+1, e, p, res)
    dfs(s+1, e, p, res+m_li[s])

dfs(0, n // 2 - 1, p1, 0)
dfs(n//2, n-1, p2, 0)
p2.sort()

ans = 0
for i in p1:
    if i > c:
        continue
    start = 0
    end = len(p2)
    while start < end:
        mid = (start+end)//2
        if p2[mid]+i > c:
            end = mid
        else:
            start = mid+1
    ans += end

print(ans)
