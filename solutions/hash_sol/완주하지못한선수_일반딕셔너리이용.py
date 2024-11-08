def solution(participant, completion):
    temp = {} # key,value를 가진 딕셔너리 이용
    #딕셔너리에 참가자 이름(key)과 해당 이름 사람수(value) 넣기 
    for i in participant :
        if i in temp : 
            temp[i]+=1
        else: 
            temp[i] =1
  
    #완주자 이름(key)의 value가 1이면 지우기, 동명이인이면 -1  
    for i in completion :
        if temp[i]==1 : 
            del temp[i]
        else : 
            temp[i] -=1

    #딕셔너리를 리스트로 바꾸고 가장 첫번째꺼 리턴(어차피 하나뿐)
    return list(temp.keys())[0]