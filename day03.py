# ADVENT OF CODE 2024 - DAY 03
import re

# Part 1
total = 0
with open('./inputs/day03input.txt', 'r') as file:
    for line in file:
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = [list(map(int, match)) for match in re.findall(pattern, line)]
        total += (sum([x * y for x, y in matches]))
    print(total)

# Part 2
total = 0
with open('./inputs/day03input.txt', 'r') as file:
    do = True
    for line in file:
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            elif do:
                pair = list(map(int, match[4:-1].split(',')))
                total += pair[0] * pair[1]
    print(total)