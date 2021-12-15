import math

with open("day4_input.txt", 'r') as file:
    data = file.readlines()

num_list = [int(num_str) for num_str in data[0].strip().split(',')]

board_num = 0
boards = []
completion = []

def checkComplete(start):
    # Check vertical
    for i in range(start, start+5):
        sum = 0
        for j in range(i, i+21, 5):
            sum += boards[j]
        if sum == -5:
            return True
    for i in range(start, start+21, 5):
        sum = 0
        for j in range(i, i+5):
            sum += boards[j]
        if sum == -5:
            return True
    return False
    
def markCalled(num):
    for i in range(0, len(boards)-1):
        if boards[i] == num:
            boards[i] = -1
    return

for row in data[1::]:
    if row == '\n':
        continue
    processed_row = row.strip().split()
    boards += [int(ele) for ele in processed_row]


completed = []
for num in num_list:
    # Part 1
    # done = False
    # markCalled(num)
    # for i in range(0, len(boards)-1, 25):
    #     if (checkComplete(i)):
    #         done = True
    #         print(f'Board {math.floor(i / 25)} Complete!')
    #         # Calculate score
    #         score = 0
    #         for j in range(i, i+25):
    #             if boards[j] != -1:
    #                 score += boards[j]
    #         print(boards[i:i+25])
    #         print(f'Score: {score * num}')
    #         break
    # if done:
    #     print(f'Done at {num}')
    #     break

    # Part 2
    markCalled(num)
    for i in range(0, len(boards)-1, 25):
        if i/25 not in completed:
            if (checkComplete(i)):
                completed.append(math.floor(i/25))
                if len(completed) == 100:
                    score = 0
                    for j in range(i, i+25):
                        if boards[j] != -1:
                            score += boards[j]
                    print(f'Score: {score * num}')