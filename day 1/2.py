input = open("./input.txt", "r")
lines = input.readlines()
list1 = []
list2 = []
for line in lines:
    numbers = line.split(" ")
    list1.append(int(numbers[0].strip()))
    list2.append(int(numbers[-1].strip()))

total = 0

for i in range(len(list1)):
    total += list1[i] * list2.count(list1[i])

print(total)
