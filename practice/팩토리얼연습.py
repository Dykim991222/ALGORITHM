'''def recursive_f(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_f(n-1)
    
print(recursive_f(3))'''

'''def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)
    
print(GCD(192, 162))'''

'''def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False] * 9
DFS(graph, 1, visited)'''

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(maps[0][1])
