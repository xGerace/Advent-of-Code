def is_safe_report(levels):
    differences = [abs(levels[i] - levels[i+1]) for i in range(len(levels) - 1)]
    if any(diff < 1 or diff > 3 for diff in differences):
        return False

    if all(levels[i] < levels[i+1] for i in range(len(levels) - 1)):
        return True
    if all(levels[i] > levels[i+1] for i in range(len(levels) - 1)):
        return True

    return False

def can_be_safe_with_dampener(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:] 
        if is_safe_report(modified_levels):
            return True
    return False

def count_safe_reports_with_dampener(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()

    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe_report(levels) or can_be_safe_with_dampener(levels):
            safe_count += 1

    return safe_count

filename = 'input2.txt'
safe_reports = count_safe_reports_with_dampener(filename)
print(f"Number of safe reports (with Problem Dampener): {safe_reports}")