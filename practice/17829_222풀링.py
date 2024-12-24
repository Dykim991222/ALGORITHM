import sys
input = sys.stdin.readline

N = int(input().rstrip())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

new_board = []  

for i in range(0, N, 2):  
    new_row = []
    for k in range(0, N, 2):  
        matrix = [
            board[i][k], board[i][k+1],
            board[i+1][k], board[i+1][k+1]
        ]
        
        matrix.sort(reverse=True)
        new_row.append(matrix[1])
    new_board.append(new_row)


