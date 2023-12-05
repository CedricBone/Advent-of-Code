input = open("../inputs/input4.txt", "r")
totalPoints = 0

for line in input:
    points = 0
    card = line.split("|")
    nums = card[0].split()
    nums = nums[2:]
    nums = [int(num) for num in nums if num != " "]
    winningNums = card[1][:-1].split(" ")
    winningNums = [int(num) for num in winningNums if num != ""]

    for num in nums:
        if num in winningNums:
            if points == 0:
                points = 1
            else:
                points *= 2
    totalPoints += points

print(f"The total number of points is {totalPoints}")
