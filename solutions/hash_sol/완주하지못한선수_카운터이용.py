from collections import Counter

def solution(participant, completion):
    answer = ''
    dict_result=Counter(participant)-Counter(completion)
    return list(dict_result.keys())[0] 



