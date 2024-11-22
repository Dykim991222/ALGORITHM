import sys
input = sys.stdin.readline

def DFS(r, c, visited, maps):
    global R, C, cnt
    visited[r][c] = 1
    cnt += int(maps[r][c])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            continue
        if visited[nr][nc] == 1:
            continue
        if maps[nr][nc] == 'X':
            continue
        
        visited[nr][nc] = 1
        DFS(nr, nc, visited, maps)

def solution(maps):
    global R, C, cnt
    answer = []
    R, C = len(maps), len(maps[0])
    visited = [[0] * C for _ in range(R)]
    for r, row in enumerate(maps):
        for c, point in enumerate(row):
            if point == 'X' or visited[r][c] == 1:
                continue
            else:
                cnt = 0
                DFS(r, c, visited, maps)
                answer.append(cnt)
    if cnt == 0:
        return -1
    
    return answer