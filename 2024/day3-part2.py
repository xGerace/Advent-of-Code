import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

with open("input3.txt", "r") as file:
    data = file.read()

mul_enabled = True

result_sum = 0

instructions = re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", data)

for match in instructions:
    if match.group(0).startswith("mul"):
        if mul_enabled:
            x, y = map(int, match.groups())
            result_sum += x * y
    elif match.group(0) == "do()":
        mul_enabled = True
    elif match.group(0) == "don't()":
        mul_enabled = False

print(f"The sum of all enabled mul instruction results is: {result_sum}")