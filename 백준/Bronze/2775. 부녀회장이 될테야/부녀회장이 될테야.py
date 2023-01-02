import sys

t = int(sys.stdin.readline().rstrip())
arr = []

for i in range(t):
    arr.append(tuple((int(sys.stdin.readline().rstrip()), int(sys.stdin.readline().rstrip()))))

num = []

for i in arr:
    num = [i for i in range(1, i[1]+1)]
    for j in range(i[0]):
        for k in range(i[1]-1):
            num[k+1] = num[k] + num[k+1]
    print(num[i[1]-1])
