import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))
stack = [-1]
res = [-1]
for i in range(1, n):
    #print(li[n-i-1], li[n-i])
    if li[n-i-1] < li[n-i]:
        stack.append(li[n-i])
        res.append(li[n-i])
    elif li[n-i-1] >= stack[-1]:
        #print('b')
        while stack[-1] <= li[n-i-1] and stack[-1] != -1:
            #print('a')
            stack.pop()
        stack.append(stack[-1])
        res.append(stack[-1])

    else:
        stack.append(stack[-1])
        res.append(stack[-1])
    #print('s', stack)
    #print('r', res)
print(*res[::-1])