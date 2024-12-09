input = open("./input.txt", "r")
lines = input.readlines()
x, y, direction = 0, 0 , 0
chars = ["^", ">", "v", "<"]
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    for j in range(len(lines[i])):
        if lines[i][j] in chars:
            x = j
            y = i
            direction = chars.index(lines[i][j])

def path(lines, x, y, direction):
    visited = set()
    while x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines):
        if (x, y, direction) in visited:
            return 1
        if (lines[y][x] == "#"):
            x -= directions[direction][0]
            y -= directions[direction][1]
            direction += 1
            if direction > 3:
                direction = 0
        visited.add((x, y, direction))
        lines[y] = lines[y][:x] + chars[direction] + lines[y][x+1:]
        x += directions[direction][0]
        y += directions[direction][1]
    return 0

total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == ".":
            tempLines = lines.copy()
            tempLines[i] = tempLines[i][:j] + "#" + tempLines[i][j+1:]
            total += path(tempLines, x, y, direction)
print(total)
