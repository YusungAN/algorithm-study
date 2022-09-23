import sys
from collections import defaultdict

input = sys.stdin.readline

dic = defaultdict(int)
n = int(input())
li = list(map(int, input().split(' ')))

for i in li:
    dic[i] += 1

stack = [-1]
res = [-1]
for i in range(1, len(li)):
    if dic[li[n-i-1]] < dic[li[n-i]]:
        stack.append(li[n-i])
        res.append(li[n-i])
    elif dic[li[n-i-1]] >= dic[stack[-1]]:
        while dic[stack[-1]] <= dic[li[n-i-1]] and stack[-1] != -1:
            stack.pop()
        stack.append(stack[-1])
        res.append(stack[-1])
    else:
        stack.append(stack[-1])
        res.append(stack[-1])

print(*res[::-1])