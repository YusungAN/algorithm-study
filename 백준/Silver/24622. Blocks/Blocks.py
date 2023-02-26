import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

blocks = [set(input().rstrip()) for _ in range(4)]

for _ in range(N):
    word = input().rstrip()
    for p in permutations(range(4), len(word)):
        flag = True
        for i in range(len(word)):
            if word[i] not in blocks[p[i]]:
                flag = False
                break
        if flag:
            break
    else:
        print('NO')
        continue
    print('YES')