import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
node = [[] for _ in range(K+1)]
score_list = []

def bfs(i):
    queue = deque()
    queue.append(i)
    visited = [-1] * (K+1)
    visited[i] = 0
    max_distance = 0

    while queue:
        current = queue.popleft()

        for next_node in node[current]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = visited[current] + 1
                max_distance = max(max_distance, visited[next_node])

    return max_distance


while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    node[a].append(b)
    node[b].append(a)


for i in range(1, K+1):
    score_list.append(bfs(i))
    
min_score = min(score_list)
candidates = [i+1 for i, score in enumerate(score_list) if score == min_score]

print(min_score, len(candidates))
print(" ".join(map(str, candidates)))