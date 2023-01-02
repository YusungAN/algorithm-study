n = int(input())
room = []
cnt = 0

for i in range(0, n):
    room.append(list(map(int, input().split())))

room = sorted(room, key=lambda a: a[0])
room = sorted(room, key=lambda a: a[1])

start = 0
end = 0

for s, e in room:
    if end <= s:
        start = s
        end = e
        cnt += 1

print(cnt)