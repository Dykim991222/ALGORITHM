from collections import deque
import sys
input = sys.stdin.readline

def BFS(start_r, start_c, visited, board):
    queue = deque()
    queue.append((start_r, start_c))
    distance = 0
    global R, C
    visited[start_r][start_c] = 1

    dc = [1, -1 ,0, 0]
    dr = [0, 0, 1, -1]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc] == 1:
                continue
            if board[nr][nc] == 'W':
                continue

            queue.append((nr, nc))
            distance += 1
            visited[nr][nc] = 1

    return distance


global R, C
answer = 0
board = []
R , C = map(int, input().split())
for _ in range(R):
    row = list(input().strip())
    board.append(row)
visited = [[0] * C for _ in range(R)]
for r, row in enumerate(board):
    for c, point in enumerate(row):
        if board[r][c] == 'W' or visited[r][c] == 1:
            continue
        else:
            answer = max(answer, int(BFS(r,c,visited,board)))

print(answer)