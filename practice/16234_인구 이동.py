from collections import deque
import sys
import copy
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def BFS(start_r, start_c, visited, board):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True
    total_population = board[start_r][start_c]
    moved_cnt = 1
    save_address = []
    save_address.append([start_r, start_c])
    moved_occured = False

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            if visited[nr][nc] == True:
                continue

            if not L <= abs(board[nr][nc] - board[r][c]) <= R:
                continue

            visited[nr][nc] = True
            queue.append((nr, nc))
            total_population += board[nr][nc]
            save_address.append([nr, nc])
            moved_cnt += 1
            moved_occured = True

    after_move = total_population // moved_cnt
    
    for p, q in save_address:
        board[p][q] = after_move

    return moved_occured

days = 0

while True:
    moved = False
    visited = [[False] * N for _ in range(N)]

    for r, row in enumerate(board):
        for c, point in enumerate(row):
            if not visited[r][c]:
                if BFS(r, c, visited, board):
                    moved = True


    if not moved:
        break

    days += 1



print(days)