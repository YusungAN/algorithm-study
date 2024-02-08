import sys
from collections import deque

input = sys.stdin.readline

visited  = [[[False]*8 for _ in range(8)] for _ in range(8)] # [8][8][8]
wall_check = [[False]*8 for _ in range(8)]

for i in range(8):
    map_row = list(input().rstrip())
    for j in range(8):
        if map_row[j] == '#':
            wall_check[i][j] = True


q = deque()
q.append((0, 7, 0)) # start


def range_check(x, y):
    return (0 <= x < 8) and (0 <= y < 8)

def is_wall(x, y, time):
    if y-time < 0:
        return False
    
    return wall_check[y-time][x]

# print(is_wall(1, 7, 1), wall_check[7][1])
while q:
    x, y, time = q.popleft()
    if is_wall(x, y, time):
        continue

    if x == 7 and y == 0:
        print(1)
        exit(0)


    if range_check(x+1, y) and not is_wall(x+1, y, time) and not visited[y][x+1][0]:
        q.append((x+1, y, time+1))
        visited[y][x+1][0] = True

    if range_check(x-1, y) and not is_wall(x-1, y, time) and not visited[y][x-1][1]:
        q.append((x-1, y, time+1))
        visited[y][x-1][1] = True
    
    if range_check(x, y-1) and not is_wall(x, y-1, time) and not visited[y-1][x][2]:
        q.append((x, y-1, time+1))
        visited[y-1][x][2] = True
    
    if range_check(x, y+1) and not is_wall(x, y+1, time) and not visited[y+1][x][3]:
        q.append((x, y+1, time+1))
        visited[y+1][x][3] = True

    if range_check(x-1, y-1) and not is_wall(x-1, y-1, time) and not visited[y-1][x-1][3]:
        q.append((x-1, y-1, time+1))
        visited[y-1][x-1][3] = True
    
    if range_check(x+1, y-1) and not is_wall(x+1, y-1, time) and not visited[y-1][x+1][3]:
        q.append((x+1, y-1, time+1))
        visited[y-1][x+1][3] = True
    
    if range_check(x-1, y+1) and not is_wall(x-1, y+1, time) and not visited[y+1][x-1][3]:
        q.append((x-1, y+1, time+1))
        visited[y+1][x-1][3] = True
    
    if range_check(x+1, y+1) and not is_wall(x+1, y+1, time) and not visited[y+1][x+1][3]:
        q.append((x+1, y+1, time+1))
        visited[y+1][x+1][3] = True
    
    # stay
    q.append((x, y, time+1))

print(0)