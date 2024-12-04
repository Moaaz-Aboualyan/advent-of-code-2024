input = open("./input.txt", "r")
lines = input.readlines()
word = "XMAS"
occurences = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != word[0]:
            continue
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        for direction in directions:
            x = j
            y = i
            for k in range(1, len(word)):
                x += direction[0]
                y += direction[1]
                if (y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0])):
                    break
                if lines[y][x] != word[k]:
                    break
                if word[k] == word[-1]:
                    occurences += 1

print(occurences)
