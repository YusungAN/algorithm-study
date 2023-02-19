import sys

input = sys.stdin.readline

def det(a, b_idx):
    z = 0
    o = 1
    t = 2
    if b_idx == 0:
        z = 3
    elif b_idx == 1:
        o = 3
    elif b_idx == 2:
        t = 3
    else:
        pass
    return a[0][z]*(a[1][o]*a[2][t]-a[1][t]*a[2][o])-a[0][o]*(a[1][z]*a[2][t]-a[1][t]*a[2][z])+a[0][t]*(a[1][z]*a[2][o]-a[1][o]*a[2][z])

for _ in range(int(input())):
    A = []
    for _ in range(3):
        A.append(list(map(int, input().split(' '))))

    detA = det(A, -1)
    detA1 = det(A, 0)
    detA2 = det(A, 1)
    detA3 = det(A, 2)
    print(detA1, detA2, detA3, detA)
    if detA == 0:
        print("No unique solution")
    else:
        print("Unique solution: {:.3f} {:.3f} {:.3f}".format(0 if -0.0005 < detA1/detA < 0.0005 else detA1/detA,
                                                             0 if -0.0005 < detA2/detA < 0.0005 else detA2/detA,
                                                             0 if -0.0005 < detA3/detA < 0.0005 else detA3/detA))
    print('')
