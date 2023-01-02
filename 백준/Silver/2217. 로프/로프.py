n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

rope = sorted(rope)

_max = 0
for i in range(n):
    if _max < rope[i] * (n-i):
        _max = rope[i] * (n-i)

print(_max)
