input = open("../inputs/input1.txt", "r")
calibrationValueSum = 0


def calibrationSum(calibrationValue):
    if calibrationValue[0].isdigit() and calibrationValue[-1].isdigit():
        calibrationValueSum = int(calibrationValue[0] + calibrationValue[-1])
        return calibrationValueSum
    elif calibrationValue[0].isdigit() and (not calibrationValue[-1].isdigit()):
        calibrationValue = calibrationValue[:-1]
        return calibrationSum(calibrationValue)
    elif (not calibrationValue[0].isdigit()) and calibrationValue[-1].isdigit():
        calibrationValue = calibrationValue[1:]
        return calibrationSum(calibrationValue)
    else:
        calibrationValue = calibrationValue[1:-1]
        return calibrationSum(calibrationValue)
    return -1


for line in input:
    if calibrationSum(line) != -1:
        calibrationValueSum += calibrationSum(line)
    else:
        print("Error: Invalid input")
        break

print(f"The sum of all of the calibration values is {calibrationValueSum}")
