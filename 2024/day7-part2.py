import itertools

def solve_calibration(filename):
    total_calibration_result = 0
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue 

            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str.strip())
            numbers = list(map(int, numbers_str.split()))

            found_solution = False

            for ops in itertools.product(['+', '*', '||'], repeat=len(numbers)-1):
                result = numbers[0]

                for i, op in enumerate(ops, start=1):
                    next_num = numbers[i]
                    
                    if op == '+':
                        result += next_num
                    elif op == '*':
                        result *= next_num
                    elif op == '||':
                        result = int(str(result) + str(next_num))
                
                if result == test_value:
                    found_solution = True
                    break  

            if found_solution:
                total_calibration_result += test_value

    return total_calibration_result

if __name__ == "__main__":
    filename = "input7.txt"
    answer = solve_calibration(filename)
    print("Total Calibration Result:", answer)