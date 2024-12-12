def is_safe_report(levels):
    differences = [abs(levels[i] - levels[i+1]) for i in range(len(levels) - 1)]
    if any(diff < 1 or diff > 3 for diff in differences):
        return False

    if all(levels[i] < levels[i+1] for i in range(len(levels) - 1)):
        return True
    if all(levels[i] > levels[i+1] for i in range(len(levels) - 1)):
        return True

    return False

def count_safe_reports(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()
    
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe_report(levels):
            safe_count += 1

    return safe_count

filename = 'input2.txt'
safe_reports = count_safe_reports(filename)
print(f"Number of safe reports: {safe_reports}")