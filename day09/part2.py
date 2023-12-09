with open("day09/input.in", "r") as f:
    data = f.readlines()
                
res = []

for x in [list(map(int, line.split())) for line in data]:
    count = 0
    extra = x[0]
    
    while any([i != 0 for i in x]):
        count += 1
        x = [h2 - h1 for h1, h2 in zip(x, x[1:])]

        if count % 2 == 0:
            extra += x[0]
        else:
            extra -= x[0]

    res.append(extra)
    
print(sum(res))