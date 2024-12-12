def parse_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    blank_index = lines.index('')
    rule_lines = lines[:blank_index]
    update_lines = lines[blank_index+1:]

    return rule_lines, update_lines

def main():
    rule_lines, update_lines = parse_input('input5.txt')
    
    must_before = {}
    for line in rule_lines:
        left, right = line.split('|')
        A, B = int(left), int(right)
        if A not in must_before:
            must_before[A] = set()
        must_before[A].add(B)

    total = 0
    for update_line in update_lines:
        pages = list(map(int, update_line.split(',')))
        pos = {p: i for i, p in enumerate(pages)}

        correctly_ordered = True
        for A, after_set in must_before.items():
            if A in pos:
                for B in after_set:
                    if B in pos:
                        if pos[A] >= pos[B]:
                            correctly_ordered = False
                            break
                if not correctly_ordered:
                    break
        
        if correctly_ordered:
            mid_index = len(pages) // 2
            total += pages[mid_index]

    print(total)

if __name__ == "__main__":
    main()
