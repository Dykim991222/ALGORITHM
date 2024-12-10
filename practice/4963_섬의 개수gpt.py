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
        for i in range(8):  # 8방향 탐색
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            # 범위를 벗어나면 무시
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue

            # 이미 방문했거나, 바다인 경우 무시
            if visited[nr][nc] or board[nr][nc] == 0:
                continue

            visited[nr][nc] = True
            queue.append((nr, nc))

while True:
    w, h = map(int, input().split())  # 너비(w)와 높이(h)
    if w == 0 and h == 0:  # 종료 조건
        break

    board = [list(map(int, input().split())) for _ in range(h)]  # h행 w열 보드 생성
    visited = [[False] * w for _ in range(h)]  # 방문 여부 저장

    count = 0  # 섬 개수 카운트
    for i in range(h):  # 행 순회
        for j in range(w):  # 열 순회
            if not visited[i][j] and board[i][j] == 1:  # 새로운 섬 발견
                BFS(i, j, visited, board, h, w)
                count += 1  # 섬 개수 증가

    print(count)  # 결과 출력
