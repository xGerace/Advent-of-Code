from collections import Counter

with open('input.txt', 'r') as file:
    lines = file.readlines()

left_list = []
right_list = []
for line in lines:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)

right_count = Counter(right_list)

similarity_score = 0
for num in left_list:
    similarity_score += num * right_count.get(num, 0)

print("The similarity score is:", similarity_score)