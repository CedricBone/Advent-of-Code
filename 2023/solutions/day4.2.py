input = open("../inputs/input4.txt", "r")
cards = {}
cardNum = 1
totalOccurences = 0


def process(card):
    card = line.split("|")
    nums = card[0].split()
    nums = nums[2:]
    nums = [int(num) for num in nums if num != " "]
    winningNums = card[1][:-1].split(" ")
    winningNums = [int(num) for num in winningNums if num != ""]
    return nums, winningNums


def score(nums, winningNums):
    score = 0
    for num in nums:
        if num in winningNums:
            score += 1
    return score


for line in input:
    occurences = 1
    cards[cardNum] = [process(line), occurences]
    cardNum += 1

for card in cards.keys():
    nums, winningNums = cards[card][0]
    cardScore = score(nums, winningNums)
    for cardOccurence in range(cards[card][1]):
        tempCardScore = cardScore
        while tempCardScore > 0:
            cards[card + tempCardScore][1] += 1
            tempCardScore -= 1

for card in cards.keys():
    totalOccurences += cards[card][1]

print(f"The total number of points is {totalOccurences}")
