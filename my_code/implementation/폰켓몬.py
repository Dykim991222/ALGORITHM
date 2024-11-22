def solution(nums):
    answer = 0
    set_list = list(set(nums))
    pick = len(nums)/2
    if pick < len(set_list) or pick == len(set_list):
        answer = pick
    else:
        answer = len(set_list)
    return answer