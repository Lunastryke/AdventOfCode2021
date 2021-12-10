with open("day1_input.txt", 'r') as file:
    data = file.readlines()
processed_data = []
for ele in data:
    processed_data.append(int(ele.strip()))
count = 0
for i in range(1,len(processed_data)):
    if processed_data[i] > processed_data[i-1]:
        count += 1
print(f"Part 1 : {count}")

count2 = 0
for i in range(2, len(processed_data)-1):
    if processed_data[i-2] < processed_data[i+1]:
        count2 += 1
print(f"Part 2 : {count2}")