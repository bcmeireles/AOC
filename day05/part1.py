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

for map in maps:
    mapped = []
    for seed in seeds:
        for destination, source, range in map:
            if source <= seed <= source + range:
                mapped.append(destination + seed - source)
                break
        else:
            mapped.append(seed)
    seeds = mapped

print(min(seeds))