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

while x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines):
    if lines[y][x] == "#":
        x -= directions[direction][0]
        y -= directions[direction][1]
        direction += 1
        if direction > len(directions) - 1:
            direction = 0

    lines[y] = lines[y][:x] + "X" + lines[y][x + 1:]
    x += directions[direction][0]
    y += directions[direction][1]
    
total = 0
for line in lines:
    total += line.count("X")

print(total)
