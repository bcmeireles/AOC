with open("day08/input.in", "r") as f:
    data = f.readlines()
                
paths = {}

for line in data[2:]:
    line = line.strip().split(" ")
    paths[line[0]] = {
        "L": line[2][1:-1],
        "R": line[3][:-1]
    }

current = "AAA"
i = 0
path = data[0].strip()

while True:
    if current == "ZZZ":
        break
    current = paths[current][path[i % len(path)]]
    i += 1

print(i)
