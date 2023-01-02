import sys

n = int(sys.stdin.readline().rstrip())
li = []
li2 = [0 for i in range(8002)]
for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    li.append(temp)
    li2[temp+4000] += 1
li.sort()
mode = 10000
_max = max(li2)
cnt = 0
for i in range(len(li2)):
    if li2[i] == _max:
        mode = i
        cnt += 1
        if cnt == 2:
            break

print(round(sum(li) / len(li)))
print(li[len(li)//2])
print(mode-4000)
print(li[len(li)-1]-li[0])
