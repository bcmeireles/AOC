with open("day04/input.in", "r") as f:
    data = f.readlines()
total = 0

for i, line in enumerate(data):
    line = line.strip()
    winning, nums = line.split('|')
    winning = winning.split(':')[1].split(' ')
    nums = nums.split(' ')

    winners = 0

    for x in winning:
        if x == '':
            continue
        if x in nums:
            winners += 1
        if winners == 0:
            continue
    
    if winners == 1:
        total += 1
    elif winners > 1:
        total += 2 ** (winners - 1)

print(total)