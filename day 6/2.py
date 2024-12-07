input = open("./input.txt", "r")
lines = input.readlines()
direction = 0
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
chars = ["^", ">",  "v", "<"]
x = 0
y = 0
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    for j in range(len(chars)):
        if lines[i].find(chars[j][0]) != -1:
            x = lines[i].find(chars[j][0])
            y = i
            direction = j
            break

def isLoop(lines, x, y, direction):
    while x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines):
        if lines[y][x] == "#":
            x -= directions[direction][0]
            y -= directions[direction][1]
            direction += 1
            if direction > len(directions) - 1:
                direction = 0
            x += directions[direction][0]
            y += directions[direction][1]

        lines[y] = lines[y][:x] + chars[direction] + lines[y][x + 1:]
        x += directions[direction][0]
        y += directions[direction][1]
        try:
            if lines[y][x] == chars[direction]:
                return 1
        except:
            break

    return 0
    
total = 0
iterations = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        tempLines = lines.copy()
        iterations += 1
#        print(iterations, total)
        tempLines[i] = tempLines[i][:j] + "#" + tempLines[i][j + 1:]
        #total += isLoop(tempLines, x, y, direction)
        if isLoop(tempLines, x, y, direction):
            print(tempLines)


print(total)
