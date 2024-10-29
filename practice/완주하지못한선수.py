def solution(participant, completion):
    answer = ''
    answer_dict = {}
    for person in participant:
        if person not in answer_dict:
            answer_dict[person] = 1
        else:
            answer_dict[person] += 1
            
    for person in completion:
        if person in answer_dict:
            answer_dict[person] -= 1
    
    for person in participant:
        if answer_dict[person] == 1:
            return person
    
    return answer_dict