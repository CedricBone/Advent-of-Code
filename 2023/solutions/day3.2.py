input = open("../inputs/input3.txt", "r")
lines = []
lineNum = 0
gear = "*"
ratios = []
sum = 0


def isValid(lines, lineNum, index):
    output = []
    if lineNum == 0 and index == 0:
        if lines[lineNum][index + 1].isdigit():
            output.append(getNum(lines[lineNum], index + 1))
        if lines[lineNum + 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum + 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        return output
    if lineNum == 0 and index == len(lines[lineNum]) - 1:
        if lines[lineNum][index - 1].isdigit():
            output.append(getNum(lines[lineNum], index - 1))
        if lines[lineNum + 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum + 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        return output
    if lineNum == 0:
        if lines[lineNum][index - 1].isdigit():
            output.append(getNum(lines[lineNum], index - 1))
        if lines[lineNum][index + 1].isdigit():
            output.append(getNum(lines[lineNum], index + 1))
        if lines[lineNum + 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum + 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum + 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        return output

    if lineNum == len(lines) - 1 and index == 0:
        if lines[lineNum - 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index))
        if lines[lineNum - 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index + 1))
        if lines[lineNum][index + 1].isdigit():
            output.append(getNum(lines[lineNum], index + 1))
        return output
    if lineNum == len(lines) - 1 and index == len(lines[lineNum]) - 1:
        if lines[lineNum - 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum - 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index))
        if lines[lineNum][index - 1].isdigit():
            output.append(getNum(lines[lineNum], index - 1))
        return output
    if lineNum == len(lines) - 1:
        if lines[lineNum - 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum - 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index))
        if lines[lineNum - 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index + 1))
        if lines[lineNum][index - 1].isdigit():
            output.append(getNum(lines[lineNum], index - 1))
        if lines[lineNum][index + 1].isdigit():
            output.append(getNum(lines[lineNum], index + 1))
        return output

    if index == 0:
        if lines[lineNum - 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index))
        if lines[lineNum - 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index + 1))
        if lines[lineNum][index + 1].isdigit():
            output.append(getNum(lines[lineNum], index + 1))
        if lines[lineNum + 1][index].isdigit():
            output.append(getNum(lines[lineNum + 1], index))
        if lines[lineNum + 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum + 1], index + 1))
        return output
    if index == len(lines[lineNum]) - 1:
        if lines[lineNum - 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum - 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index))
        if lines[lineNum][index - 1].isdigit():
            output.append(getNum(lines[lineNum], index - 1))
        if lines[lineNum + 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum + 1], index - 1))
        if lines[lineNum + 1][index].isdigit():
            output.append(getNum(lines[lineNum + 1], index))
        return output
    else:
        if lines[lineNum - 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index - 1))
        if lines[lineNum - 1][index].isdigit():
            output.append(getNum(lines[lineNum - 1], index))
        if lines[lineNum - 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum - 1], index + 1))
        if lines[lineNum][index - 1].isdigit():
            output.append(getNum(lines[lineNum], index - 1))
        if lines[lineNum][index + 1].isdigit():
            output.append(getNum(lines[lineNum], index + 1))
        if lines[lineNum + 1][index - 1].isdigit():
            output.append(getNum(lines[lineNum + 1], index - 1))
        if lines[lineNum + 1][index].isdigit():
            output.append(getNum(lines[lineNum + 1], index))
        if lines[lineNum + 1][index + 1].isdigit():
            output.append(getNum(lines[lineNum + 1], index + 1))
        return output


def getNum(line, index):
    num = line[index]
    tempIndex = index
    while line[index - 1].isdigit():
        num = line[index - 1] + num
        index -= 1
    index = tempIndex
    while line[index + 1].isdigit():
        num += line[index + 1]
        index += 1
    return num


for line in input:
    lines.append(line)
for line in lines:
    for index in range(len(line)):
        if line[index] == gear:
            numbers = list(set(isValid(lines, lineNum, index)))
            if len(numbers) == 2:
                ratios.append(numbers)
    lineNum += 1
for ratio in ratios:
    sum += int(ratio[0]) * int(ratio[1])

print(f"The sum of all of the gear ratios is {sum}")
