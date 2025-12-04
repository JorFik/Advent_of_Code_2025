import os
import sys
from dotenv import load_dotenv

load_dotenv("dic_4.env")
input = os.getenv("input")

if input is None:
    print("No input")
    sys.exit()

parse_input = input.split()

def check_around(row_idx, parse_input, idx, jump = False):
    roll_around_count = 0
    step = 2 if jump else 1
    coincidences = []
    for i in range(idx - 1, idx + 2, step):
        if i < 0 or i > len(parse_input[row_idx]) - 1:
            continue 
        if parse_input[row_idx][i] in ['@', 'X']:
            coincidences.append((row_idx, i))
            roll_around_count += 1
    # if coincidences:
    #     print(coincidences)
    return roll_around_count

total_removed = 0
available_rolls = 1
while available_rolls != 0:
    available_rolls = 0
    for row_idx, row in enumerate(parse_input):
        for idx, char in enumerate(row):
            if parse_input[row_idx][idx] != '@':
                continue
            roll_around_count = 0
            if row_idx != 0:
                roll_around_count += check_around(row_idx -1, parse_input, idx)
            roll_around_count += check_around(row_idx, parse_input, idx, jump=True)
            if row_idx < len(parse_input) - 1:
                roll_around_count += check_around(row_idx + 1, parse_input, idx)
            # print(roll_around_count)
            if roll_around_count < 4:
                parse_input[row_idx] = parse_input[row_idx][:idx] + 'X' + parse_input[row_idx][idx + 1:]
                available_rolls += 1
    parse_input = [line.replace("X",'.') for line in parse_input]
    total_removed += available_rolls
    # print(parse_input[row_idx])

print(total_removed)
