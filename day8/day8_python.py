with open("day8_input.txt", 'r') as file:
    data = file.readlines()

processedData = [line.strip() for line in data]
# 1 = len 2
# 4 = len 4
# 7 = len 3
# 8 = len 7

# Part 1
# count = 0
# for line in processedData:
#     output = line.split('|')[1]
#     digit_list = output.split()
#     for digit in digit_list:
#         if len(digit) in [2,3,4,7]:
#             count += 1
# print(count)

# Part 2
total_sum = 0
for line in processedData:
    sig_input, sig_output = line.split('|')
    input_list = [''.join(sorted(ele)) for ele in sig_input.split()]
    output_list = [''.join(sorted(ele)) for ele in sig_output.split()]
    mapping = {}
    reverse_mapping = {}
    # Identify each number:
    for digit in input_list:
        digit_length = len(digit)
        if digit_length == 2:
            mapping[digit] = 1
            reverse_mapping[1] = digit
        elif digit_length == 3:
            mapping[digit] = 7
            reverse_mapping[7] = digit
        elif digit_length == 4:
            mapping[digit] = 4
            reverse_mapping[4] = digit
        elif digit_length == 7:
            mapping[digit] = 8
            reverse_mapping[8] = digit

    for digit in input_list:
        digit_length = len(digit)
        digit_set = set(digit)
        if digit_length == 6:
            if set(reverse_mapping[1]) <= digit_set:
                if set(reverse_mapping[4]) <= digit_set:
                    mapping[digit] = 9
                else:
                    mapping[digit] = 0
            else:
                mapping[digit] = 6
        elif digit_length == 5:
            if set(reverse_mapping[1]) <= digit_set:
                mapping[digit] = 3
            else:
                count = 0
                for i in digit:
                    if i in reverse_mapping[4]:
                        count += 1
                if count == 3:
                    mapping[digit] = 5
                else:
                    mapping[digit] = 2
    ans = ''
    for digit in output_list:
        ans += str(mapping[digit])
    total_sum += int(ans)
print(total_sum)