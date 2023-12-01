import re
with open("day01/input.in", "r") as f:
    data = f.readlines()

total = 0

valid_words = {
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9"
}
for line in data:
    matches = []
    for word in valid_words:
        for match in re.finditer(word, line):
            matches.append((match.start(), valid_words[word]))
    matches.sort()
    #print(int(matches[0][1] + matches[-1][1]))
    total += int(matches[0][1] + matches[-1][1])
    
print(total)