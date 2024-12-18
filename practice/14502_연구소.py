import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def BFS(board, virus_positions):
    global N, M
    queue = deque(virus_positions)
    visited = [[0] * M for _ in range(N)]
    
    for x, y in virus_positions:
        visited[x][y] = 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if visited[nr][nc] == 1:
                continue
            if board[nr][nc] != 0:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = 1
            board[nr][nc] = 2

def count_safe_area(board):
    return sum(row.count(0) for row in board)

global N, M
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            empty.append((r, c))
        elif board[r][c] == 2:
            virus.append((r, c))

max_safe_area = 0

for walls in combinations(empty, 3):
    temp_board = [row[:] for row in board]

    for r, c in walls:
        temp_board[r][c] = 1

    BFS(temp_board, virus)

    max_safe_area = max(max_safe_area, count_safe_area(temp_board))

print(max_safe_area)
