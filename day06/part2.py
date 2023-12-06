with open("day06/input.in", "r") as f:
    data = f.readlines()
                
sum = 0

lasts = int("".join(data[0].split()[1:]))
record = int("".join(data[1].split()[1:]))

racing = record - lasts
raced = 0

for held in range(1, record):
    raced = lasts - held
    distance = raced * held
    if raced == distance == 0:
        break
    if distance > record:
        sum += 1

print(sum)