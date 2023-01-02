import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
li = [0]*len(t)
t_set = set(t)

for i in s:
    if i in t_set:
        if i == t[0]:
            li[0] += 1
        else:
            idx = t.find(i)
            if li[idx-1] > 0:
                li[idx-1] -= 1
                li[idx] += 1

print(li[-1])