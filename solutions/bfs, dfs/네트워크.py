from collections import deque

def bfs(start_r, start_c, visited, computers):
    global R, C
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = 1
    answer1 = 0
    answer1 += int(computers[start_r][start_c])

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
            if computers[nr][nc] == 0:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = 1
            answer1 += int(computers[nr][nc])
    return answer1




def solution(n, computers):
    answer = []
    global R, C
    R, C = len(computers), len(computers[0])
    visited = [[0] * C for _ in range(R)]

    for r, row in enumerate(computers):
        for c, point in enumerate(row):
            if visited[r][c] == 1 or computers[r][c] == 0:
                continue
            else:
                answer.append(bfs(r, c, visited, computers))
    
    if len(answer) == 0:
        return 0
    return len(answer)