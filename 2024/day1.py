with open('input.txt', 'r') as file:
    lines = file.readlines()

left_list = []
right_list = []
for line in lines:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

distances = [abs(left - right) for left, right in zip(left_list, right_list)]

total_distance = sum(distances)

print("The total distance is:", total_distance)