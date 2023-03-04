import sys

input = sys.stdin.readline

s = input().rstrip().split(' ')

for item in s:
    idx = 0
    visited = [False]*len(item)
    for i in range(len(item)):
        if item[i] == '<' or item[i] == '>' or item[i] == '(' or item[i] == ')':
            if idx <= i-1:
                print(item[idx:i], end=' ')
            print(item[i], end=' ')
            idx = i+1
        elif item[i] == '&' or item[i] == '|':
            if i > 0 and item[i] == item[i-1] and not visited[i-1]:
                if idx < i-1:
                    print(item[idx:i-1], end=' ')
                print(item[i-1]+item[i], end=' ')
                idx = i + 1
                visited[i] = True
                visited[i-1] = True
    if idx <= len(item)-1:
        print(item[idx:], end=' ')