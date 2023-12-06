with open("day06/input.in", "r") as f:
    data = f.readlines()
                
res = 1

lasts = list(map(int, data[0].split()[1:]))
records = list(map(int, data[1].split()[1:]))

for i, x in enumerate(lasts):
    racing = records[i] - x
    raced = 0
    sum = 0

    for held in range(1, records[i]):
        raced = x - held
        distance = raced * held


        if raced == distance == 0:
            break

        if distance > records[i]:
            sum += 1
    
    res *= sum

print(res)