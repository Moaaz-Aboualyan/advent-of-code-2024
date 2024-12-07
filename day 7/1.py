import itertools

input = open("./input.txt", "r")
numbers = []
for line in input.readlines():
    if line != "":
        numbers.append(line.strip().split())

total = 0
for i in range(len(numbers)):
    numbers[i][0] = numbers[i][0][:-1]
    for j in range(len(numbers[i])):
        numbers[i][j] = int(numbers[i][j])

    for combination in itertools.product(["+", "*"], repeat=len(numbers[i]) - 2):
        answer = numbers[i][1]
        for j in range(len(combination)):
            if combination[j] == "+":
                answer += numbers[i][j + 2]
            else:
                answer *= numbers[i][j + 2]
        if answer == numbers[i][0]:
            total += answer
            break




print(total)
