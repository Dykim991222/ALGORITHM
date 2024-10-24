import sys
def dfs(r, c, visited, maps):
    global cnt
    global R, C
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    cnt += int(maps[r][c])
    
    # return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if visited[nr][nc] == 1:
            continue
        if maps[nr][nc] == 'X':
            continue

        visited[nr][nc] = 1
        dfs(nr, nc, visited, maps)


def solution(maps):
    global R, C
    global cnt
    sys.setrecursionlimit(1<<30)

    R, C = len(maps), len(maps[0])
    answer = []
    visited = [[0] * C for _ in range(R)]
    for r, row in enumerate(maps):
        for c, point in enumerate(row):
            if point == "X" or visited[r][c] == 1:
                continue
            else:
                cnt = 0
                visited[r][c] = 1
                dfs(r, c, visited, maps)
                answer.append(cnt)
                

    answer.sort()
    if len(answer) == 0:
        return [-1]
    
    return answer