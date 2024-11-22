answer = 0
input_number = input()
onlyplus_list = list(input_number.split('-'))


calculate_list = []
for number in onlyplus_list:
    if '+' in number:
        calculate_list.append(sum(map(int, number.split('+'))))
    else:
        calculate_list.append(int(number))


answer += calculate_list[0]
for i in range(1, len(calculate_list)):
    answer -= calculate_list[i]

print(answer)