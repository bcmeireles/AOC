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
for num in numbers:
	for char in characters:
		if char[0] <= num[1] and abs(num[2] - char[1]) <= 1 and char[0] >= num[0]-1:
			total += num[3]
print(total)