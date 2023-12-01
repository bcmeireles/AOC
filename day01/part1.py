with open("day01/input.in", "r") as f:
    data = f.readlines()
    
total = 0

for line in data:
    first_digit = next(i for i in line if i.isdigit())
    last_digit = next(i for i in line[::-1] if i.isdigit())
    total += int(first_digit + last_digit)

print(total)