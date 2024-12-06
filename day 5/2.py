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
    sorted = False
    valid = True
    while not sorted:
        sorted = True
        for i in range(len(update)):
            for rule in rules:
                if update[i] == rule[0] and rule[1] in update[:i]:
                    sorted = False
                    valid = False
                    update[i] = rule[1]
                    update[update.index(rule[1])] = rule[0]
    if not valid:
        total += update[len(update) // 2]


print(total)
