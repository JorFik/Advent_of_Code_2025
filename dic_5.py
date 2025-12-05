import os
import sys
from dotenv import load_dotenv

load_dotenv("dic_5.env")
input = os.getenv("input")

if input is None:
    print("No input")
    sys.exit()

parse_input = input.split()
raw_ranges = [line for line in parse_input if '-' in line]
available_ingredients = [int(line) for line in parse_input if '-' not in line]

def parse_range(raw_str: str):
    split_str = raw_str.split('-')
    end_range = range(int(split_str[0]), int(split_str[1]) + 1)
    return end_range # , end_range_tuple

fresh_ingredients_ranges = []
for raw_range in raw_ranges:
    fresh_ingredients_ranges.append(parse_range(raw_range))

def optimize_ranges(ranges: list[range]):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    optimized_ranges: list[tuple[int, int]] = []
    for range in sorted_ranges:
        start = range[0]
        end = range[-1]
        if not optimized_ranges or\
            start > optimized_ranges[-1][1]:
            optimized_ranges.append((start, end))
        else:
            prev_start, prev_end = optimized_ranges[-1]
            new_end = max(prev_end, end)
            optimized_ranges[-1] = (prev_start, new_end)
    return optimized_ranges

optimized_ranges = optimize_ranges(fresh_ingredients_ranges)
fresh_ingredients = []
for ingredient in available_ingredients:
    if any(ingredient in id_range for id_range in fresh_ingredients_ranges):
        fresh_ingredients.append(ingredient)

fresh_ids = 0
for start, end in optimized_ranges:
    fresh_ids += (end - start) + 1

print("Fresh ingredients =", len(fresh_ingredients))
print("Fresh ids =", fresh_ids)

