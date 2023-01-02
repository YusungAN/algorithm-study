import sys

n = int(sys.stdin.readline().rstrip())
li = []

for i in range(n):
    umm = True
    txt = sys.stdin.readline().rstrip()
    li.append((len(txt), txt))

li.sort()

prior = ''
for (i, j) in li:
    if prior != j:
        print(j)
    prior = j