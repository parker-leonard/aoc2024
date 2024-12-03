# ADVENT OF CODE 2024 - DAY 02

# Part 1
sum = 0
with open('./inputs/day01input.txt', 'r') as file:
    left_list, right_list = [], []
    for line in file:
        left_list.append(line.split()[0])
        right_list.append(line.split()[1])
    left_list.sort()
    right_list.sort()
    for i in range(0, len(left_list)):
        sum += abs(int(left_list[i]) - int(right_list[i]))
print(sum)

# Part 2
sum = 0
with open('./inputs/day01input.txt', 'r') as file:
    left_list, right_list = [], []
    for line in file:
        left_list.append(line.split()[0])
        right_list.append(line.split()[1])
    left_list.sort()
    right_list.sort()
    for i in range(0, len(left_list)):
        sum += int(left_list[i]) * right_list.count(left_list[i])
print(sum)