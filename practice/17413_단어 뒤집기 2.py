import sys
input = sys.stdin.readline

sentence = list(input().rstrip())
answer = []
reverse1 = ''
inside_tag = False

for char in sentence:
    if char == '<':
        if reverse1:
            answer.append(reverse1[::-1])
            reverse1 = ''
        inside_tag = True
        answer.append(char)
    elif char == '>':
        inside_tag = False
        answer.append(char)
    elif inside_tag:
        answer.append(char)
    elif char == ' ':
        answer.append(reverse1[::-1])
        answer.append(char)
        reverse1 = ''
    else:
        reverse1 += char

if reverse1:
    answer.append(reverse1[::-1])

print(''.join(answer))
