import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    word = input().strip()
    words.append(word)

weight = {}

for word in words:
    length = len(word)
    for i, char in enumerate(word):
        jaritsu = length - i - 1
        if char in weight:
            weight[char] += 10 ** jaritsu
        else:
            weight[char] = 10 ** jaritsu

sorted_weight = sorted(weight.items(), key = lambda x : x[1], reverse = True)

number = 9
changed_number = {}

for char, _ in sorted_weight:
    changed_number[char] = number
    number -= 1

total = 0
for word in words:
    num = 0
    for char in word:
        num = num * 10 + changed_number[char]  
    total += num

print(total)