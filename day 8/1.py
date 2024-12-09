input = open("./input.txt", "r")
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
antinodes = []
for i in range(len(lines)):
    antinodes.append([])
    for j in range(len(lines[i])):
        antinodes[i].append(0)

for i in range(len(lines)):
    for j in range(len(lines[i])):
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if not (y == i and x == j):
                    if lines[y][x] == lines[i][j] and lines[i][j] != ".":
                        fary = i + 2 * (y - i)
                        farx = j + 2 * (x - j)
                        if fary < len(lines) and fary >= 0 and farx < len(lines[y]) and farx >= 0:
                            antinodes[fary][farx] = 1
                        closey = i - (y - i)
                        closex = j - (x - j)
                        if closey < len(lines) and closey >= 0 and closex < len(lines[y]) and closex >= 0:
                            antinodes[closey][closex] = 1

total = 0
for line in antinodes:
    for number in line:
        total += number

print(total)