import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = input().rstrip().split()
N = list(N)
K = int(K)
n_len = len(N)

same_num_flag = False
for i in range(1, n_len):
    for j in range(i):
        if N[i] == N[j]:
            same_num_flag = True
            break

_max = '0'*n_len

visited = defaultdict(int)

if n_len == 1 or (n_len == 2 and N[1] == '0'):
    print(-1)
    exit(0)

def list_max(a, b):
    for i in range(n_len):
        if ord(a[i]) > ord(b[i]):
            return a
        elif ord(a[i]) < ord(b[i]):
            return ''.join(b)
    
    return a


def DFS(count, now_list):
    global _max
    list_str = ''.join(now_list)

    visited[list_str] = count
    # print(list_str, count)
    # print(list_str, count)
    if same_num_flag or (K-count) % 2 == 0:
        _max = list_max(_max, list_str)
    if count == K:
        _max = list_max(_max, list_str)
        return
    
    for j in range(1, n_len):
        for i in range(j):
            if now_list[j] != '0' or i != 0:
                now_list[i], now_list[j] = now_list[j], now_list[i]
                # if list_str == '123456':
                #     print(now_list, visited[''.join(now_list)])
                if visited[''.join(now_list)] == 0 or visited[''.join(now_list)] > count:
                    DFS(count+1, now_list)
                now_list[i], now_list[j] = now_list[j], now_list[i]

DFS(0, N)
print(_max if _max[0] != '0' else '-1')