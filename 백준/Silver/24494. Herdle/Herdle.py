import sys

input = sys.stdin.readline

correct = [list(input().rstrip()) for _ in range(3)]
guess = [list(input().rstrip()) for _ in range(3)]
check = [0]*26
green = 0
yellow = 0



for i in range(3):
    for j in range(3):
        if correct[i][j] == guess[i][j]:
            green += 1
            guess[i][j] = '.'
        else:
            check[ord(correct[i][j])-65] += 1

for i in range(3):
    for j in range(3):
        if guess[i][j] != '.' and check[ord(guess[i][j])-65] > 0:
            check[ord(guess[i][j]) - 65] -= 1
            yellow += 1

print(green)
print(yellow)
