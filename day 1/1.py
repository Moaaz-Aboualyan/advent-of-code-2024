input = open("./input.txt", "r")
lines = input.readlines()
list1 = []
list2 = []
for line in lines:
    numbers = line.split(" ")
    list1.append(int(numbers[0].strip()))
    list2.append(int(numbers[-1].strip()))

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    difference = list1[i] - list2[i]
    if difference < 0:
        difference = -difference

    total += difference

print(total)
