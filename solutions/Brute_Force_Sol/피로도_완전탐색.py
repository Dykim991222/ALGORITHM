from itertools import permutations
def solution(k, dungeons):
    answer = 0
    # 순열을 이용해 모든 가능한 경우의 수를 구함
    for perm in permutations(dungeons, len(dungeons)):
        current_k = k
        cnt = 0
        for essential, reduce in perm:
            if current_k >= essential:
                current_k -= reduce
                cnt += 1
            else:
                break    
        answer = max(cnt, answer)    
    return answer