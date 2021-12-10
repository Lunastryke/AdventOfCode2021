with open("day4_input.txt", 'r') as file:
    data = file.readlines()

num = data[0]

for row in data[1::]:
    row.strip()
