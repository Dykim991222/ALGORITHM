import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.pop() # 이게뭐지, popleft() 안쓰고 이래넘겨줘?
        current_node_visit = visited[current] 
        ''' 지금 1부터 시작했고, 1이 방문 안됐으니까 bfs(1)로 들어왔겠지.
        queue에 1이 들어가고, visited가 [-1][0][-1][-1] 로 바껴서 왔다는거 확인
        '''

        for next_node in node[current]: #node[1] 에 지금 3있으니까 nextnode는 3
            if visited[next_node] == -1: # 3에 방문안했으면?
                queue.append(next_node) # queue에 3 넣어주고

K = int(input())
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
            if not result :
                print("NO")
                is_failed = True
                break
    
    if not is_failed:
        print("YES")
