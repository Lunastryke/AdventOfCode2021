with open("day3_input.txt", 'r') as file:
    data = file.readlines()
count = [0 for digit in data[0]]
gamma = ''
epsilon = ''
for ele in data:
    val = [int(digit) for digit in ele.strip()]
    count = [x + y for x,y in zip(count, val)]

for ele in count:
    if ele >= len(data)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
power = int(gamma,2) * int(epsilon,2)
print(f"Part 1: Gamma: {gamma} Epsilon: {epsilon} Power: {power}")

# Gets most common number out of first index of arr
def getCommon(arr, idx, more):
    count_1 = 0
    if len(arr) == 1:
        return arr
    for ele in arr:
        if ele[idx] == '1':
            count_1 += 1
    if more == True:
        if count_1 >= (len(arr) - count_1):
            return [x for x in arr if x[idx] == '1']
        else:
            return [x for x in arr if x[idx] == '0']
    else:
        if count_1 < (len(arr) - count_1):
            return [x for x in arr if x[idx] == '1']
        else:
            return [x for x in arr if x[idx] == '0']
    

curr_idx = 0
data = [ele.strip() for ele in data]
possible_ox = data
possible_co2 = data

while (curr_idx != len(count)):
    possible_ox = getCommon(possible_ox, curr_idx, True)
    possible_co2 = getCommon(possible_co2, curr_idx, False)
    curr_idx += 1

possible_ox = bytes(possible_ox[0], 'utf-8')
possible_co2 = bytes(possible_co2[0], 'utf-8')

print(int(possible_ox,2))
print(f"Life Support Rating: {int(possible_ox,2) * int(possible_co2,2)}")