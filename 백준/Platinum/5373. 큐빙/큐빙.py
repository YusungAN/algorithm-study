import sys

input = sys.stdin.readline

def scr_processing(scr):
    scr_split = scr.split()
    cube_state = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                  ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                  ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
                  ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']]

    for i in scr_split:
        if i[0] == 'U':
            if i[1] == '+':
                temp = cube_state[1][0:3]
                cube_state[1][0:3] = cube_state[5][0:3]
                cube_state[5][0:3] = cube_state[4][0:3]
                cube_state[4][0:3] = cube_state[2][0:3]
                cube_state[2][0:3] = temp

                tt1 = cube_state[0][0::3]
                tt2 = cube_state[0][1::3]
                tt3 = cube_state[0][2::3]
                tt1.reverse()
                tt2.reverse()
                tt3.reverse()
                cube_state[0] = tt1 + tt2 + tt3
            else:
                temp = cube_state[1][0:3]
                cube_state[1][0:3] = cube_state[2][0:3]
                cube_state[2][0:3] = cube_state[4][0:3]
                cube_state[4][0:3] = cube_state[5][0:3]
                cube_state[5][0:3] = temp

                tt1 = cube_state[0][0::3]
                tt2 = cube_state[0][1::3]
                tt3 = cube_state[0][2::3]
                cube_state[0] = tt3 + tt2 + tt1
        if i[0] == 'R':
            if i[1] == '+':
                temp = cube_state[2][2::3]
                cube_state[2][2::3] = cube_state[3][2::3]
                cube_state[3][2::3] = list(reversed(cube_state[5][0::3]))
                cube_state[5][0::3] = list(reversed(cube_state[0][2::3]))
                cube_state[0][2::3] = temp

                tt1 = cube_state[1][0::3]
                tt2 = cube_state[1][1::3]
                tt3 = cube_state[1][2::3]
                tt1.reverse()
                tt2.reverse()
                tt3.reverse()
                cube_state[1] = tt1 + tt2 + tt3
            else:
                temp = cube_state[2][2::3]
                cube_state[2][2::3] = cube_state[0][2::3]
                cube_state[0][2::3] = list(reversed(cube_state[5][0::3]))
                cube_state[5][0::3] = list(reversed(cube_state[3][2::3]))
                cube_state[3][2::3] = list(temp)

                tt1 = cube_state[1][0::3]
                tt2 = cube_state[1][1::3]
                tt3 = cube_state[1][2::3]
                cube_state[1] = tt3 + tt2 + tt1
        if i[0] == 'F':
            if i[1] == '+':
                temp = cube_state[0][6:9]
                cube_state[0][6:9] = list(reversed(cube_state[4][2::3]))
                cube_state[4][2::3] = cube_state[3][0:3]
                cube_state[3][0:3] = list(reversed(cube_state[1][0::3]))
                cube_state[1][0::3] = temp

                tt1 = cube_state[2][0::3]
                tt2 = cube_state[2][1::3]
                tt3 = cube_state[2][2::3]
                tt1.reverse()
                tt2.reverse()
                tt3.reverse()
                cube_state[2] = tt1 + tt2 + tt3
            else:
                temp = cube_state[0][6:9]
                cube_state[0][6:9] = cube_state[1][0::3]
                cube_state[1][0::3] = list(reversed(cube_state[3][0:3]))
                cube_state[3][0:3] = cube_state[4][2::3]
                cube_state[4][2::3] = list(reversed(temp))

                tt1 = cube_state[2][0::3]
                tt2 = cube_state[2][1::3]
                tt3 = cube_state[2][2::3]
                cube_state[2] = tt3 + tt2 + tt1
        if i[0] == 'D':
            if i[1] == '+':
                temp = cube_state[2][6:9]
                cube_state[2][6:9] = cube_state[4][6:9]
                cube_state[4][6:9] = cube_state[5][6:9]
                cube_state[5][6:9] = cube_state[1][6:9]
                cube_state[1][6:9] = temp

                tt1 = cube_state[3][0::3]
                tt2 = cube_state[3][1::3]
                tt3 = cube_state[3][2::3]
                tt1.reverse()
                tt2.reverse()
                tt3.reverse()
                cube_state[3] = tt1 + tt2 + tt3
            else:
                temp = cube_state[1][6:9]
                cube_state[1][6:9] = cube_state[5][6:9]
                cube_state[5][6:9] = cube_state[4][6:9]
                cube_state[4][6:9] = cube_state[2][6:9]
                cube_state[2][6:9] = temp

                tt1 = cube_state[3][0::3]
                tt2 = cube_state[3][1::3]
                tt3 = cube_state[3][2::3]
                cube_state[3] = tt3 + tt2 + tt1
        if i[0] == 'L':
            if i[1] == '+':
                temp = cube_state[2][0::3]
                cube_state[2][0::3] = cube_state[0][0::3]
                cube_state[0][0::3] = list(reversed(cube_state[5][2::3]))
                cube_state[5][2::3] = list(reversed(cube_state[3][0::3]))
                cube_state[3][0::3] = list(temp)

                tt1 = cube_state[4][0::3]
                tt2 = cube_state[4][1::3]
                tt3 = cube_state[4][2::3]
                tt1.reverse()
                tt2.reverse()
                tt3.reverse()
                cube_state[4] = tt1 + tt2 + tt3
            else:
                temp = cube_state[2][0::3]
                cube_state[2][0::3] = cube_state[3][0::3]
                cube_state[3][0::3] = list(reversed(cube_state[5][2::3]))
                cube_state[5][2::3] = list(reversed(cube_state[0][0::3]))
                cube_state[0][0::3] = temp

                tt1 = cube_state[4][0::3]
                tt2 = cube_state[4][1::3]
                tt3 = cube_state[4][2::3]
                cube_state[4] = tt3 + tt2 + tt1
        if i[0] == 'B':
            if i[1] == '+':
                temp = cube_state[0][0:3]
                cube_state[0][0:3] = cube_state[1][2::3]
                cube_state[1][2::3] = list(reversed(cube_state[3][6:9]))
                cube_state[3][6:9] = cube_state[4][0::3]
                cube_state[4][0::3] = list(reversed(temp))

                tt1 = cube_state[5][0::3]
                tt2 = cube_state[5][1::3]
                tt3 = cube_state[5][2::3]
                tt1.reverse()
                tt2.reverse()
                tt3.reverse()
                cube_state[5] = tt1 + tt2 + tt3
            else:
                temp = cube_state[0][0:3]
                cube_state[0][0:3] = list(reversed(cube_state[4][0::3]))
                cube_state[4][0::3] = cube_state[3][6:9]
                cube_state[3][6:9] = list(reversed(cube_state[1][2::3]))
                cube_state[1][2::3] = temp

                tt1 = cube_state[5][0::3]
                tt2 = cube_state[5][1::3]
                tt3 = cube_state[5][2::3]
                cube_state[5] = tt3 + tt2 + tt1
        if i[0] == 'M':
            if i[1] == '+':
                temp = cube_state[0][1::3]
                cube_state[0][1::3] = list(reversed(cube_state[5][1::3]))
                cube_state[5][1::3] = list(reversed(cube_state[3][1::3]))
                cube_state[3][1::3] = cube_state[2][1::3]
                cube_state[2][1::3] = temp
            else:
                temp = cube_state[0][1::3]
                cube_state[0][1::3] = cube_state[2][1::3]
                cube_state[2][1::3] = cube_state[3][1::3]
                cube_state[3][1::3] = list(reversed(cube_state[5][1::3]))
                cube_state[5][1::3] = list(reversed(temp))
    return cube_state[0]

n = int(input())
for i in range(n):
    a = int(input())
    li = input().rstrip()
    tmp = scr_processing(li)
    for ii in range(3):
        for j in range(3):
            print(tmp[3*ii+j], end='')
        print('')


