
def dfs(idx, connections, visited):
    visited[idx] = True
    for c in connections[idx]:
        if not visited[c]:
            dfs(c, connections, visited)


def solution(n, computers):
    connections = [[] for _ in range(n+1)]
    
    for r in range(1, n+1):
        for c in range(1, n+1):
            if computers[r-1][c-1] == 1 and r != c:
                connections[r].append(c)
                
    visited = [False for _ in range(n+1)]
    answer = 0

    for idx in range(1, n+1):
        if not visited[idx]:
            answer += 1
            dfs(idx, connections, visited)
                
    
    return answer