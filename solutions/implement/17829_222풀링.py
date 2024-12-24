import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def pooling(board, offset_r, offset_c):
    item_list = [
        board[offset_r][offset_c],
        board[offset_r + 1][offset_c],
        board[offset_r][offset_c + 1],
        board[offset_r + 1][offset_c + 1],
    ]

    return sorted(item_list)[2]


def down_sampling(board, R, C):
    new_board = [[0] * (C // 2) for _ in range(R // 2)]

    for r in range(0, R, 2):
        for c in range(0, C, 2):
            new_board[r // 2][c // 2] = pooling(board, r, c)

    return new_board


while True:
    if N == 1:
        break
    else:
        board = down_sampling(board, N, N)
        N //= 2

print(board[0][0])
