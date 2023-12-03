input = open("../inputs/input1.txt", "r")
calibrationValueSum = 0
digits = {
    "one": "o1e",
    "two": "t2w",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def process(calibrationValue):
    for digit in digits.keys():
        while digit in calibrationValue:
            calibrationValue = calibrationValue.replace(digit, digits[digit])
    return calibrationValue


def calibrationSum(calibrationValue):
    calibrationValue = process(calibrationValue)
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
    value = calibrationSum(line)
    if value != -1:
        calibrationValueSum += value
    else:
        print("Error: Invalid input")

print(f"The sum of all of the calibration values is {calibrationValueSum}")
