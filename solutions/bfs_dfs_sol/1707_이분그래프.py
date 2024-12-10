import sys
from collections import deque

input = sys.stdin.readline

K = int(input())


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.pop()
        current_node_visit = visited[current]

        for next_node in node[current]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = 1 - current_node_visit
            elif visited[next_node] == current_node_visit:
                return False
            elif visited[next_node] == (1 - current_node_visit):
                continue

    return True


for _ in range(K):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    visited = [-1] * (V + 1)

    is_failed = False
    for i in range(1, V + 1):
        if visited[i] == -1:
            result = bfs(i)
            if not result:
                print("NO")
                is_failed = True
                break

    if not is_failed:
        print("YES")
