import sys
from itertools import permutations

input = sys.stdin.readline
num = list(range(1, 10))
number_list = list(permutations(num, 3))


N = int(input())
for _ in range(N):
    input_number, answer_strike, answer_ball = map(int, input().split())
    hoobo = []

    for number in number_list:
        guess_strike, guess_ball = 0, 0
        for i, k in enumerate(str(input_number)):
            if int(k) == number[i]:
                guess_strike += 1
            if int(k) != number[i] and int(k) in number:
                guess_ball += 1
        
        if guess_strike == answer_strike and guess_ball == answer_ball:
            hoobo.append(number)
    
    number_list = hoobo
print(len(hoobo))



