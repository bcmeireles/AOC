with open("day09/input.in", "r") as f:
    data = f.readlines()
                
res = []

for x in [list(map(int, line.split())) for line in data]:
    extra = x[-1]

    while x[-1] != 0:
        x = [h2 - h1 for h1, h2 in zip(x, x[1:])]
        extra += x[-1]

    res.append(extra)

print(sum(res))