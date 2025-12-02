import os
import sys
from dotenv import load_dotenv

load_dotenv()
input = os.getenv("input")

if input is None:
    print("No input")
    sys.exit()

zero_count = 0
dial_value = 50


def rotate_dial(instruction: str):
    global dial_value
    global zero_count
    instruction = instruction.upper()
    print(f"Instruction {instruction}")
    print(f"Initial position = {dial_value}")
    og_0_count = zero_count
    direction = 1
    if instruction[0] == 'L':
        direction = -1
    rotation_value = int(instruction[1:])
    if rotation_value > 99:
        zero_count += rotation_value // 100
        rotation_value %= 100
    if rotation_value > dial_value and direction == -1 and dial_value != 0:
        zero_count += 1
    initial_dial_value = dial_value + (rotation_value * direction)
    dial_value = initial_dial_value % 100
    if initial_dial_value > 100:
        zero_count += initial_dial_value // 100
    if dial_value == 0:
        zero_count += 1
    print(f"End position = {dial_value}")
    if og_0_count != zero_count:
        print(f"0 count from {og_0_count} to {zero_count}")
    print(f"==============================")


parse_input = input.split()
for instruction in parse_input:
    rotate_dial(instruction)

print(f"zero count = {zero_count}")