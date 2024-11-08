R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

print(R, C)
print(board)
board[1][1] = "p"
print(board)