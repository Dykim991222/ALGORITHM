import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(r)]


def BFS(start_r, start_c, visited, board):
    queue = deque()
    queue.append((start_r, start_c))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[start_r][start_c] = True

    while queue:
        curr_r, curr_c = queue.popleft()
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue

            if visited[nr][nc] == True:
                continue

            if board[nr][nc] == 0:
                continue
            
            visited[nr][nc] = True
            queue.append((nr, nc))

def check_zero(r, c, board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    melt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= r or nc >= c:
            continue

        if board[nr][nc] == 0:
            melt += 1
    
    return max(0, board[r][c] - melt)

def after_year(r, c, board):
    new_board = [[board[i][j]for j in range(c)]for i in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                new_board[i][j] = check_zero(i, j, board)
    return new_board

year = 0

while True:
    visited = [[False] * c for _ in range(r)]
    count = 0

    for p in range(r):
        for q in range(c):
            if not visited[p][q] and board[p][q] > 0:
                BFS(p, q, visited, board)
                count += 1
    
    if count >= 2:
        print(year)
        break

    if count == 0:
        print(0)
        break

    board = after_year(r, c, board)
    year += 1


 