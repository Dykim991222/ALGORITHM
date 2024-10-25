def solution(k, dungeons):
    global visited, answer
    answer = 0
    visited = [False for _ in range(len(dungeons))] 
    dfs(k, 0, dungeons)
    return answer

def dfs(k, cnt, dungeons):
    global visited, answer
    # 최대 값으로 변경
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        # 방문 하지 않고, 필요피로도보다 k가 큰거나 같은 경우
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = False