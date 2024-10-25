import itertools
import math

def is_sosu(num):  
    if num < 2:
        return False
    for i in range(2, math.sqrt(num)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    list_numbers = list(numbers)
    new_set = set()
    
    for i in range(1, len(list_numbers) + 1):
        perms = itertools.permutations(list_numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            new_set.add(num)
    
    answer_list = list(new_set)
    
    for num in answer_list:
        if is_sosu(num):
            answer += 1
    
    return answer