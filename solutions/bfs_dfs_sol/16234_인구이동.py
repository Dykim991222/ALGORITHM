import sys
from collections import deque


input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def bfs(s_r, s_c, visited):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    res = False
    queue = deque()
    queue.append((s_r, s_c))
    visited[s_r][s_c] = True
    visit_list = [(s_r, s_c)]
    total_population = board[s_r][s_c]
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            if visited[nr][nc]:
                continue

            diff = abs(board[r][c] - board[nr][nc])
            if not (L <= diff <= R):
                continue

            res = True
            queue.append((nr, nc))
            visited[nr][nc] = True
            visit_list.append((nr, nc))
            total_population += board[nr][nc]

    new_population = total_population // len(visit_list)
    for item in visit_list:
        board[item[0]][item[1]] = new_population
    return res


def move(board):
    visited = [[False] * N for _ in range(N)]
    is_moved = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                res = bfs(r, c, visited)
                if res:
                    is_moved = True

    return is_moved


ans = 0
while True:
    is_moved = move(board)
    if not is_moved:
        break
    ans += 1

print(ans)
