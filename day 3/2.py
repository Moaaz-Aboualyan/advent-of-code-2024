import re

input = open("./input.txt", "r")
lines = input.readlines()

total = 0
do = True
for line in lines:
    realmul = re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
    for operation in realmul:
        if operation == "do()":
            do = True
        elif operation == "don't()":
            do = False
        else:
            if do:
                operation = operation.split(',')
                total += int(operation[0].lstrip("mul(")) * int(operation[1].rstrip(")"))

print(total)
