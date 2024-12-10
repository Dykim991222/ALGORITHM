import sys
from collections import deque
input = sys.stdin.readline

def BFS(start_r, start_c, visited, board, r, c):
    dr = [-1, 0, 1, -1, 1, -1, 0, 1]
    dc = [1, 1, 1, 0, 0, -1, -1, -1]
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True
    
    while queue:
        curr_r, curr_c = queue.popleft()
        for i in range(8):
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

answers = []
while True:
    w, h = map(int, input().split())
    count = 0
    

    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == 1:
                BFS(i, j, visited, board, h, w)
                count += 1
            


    answers.append(count)

for answer in answers:
    print(answer)