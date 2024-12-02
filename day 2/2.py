input = open("./input.txt", "r")
lines = input.readlines()
reports = []
for line in lines:
    reports.append(line.strip().split(" "))

def issafe(report):
    for i in range(len(report)):
        report[i] = int(report[i])
    increasing = False
    for i in range(len(report)):
        if i == 0:
            if (report[i] - report[i + 1]) < 0:
                increasing = True
        else:
            difference = report[i] - report[i - 1]
            if ((difference > 0 and increasing) or (difference < 0 and not increasing)) and (difference >= -3 and difference <= 3 and difference != 0):
                if (i == len(report) - 1):
                    return 1
            else:
                return 0

        i += 1

safe = 0
for report in reports:
    if (issafe(report)):
        safe += 1
    else:
        for i in range(len(report)):
            if issafe(report[:i] + report[i + 1:]):
                safe += 1
                break

print(safe)
