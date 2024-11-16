from collections import deque

def BFS1(start_r, start_c, visited, board):
    global R, C
    notyet = []
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = 1
    
    notyet.append(board[start_r][start_c])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc] == 1:
                continue
            if board[nr][nc] == board[r][c]:
                queue.append((nr, nc))
                notyet.append(board[nr][nc])
                visited[nr][nc] = 1      
    return notyet


def BFS2(start_r, start_c, visited, board):
    notyet2 = []
    queue2 = deque()
    queue2.append((start_r, start_c))
    visited[start_r][start_c] = 1
    global R, C
    for a in range(R):
        for b in range(C):
            if board[a][b] == 'G' or board[a][b] == 'R':
                board[a][b] = 'Z'
    notyet2.append(board[start_r][start_c])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue2:
        r, c = queue2.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc] == 1:
                continue
            if board[nr][nc] == board[r][c]:
                queue2.append((nr, nc))
                notyet2.append(board[nr][nc])
                visited[nr][nc] = 1      
    return notyet2

N = int(input())
board = []
for _ in range(N):
    row = list(input().strip())
    board.append(row)

answer1 = []
answer2 = []
global R, C
R, C = len(board), len(board[0])
visited = [[0] * C for _ in range(R)]

# BFS1 실행
visited = [[0] * C for _ in range(R)]
for r, row in enumerate(board):
    for c, point in enumerate(row):
        if visited[r][c] == 0:
            answer1.append(BFS1(r, c, visited, board))

# visited 배열 초기화
visited = [[0] * C for _ in range(R)]

# BFS2 실행
for r, row in enumerate(board):
    for c, point in enumerate(row):
        if visited[r][c] == 0:
            answer2.append(BFS2(r, c, visited, board))

print(len(answer1), len(answer2))