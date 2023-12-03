with open("day03/input.in", "r") as f:
    data = f.readlines()
import re
numbers = []
characters = []

for i, line in enumerate(data):
	line = line.strip()
	for element in re.finditer(r'[^\d\.]', line):
		characters.append([element.start(0), i, element.group(0)])
	for num in re.finditer(r'\d+', line):
		numbers.append([num.start(0), num.end(0), i, int(num.group(0))])

total = 0

gears = [x for x in characters if x[2] == '*']

for gear in gears:
	adjacent = [num for num in numbers if (gear[0] <= num[1] and abs(num[2] - gear[1]) <= 1 and gear[0] >= num[0]-1)]
	if len(adjacent) == 2:
		total += adjacent[0][3] * adjacent[1][3]

print(total)