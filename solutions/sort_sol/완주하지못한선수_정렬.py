def solution(participant, completion):
	# 리스트를 이름 순으로 정렬
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
         # 순서가 맞지않으면 완주하지 못한 선수
        if participant[i] != completion[i]:
            return participant[i]
    # 위에서 순서가 다 맞았다면 마지막 선수가 완주하지 못한 선수        
    return participant[-1]
