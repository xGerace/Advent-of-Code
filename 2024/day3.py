import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

with open("input3.txt", "r") as file:
    data = file.read()

matches = re.findall(pattern, data)

result_sum = sum(int(x) * int(y) for x, y in matches)

print(f"The sum of all valid mul instruction results is: {result_sum}")