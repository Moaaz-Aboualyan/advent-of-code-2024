input = open("./input.txt", "r")
line = input.readline().strip()
numbers = []
answers = []
for char in line:
    numbers.append(int(char))
for i in range(len(numbers)):
    if i % 2 != 0:
        for j in range(numbers[i]):
            answers.append(-1)
    else:
        for j in range(numbers[i]):
            answers.append(i // 2)

for i in range(len(answers)):
    if answers[i] == -1:
        for j in range(len(answers) - 1, i, -1):
            if answers[j] != -1:
                temp = answers[j]
                answers[j] = answers[i]
                answers[i] = temp
                break
checksum = 0
for i in range(len(answers)):
    if answers[i] != -1:
        checksum += answers[i] * i
print(checksum)
