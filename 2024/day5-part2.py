from collections import defaultdict, deque

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    blank_index = lines.index('')
    rule_lines = lines[:blank_index]
    update_lines = lines[blank_index+1:]
    return rule_lines, update_lines

def topological_sort(nodes, edges):
    in_degree = {n: 0 for n in nodes}
    for a in edges:
        for b in edges[a]:
            in_degree[b] += 1

    q = deque([n for n in nodes if in_degree[n] == 0])

    order = []
    while q:
        current = q.popleft()
        order.append(current)
        if current in edges:
            for nxt in edges[current]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)

    if len(order) != len(nodes):
        raise ValueError("Cycle detected or invalid constraints.")
    return order

def main():
    rule_lines, update_lines = parse_input('input5.txt')
    
    must_before = {}
    for line in rule_lines:
        left, right = line.split('|')
        A, B = int(left), int(right)
        if A not in must_before:
            must_before[A] = set()
        must_before[A].add(B)

    incorrect_updates = []
    correct_updates = []

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
            correct_updates.append(pages)
        else:
            incorrect_updates.append(pages)

    total = 0
    for pages in incorrect_updates:
        relevant_pages = set(pages)
        edges = defaultdict(set)
        for A, after_set in must_before.items():
            if A in relevant_pages:
                for B in after_set:
                    if B in relevant_pages:
                        edges[A].add(B)

        ordered = topological_sort(relevant_pages, edges)
        mid_index = len(ordered) // 2
        total += ordered[mid_index]

    print(total)

if __name__ == "__main__":
    main()