import sys
input = sys.stdin.readline

sentence = list(input().rstrip())
print(sentence)


S = list(map(str, input().split()))

answer = []
reverse1 = ''
for i in range(len(S)):
    word = S[i]
    for k in range(len(word)-1,-1,-1):
        reverse1 += word[k]
    answer.append(reverse1)
    reverse1 = ''

print(answer)