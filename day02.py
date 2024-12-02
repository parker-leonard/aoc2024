# ADVENT OF CODE 2024 - DAY 02
import collections

# Part 1
sum = 0
with open('./inputs/day02input.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.split()]
        valid = True
        # increasing
        if (report == sorted(report)):
            for i in range(0, len(report) - 1):
                if not (report[i+1] - report[i] >= 1 and report[i+1] - report[i] <= 3): valid = False
            if (valid): sum += 1
        # decreasing
        if (list(reversed(report)) == sorted(report)):
            for i in range(0, len(report) - 1):
                if not (report[i] - report[i+1] >= 1 and report[i] - report[i+1] <= 3): valid = False
            if (valid): sum += 1
    print(sum)

# Part 2
sum = 0
with open('./inputs/day02input.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.split()]
        reports = [report] + [report[:i] + report[i+1:] for i in range(len(report))]
        validity = []
        # increasing
        for i in reports:
            if (i == sorted(i)):
                valid = True
                for j in range(0, len(i) - 1):
                    if not (i[j+1] - i[j] >= 1 and i[j+1] - i[j] <= 3): valid = False
                validity.append(valid)
        # decreasing
        for i in reports:
            if (list(reversed(i)) == sorted(i)):
                valid = True
                for j in range(0, len(i) - 1):
                    if not (i[j] - i[j+1] >= 1 and i[j] - i[j+1] <= 3): valid = False
                validity.append(valid)
        if True in validity: sum += 1
    print(sum)