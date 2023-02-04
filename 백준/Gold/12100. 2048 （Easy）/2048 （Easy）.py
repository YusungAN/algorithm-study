import sys

input = sys.stdin.readline

n = int(input())
game = [list(map(int, input().split(' '))) for _ in range(n)]

def to_up(game_state):
    for col in range(n):
        new_col = [0]*n
        li = [i[col] for i in game_state]
        idx = 0
        prev = 0
        while li:
            if li[0] == 0:
                li.pop(0)
            elif li[0] == prev:
                new_col[idx] = li[0]*2
                li.pop(0)
                idx += 1
                prev = 0
            else:
                if prev != 0:
                    new_col[idx] = prev
                    idx += 1
                prev = li[0]
                li.pop(0)
        if prev != 0:
            new_col[idx] = prev
        for row in range(n):
            game_state[row][col] = new_col[row]

def to_down(game_state):
    for col in range(n):
        new_col = [0]*n
        li = [i[col] for i in game_state]
        idx = 0
        prev = 0
        while li:
            if li[-1] == 0:
                li.pop()
            elif li[-1] == prev:
                new_col[idx] = li[-1] * 2
                li.pop()
                idx += 1
                prev = 0
            else:
                if prev != 0:
                    new_col[idx] = prev
                    idx += 1
                prev = li[-1]
                li.pop()
        if prev != 0:
            new_col[idx] = prev
        new_col.reverse()
        for row in range(n):
            game_state[row][col] = new_col[row]

def to_left(game_state):
    for row in range(n):
        new_row = [0]*n
        li = game_state[row][:]
        idx = 0
        prev = 0
        while li:
            if li[0] == 0:
                li.pop(0)
            elif li[0] == prev:
                new_row[idx] = li[0] * 2
                li.pop(0)
                idx += 1
                prev = 0
            else:
                if prev != 0:
                    new_row[idx] = prev
                    idx += 1
                prev = li[0]
                li.pop(0)
        if prev != 0:
            new_row[idx] = prev
        for col in range(n):
            game_state[row][col] = new_row[col]

def to_right(game_state):
    for row in range(n):
        new_row = [0]*n
        li = game_state[row][:]
        idx = 0
        prev = 0
        while li:
            if li[-1] == 0:
                li.pop()
            elif li[-1] == prev:
                new_row[idx] = li[-1] * 2
                li.pop()
                idx += 1
                prev = 0
            else:
                if prev != 0:
                    new_row[idx] = prev
                    idx += 1
                prev = li[-1]
                li.pop()
        if prev != 0:
            new_row[idx] = prev
        new_row.reverse()
        for col in range(n):
            game_state[row][col] = new_row[col]

def find_max(game_state):
    tmp = [max(i) for i in game_state]
    return max(tmp)

ans = 0
def bt(depth, game_state):
    global ans
    ans = max(ans, find_max(game_state))
    if depth == 5:
        return

    gt = [x[:] for x in game_state]
    to_up(gt)
    bt(depth+1, gt)

    gt = [x[:] for x in game_state]
    to_down(gt)
    bt(depth + 1, gt)

    gt = [x[:] for x in game_state]
    to_left(gt)
    bt(depth + 1, gt)

    gt = [x[:] for x in game_state]
    to_right(gt)
    bt(depth + 1, gt)

bt(0, game)
print(ans)
