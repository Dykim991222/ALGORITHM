def find(word, target_word):
    global cnt
    global flag
    cnt += 1
    if word == target_word:
        flag = cnt

    if flag:
        return
    
    if len(word) == 5:
        return
    else:
        for char in ["A", "E", "I", "O", "U"]:
            find(word+char, target_word)


def solution(target_word):
    global cnt
    global flag
    cnt = -1
    flag = False
    find("", target_word)
    answer = flag
    return answer

print(solution("AAAE"))