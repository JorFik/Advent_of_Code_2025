import os
import sys
from dotenv import load_dotenv

load_dotenv()
input = os.getenv("input")

if input is None:
    print("No input")
    sys.exit()

parse_input = input.split()
total_joltage = 0

def tbd(battery_bank: str, num: int):
    available_chars = [char for char in battery_bank]
    final_list = []
    for i in range(num):
        biggest_value = 0
        # print(-i + len(final_list) if -i + len(final_list) != 0 else None)
        for str_value in available_chars[:-(num - 1 - len(final_list)) if -(num - 1 - len(final_list)) != 0 else None]:
            value = int(str_value)
            if value > biggest_value:
                biggest_value = value
        final_list.append(str(biggest_value))
        available_chars = available_chars[available_chars.index(str(biggest_value)) + 1:]
    return "".join(final_list)

for battery_bank in parse_input:
    # biggest_idx, bigger_idx = 0,1
    # for idx in range(len(battery_bank)):
    #     value = int(battery_bank[idx])
    #     if value > int(battery_bank[biggest_idx]) and idx < len(battery_bank) - 1:
    #         biggest_idx = idx
    #         bigger_idx = idx + 1
    #     elif value > int(battery_bank[bigger_idx]) and idx > biggest_idx:
    #         bigger_idx = idx
        # print(f"{battery_bank[biggest_idx]}{battery_bank[bigger_idx]}")
    # print(f"BB = {battery_bank}\n",f"{battery_bank[biggest_idx]}{battery_bank[bigger_idx]}")
    # total_joltage += int(f"{battery_bank[biggest_idx]}{battery_bank[bigger_idx]}")
    print(f"new version {tbd(battery_bank, 12)}")
    total_joltage += int(tbd(battery_bank, 12))

print(f"Total Joltage {total_joltage}")