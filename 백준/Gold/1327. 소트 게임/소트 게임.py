import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))

def rv(idx, P):
    global K
    for i in range(K//2):
        P[idx+i], P[idx+K-i-1] = P[idx+K-i-1], P[idx+i]


def check(P):
    for i in range(N-1):
        if P[i] > P[i+1]:
            return False
    return True


def list_to_idx(per):
    ret = 0
    mul = 1
    for i in range(1, N+1):
        ret += per[-i]*mul
        mul *= 10
    return ret


q = deque()
q.append((P, 0))

visited = defaultdict(int)

visited[list_to_idx(P)] = 1
while q:
    per, cnt = q.popleft()

    if check(per):
        print(cnt)
        exit(0)

    for i in range(N-K+1):
        rv(i, per)
        if visited[list_to_idx(per)]:
            rv(i, per)
            continue
        visited[list_to_idx(per)] = 1
        q.append((per[:], cnt+1))
        rv(i, per)

print(-1)