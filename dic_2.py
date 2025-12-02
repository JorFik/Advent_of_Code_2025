import os
import sys
from dotenv import load_dotenv

load_dotenv()
input = os.getenv("input")

if input is None:
    print("No input")
    sys.exit()

sum_invalid_ids = 0

parse_input = input.split(',')
str_ranges = [str_range.split('-') for str_range in parse_input]
range_list = [range(int(str_range[0]), int(str_range[1]) + 1) for str_range in str_ranges]

def is_pattern(id:str, div: int)-> bool:
    len_id = len(id)
    if len_id % div != 0:
        return False
    first_part = id[: len_id // div]
    if first_part * div == id:
        return True
    return False

for id_range in range_list:
    for id in id_range:
        str_id = str(id)
        len_id = len(str_id)
        if is_pattern(str_id, 2):
            sum_invalid_ids += id
        elif is_pattern(str_id, 3):
            sum_invalid_ids += id
        elif is_pattern(str_id, 5):
            sum_invalid_ids += id
        elif is_pattern(str_id, 7):
            sum_invalid_ids += id


print(sum_invalid_ids)
