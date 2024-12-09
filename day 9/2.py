input = open("./input.txt", "r")
line = input.readline().strip()
numbers = []
answers = []
for char in line:
    numbers.append(int(char))
for i in range(len(numbers)):
    if i % 2 != 0:
        answers.append([-1, numbers[i]])
    else:
        answers.append([i // 2, numbers[i]])

for i in range(len(answers) - 1, 0, -1):
    if answers[i][0] != -1:
        for j in range(i):
            if answers[j][0] == -1:
                if answers[j][1] >= answers[i][1]:
                    difference = answers[j][1] - answers[i][1]
                    temp = answers[j]
                    answers[j] = answers[i]
                    answers[i] = temp
                    if difference > 0:
                        answers[i][1] -= difference
                        answers = answers[:j+1] + [[-1, difference]] + answers[j+1:]
                    break
checksum = 0
index = 0
for i in range(len(answers)):
    if answers[i][0] != -1:
        for j in range(i, i + answers[i][1]):
            checksum += answers[i][0] * index
            index += 1
    else:
        index += answers[i][1]
print(checksum)
