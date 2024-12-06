input = open("./input.txt", "r")
lines = input.readlines()
rules = []
updates = []
for line in lines:
    if "|" in line:
        rules.append([int(num) for num in line.strip().split("|")])
    elif "," in line:
        updates.append([int(num) for num in line.strip().split(",")])

total = 0
for update in updates:
    valid = True
    for i in range(len(update)):
        for rule in rules:
            if update[i] == rule[0] and rule[1] in update[:i]:
                valid = False
                break
        if not valid:
            break
    if valid:
        total += update[len(update) // 2]

print(total)
