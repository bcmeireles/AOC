with open("day05/input.in", "r") as f:
    data = f.readlines()
    
seeds = list(map(int, data[0].strip("seeds: ").split()))

maps = []
new_map = []

for line in data[3:]:
    if "map:\n" in line:
        maps.append(new_map)
        new_map = []
        continue
    if line != "\n":
        new_map.append([int(x) for x in line.strip().split()])

maps.append(new_map)


merged = []
for i in range(0, len(seeds), 2):
    merged.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

all = []
for map in maps:
    new = [(s, s + r - 1, d, d + r - 1) for d, s, r in map]
    all.append(new)

for map in all:
    new = []
    control = merged
    while control:
        first, second = control.pop()
        for source, treshold, destination, last in map:
            if second < source or first > treshold:
                continue
            if first < source:
                control.append((first, source - 1))
            if second > treshold:
                control.append((treshold + 1, second))
            new.append((max(destination, destination + first - source), min(destination + second - source, last)))
            break
        else:
            new.append((first, second))
    merged = new

print(min(merged)[0])