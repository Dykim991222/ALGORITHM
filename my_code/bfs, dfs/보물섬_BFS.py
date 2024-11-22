import sys
from collections import deque
input = sys.stdin.readline

def BFS(start_r, start_c, board):
    global R, C
    queue = deque()
    queue.append((start_r, start_c, 0))
    visited = [[0] * C for _ in range(R)]
    visited[start_r][start_c] = 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    max_distance = 0
    
    while queue:
        r, c, dist = queue.popleft()
        max_distance = max(dist, max_distance)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc] == 1:
                continue
            if board[nr][nc] == 'W':
                continue

            queue.append((nr, nc, dist + 1))
            visited[nr][nc] = 1

    return max_distance

    
global R, C
R, C = map(int, input().split(' '))
board = []
answer = 0
for _ in range(R):
    row = list(input().strip())
    board.append(row)

for r in range(R):
    for c in range(C):
        if board[r][c] == 'L':
            answer = max(answer, BFS(r, c, board))

print(answer)