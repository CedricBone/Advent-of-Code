"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: 
X means you need to lose, 
Y means you need to end the round in a draw, 
and Z means you need to win. 
Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. 
The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. 
This gives you a score of 1 + 3 = 4.

In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.

In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.


Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""


def response(elf1, elf2):
    if (elf1 == "A"):
        match elf2:
            case "X":
                return "Scissors"
            case "Y":
                return "Rock"
            case "Z":
                return "Paper"
    elif (elf1 == "B"):
        match elf2:
            case "X":
                return "Rock"
            case "Y":
                return "Paper"
            case "Z":
                return "Scissors"
    elif (elf1 == "C"):
        match elf2:
            case "X":
                return "Paper"
            case "Y":
                return "Scissors"
            case "Z":
                return "Rock"


def score(elf1, elf2):
    score = 0
    match elf2:
        case "X":
            score += 0
        case "Y":
            score += 3
        case "Z":
            score += 6

    match response(elf1, elf2):
        case "Rock":
            score += 1
        case "Paper":
            score += 2
        case "Scissors":
            score += 3

    return score


input = open("input.txt", "r")
output = 0
for round in input:
    print(
        f"You responded with a {response(round[0], round[2])} and had a score of {score(round[0],round[2])}")
    output += score(round[0], round[2])
input.close()

print(
    f"\nIf everything goes exactly according to the strategy guide, your score is {output}.\n")
