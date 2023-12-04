with open("day04/input.in", "r") as f:
    data = f.readlines()

totals = {1: 1}

for i, line in enumerate(data):
    if i + 1 not in totals.keys():
        totals[i + 1] = 1

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

    for j in range(i + 2, i + winners + 2):
        if j in totals.keys():
            totals[j] += totals[i + 1]
        else:
            totals[j] = 1 + totals[i + 1]

print(sum([totals[x] for x in totals.keys()]))