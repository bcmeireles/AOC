with open("day07/input.in", "r") as f:
    data = f.readlines()
                
order = "23456789TJQKA"
patterns = (1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)

parsed = []
total = 0

for line in data:
    count = {}
    hand, score = line.strip().split()

    for x in hand:
        if x not in count.keys():
            count[x] = 1
        else:
            count[x] += 1
    
    vals = []
    for x in hand:
        vals.append(order.index(x))

    pattern = tuple(sorted(count.values()))
    pattern_val = patterns.index(pattern)

    parsed.append((pattern_val, vals, score))

for i, (_, _, score) in enumerate(sorted(parsed)):
    total += i * int(score) + int(score)

print(total)