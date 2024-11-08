
from collections import deque

def bfs(start_idx, visited, connections):
    queue = deque()
    queue.append(start_idx)
    visited[start_idx] = True
    
    while queue:
        current_idx = queue.popleft()
        for c in connections[current_idx]:
            if not visited[c]:
                queue.append(c)
                visited[c] = True


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
            bfs(idx, visited, connections)
                
    
    return answer