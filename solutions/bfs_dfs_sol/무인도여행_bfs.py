from collections import deque

def bfs(start_r, start_c, visited, maps):
    global R, C
    queue = deque()
    answer = 0
    queue.append((start_r, start_c))
    visited[start_r][start_c] = 1
    answer += int(maps[start_r][start_c])
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue

            if maps[nr][nc] == "X":
                continue

            if visited[nr][nc] == 1:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = 1
            answer += int(maps[nr][nc])

    return answer


def solution(maps):
    global R, C
    R, C = len(maps), len(maps[0])
    answer = []
    visited = [[0] * C for _ in range(R)]
    for r, row in enumerate(maps):
        for c, point in enumerate(row):
            if point == "X" or visited[r][c] == 1:
                continue
            else:
                answer.append(bfs(r, c, visited, maps))

    answer.sort()
    if len(answer) == 0:
        return [-1]
    
    return answer