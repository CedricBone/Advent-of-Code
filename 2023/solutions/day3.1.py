input = open("../inputs/input3.txt", "r")
sum = 0
lines = []
lineNum = 0
symbols = ["$", "-", "=", "%", "@", "#", "+", "&", "/", "*"]


def isValid(lines, lineNum, index):
    if lineNum == 0 and index == 0:
        check1 = lines[lineNum][index + 1] in symbols
        check2 = lines[lineNum + 1][index] in symbols
        check3 = lines[lineNum + 1][index + 1] in symbols
        return check1 or check2 or check3
    if lineNum == 0 and index == len(lines[lineNum]) - 1:
        check1 = lines[lineNum][index - 1] in symbols
        check2 = lines[lineNum + 1][index - 1] in symbols
        check3 = lines[lineNum + 1][index] in symbols
        return check1 or check2 or check3
    if lineNum == 0:
        check1 = lines[lineNum][index - 1] in symbols
        check2 = lines[lineNum][index + 1] in symbols
        check3 = lines[lineNum + 1][index - 1] in symbols
        check4 = lines[lineNum + 1][index] in symbols
        check5 = lines[lineNum + 1][index + 1] in symbols
        return check1 or check2 or check3 or check4 or check5

    if lineNum == len(lines) - 1 and index == 0:
        check1 = lines[lineNum - 1][index] in symbols
        check2 = lines[lineNum - 1][index + 1] in symbols
        check3 = lines[lineNum][index + 1] in symbols
        return check1 or check2 or check3
    if lineNum == len(lines) - 1 and index == len(lines[lineNum]) - 1:
        check1 = lines[lineNum - 1][index - 1] in symbols
        check2 = lines[lineNum - 1][index] in symbols
        check3 = lines[lineNum][index - 1] in symbols
        return check1 or check2 or check3
    if lineNum == len(lines) - 1:
        check1 = lines[lineNum - 1][index - 1] in symbols
        check2 = lines[lineNum - 1][index] in symbols
        check3 = lines[lineNum - 1][index + 1] in symbols
        check4 = lines[lineNum][index - 1] in symbols
        check5 = lines[lineNum][index + 1] in symbols
        return check1 or check2 or check3 or check4 or check5

    if index == 0:
        check1 = lines[lineNum - 1][index] in symbols
        check2 = lines[lineNum - 1][index + 1] in symbols
        check3 = lines[lineNum][index + 1] in symbols
        check4 = lines[lineNum + 1][index] in symbols
        check5 = lines[lineNum + 1][index + 1] in symbols
        return check1 or check2 or check3 or check4 or check5
    if index == len(lines[lineNum]) - 1:
        check1 = lines[lineNum - 1][index - 1] in symbols
        check2 = lines[lineNum - 1][index] in symbols
        check3 = lines[lineNum][index - 1] in symbols
        check4 = lines[lineNum + 1][index - 1] in symbols
        check5 = lines[lineNum + 1][index] in symbols
        return check1 or check2 or check3 or check4 or check5
    else:
        check1 = lines[lineNum - 1][index - 1] in symbols
        check2 = lines[lineNum - 1][index] in symbols
        check3 = lines[lineNum - 1][index + 1] in symbols
        check4 = lines[lineNum][index - 1] in symbols
        check5 = lines[lineNum][index + 1] in symbols
        check6 = lines[lineNum + 1][index - 1] in symbols
        check7 = lines[lineNum + 1][index] in symbols
        check8 = lines[lineNum + 1][index + 1] in symbols
        return (
            check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8
        )


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
    validIndexs = []
    nums = []
    for index in range(len(line)):
        if line[index].isdigit() and isValid(lines, lineNum, index):
            validIndexs.append(index)
    index = 0
    while index < len(validIndexs) - 1:
        if validIndexs[index] + 1 == validIndexs[index + 1]:
            validIndexs.pop(index)
        else:
            index += 1
    for index in range(len(validIndexs)):
        nums.append(getNum(line, validIndexs[index]))
    for num in nums:
        sum += int(num)
    lineNum += 1

print(f"The sum of all of the valid numbers is {sum}")
