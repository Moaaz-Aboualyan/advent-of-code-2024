input = open("./input.txt", "r")
lines = input.readlines()
reports = []
for line in lines:
    reports.append(line.strip().split(" "))

safe = 0
for report in reports:
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
                    safe += 1
                    break
            else:
                break

        i += 1

print(safe)
