def solution(number, k):
    # comment
    result=[]
    index = 0
    for i in range(len(number)-k):
        if "9" in number[index:k+i+1]: max_val = "9"
        else: max_val = max(number[index:k+i+1])
        for j in range(index,len(number)-1):
            if number[j] == max_val:
                index = j+1
                break
        result.append(max_val)    
    
    answer = "".join(result)
    return answer