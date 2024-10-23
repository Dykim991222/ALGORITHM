def solution(word):
    answer = 0
    alphanum = {'A':0,'E':1,'I':2,'O':3,'U':4}
    
    my_list = [781, 156, 31, 6, 1]
    
    for i, ch in enumerate(word):
        answer += alphanum[ch] * my_list[i] + 1
    
        
    return answer