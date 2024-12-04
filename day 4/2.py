input = open("./input.txt", "r")
lines = input.readlines()
word = "MAS"
occurences = 0

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        if lines[i][j] != 'A':
            continue
        directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        if (lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S') or (lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M'):
            if (lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S') or (lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M'):
                occurences += 1

print(occurences)
