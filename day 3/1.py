import re

input = open("./input.txt", "r")
lines = input.readlines()

total = 0
for line in lines:
    realmul = re.findall("mul\(\d+,\d+\)", line)
    for operation in realmul:
        operation = operation.split(',')
        total += int(operation[0].lstrip("mul(")) * int(operation[1].rstrip(")"))

print(total)
