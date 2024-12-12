import re

def convert_written_to_digit(word):
    words_to_digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return words_to_digits.get(word, '')

def find_first_and_last_digit(line):
    pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
    matches = re.findall(pattern, line, re.IGNORECASE)

    digits = []
    for match in matches:
        digit = match if match.isdigit() else convert_written_to_digit(match.lower())
        if digit:  
            digits.append(digit)

    if len(digits) == 0:
        return None 
    elif len(digits) == 1:
        return int(digits[0] + digits[0]) 
    else:
        return int(digits[0] + digits[-1])

def calculate_sum_of_values(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            value = find_first_and_last_digit(line)
            if value is not None:
                total_sum += value
    return total_sum

file_path = '1.txt'
total_value = calculate_sum_of_values(file_path)
print(f'Total sum of all calibration values: {total_value}')
