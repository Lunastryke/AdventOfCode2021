with open("day2_input.txt", 'r') as file:
    data = file.readlines()
processed_data = []
horizontal = 0
depth = 0
for ele in data:
    processed_ele = ele.strip().split(' ')
    if processed_ele[0] == 'forward':
        horizontal += int(processed_ele[1])
    elif processed_ele[0] == 'up':
        depth -= int(processed_ele[1])
    elif processed_ele[0] == 'down':
        depth += int(processed_ele[1])
print(f"Part 1: H: {horizontal} D: {depth} H*D : {horizontal * depth}")

horizontal = 0
depth = 0
aim = 0
for ele in data:
    processed_ele = ele.strip().split(' ')
    if processed_ele[0] == 'forward':
        horizontal += int(processed_ele[1])
        depth += aim * int(processed_ele[1])
    elif processed_ele[0] == 'up':
        aim -= int(processed_ele[1])
    elif processed_ele[0] == 'down':
        aim += int(processed_ele[1])
    
print(f"Part 1: H: {horizontal} D: {depth} H*D : {horizontal * depth}")
