import sys

input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())
board = [[0] * C for _ in range(R)]

if K == 1:
    print("1 1")
elif K > R * C:
    print(0)

else:
    r = 0
    c = 0
    board[0][0] = 1
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    direction = 0

    for _ in range(K - 1):
        nr = r + dr[direction]
        nc = c + dc[direction]

        if nr < 0 or nr >= R or nc < 0 or nc >= C or board[nr][nc] != 0:
            direction = (direction + 1) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]
        r = nr
        c = nc
        board[r][c] = 1

    print(c + 1, r + 1)
