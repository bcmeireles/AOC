with open("day07/input.in", "r") as f:
    data = f.readlines()
                
order = "J23456789TQKA"
patterns = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]

parsed = []
total = 0
score_hands = []

for line in data: 
    hand, score = line.strip().split()

    vals = []
    evaluated = []
    for x in hand:
        vals.append(order.index(x))

    for replacement in order:
        replaced = hand.replace('J', replacement)
        count = {}
        for x in replaced:
            if x not in count.keys():
                count[x] = 1
            else:
                count[x] += 1
                
        pattern = tuple(sorted(count.values()))
        pattern_val = patterns.index(pattern)

        evaluated.append(pattern_val)

    score_hands.append((max(evaluated), vals, score))

for i, (_, _, score) in enumerate(sorted(score_hands)):
    total += i * int(score) + int(score)

print(total)