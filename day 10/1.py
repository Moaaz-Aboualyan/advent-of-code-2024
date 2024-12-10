input = open("./input.txt", "r")
lines = input.readlines()
numbers = []
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    numbers.append([])
    for j in range(len(lines[i])):
        numbers[i].append(int(lines[i][j]))

total = 0
def check(lines, x, y, visited):
    global total
    if lines[y][x] == 9:
        if [x, y] not in visited:
            visited.append([x, y])
            total += 1
        return
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for direction in directions:
        nextX = x + direction[0]
        nextY = y + direction[1]
        if nextX >= 0 and nextX < len(lines[0]) and nextY >= 0 and nextY < len(lines):
            if lines[nextY][nextX] == (lines[y][x] + 1):
                check(lines, nextX, nextY, visited)

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] == 0:
            check(numbers, j, i, [])

print(total)
