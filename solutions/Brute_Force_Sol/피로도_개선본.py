import itertools

def solution(k, dungeons):
    answer = -1
    
    length = len(dungeons)
    start_num = 0
    dungeons_index = []
    for i in range(length):
        dungeons_index.append(start_num)
        start_num += 1
        
    permutations_index = list(itertools.permutations(dungeons_index, length))
    cnt = 0
    max_cnt = 0
    
    for x in permutations_index:
        dungeon_list = [dungeons[i] for i in x]
        current_k = k
        cnt = 0
        for dungeon in dungeon_list:
            if current_k >= int(dungeon[0]):
                current_k -= int(dungeon[1])
                cnt += 1
            else:
                break
        if cnt > max_cnt:
            max_cnt = cnt
    
    if max_cnt == 0:
        return -1
    else:
        return max_cnt