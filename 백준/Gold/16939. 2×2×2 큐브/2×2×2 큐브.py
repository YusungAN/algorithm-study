import sys

input = sys.stdin.readline

def scr_processing(scr, li):
    scr_split = scr.split()
    cube_state = [[] for i in range(6)]

    cnt = -1
    temp = []
    um = [0, 2, 3, 4, 1, 5]
    for i in range(len(li)):
        if i % 4 == 0:
            cnt += 1
            temp = []
            cube_state[um[cnt]] = temp

        temp.append(li[i])

    for i in scr_split:
        if i[0] == 'U':
            if len(i) == 1:
                temp = cube_state[1][0:2]
                cube_state[1][0:2] = cube_state[5][0:2]
                cube_state[5][0:2] = cube_state[4][0:2]
                cube_state[4][0:2] = cube_state[2][0:2]
                cube_state[2][0:2] = temp

                tt1 = cube_state[0][0::2]
                tt2 = cube_state[0][1::2]
                tt1.reverse()
                tt2.reverse()
                cube_state[0] = tt1 + tt2
            else:
                temp = cube_state[1][0:2]
                cube_state[1][0:2] = cube_state[2][0:2]
                cube_state[2][0:2] = cube_state[4][0:2]
                cube_state[4][0:2] = cube_state[5][0:2]
                cube_state[5][0:2] = temp

                tt1 = cube_state[0][0::2]
                tt2 = cube_state[0][1::2]
                cube_state[0] = tt2 + tt1
        if i[0] == 'R':
            if len(i) == 1:
                temp = cube_state[2][1::2]
                cube_state[2][1::2] = cube_state[3][1::2]
                cube_state[3][1::2] = list(reversed(cube_state[5][0::2]))
                cube_state[5][0::2] = list(reversed(cube_state[0][1::2]))
                cube_state[0][1::2] = temp

                tt1 = cube_state[1][0::2]
                tt2 = cube_state[1][1::2]
                tt1.reverse()
                tt2.reverse()
                cube_state[1] = tt1 + tt2
            else:
                temp = cube_state[2][1::2]
                cube_state[2][1::2] = cube_state[0][1::2]
                cube_state[0][1::2] = list(reversed(cube_state[5][0::2]))
                cube_state[5][0::2] = list(reversed(cube_state[3][1::2]))
                cube_state[3][1::2] = list(temp)

                tt1 = cube_state[1][0::2]
                tt2 = cube_state[1][1::2]
                cube_state[1] = tt2 + tt1
        if i[0] == 'F':
            if len(i) == 1:
                temp = cube_state[0][2:4]
                cube_state[0][2:4] = list(reversed(cube_state[4][1::2]))
                cube_state[4][1::2] = cube_state[3][0:2]
                cube_state[3][0:2] = list(reversed(cube_state[1][0::2]))
                cube_state[1][0::2] = temp

                tt1 = cube_state[2][0::2]
                tt2 = cube_state[2][1::2]
                tt1.reverse()
                tt2.reverse()
                cube_state[2] = tt1 + tt2
            else:
                temp = cube_state[0][2:4]
                cube_state[0][2:4] = cube_state[1][0::2]
                cube_state[1][0::2] = list(reversed(cube_state[3][0:2]))
                cube_state[3][0:2] = cube_state[4][1::2]
                cube_state[4][1::2] = list(reversed(temp))

                tt1 = cube_state[2][0::2]
                tt2 = cube_state[2][1::2]
                cube_state[2] = tt2 + tt1
        if i[0] == 'D':
            if len(i) == 1:
                temp = cube_state[2][2:4]
                cube_state[2][2:4] = cube_state[4][2:4]
                cube_state[4][2:4] = cube_state[5][2:4]
                cube_state[5][2:4] = cube_state[1][2:4]
                cube_state[1][2:4] = temp

                tt1 = cube_state[3][0::2]
                tt2 = cube_state[3][1::2]
                tt1.reverse()
                tt2.reverse()
                cube_state[3] = tt1 + tt2
            else:
                temp = cube_state[1][2:4]
                cube_state[1][2:4] = cube_state[5][2:4]
                cube_state[5][2:4] = cube_state[4][2:4]
                cube_state[4][2:4] = cube_state[2][2:4]
                cube_state[2][2:4] = temp

                tt1 = cube_state[3][0::2]
                tt2 = cube_state[3][1::2]
                cube_state[3] = tt2 + tt1
        if i[0] == 'L':
            if len(i) == 1:
                temp = cube_state[2][0::2]
                cube_state[2][0::2] = cube_state[0][0::2]
                cube_state[0][0::2] = list(reversed(cube_state[5][1::2]))
                cube_state[5][1::2] = list(reversed(cube_state[3][0::2]))
                cube_state[3][0::2] = list(temp)

                tt1 = cube_state[4][0::2]
                tt2 = cube_state[4][1::2]
                tt1.reverse()
                tt2.reverse()
                cube_state[4] = tt1 + tt2
            else:
                temp = cube_state[2][0::2]
                cube_state[2][0::2] = cube_state[3][0::2]
                cube_state[3][0::2] = list(reversed(cube_state[5][1::2]))
                cube_state[5][1::2] = list(reversed(cube_state[0][0::2]))
                cube_state[0][0::2] = temp

                tt1 = cube_state[4][0::2]
                tt2 = cube_state[4][1::2]
                cube_state[4] = tt2 + tt1
        if i[0] == 'B':
            if len(i) == 1:
                temp = cube_state[0][0:2]
                cube_state[0][0:2] = cube_state[1][1::2]
                cube_state[1][1::2] = list(reversed(cube_state[3][2:4]))
                cube_state[3][2:4] = cube_state[4][0::2]
                cube_state[4][0::2] = list(reversed(temp))

                tt1 = cube_state[5][0::2]
                tt2 = cube_state[5][1::2]
                tt1.reverse()
                tt2.reverse()
                cube_state[5] = tt1 + tt2
            else:
                temp = cube_state[0][0:2]
                cube_state[0][0:2] = list(reversed(cube_state[4][0::2]))
                cube_state[4][0::2] = cube_state[3][2:4]
                cube_state[3][2:4] = list(reversed(cube_state[1][1::2]))
                cube_state[1][1::2] = temp

                tt1 = cube_state[5][0::2]
                tt2 = cube_state[5][1::2]
                cube_state[5] = tt2 + tt1

    for i in cube_state:
        for j in range(1, 4):
            if i[j] != i[j-1]:
                return False
    return True

li = list(map(int, input().split(' ')))
ress = [[] for i in range(6)]




a = scr_processing('U', li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("U'", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("R'", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("R", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("F", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("F'", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("L", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("L'", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("D'", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("D", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("B'", li[:])
if a:
    print('1')
    exit(0)
a = scr_processing("B", li[:])
if a:
    print('1')
    exit(0)

print(0)